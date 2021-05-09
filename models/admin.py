from flask import *
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL
import hashlib
import flask_excel as excel
import pyexcel_xlsx
import datetime

app = Flask(__name__)
CORS(app)
excel.init_excel(app) # required since version 0.0.7

app.config.from_object('config.DevConfig')

mysql = MySQL(app)

def admin_dashboard():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    cur = mysql.connection.cursor()
    cur.execute(''' select count(*) from student; ''')
    rv = cur.fetchall()
    count_students = rv[0][0]
    cur.execute(''' select count(*) from faculty; ''')
    rv = cur.fetchall()
    count_faculty = rv[0][0]
    cur.execute(''' select count(*) from department; ''')
    rv = cur.fetchall()
    count_dept = rv[0][0]
    cur.execute(''' select count(*) from course; ''')
    rv = cur.fetchall()
    count_course = rv[0][0]
    cur.execute(''' select count(*) from student where sem in (1,2); ''')
    rv = cur.fetchall()
    countyear1 = rv[0][0]
    cur.execute(''' select count(*) from student where sem in (3,4); ''')
    rv = cur.fetchall()
    countyear2 = rv[0][0]
    cur.execute(''' select count(*) from student where sem in (5,6); ''')
    rv = cur.fetchall()
    countyear3 = rv[0][0]
    cur.execute(''' select count(*) from student where sem in (7,8); ''')
    rv = cur.fetchall()
    countyear4 = rv[0][0]
    cur.execute(''' select student_id, first_name, last_name,
    cpi, sem / 2 from student order by cpi desc; ''')
    rv = cur.fetchall()
    star_student = rv
    cur.execute(''' select faculty_id, first_name, emailid,
    dob from faculty order by dob; ''')
    rv = cur.fetchall()
    star_faculty = rv
    mysql.connection.commit()
    dt = datetime.datetime.now().year
    count_year = []
    count_year.append([(str)(dt), countyear1])
    count_year.append([(str)(dt-1), countyear2])
    count_year.append([(str)(dt-2), countyear3])
    count_year.append([(str)(dt-3), countyear4])
    cur.close()

    return render_template('admin_panel/index.html', count_student = count_students,
        count_faculty = count_faculty, count_course = count_course, count_dept = count_dept,
        count_year = count_year, star_student = star_student, star_faculty = star_faculty)

def admin_add_student():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    if request.method == 'POST':
        student_details = request.form
        first_name = student_details['first_name']
        last_name = student_details['last_name']
        student_id = student_details['student_id']
        phone = student_details['phone']
        sem = student_details['sem']
        program = student_details['program']
        branch = student_details['branch']
        dob = student_details['dob']
        gender = student_details['gender']
        address = student_details['address']
        sem = (int)(sem)
        phone = (int)(phone)
        cur = mysql.connection.cursor()
        hashedpassword = hashlib.md5(student_id.encode()).hexdigest()
        if (gender == 'Select Gender'):
            gender = 'Male'
        cur.execute(''' insert into student (student_id, gender, first_name, last_name, 
        phone, sem, program, branch, dob, address, password) values ('%s','%s','%s','%s','%d',%d,'%s','%s','%s','%s','%s');
        '''%(student_id, gender, first_name, last_name, phone, sem, program, branch, dob, address, hashedpassword))
        
        cur.execute(''' select * from student; ''')
        rv = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('admin_student_list'))

    return render_template('admin_panel/add-student.html')

def admin_add_faculty():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    return render_template('admin/admin_add_faculty_dashboard.html')

def admin_student_list():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    cur = mysql.connection.cursor()
    cur.execute(''' select * from student; ''')
    rv = cur.fetchall()
    mysql.connection.commit()
    cur.close()

    return render_template('admin_panel/students.html', list = rv)

def admin_student_list_edit():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    cur = mysql.connection.cursor()
    cur.execute(''' select * from student; ''')
    rv = cur.fetchall()
    mysql.connection.commit()
    cur.close()

    return render_template('/admin/student.html', list = rv)

def admin_student_delete(student_id):
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    cur = mysql.connection.cursor()
    cur.execute(''' delete from student where student_id = '%s'; '''%(student_id))
    cur.execute(''' select * from student; ''')
    rv = cur.fetchall()
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('admin_student_list_edit', list = rv))

def admin_student_edit(student_id):
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    if request.method == 'POST':

        student_details = request.form
        first_name = student_details['first_name']
        last_name = student_details['last_name']
        phone = student_details['phone']
        sem = student_details['sem']
        program = student_details['program']
        branch = student_details['branch']
        dob = student_details['dob']
        address = student_details['address']
        gender = student_details['gender']
        sem = (int)(sem)
        phone = (phone)
        if (gender == 'Select Gender'):
            gender = 'Male'
        cur = mysql.connection.cursor()
        hashedpassword = hashlib.md5(student_id.encode()).hexdigest()
        cur.execute(''' update student set first_name = '%s', last_name = '%s', gender = '%s', 
        phone = '%s', sem = %d, program = '%s', branch = '%s', dob = '%s', address = '%s'
        where student_id = '%s';
        '''%(first_name, last_name, gender, phone, sem, program, branch, dob, address, student_id))
        
        cur = mysql.connection.cursor()
        cur.execute(''' select * from student; ''')
        rv = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('admin_student_list_edit', list = rv))

    cur = mysql.connection.cursor()
    cur.execute(''' select * from student where student_id = '%s'; '''%(student_id))
    rv = cur.fetchall()
    mysql.connection.commit()
    cur.close()

    return render_template('/admin/student-edit.html', list = rv[0])

def admin_student_view(student_id):
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    cur = mysql.connection.cursor()
    cur.execute(''' select * from student where student_id = '%s'; '''%(student_id))
    rv = cur.fetchall()
    mysql.connection.commit()
    cur.close()

    return render_template('admin/student-detail.html', list = rv[0])

def ExcelDownload_student():
    cur = mysql.connection.cursor()
    cur.execute('''select student_id, first_name, last_name, gender, 
        phone, sem, program, branch, cpi,dob, address, password from student;''')
    rv = cur.fetchall()

    studentlist = [['student_id', 'first_name', 'last_name', 'gender', 
        'phone', 'sem', 'program', 'branch','cpi', 'dob', 'address', 'password']]
    for rows in rv:
        temp = []
        for items in rows:
            item = (str)(items)
            temp.append(item)
        studentlist.append(temp)

    mysql.connection.commit()
    cur.close()

    return excel.make_response_from_array(studentlist, "xlsx")

def admin_faculty_list():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    cur = mysql.connection.cursor()
    cur.execute(''' select * from faculty; ''')
    rv = cur.fetchall()
    mysql.connection.commit()
    cur.close()

    return render_template('admin/faculty_list.html', list = rv)


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

# util
def debug():
    print('!!!!!!!!!!!!!!!!!!\n\n\n\n\n\n\n\n\n\n\n\n\n\n!!!!!!!!!!!!!!!')

def sanitize_course_sem(rv):
    dt = {}
    print(rv)
    for rows in rv:
        if rows[0] not in dt:
            dt[rows[0]] = []
        dt[rows[0]].append(rows)
    print(dt)
    return dt



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

    return render_template('admin/index.html', count_student = count_students,
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

    return render_template('admin/add-student.html')

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

    return render_template('/admin/students_list.html', list = rv)

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
    if(request.method == 'POST'):
        print('asdasd')
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

def admin_modal_update():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html') 

    cur = mysql.connection.cursor()
    cur.execute(''' select * from student; ''')
    rv = cur.fetchall()
    mysql.connection.commit()
    cur.close()

    if request.method == 'POST':
        form_details = request.form
        sem = form_details['sem']
        sem = (int)(sem)
        cur = mysql.connection.cursor()
        cur.execute(''' update student set sem = sem+1 where sem = %d; '''%(sem))
        mysql.connection.commit()
        cur.close()
        return redirect(request.referrer)

    return render_template('/admin/modal_update.html', list=rv)


# Faculty start

def admin_add_faculty():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')
    cur = mysql.connection.cursor()
    cur.execute(''' select dept_id,name from department; ''')
    depts = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('admin/add-faculty.html', deptList=depts)

def admin_faculty_list():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    cur = mysql.connection.cursor()
    cur.execute(''' select faculty_id, first_name, last_name, DOB, phone, address, emailid, position from faculty; ''')
    faculty = cur.fetchall()
    mysql.connection.commit()
    cur.close()

    return render_template('admin/faculty_list.html', facultyList = faculty)

# department

# course
def admin_add_course():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    if request.method == 'POST':
        course_details = request.form
        c_id = course_details['c_id']
        name = course_details['name']
        # sem = course_details['sem']
        # sem = (int)(sem)
        year = (str)(datetime.datetime.now().date())
        _credits = course_details['credits']
        cur = mysql.connection.cursor()
        cur.execute(''' insert ignore into course (c_id, name, credits, year) 
                values ('%s','%s','%s','%s'); '''%(c_id, name, _credits, year))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('admin_add_course'))

    return render_template('admin/add_course.html')

def admin_course_list():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')
    
    cur = mysql.connection.cursor()
    cur.execute(''' select * from course; ''')
    rv = cur.fetchall()
    mysql.connection.commit()
    cur.close()

    return render_template('/admin/course_list.html', list = rv)

def ExcelDownload_course():
    cur = mysql.connection.cursor()
    cur.execute('''select c_id,name,description,year,credits,hours,syllabus from course;''')
    rv = cur.fetchall()

    courselist = [['c_id','name','description','year','credits','hours','syllabus']]
    for rows in rv:
        temp = []
        for items in rows:
            item = (str)(items)
            temp.append(item)
        courselist.append(temp)

    mysql.connection.commit()
    cur.close()

    return excel.make_response_from_array(courselist, "xlsx")

def admin_course_edit(c_id):
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')
    
    if (request.method == 'POST'):
        course_details = request.form
        name = course_details['name']
        description = course_details['description']
        syllabus = course_details['syllabus']
        # sem = course_details['sem']
        # sem = (int)(sem)
        _credits = course_details['credits']
        cur = mysql.connection.cursor()
        cur.execute(''' update course set name = '%s', credits = '%s', description = '%s', syllabus = '%s' where c_id = '%s' ; '''%(name, _credits, description, syllabus, c_id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('admin_course_list'))

    cur = mysql.connection.cursor()
    cur.execute(''' select c_id, name, description, syllabus, year, credits from course where c_id = '%s'; '''%(c_id))
    rv = cur.fetchall()
    mysql.connection.commit()
    cur.close()

    return render_template('/admin/edit_course.html', list = rv[0])

def admin_course_sem_assign():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')
    
    cur = mysql.connection.cursor()
    cur.execute(''' 
    SELECT 
    course.c_id, course.name, course.credits, section.sec_id, section.sem
    FROM
        course
            JOIN
        section
    WHERE
    course.c_id = section.c_id;''')
    rv = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    course_sem = sanitize_course_sem(rv)

    return render_template('/admin/course_section_assign.html', course_sem = course_sem)

def admin_course_sem_edit(c_id):
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')
    if request.method == 'POST':
        details = request.form
        sem = details['sem']
        cur = mysql.connection.cursor()
        cur.execute(''' insert ignore into section (c_id, sem) values ('%s','%s');'''%(c_id, sem))
        rv = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('admin_course_sem_assign'))
    
    return "ok no get here"

# faculty end

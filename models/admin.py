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
    for rows in rv:
        if rows[0] not in dt:
            dt[rows[0]] = []
        dt[rows[0]].append(rows)
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

def admin_profile():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    return render_template('admin_panel_extras/profile.html')

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
        cur.execute(''' insert ignore into student (student_id, gender, first_name, last_name,
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
    if request.method == 'POST':
        faculty_details = request.form
        first_name = faculty_details['first_name']
        last_name = faculty_details['last_name']
        faculty_id = faculty_details['faculty_id']
        gender = faculty_details['gender']
        dob = faculty_details['dob']
        phone = faculty_details['phone']
        address = faculty_details['address']
        email = faculty_details['email']
        salary = faculty_details['salary']
        researchint = faculty_details['ri']
        position = faculty_details['position']
        dept_id = faculty_details['department']
        phone = int(phone) if phone else -1
        salary = int(salary) if salary else -1
        cur = mysql.connection.cursor()
        hashedpassword = hashlib.md5(faculty_id.encode()).hexdigest()
        if(phone != -1 and len(faculty_id) > 0 and len(first_name) > 0 and len(email) > 0 and salary != -1 and len(position) > 0 and len(dob) > 0):
            cur = mysql.connection.cursor()
            cur.execute(''' insert ignore into faculty (faculty_id, first_name, last_name, gender, dob, phone, address, emailid,
            salary, research_interests, position, password) values ('%s','%s','%s','%s','%s',%d,'%s','%s','%d','%s','%s','%s');
            '''%(faculty_id, first_name, last_name, gender, dob, phone, address, email, salary, researchint, position, hashedpassword))
            if(dept_id!=None):
                cur.execute(''' insert ignore into works (faculty_id, dept_id) VALUES ('%s','%s');'''%((faculty_id,dept_id)))
            mysql.connection.commit()
            cur.close()
        return redirect(url_for('admin_faculty_list'))
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

def admin_faculty_view(faculty_id):
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    cur = mysql.connection.cursor()
    cur.execute(''' select faculty_id, first_name, last_name, gender, dob, phone, address, emailid,
            salary, research_interests, position from faculty where faculty_id = '%s'; '''%(faculty_id))
    faculty = cur.fetchall()
    cur.execute(''' select name from department where dept_id in (select dept_id from works where faculty_id = '%s'); '''%(faculty_id))
    department = cur.fetchall()
    department = department[0][0] if department else None
    mysql.connection.commit()
    cur.close()

    return render_template('admin/faculty-detail.html', facultyDetails = faculty[0], department = department)
    
def ExcelDownload_faculty():
    cur = mysql.connection.cursor()
    cur.execute('''select faculty_id, first_name, last_name, gender, dob, phone, address, emailid,
            salary, research_interests, position from faculty;''')
    rv = cur.fetchall()

    facultylist = [['faculty_id', 'first_name', 'last_name', 'gender',
        'dob', 'phone', 'address', 'emailid','salary', 'research_interests', 'position']]
    for rows in rv:
        temp = []
        for items in rows:
            item = (str)(items)
            temp.append(item)
        facultylist.append(temp)

    mysql.connection.commit()
    cur.close()

    return excel.make_response_from_array(facultylist, "xlsx")

def admin_faculty_list_edit():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    cur = mysql.connection.cursor()
    cur.execute(''' select faculty_id, first_name, last_name, DOB, phone, address, emailid, position from faculty; ''')
    faculty = cur.fetchall()
    mysql.connection.commit()
    cur.close()

    return render_template('/admin/faculty.html', facultyList = faculty)

def admin_faculty_edit(faculty_id):
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    if request.method == 'POST':

        faculty_details = request.form

        first_name = faculty_details['first_name']
        last_name = faculty_details['last_name']
        gender = faculty_details['gender']
        dob = faculty_details['dob']
        phone = faculty_details['phone']
        address = faculty_details['address']
        email = faculty_details['email']
        salary = faculty_details['salary']
        researchint = faculty_details['ri']
        position = faculty_details['position']
        dept_id = faculty_details['department']
        if salary!= 'None':
            salary = int(salary) if salary else -1
        cur = mysql.connection.cursor()
        if(len(phone) > 0 and len(faculty_id) > 0 and len(first_name) > 0 and len(email) > 0 and salary != -1 and len(position) > 0 and len(dob) > 0):
            cur = mysql.connection.cursor()
            cur.execute(''' UPDATE faculty SET first_name = '%s', last_name = '%s', gender = '%s', dob = '%s', phone = '%s', address = '%s', emailid = '%s',
            salary = '%d', research_interests = '%s', position = '%s' where faculty_id = '%s' ;'''%(first_name, last_name, gender, dob, phone, address, email, salary, researchint, position, faculty_id))
            if(dept_id!=None):
                cur.execute(''' UPDATE works set dept_id = '%s' WHERE faculty_id = '%s';'''%(dept_id,faculty_id))
            mysql.connection.commit()
            cur.close()
        return redirect(url_for('admin_faculty_list'))
    cur = mysql.connection.cursor()
    cur.execute(''' select faculty_id, first_name, last_name, gender, dob, phone, address, emailid,
            salary, research_interests, position from faculty where faculty_id = '%s'; '''%(faculty_id))
    faculty = cur.fetchall()
    cur.execute(''' select dept_id,name from department where dept_id in (select dept_id from works where faculty_id = '%s'); '''%(faculty_id))
    department = cur.fetchall()
    department = department[0] if department else None
    mysql.connection.commit()
    cur = mysql.connection.cursor()
    cur.execute(''' select dept_id,name from department; ''')
    depts = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('/admin/edit-faculty.html', facultyDetails = faculty[0], department = department, deptList=depts)

def admin_faculty_delete():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')
    if(request.method == 'POST'):
        faculty_id = str(request.json['id'])
        print(faculty_id)
        cur = mysql.connection.cursor()
        cur.execute(''' DELETE FROM faculty WHERE faculty_id= '%s'; '''%(faculty_id))
        mysql.connection.commit()
        cur.close()
        return "Executed"
    return "ok no get here"

# faculty end

# department start
def admin_department_list():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    cur = mysql.connection.cursor()
    cur.execute(''' select department.dept_id, department.name, budget, faculty.first_name,faculty.last_name,
                (SELECT count(*) FROM student where student.branch=department.dept_id) as noofstudent
                from department JOIN faculty WHERE department.hod_id = faculty.faculty_id; ''')
    departments = cur.fetchall()
    mysql.connection.commit()
    cur.close()

    return render_template('admin/department_list.html', departmentList = departments)

def admin_add_department():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')
    if request.method == 'POST':
        dept_details = request.form
        name = dept_details['name']
        dept_id = dept_details['dept_id']
        contact_no = dept_details['phone']
        budget = dept_details['budget']
        hod_id = dept_details['hod_id']
        budget = int(budget) if budget else 0
        if hod_id == "" :
            hod_id = None
        cur = mysql.connection.cursor()
        if(len(dept_id) > 0 and len(name) > 0 and len(contact_no) > 0):
            cur = mysql.connection.cursor()
            cur.execute(''' insert ignore into department (dept_id, name, budget,contact_no,hod_id)
            values ('%s','%s','%d','%s','%s');'''%(dept_id, name, budget, contact_no, hod_id ))
            mysql.connection.commit()
            cur.close()
        return redirect(url_for('admin_department_list'))
    cur = mysql.connection.cursor()
    cur.execute(''' select faculty_id,first_name,last_name from faculty; ''')
    faculty = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('admin/add-department.html', facultyList=faculty)

def ExcelDownload_department():
    cur = mysql.connection.cursor()
    cur.execute('''select department.dept_id, department.name, budget, faculty.first_name,faculty.last_name,
                (SELECT count(*) FROM student where student.branch=department.dept_id) as noofstudent, department.contact_no
                from department JOIN faculty WHERE department.hod_id = faculty.faculty_id;''')
    rv = cur.fetchall()

    deptlist = [['department_id', 'name', 'Budget', 'HOD first_name', 'HOD last_name',
        'No of student', 'Contact']]
    for rows in rv:
        temp = []
        for items in rows:
            item = (str)(items)
            temp.append(item)
        deptlist.append(temp)

    mysql.connection.commit()
    cur.close()

    return excel.make_response_from_array(deptlist, "xlsx")

def admin_department_list_edit():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    cur = mysql.connection.cursor()
    cur.execute(''' select department.dept_id, department.name, budget, faculty.first_name,faculty.last_name,
                (SELECT count(*) FROM student where student.branch=department.dept_id) as noofstudent
                from department JOIN faculty WHERE department.hod_id = faculty.faculty_id; ''')
    departments = cur.fetchall()
    mysql.connection.commit()
    cur.close()

    return render_template('/admin/department.html', departmentList = departments)

def admin_department_edit(dept_id):
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    if request.method == 'POST':
        dept_details = request.form
        name = dept_details['name']
        contact_no = dept_details['phone']
        budget = dept_details['budget']
        hod_id = dept_details['hod_id']
        budget = int(budget) if budget else 0
        if hod_id == "" :
            hod_id = None
        cur = mysql.connection.cursor()
        if(len(dept_id) > 0 and len(name) > 0 and len(contact_no) > 0):
            cur = mysql.connection.cursor()
            cur.execute(''' UPDATE department SET name = '%s', budget = '%d', contact_no = '%s',hod_id = '%s'
            WHERE dept_id = '%s';'''%(name, budget, contact_no, hod_id, dept_id ))
            mysql.connection.commit()
            cur.close()
        return redirect(url_for('admin_department_list'))
    cur = mysql.connection.cursor()
    cur.execute(''' select * from department where dept_id = '%s'; '''%(dept_id))
    department = cur.fetchall()
    cur.execute(''' select faculty.faculty_id, faculty.first_name, faculty.last_name from faculty where faculty_id in (select faculty_id from works where dept_id = '%s') ; '''%(dept_id))
    faculty = cur.fetchall()
    cur.close()
    return render_template('/admin/edit-department.html', facultyList=faculty, deptDetails = department[0])

def admin_department_delete():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')
    if(request.method == 'POST'):
        dept_id = str(request.json['id'])
        print(dept_id)
        cur = mysql.connection.cursor()
        cur.execute(''' DELETE FROM department WHERE dept_id= '%s'; '''%(dept_id))
        mysql.connection.commit()
        cur.close()
        return "Executed"
# department end

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
    debug()
    cur.execute(''' select c_id, name, description, syllabus, year, credits from course where c_id = '%s'; '''%(c_id))
    rv = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('/admin/edit_course.html', list = rv[0])

def admin_course_delete():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    if (request.method == 'POST'):
        c_id = request.form['c_id']
        cur = mysql.connection.cursor()
        cur.execute(''' delete from course where c_id = '%s' ; '''%(c_id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('admin_course_list'))

    return "ok no get here"

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
            LEFT JOIN
        section
    on
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

def admin_course_sem_delete(c_id):
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')
    if request.method == 'POST':
        details = request.form
        sem = details['sem']
        cur = mysql.connection.cursor()
        cur.execute(''' delete from section where c_id = '%s' and sem = '%s';'''%(c_id, sem))
        rv = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('admin_course_sem_assign'))

    return "ok no get here"

def admin_course_student_assign():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    cur = mysql.connection.cursor()
    cur.execute('''
    select
	student.student_id, student.first_name, course.name, section.sec_id, student.sem
    from
        student
            join
        section
			join
		course
    where
    section.sem = student.sem and
    section.c_id = course.c_id order by student.student_id;''')
    rv = cur.fetchall()

    cur.execute('''
    select
	student.student_id, student.first_name, course.name, section.sec_id
    from
        student
            join
        enroll
			join
		section
			join
        course
    where
    section.c_id = course.c_id and
    student.student_id = enroll.student_id and
    enroll.sec_id = section.sec_id order by student.student_id;''')
    cv = cur.fetchall()

    mysql.connection.commit()
    cur.close()
    course_student = sanitize_course_sem(rv)
    course_enrolled = sanitize_course_sem(cv)
    return render_template('/admin/course_student_assign.html', course_student = course_student, course_enrolled = course_enrolled)

def admin_course_student_add(student_id):
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    if request.method == 'POST':
        details = request.form
        sec_id = details['sec_id']
        cur = mysql.connection.cursor()
        cur.execute(''' insert ignore into enroll (student_id, sec_id) values ('%s','%s');'''%(student_id, sec_id))
        rv = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('admin_course_student_assign'))

    return "ok no get here"

def admin_course_student_delete(student_id):
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    if request.method == 'POST':
        details = request.form
        sec_id = details['sec_id']
        cur = mysql.connection.cursor()
        cur.execute(''' delete from enroll where student_id = '%s' and sec_id = '%s';'''%(student_id, sec_id))
        rv = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('admin_course_student_assign'))

    return "ok no get here"

def admin_inbox():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    cur = mysql.connection.cursor()
    cur.execute(''' select * from requests where status = 'pending' order by dob desc; ''')
    rv = cur.fetchall()
    mysql.connection.commit()
    cur.close()

    return render_template('/admin/inbox.html', list = rv)

def admin_accepted_requests():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')
    if request.method == 'POST':
        r_id = request.form['r_id']
        cur = mysql.connection.cursor()
        cur.execute(''' update requests set status='accepted' where r_id = '%s';'''%(r_id))
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('admin_inbox'))

    cur = mysql.connection.cursor()
    cur.execute(''' select * from requests where status = 'accepted' order by dob desc; ''')
    rv = cur.fetchall()
    mysql.connection.commit()
    cur.close()
    return render_template('/admin/inbox.html', list = rv)

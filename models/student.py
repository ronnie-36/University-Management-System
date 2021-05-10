from flask import *
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL
import datetime

app = Flask(__name__)
CORS(app)

app.config.from_object('config.DevConfig')

mysql = MySQL(app)

# util
def debug():
    print('!!!!!!!!!!!!!!!!!!\n\n\n\n\n\n\n\n\n\n\n\n\n\n!!!!!!!!!!!!!!!')





def student_dashboard():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "student":
        return render_template('error.html')

    cur = mysql.connection.cursor()
    cur.execute(''' select * from student where student_id = '%s'; '''%(session['id']))
    rv = cur.fetchall()
    details = rv[0]

    cur.execute('''
    select 
	count(*)
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
    enroll.sec_id = section.sec_id and
    student.student_id = '%s';'''%(session['id']))
    rv = cur.fetchall()
    enrolled_courses = int(rv[0][0])

    cur.execute('''
    select 
	count(*)
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
    enroll.sec_id = section.sec_id and
    student.sem = section.sem and
    student.student_id = '%s';'''%(session['id']))
    rv = cur.fetchall()
    active_courses = int(rv[0][0])

    completed_courses = enrolled_courses - active_courses

    cur.execute('''
    select 
	course.name, grade
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
    enroll.sec_id = section.sec_id and
    student.sem = section.sem and
    student.student_id = '%s';'''%(session['id']))
    rv = cur.fetchall()
    current_grades = rv

    mysql.connection.commit()
    cur.close()
    print(details)
    return render_template('student_panel/dashboard.html', details = details, enrolled_courses = enrolled_courses,
    active_courses = active_courses, completed_courses = completed_courses,
    current_grades = current_grades)

def student_profile():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "student":
        return render_template('error.html')
    

    if request.method == 'POST':
        details = request.form
        address = details['address']
        dob = details['dob']
        gender = details['gender']
        emailid = details['emailid']
        cur = mysql.connection.cursor()
        cur.execute(''' update student set dob='%s', gender='%s', address='%s', emailid='%s' where student_id = '%s'; '''%(str(dob), gender, address, emailid ,session['id']))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('student_profile'))
 
    cur = mysql.connection.cursor()
    cur.execute(''' select * from student where student_id = '%s'; '''%(session['id']))
    rv = cur.fetchall()

    mysql.connection.commit()
    cur.close()

    return render_template('student_panel/dashboard-profile.html', details = rv[0])

def student_setting():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "student":
        return render_template('error.html')
        
    return render_template('student_panel/dashboard-settings.html')

def student_enrolled_courses():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "student":
        return render_template('error.html')
        
    if request.method == 'POST':
        details = request.form
        sec_id = details['sec_id']
        sec_name = details['sec_name']
        dt = datetime.datetime.now()
        dt = str(dt)
        cur = mysql.connection.cursor()
        cur.execute(''' select first_name from student where student_id = '%s' ;'''%(session['id']))
        rv = cur.fetchall()
        name = rv[0][0]
        note = "Request for enroll course %s name %s for student id %s"%(sec_id, sec_name, session['id'])
        cur.execute(''' insert ignore into requests (name, id, notes, dob) VALUES ('%s','%s','%s','%s');'''%(name, session['id'], note, dt))
        rv = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('student_enrolled_courses'))

    cur = mysql.connection.cursor()
    cur.execute('''
    select 
	section.sec_id, course.name, section.sem, course.credits, course.hours, student.sem
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
    enroll.sec_id = section.sec_id and
    student.sem = section.sem and
    student.student_id = '%s';'''%(session['id']))
    rv = cur.fetchall()
    my_courses = rv

    cur.execute('''
    select DISTINCT
	section.sec_id, course.name, student.sem, course.credits, course.hours, student.sem
    from
        student
            join
		section
			join
        course
			join
		has_course
    where
    section.c_id = course.c_id and
    student.sem = section.sem and
    has_course.branch = student.branch and
    has_course.c_id = course.c_id and
    student.student_id = '%s';'''%(session['id']))
    rv = cur.fetchall()
    sem_courses = rv

    mysql.connection.commit()
    cur.close()
    return render_template('student_panel/dashboard-enrolled-courses.html', list = my_courses, list2 = sem_courses)

def student_my_courses():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "student":
        return render_template('error.html')
        
    cur = mysql.connection.cursor()
    cur.execute('''
    select 
	section.sec_id, course.name, section.sem, course.credits, course.hours, student.sem
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
    enroll.sec_id = section.sec_id and
    student.student_id = '%s';'''%(session['id']))
    rv = cur.fetchall()
    my_courses = rv

    mysql.connection.commit()
    cur.close()
    return render_template('student_panel/dashboard-courses.html', list = my_courses)

def student_submit_course():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "student":
        return render_template('error.html')
        
    return render_template('student_panel/dashboard-submit-assignment.html')
from flask import *
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL

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
        debug()

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
        
    return render_template('student_panel/dashboard-enrolled-courses.html')

def student_submit_course():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "student":
        return render_template('error.html')
        
    return render_template('student_panel/dashboard-submit-assignment.html')
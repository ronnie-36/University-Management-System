from flask import *
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL
import hashlib

app = Flask(__name__)
CORS(app)

app.config.from_object('config.DevConfig')

mysql = MySQL(app)

def faculty_dashboard():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "faculty":
        return render_template('error.html')
    fid = session['id']
    cur = mysql.connection.cursor()
    cur.execute("SELECT first_name FROM faculty WHERE faculty_id = '%s' "% (fid))
    name = cur.fetchall()
    cur.close()
    name = name[0][0]
    return render_template('faculty/instructor_dashboard.html', name = name)

def faculty_setting():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "faculty":
        return render_template('error.html')
    fid = session['id']
    cur = mysql.connection.cursor()
    cur.execute("SELECT first_name FROM faculty WHERE faculty_id = '%s' "% (fid))
    name = cur.fetchall()
    cur.close()
    name = name[0][0]
    return render_template('faculty/setting.html', name=name)

def faculty_profile():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "faculty":
        return render_template('error.html')
    faculty_id = session['id']
    if request.method == 'POST':
        faculty_details = request.form
        phone = faculty_details['phone']
        address = faculty_details['address']
        email = faculty_details['email']
        researchint = faculty_details['ri']
        cur = mysql.connection.cursor()
        if(len(phone) > 0 and len(email) > 0):
            cur = mysql.connection.cursor()
            cur.execute(''' UPDATE faculty SET phone = '%s', address = '%s', emailid = '%s', research_interests = '%s' 
            where faculty_id = '%s' ;'''%(phone, address, email,researchint,faculty_id))
            mysql.connection.commit()
            cur.close()
        return redirect(url_for('faculty_profile'))
    cur = mysql.connection.cursor()
    cur.execute(''' select faculty_id, first_name, last_name, gender, dob, phone, address, emailid,
            salary, research_interests, position from faculty where faculty_id = '%s'; '''%(faculty_id))
    faculty = cur.fetchall()
    cur.execute(''' select name from department where dept_id in (select dept_id from works where faculty_id = '%s'); '''%(faculty_id))
    department = cur.fetchall()
    department = department[0][0] if department else None
    mysql.connection.commit()
    cur.close()
    return render_template('faculty/faculty-profile.html', facultyDetails = faculty[0], department = department, name=faculty[0][1])

def faculty_change_password():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "faculty":
        return render_template('error.html')
    flash=""
    fid = session['id']
    cur = mysql.connection.cursor()
    cur.execute("SELECT password FROM faculty WHERE faculty_id = '%s' "% (fid))
    password = cur.fetchall()
    cur.close()
    passwordcheck = password[0][0]
    if request.method == 'POST':
        # Fetch form data
        formDetails = request.form
        curpassword = formDetails['curpassword']
        newpassword = formDetails['newpassword']
        conpassword = formDetails['conpassword']
        hashedpassword = hashlib.md5(curpassword.encode()).hexdigest()
        hashednewpassword = hashlib.md5(newpassword.encode()).hexdigest()
        if (len(curpassword) == 0 or len(newpassword) == 0 or len(conpassword) == 0):
            flash = "Null Values Encountered."
            return render_template('faculty/setting.html',flash=flash)
        elif (conpassword != newpassword):
            flash = "Passwords do not match. Check password."
            return render_template('faculty/setting.html',flash=flash)
        elif (passwordcheck != hashedpassword):
            flash = "Current Password is wrong."
            return render_template('faculty/setting.html',flash=flash)    
        else:
            cur = mysql.connection.cursor()
            cur.execute("UPDATE faculty SET password = %s WHERE faculty_id = %s",(hashednewpassword,fid) )
            mysql.connection.commit()
            flash="Password Changed."
            return render_template('faculty/setting.html',flash=flash)

def faculty_course():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "faculty":
        return render_template('error.html')
    fid = session['id']
    cur = mysql.connection.cursor()
    cur.execute(''' select course.c_id,course.name, course.credits, course.hours, section.year from 
                            teaches
                                join 
                            section 
                                join 
                            course 
    where teaches.sec_id = section.sec_id and section.c_id = course.c_id and section.year = year(curdate()) and teaches.faculty_id = '%s' '''% (fid))
    ongoing = cur.fetchall()
    cur = mysql.connection.cursor()
    cur.execute(''' select course.c_id,course.name, course.credits, course.hours, section.year from 
                            teaches
                                join 
                            section 
                                join 
                            course 
    where teaches.sec_id = section.sec_id and section.c_id = course.c_id and section.year != year(curdate()) and teaches.faculty_id = '%s' '''% (fid))
    completed = cur.fetchall()
    cur.close()
        
    return render_template('faculty/faculty-courses.html',ongoingList=ongoing,completedList=completed)

def faculty_create_new_assignment():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "faculty":
        return render_template('error.html')
    fid = session['id']
    if request.method == 'POST':
        formDetails = request.form
        marks = formDetails['marks']
        # currently storing name in notes
        name = formDetails['name'] 
        text = formDetails['text']
        sec_id = formDetails['sec_id']
        start = formDetails['start']
        end = formDetails['end']
        sec_id = int(sec_id)
        marks = int(marks)
        cur = mysql.connection.cursor()
        if(len(fid) > 0 and sec_id > 0 and len(name)>0):
            cur.execute(''' INSERT INTO assignment (faculty_id, sec_id, created_at, start_at, end_at, text, marks_total, notes) 
            values ('%s','%d',NOw(),'%s','%s','%s','%d', '%s');'''% (fid,sec_id,start,end,text,marks,name))
            flash("Assignment created",'success') 
            mysql.connection.commit()
            cur.close()
        else:
            flash("Some error occured",'error')
        return redirect(url_for('faculty_create_new_assignment'))
    cur = mysql.connection.cursor()
    cur.execute(''' select course.c_id,course.name, course.credits, course.hours, section.year, section.sec_id from 
                            teaches
                                join 
                            section 
                                join 
                            course 
    where teaches.sec_id = section.sec_id and section.c_id = course.c_id and section.year = year(curdate()) and teaches.faculty_id = '%s' '''% (fid))
    ongoing = cur.fetchall()
    cur.close()
    return render_template('faculty/create_new_assignment.html',ongoingList=ongoing)

def select_section_for_assignment():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "faculty":
        return render_template('error.html')
    fid = session['id']
    if request.method == 'POST':
        return redirect(url_for('select_section_for_assignment'))
    cur = mysql.connection.cursor()
    cur.execute(''' select course.c_id,course.name, course.credits, course.hours, section.year, section.sec_id from 
                            teaches
                                join 
                            section 
                                join 
                            course 
    where teaches.sec_id = section.sec_id and section.c_id = course.c_id and section.year = year(curdate()) and teaches.faculty_id = '%s' '''% (fid))
    ongoing = cur.fetchall()
    cur.close()
    return render_template('faculty/select_section_for_assignment.html',ongoingList=ongoing)

def select_assignment_for_grade(sec_id):
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "faculty":
        return render_template('error.html')
    fid = session['id']
    if request.method == 'POST':
        return redirect(url_for('select_assignment_for_grade',sec_id=sec_id))
    sec_id = int(sec_id)
    cur = mysql.connection.cursor()
    cur.execute(''' select * from 
                            assignment
    where sec_id='%d' and faculty_id = '%s' '''% (sec_id,fid))
    assignments = cur.fetchall()
    cur.close()
    return render_template('faculty/select_assignment_for_grade.html',assgList=assignments, sec_id=sec_id)

def select_student_for_grade(sec_id,a_id):
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "faculty":
        return render_template('error.html')
    fid = session['id']
    if request.method == 'POST':
        return redirect(url_for('select_student_for_grade',sec_id=sec_id, a_id=a_id))
    sec_id = int(sec_id)
    a_id = int(a_id)
    cur = mysql.connection.cursor()
    cur.execute(''' select * from 
                            assignment
    where a_id= '%s' '''% (a_id))
    assignment = cur.fetchall()
    cur.execute(''' 
    select 
        submission.student_id,first_name, last_name, submitted_at, marks_got, submission_id 
    from 
        submission 
        join 
        student 
    where 
    a_id= '%s' and submission.student_id = student.student_id '''
    % (a_id))
    submission = cur.fetchall()
    cur.close()
    return render_template('faculty/select_student_for_grade.html',assgDetails=assignment[0], submissionList=submission)

def faculty_assignment_grade_submission(submission_id):
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "faculty":
        return render_template('error.html')
    fid = session['id']
    if request.method == 'POST':
        formDetails = request.form
        marksobtained = formDetails['marksobtained']
        # currently storing feedback in notes(submission table)
        feedback = formDetails['feedback']
        submission_id = int(submission_id)
        marksobtained = int(marksobtained)
        cur = mysql.connection.cursor()
        if(submission_id > 0):
            cur.execute(''' 
            UPDATE 
                submission
            SET 
                marks_got = '%d', notes = '%s' 
            WHERE 
                submission_id ='%d' ;'''% (marksobtained,feedback,submission_id))
            flash("Marks Updated",'success') 
            mysql.connection.commit()
            cur.close()
        else:
            flash("Some error occured",'error')
        return redirect(request.referrer)
    cur = mysql.connection.cursor()
    cur.execute(''' 
    select 
        student.student_id, student.first_name, student.last_name, submission.marks_got, submission.text,
        submission.a_id, submission.submitted_at, submission.files_link, submission.notes 
    from  
        submission 
        join 
        student
    where 
    submission.student_id = student.student_id and submission.submission_id= '%s' '''% (submission_id))
    submission = cur.fetchall()
    a_id = submission[0][5]
    a_id = int(a_id)
    cur.execute(''' select * from 
                            assignment
    where a_id= '%s' '''% (a_id))
    assignment = cur.fetchall()
    cur.close()
    return render_template('faculty/grade_submission.html',assgDetails=assignment[0], submissionDetails=submission[0])
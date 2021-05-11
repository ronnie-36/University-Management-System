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
        
    return render_template('faculty/setting.html')

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
    return render_template('faculty/faculty-profile.html', facultyDetails = faculty[0], department = department)

def change_password():
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
    
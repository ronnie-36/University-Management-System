from flask import *
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL

app = Flask(__name__)
CORS(app)

app.config.from_object('config.DevConfig')

mysql = MySQL(app)

def admin_dashboard():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    return render_template('admin_panel/index.html')

def admin_add_student_dashboard():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    return render_template('admin/admin_add_student_dashboard.html')

def admin_add_faculty_dashboard():
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
    
    return render_template('admin/student_list.html', list = rv)

def admin_search_semester(sem):
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    cur = mysql.connection.cursor()
    cur.execute(''' select * from student where sem = %d; '''%(sem))
    rv = cur.fetchall()
    mysql.connection.commit()
    
    return redirect(url_for('admin_student_list'), list = rv)

def admin_search_year(year):
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    cur = mysql.connection.cursor()
    cur.execute(''' select * from student where (sem+1) / 2 = %d; '''%(year))
    rv = cur.fetchall()
    mysql.connection.commit()
    
    return redirect(url_for('admin_student_list'), list = rv)

def admin_search_name(name):
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    cur = mysql.connection.cursor()
    cur.execute(''' select * from student where name like '%s%%'; '''%(name))
    rv = cur.fetchall()
    mysql.connection.commit()
    
    return redirect(url_for('admin_student_list'), list = rv)

def admin_faculty_list():
    if 'id' not in session or 'role' not in session:
        return render_template('error.html')
    elif session['role'] != "admin":
        return render_template('error.html')

    cur = mysql.connection.cursor()
    cur.execute(''' select * from faculty; ''')
    rv = cur.fetchall()
    mysql.connection.commit()

    return render_template('admin/faculty_list.html', list = rv)

    
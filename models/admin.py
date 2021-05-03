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

    return render_template('admin/dashboard.html')
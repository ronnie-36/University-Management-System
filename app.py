from flask import *
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL

# models
import models.student as student
import models.admin as admin
import models.faculty as faculty
import models.auth as auth

app = Flask(__name__)
CORS(app)

app.config.from_object('config.DevConfig')

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# auth start
app.add_url_rule('/login/<user>', view_func=auth.login, methods=['GET','POST'])
app.add_url_rule('/logout', view_func=auth.logout, methods=['GET','POST'])

# auth end

# student start
app.add_url_rule('/student/dashboard', view_func=student.student_dashboard, methods=['GET','POST'])
# student end

# faculty start
app.add_url_rule('/faculty/dashboard', view_func=faculty.faculty_dashboard, methods=['GET','POST'])
# faculty end

# admin start
app.add_url_rule('/admin/dashboard', view_func=admin.admin_dashboard, methods=['GET','POST'])
# admin end  

if __name__ == '__main__':
    flag = 0
    app.run()
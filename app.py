from flask import *
from flask_cors import CORS, cross_origin
from flask_mysqldb import MySQL
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_mail import Mail
from flask_mail import Message

# models
import models.student as student
import models.admin as admin
import models.faculty as faculty
import models.auth as auth

app = Flask(__name__)
CORS(app)

app.config.from_object('config.DevConfig')

mysql = MySQL(app)
mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/getStarted', methods=['GET', 'POST'])
def getStarted():
    return render_template('getStarted.html')

# auth start
app.add_url_rule('/login/<user>', view_func=auth.login, methods=['GET','POST'])
app.add_url_rule('/logout', view_func=auth.logout, methods=['GET','POST'])
app.add_url_rule('/resetpassword/<user>', view_func=auth.resetpassword, methods=['GET','POST'])
app.add_url_rule('/reset_password/<user>/<token>', view_func=auth.reset_token,  methods=['GET','POST'])
# auth end

# student start
app.add_url_rule('/student/dashboard', view_func=student.student_dashboard, methods=['GET','POST'])
# student end

# faculty start
app.add_url_rule('/faculty/dashboard', view_func=faculty.faculty_dashboard, methods=['GET','POST'])
# faculty end

# admin start
app.add_url_rule('/admin/dashboard', view_func=admin.admin_dashboard, methods=['GET','POST'])
app.add_url_rule('/admin/add_student_dashboard', view_func=admin.admin_add_student_dashboard, methods=['GET','POST'])
app.add_url_rule('/admin/add_faculty_dashboard', view_func=admin.admin_add_faculty_dashboard, methods=['GET','POST'])
app.add_url_rule('/admin/student_list', view_func=admin.admin_student_list, methods=['GET','POST'])
app.add_url_rule('/admin/faculty_list', view_func=admin.admin_faculty_list, methods=['GET','POST'])
app.add_url_rule('/admin/admin_search_semester/<sem>', view_func=admin.admin_search_semester, methods=['GET','POST'])
app.add_url_rule('/admin/admin_search_year/<year>', view_func=admin.admin_search_year, methods=['GET','POST'])
app.add_url_rule('/admin/admin_search_name/<name>', view_func=admin.admin_search_name, methods=['GET','POST'])

# admin end  

if __name__ == '__main__':
    flag = 0
    app.run(debug=True)
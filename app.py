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
app.add_url_rule('/student/setting', view_func=student.student_setting, methods=['GET','POST'])
app.add_url_rule('/student/profile', view_func=student.student_profile, methods=['GET','POST'])
app.add_url_rule('/student/submit', view_func=student.student_submit_course, methods=['GET','POST'])
app.add_url_rule('/student/enrolled-courses', view_func=student.student_enrolled_courses, methods=['GET','POST'])
# student end

# faculty start
app.add_url_rule('/faculty/dashboard', view_func=faculty.faculty_dashboard, methods=['GET','POST'])
app.add_url_rule('/faculty/setting', view_func=faculty.faculty_setting, methods=['GET','POST'])
app.add_url_rule('/faculty/profile', view_func=faculty.faculty_profile, methods=['GET','POST'])

# faculty end

# admin start
app.add_url_rule('/admin/dashboard', view_func=admin.admin_dashboard, methods=['GET','POST'])

# admin student start
app.add_url_rule('/admin/add_student', view_func=admin.admin_add_student, methods=['GET','POST'])
app.add_url_rule('/admin/student_list', view_func=admin.admin_student_list, methods=['GET','POST'])
app.add_url_rule('/admin/edit-student/<student_id>', view_func=admin.admin_student_edit, methods=['GET','POST'])
app.add_url_rule('/admin/student_view/<student_id>', view_func=admin.admin_student_view, methods=['GET','POST'])
app.add_url_rule('/admin/delete-student/<student_id>', view_func=admin.admin_student_delete, methods=['GET','POST'])
app.add_url_rule('/admin/student_list_edit', view_func=admin.admin_student_list_edit, methods=['GET','POST'])
app.add_url_rule('/admin/student_excel', view_func=admin.ExcelDownload_student, methods=['GET','POST'])
app.add_url_rule('/admin/modal_update', view_func=admin.admin_modal_update, methods=['GET','POST'])
# admin student end

# admin faculty start 
app.add_url_rule('/admin/add_faculty', view_func=admin.admin_add_faculty, methods=['GET','POST'])
app.add_url_rule('/admin/faculty_list', view_func=admin.admin_faculty_list, methods=['GET','POST'])
app.add_url_rule('/admin/faculty_view/<faculty_id>', view_func=admin.admin_faculty_view, methods=['GET','POST'])
app.add_url_rule('/admin/faculty_list_edit', view_func=admin.admin_faculty_list_edit, methods=['GET','POST'])
app.add_url_rule('/admin/edit-faculty/<faculty_id>', view_func=admin.admin_faculty_edit, methods=['GET','POST'])
app.add_url_rule('/admin/delete-faculty', view_func=admin.admin_faculty_delete, methods=['GET','POST'])
# admin faculty end

app.add_url_rule('/admin/add_course', view_func=admin.admin_add_course, methods=['GET','POST'])
app.add_url_rule('/admin/course_list', view_func=admin.admin_course_list, methods=['GET','POST'])
app.add_url_rule('/admin/course_edit/<c_id>', view_func=admin.admin_course_edit, methods=['GET','POST'])
app.add_url_rule('/admin/course_delete', view_func=admin.admin_course_delete, methods=['GET','POST'])
app.add_url_rule('/admin/course_excel', view_func=admin.ExcelDownload_course, methods=['GET','POST'])
app.add_url_rule('/admin/course_sem_assign', view_func=admin.admin_course_sem_assign, methods=['GET','POST'])
app.add_url_rule('/admin/course_sem_edit/<c_id>', view_func=admin.admin_course_sem_edit, methods=['GET','POST'])
app.add_url_rule('/admin/course_sem_delete/<c_id>', view_func=admin.admin_course_sem_delete, methods=['GET','POST'])
app.add_url_rule('/admin/course_student_assign', view_func=admin.admin_course_student_assign, methods=['GET','POST'])
app.add_url_rule('/admin/course_student_add/<student_id>', view_func=admin.admin_course_student_add, methods=['GET','POST'])
app.add_url_rule('/admin/course_student_delete/<student_id>', view_func=admin.admin_course_student_delete, methods=['GET','POST'])

app.add_url_rule('/admin/all_requests', view_func=admin.admin_inbox, methods=['GET','POST'])
app.add_url_rule('/admin/accepted_requests', view_func=admin.admin_accepted_requests, methods=['GET','POST'])
# admin end  

if __name__ == '__main__':
    flag = 0
    app.run(debug=True)
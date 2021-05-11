''' Store data for all the <<forms>> of the website '''

admin_login = {'user_id': '1', 'password': '1234'}
admin_student_add = dict([('first_name', 'James'), ('last_name', 'Scott'), ('student_id', '12'), ('gender', 'Male'), ('dob', '2021-03-18'), ('phone', '9022003399'), ('address', 'Lucknow'), ('sem', '4'), ('program', 'btech'), ('branch', 'cse'), ('image', '')])
admin_student_edit = dict([('first_name', 'James'), ('last_name', 'Scott'), ('gender', 'Female'), ('dob', '2021-03-06'), ('phone', '9022003322'), ('address', 'Lucknow21'), ('sem', '2'), ('program', 'btech'), ('branch', 'cse')])
admin_modal_next = dict([('sem', '1')])

admin_course_add = dict([('c_id', '12'), ('name', 'Chem'), ('credits', '2')])
admin_course_edit = dict([('name', 'Chemistry'), ('credits', '2.0'), ('description', 'Ok'), ('syllabus', 'Good')])
admin_course_delete = dict([('c_id', 12)])
admin_course_sem_assign = dict([('sem', '3')]) # cid = 2
admin_course_sem_delete = dict([('sem', '3')]) # cid = 2
admin_course_student_assign = dict([('sec_id', '2')]) # student_id = 2
admin_course_student_delete = dict([('sec_id', '2')]) # student_id = 2
admin_all_requests = dict([('r_id', 3)])

admin_faculty_add = dict([('faculty_id', '12'), ('first_name', 'Sharon'), ('last_name', 'mailk'), ('gender', 'Male'), ('dob', '2021-05-01'), ('phone', '9191020293'), ('address', '123-abc'), ('email', 'sharon@123.com'), ('salary', '123333'), ('ri', 'software'), ('position', 'Associate Professor'), ('department', 'cse')])
admin_faculty_edit = dict([('first_name', 'Sharon'), ('last_name', 'mailk'), ('gender', 'Male'), ('dob', '2021-05-01'), ('phone', '9191020294'), ('address', '123-abcd'), ('email', 'sharon@123.com'), ('salary', '1233332'), ('ri', 'software'), ('position', 'Associate Professor'), ('department', 'cse')])
admin_faculty_delete = dict([('faculty_id', '12')])

admin_department_add = dict([('dept_id', 'bio'), ('name', 'biology'), ('hod_id', '1'), ('budget', '120000'), ('phone', '1919230301')])
admin_department_edit = dict([('name', 'Computer Science and Engineering'), ('hod_id', '1'), ('budget', '120000'), ('phone', '9876512121')])


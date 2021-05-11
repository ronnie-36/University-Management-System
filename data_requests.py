''' Store data for all the <<forms>> of the website '''

admin_login = {'user_id': '1', 'password': '1234'}
admin_student_add = dict([('first_name', 'James'), ('last_name', 'Scott'), ('student_id', '12'), ('gender', 'Male'), ('dob', '2021-03-18'), ('phone', '9022003399'), ('address', 'Lucknow'), ('sem', '4'), ('program', 'btech'), ('branch', 'cse'), ('image', '')])
admin_student_edit = dict([('first_name', 'James'), ('last_name', 'Scott'), ('gender', 'Female'), ('dob', '2021-03-06'), ('phone', '9022003322'), ('address', 'Lucknow21'), ('sem', '2'), ('program', 'btech'), ('branch', 'cse')])
admin_modal_next = dict([('sem', '1')])

# for faculty
faculty_login1 = {'user_id': '1', 'password': '1234'}
faculty_login2 = {'user_id': '1', 'password': '12345'}
faculty_profile = dict([('phone', '3103413677'), ('address', '3138  Doctors Drive'), ('email', 'sih@shi.com'), ('ri', 'Logic Circuits')])
faculty_change_password1 = dict([('curpassword', ''), ('newpassword', ''), ('conpassword', '')])
faculty_change_password2 = dict([('curpassword', '1234'), ('newpassword', '12345'), ('conpassword', '123456')])
faculty_change_password3 = dict([('curpassword', '12345'), ('newpassword', '12345'), ('conpassword', '12345')])
faculty_change_password4 = dict([('curpassword', '1234'), ('newpassword', '12345'), ('conpassword', '12345')])
faculty_change_password_revert = dict([('curpassword', '12345'), ('newpassword', '1234'), ('conpassword', '1234')])
faculty_create_new_assignment = dict([('marks', '25'), ('name', 'Quiz 1'), ('text', 'test question'), ('sec_id', '2'), ('start', '2021-05-11T00:00'), ('end', '2021-05-12T00:00')])
faculty_grade_assignment = dict([('student_id', '1'), ('name', 'ron '), ('text', 'answer 2 text'), ('marksobtained', '9'), ('feedback', 'Good Work')])
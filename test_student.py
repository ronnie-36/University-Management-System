'''
For running test file
STEPS: 

    pip install -r requirements.txt
    python test_student.py

FOR DETAILED COVERAGE

    coverage run --source models -m unittest discover && coverage report
    coverage html


TestCase Details - 
1. Home section
2. Admin section
3. Student section
4. Faculty section
'''

import flask
import unittest
import flask_testing
from app import app
import data_requests
from flask import json

''' Section 3 - Student Section '''
class TestStudent(flask_testing.TestCase):
    def create_app(self):
        return app
      
    def testHomepage(self):
        with app.test_client() as TestClient:
            response= TestClient.get('/')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('index.html')

    def testStudentLoginGet(self):
        with app.test_client() as TestClient:
            response= TestClient.get('/login/student')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('student/login.html')

    def testStudentLoginPost(self):
        data = data_requests.student_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/student', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'student')
            # login done
    
    def testAdmin_logged_out(self):
        data = data_requests.student_login
        with app.test_client() as TestClient:
            # login not done
            response= TestClient.get('/student/dashboard')
            self.assert_template_used('error.html')
            response= TestClient.get('/student/profile')
            self.assert_template_used('error.html')
            response= TestClient.get('/student/setting')
            self.assert_template_used('error.html')
            response= TestClient.get('/student/enrolled-courses')
            self.assert_template_used('error.html')
            response= TestClient.get('/student/my-courses')
            self.assert_template_used('error.html')
            response= TestClient.get('/student/grades')
            self.assert_template_used('error.html')
            response= TestClient.get('/student/gradesheet')
            self.assert_template_used('error.html')
            response= TestClient.get('/student/placement-offers')
            self.assert_template_used('error.html')
            response= TestClient.get('/student/submit-assignment')
            self.assert_template_used('error.html')
            response= TestClient.get('/student/submit-assign/2')
            self.assert_template_used('error.html')

    def testAdmin_partial_logged_out(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/student/dashboard')
            self.assert_template_used('error.html')
            response= TestClient.get('/student/profile')
            self.assert_template_used('error.html')
            response= TestClient.get('/student/setting')
            self.assert_template_used('error.html')
            response= TestClient.get('/student/enrolled-courses')
            self.assert_template_used('error.html')
            response= TestClient.get('/student/my-courses')
            self.assert_template_used('error.html')
            response= TestClient.get('/student/grades')
            self.assert_template_used('error.html')
            response= TestClient.get('/student/gradesheet')
            self.assert_template_used('error.html')
            response= TestClient.get('/student/placement-offers')
            self.assert_template_used('error.html')
            response= TestClient.get('/student/submit-assignment')
            self.assert_template_used('error.html')
            response= TestClient.get('/student/submit-assign/2')
            self.assert_template_used('error.html')


    def testStudentdashboard(self):
        data = data_requests.student_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/student', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'student')
            # login done
            response= TestClient.get('/student/dashboard')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('student_panel/dashboard.html')

    def testStudent_Profile(self):
        data = data_requests.student_login
        myprofile = data_requests.student_profile
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/student', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'student')
            # login done
            response= TestClient.get('/student/profile')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('student_panel/dashboard-profile.html')
            # post
            response= TestClient.post('/student/profile', data = myprofile)
            self.assertEqual(response.status_code, 302)

    def testStudent_setting(self):
        data = data_requests.student_login
        mysetting = data_requests.student_settings
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/student', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'student')
            # login done
            response= TestClient.get('/student/setting')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('student_panel/dashboard-settings.html')
            # post
            response= TestClient.post('/student/setting', data = mysetting)
            self.assertEqual(response.status_code, 302)

    def testStudent_enrolled_course(self):
        data = data_requests.student_login
        myenroll = data_requests.student_enroll_course
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/student', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'student')
            # login done
            response= TestClient.get('/student/enrolled-courses')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('student_panel/dashboard-enrolled-courses.html')
            # post
            response= TestClient.post('/student/enrolled-courses', data = myenroll)
            self.assertEqual(response.status_code, 302)

    def testStudent_my_courses(self):
        data = data_requests.student_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/student', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'student')
            # login done
            response= TestClient.get('/student/my-courses')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('student_panel/dashboard-courses.html')

    def testStudent_grades(self):
        data = data_requests.student_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/student', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'student')
            # login done
            response= TestClient.get('/student/grades')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('student_panel/dashboard-grades.html')

    def testStudent_gradesheet(self):
        data = data_requests.student_login
        mygradesheet = data_requests.student_gradesheet
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/student', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'student')
            # login done
            response= TestClient.get('/student/gradesheet')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('student_panel/dashboard-gradesheet.html')
            # post
            response= TestClient.post('/student/gradesheet', data = mygradesheet)
            self.assertEqual(response.status_code, 200)

    def testStudent_placement(self):
        data = data_requests.student_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/student', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'student')
            # login done
            response= TestClient.get('/student/placement-offers')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('student_panel/dashboard-placement-offers.html')

    def testStudent_submit_assignment(self):
        data = data_requests.student_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/student', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'student')
            # login done
            response= TestClient.get('/student/submit-assignment')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('student_panel/dashboard-assignment-submit.html')

    def testStudent_submit_assign(self):
        data = data_requests.student_login
        myassn = data_requests.student_submit_assignment
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/student', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'student')
            # login done
            response= TestClient.get('/student/submit-assign/4')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('student_panel/dashboard-submit-assignment.html')
            # post
            response= TestClient.post('/student/submit-assign/4', data = myassn)
            self.assertEqual(response.status_code, 302)
if __name__ == "__main__":
    unittest.main()
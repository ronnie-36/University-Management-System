'''
For running test file
STEPS: 

    pip install -r requirements.txt
    python test.py

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

''' Section 1 - Home Section '''
class TestHome(flask_testing.TestCase):
    def create_app(self):
        return app

    def testHomepage(self):
        with app.test_client() as TestClient:
            response= TestClient.get('/')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('index.html')

    def testGetStartedPage(self):
        with app.test_client() as TestClient:
            response= TestClient.get('/getStarted')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('getStarted.html')
    
    def testStudentLogin(self):
        with app.test_client() as TestClient:
            response= TestClient.get('/login/student')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('student/login.html')
    
    def testAdminLogin(self):
        with app.test_client() as TestClient:
            response= TestClient.get('/login/admin')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('admin/login.html')
    
    def testFacultyLogin(self):
        with app.test_client() as TestClient:
            response= TestClient.get('/login/faculty')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('faculty/login.html')


#---------------------------------------------------------------------#


''' section 2 - Admin Section '''

class TestAdmin(flask_testing.TestCase):
    def create_app(self):
        return app

    def testHomepage(self):
        with app.test_client() as TestClient:
            response= TestClient.get('/')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('index.html')

    def testAdminLoginGet(self):
        with app.test_client() as TestClient:
            response= TestClient.get('/login/admin')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('admin/login.html')

    def testAdminLoginPost(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done

    def testAdmin_logged_out(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login not done
            response= TestClient.get('/admin/dashboard')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/student_list')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/add_student')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/student_list_edit')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/edit-student/12')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/student_view/12')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/modal_update')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/student_excel')
            self.assert_template_used('error.html')
    
    def testAdmin_partial_logged_out(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/student', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'student')
            # login done
            response= TestClient.get('/admin/dashboard')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/student_list')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/add_student')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/student_list_edit')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/edit-student/12')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/student_view/12')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/modal_update')
            self.assert_template_used('error.html')
            response= TestClient.get('/admin/student_excel')
            self.assert_template_used('error.html')

    def testAdminDashboard(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/dashboard')
            self.assert_template_used('admin/index.html')
    
    def testAdminStudent_list(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/student_list')
            self.assert_template_used('/admin/students_list.html')

    def testAdminStudent_add(self):
        data = data_requests.admin_login
        new_student = data_requests.admin_student_add
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            # get
            response= TestClient.get('/admin/add_student')
            self.assert_template_used('admin/add-student.html')
            # post
            response= TestClient.post('/admin/add_student', data = new_student)
            self.assert_template_used('admin/add-student.html')

    def testAdminStudent_list_edit(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/student_list_edit')
            self.assert_template_used('/admin/student.html')

    def testAdminEditStudent(self):
        data = data_requests.admin_login
        student_edit = data_requests.admin_student_edit
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/edit-student/1')
            self.assert_template_used('/admin/student-edit.html')
            # post
            response= TestClient.post('/admin/edit-student/12', data = student_edit)
            self.assert_template_used('/admin/student-edit.html')

    def testAdminStudentDetail(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/student_view/1')
            self.assert_template_used('admin/student-detail.html')

    def testAdminmodal_update(self):
        data = data_requests.admin_login
        modal_data = data_requests.admin_modal_next
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/modal_update')
            self.assert_template_used('/admin/modal_update.html')
            # post
            response= TestClient.post('/admin/modal_update', data = modal_data)
            self.assert_template_used('/admin/modal_update.html')

    def testAdminStudentExcel(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            response= TestClient.get('/admin/student_excel')
            self.assertEqual(response.status_code, 200)


    def testAdminStudent_delete(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login sequence
            response= TestClient.post('/login/admin', data = data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'admin')
            # login done
            # deleting student 12 which was added before
            response= TestClient.get('/admin/delete-student/12')
            self.assertEqual(response.status_code, 302)

if __name__ == "__main__":
    unittest.main()
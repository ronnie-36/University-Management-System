import flask
import unittest
import flask_testing
from flask import *
from app import app
import data_requests


class TestFaculty(flask_testing.TestCase):
    def create_app(self):
        return app

    def testHomepage(self):
        with app.test_client() as TestClient:
            response = TestClient.get('/')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('index.html')

    def testFacultyLoginGet(self):
        with app.test_client() as TestClient:
            response = TestClient.get('/login/faculty')
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('faculty/login.html')

    def testFacultyLoginPost(self):
        data1 = data_requests.faculty_login1
        data2 = data_requests.faculty_login2
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data1)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done

            # invalid login
            response = TestClient.post('/login/faculty', data=data2)
            self.assertEqual(response.status_code, 200)
            self.assert_template_used('faculty/login.html')

    def testFaculty_logged_out(self):
        data = data_requests.admin_login
        with app.test_client() as TestClient:
            # login not done
            response = TestClient.get('/faculty/dashboard')
            self.assert_template_used('error.html')
            response = TestClient.get('/faculty/setting')
            self.assert_template_used('error.html')
            response = TestClient.get('/faculty/profile')
            self.assert_template_used('error.html')
            response = TestClient.get('/faculty/changepassword')
            self.assert_template_used('error.html')
            response = TestClient.get('/faculty/create_new_assignment')
            self.assert_template_used('error.html')
            response = TestClient.get('/faculty/grade_assignment')
            self.assert_template_used('error.html')
            response = TestClient.get('/faculty/grade_assignment/1')
            self.assert_template_used('error.html')
            response = TestClient.get('/faculty/grade_assignment/1/1')
            self.assert_template_used('error.html')
            response = TestClient.get('/faculty/grade_assignment/submission/1')
            self.assert_template_used('error.html')

    def testAdmin_partial_logged_out(self):
        data = data_requests.faculty_login1
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/student', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'student')
            # login done
            response = TestClient.get('/faculty/dashboard')
            self.assert_template_used('error.html')
            response = TestClient.get('/faculty/setting')
            self.assert_template_used('error.html')
            response = TestClient.get('/faculty/profile')
            self.assert_template_used('error.html')
            response = TestClient.get('/faculty/changepassword')
            self.assert_template_used('error.html')
            response = TestClient.get('/faculty/create_new_assignment')
            self.assert_template_used('error.html')
            response = TestClient.get('/faculty/grade_assignment')
            self.assert_template_used('error.html')
            response = TestClient.get('/faculty/grade_assignment/1')
            self.assert_template_used('error.html')
            response = TestClient.get('/faculty/grade_assignment/1/1')
            self.assert_template_used('error.html')
            response = TestClient.get('/faculty/grade_assignment/submission/1')
            self.assert_template_used('error.html')

    def testFacultyDashboard(self):
        data = data_requests.faculty_login1
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done
            response = TestClient.get('/faculty/dashboard')
            self.assert_template_used('faculty/instructor_dashboard.html')

    def testFacultySetting(self):
        data = data_requests.faculty_login1
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done
            response = TestClient.get('/faculty/setting')
            self.assert_template_used('faculty/setting.html')

    def testFacultyProfileGet(self):
        data = data_requests.faculty_login1
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done
            response = TestClient.get('/faculty/profile')
            self.assert_template_used('faculty/faculty-profile.html')

    def testFacultyProfilePost(self):
        data = data_requests.faculty_login1
        data_profile = data_requests.faculty_profile
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done
            response = TestClient.post('/faculty/profile', data=data_profile)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(request.path, url_for('faculty_profile'))

    def testFacultyChangePasswordGet(self):
        data = data_requests.faculty_login1
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done
            response = TestClient.get('/faculty/changepassword')
            self.assertEqual(response.status_code, 405)

    def testFacultyChangePasswordPost(self):
        data = data_requests.faculty_login1
        data_password_change_empty = data_requests.faculty_change_password1
        data_password_change_different = data_requests.faculty_change_password2
        data_password_change_wrong = data_requests.faculty_change_password3
        data_password_change_correct = data_requests.faculty_change_password4
        data_password_change_revert = data_requests.faculty_change_password_revert
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done
            # testing for null values
            response = TestClient.post(
                '/faculty/changepassword', data=data_password_change_empty)
            self.assert_template_used('faculty/setting.html')
            self.assert_context("flash", "Null Values Encountered.")
            # new password and confirm password don't match
            response = TestClient.post(
                '/faculty/changepassword', data=data_password_change_different)
            self.assert_template_used('faculty/setting.html')
            self.assert_context(
                "flash", "Passwords do not match. Check password.")
            # wrong current password
            response = TestClient.post(
                '/faculty/changepassword', data=data_password_change_wrong)
            self.assert_template_used('faculty/setting.html')
            self.assert_context("flash", "Current Password is wrong.")
            # correct case
            response = TestClient.post(
                '/faculty/changepassword', data=data_password_change_correct)
            self.assert_template_used('faculty/setting.html')
            self.assert_context("flash", "Password Changed.")
            # reverting
            response = TestClient.post(
                '/faculty/changepassword', data=data_password_change_revert)
            self.assert_template_used('faculty/setting.html')
            self.assert_context("flash", "Password Changed.")

    def testFacultyCourseGet(self):
        data = data_requests.faculty_login1
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done
            response = TestClient.get('/faculty/courses')
            self.assert_template_used('faculty/faculty-courses.html')

    def testFacultyCreateNewAssignmentGet(self):
        data = data_requests.faculty_login1
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done
            response = TestClient.get('/faculty/create_new_assignment')
            self.assert_template_used('faculty/create_new_assignment.html')

    def testFacultyCreateNewAssignmentPost(self):
        data = data_requests.faculty_login1
        assignmentData = data_requests.faculty_create_new_assignment
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done
            response = TestClient.post(
                '/faculty/create_new_assignment', data=assignmentData)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(request.path, url_for(
                'faculty_create_new_assignment'))

    def testFacultySelectSectionForAssignmentGet(self):
        data = data_requests.faculty_login1
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done
            response = TestClient.get('/faculty/grade_assignment')
            self.assert_template_used(
                'faculty/select_section_for_assignment.html')

    def testFacultySelectSectionForAssignmentPost(self):
        data = data_requests.faculty_login1
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done
            response = TestClient.post('/faculty/grade_assignment')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(request.path, url_for(
                'select_section_for_assignment'))

    def testFacultySelectAssignmentForGradeGet(self):
        data = data_requests.faculty_login1
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done
            response = TestClient.get('/faculty/grade_assignment/1')
            self.assert_template_used(
                'faculty/select_assignment_for_grade.html')
            self.assert_context("sec_id", 1)

    def testFacultySelectAssignmentForGradePost(self):
        data = data_requests.faculty_login1
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done
            response = TestClient.post('/faculty/grade_assignment/1')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(request.path, url_for(
                'select_assignment_for_grade', sec_id=1))

    def testFacultySelectStudentForGradeGet(self):
        data = data_requests.faculty_login1
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done
            response = TestClient.get('/faculty/grade_assignment/1/1')
            self.assert_template_used(
                'faculty/select_student_for_grade.html')

    def testFacultySelectStudentForGradePost(self):
        data = data_requests.faculty_login1
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done
            response = TestClient.post('/faculty/grade_assignment/1/1')
            self.assertEqual(response.status_code, 302)
            self.assertEqual(request.path, url_for(
                'select_student_for_grade', sec_id=1, a_id=1))

    def testFacultyAssignmentGradeSubmissionGet(self):
        data = data_requests.faculty_login1
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done
            response = TestClient.get('/faculty/grade_assignment/submission/1')
            self.assert_template_used(
                'faculty/grade_submission.html')

    def testFacultyAssignmentGradeSubmissionPost(self):
        data = data_requests.faculty_login1
        gradeData = data_requests.faculty_grade_assignment
        with app.test_client() as TestClient:
            # login sequence
            response = TestClient.post('/login/faculty', data=data)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(flask.session['id'], '1')
            self.assertEqual(flask.session['role'], 'faculty')
            # login done
            response = TestClient.post(
                '/faculty/grade_assignment/submission/2', data=gradeData)
            self.assertEqual(response.status_code, 302)


if __name__ == "__main__":
    unittest.main()

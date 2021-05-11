'''
For running test file
STEPS: 

    pip install -r requirements.txt
    python test.py

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

# Section 1 - Home Section

class TestMyApp(flask_testing.TestCase):
    def create_app(self):
        return app

    def testHomepage(self):
        with app.test_client() as lTestClient:
            lResp= lTestClient.get('/')
            self.assertEqual(lResp.status_code, 200)
            self.assert_template_used('index.html')

    def testGetStartedPage(self):
        with app.test_client() as lTestClient:
            lResp= lTestClient.get('/getStarted')
            self.assertEqual(lResp.status_code, 200)
            self.assert_template_used('getStarted.html')


if __name__ == "__main__":
    unittest.main()
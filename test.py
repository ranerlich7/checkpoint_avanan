import json
import unittest
from app import app  

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    
    def test_events_endpoint(self):
        # Test the /events endpoint with a POST request
        response = self.app.post('/events', data='Test email security', content_type='text/plain')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {'message': 'Updated successfuly'})
        
    def test_stats_endpoint(self):
        # Test the /stats endpoint with a GET request
        response = self.app.get('/stats?interval=10')
        self.assertEqual(response.status_code, 200)
        self.assertIn('email', response.get_json())
        self.assertIn('security', response.get_json())
        
    def test_stats_endpoint_bad_request(self):
        # Test the /stats endpoint with an invalid interval parameter
        response = self.app.get('/stats?interval=invalid')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.get_json(), {'error': 'Bad Request', 'message': 'Invalid input provided'})

if __name__ == '__main__':
    unittest.main()

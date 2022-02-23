import unittest
import requests

class TestSite(unittest.TestCase):
    url='http://127.0.0.1:5000/'

#unit tests
    def test_site_is_working(self):
        response = requests.get(self.url).status_code
        self.assertEqual(response, 200)

    def test_input_is_working(self):
        response = requests.post(self.url, data={'text_to_send':'test input'})
        self.assertIn('id="result"', response.text)

if __name__ == '__main__':
    unittest.main()
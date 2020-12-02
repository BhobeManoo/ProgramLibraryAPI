import requests
import unittest


class URLValidate(unittest.TestCase):
    # to check if response is 200
    def test_program_url(self):
        response = requests.get("http://localhost:5000/api/v1/programs")
        self.assertEqual(response.status_code, 200)

    def test_section_url(self):
        response = requests.get("http://localhost:5000/api/v1/programs/sections/1")
        self.assertEqual(response.status_code, 200)

    def test_activities_url(self):
        response = requests.get("http://localhost:5000/api/v1/programs/activities/1")
        self.assertEqual(response.status_code,200)

    def test_questionnaires_url(self):
        response = requests.get("http://localhost:5000/api/v1/programs/activity_questionnaires/1")
        self.assertEqual(response.status_code,200)

if __name__ == "__main__":
    unittest.main()


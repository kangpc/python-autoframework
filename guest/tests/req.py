import requests
import unittest

class TestGetEventList(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/get_event_list/"
    def test_case(self):
        r = requests.get(self.url, params={"eid":3})
        # print(r.text)
        # print(type(r))
        result = r.json()
        self.assertEqual(r.status_code,200)
        self.assertEqual(result["message"], "success.")
        self.assertEqual(result["status"], 200)

if __name__ == "__main__":
    unittest.main()
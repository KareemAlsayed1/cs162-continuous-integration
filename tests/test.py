import unittest
import requests


URL = "http://localhost:5000/"

class TestWeb(unittest.TestCase):

  def test_post(self):
      r = requests.post(URL + "add", data = {'expression': '8+7+6+5+4+3+2+1'})
      self.assertEqual(r.status_code, 200)

if __name__ == '__main__':
    unittest.main()
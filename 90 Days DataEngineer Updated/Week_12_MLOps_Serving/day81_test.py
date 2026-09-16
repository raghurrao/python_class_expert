import unittest
from fastapi.testclient import TestClient
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day81_assignment

class TestDay81(unittest.TestCase):
    def test_serving(self):
        client = TestClient(day81_assignment.app)
        res = client.get("/predict_endpoint?value=4.0")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["prediction"], 10.0)

if __name__ == '__main__':
    unittest.main()
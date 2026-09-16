import unittest
from fastapi.testclient import TestClient
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day80_assignment

class TestDay80(unittest.TestCase):
    def test_predict(self):
        client = TestClient(day80_assignment.app)
        res = client.post("/predict", json={"feature1": 1.5, "feature2": 2.5})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["prediction"], 4.0)

if __name__ == '__main__':
    unittest.main()
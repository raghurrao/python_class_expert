import unittest
from fastapi.testclient import TestClient
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import week12_challenge

class TestWeek12Challenge(unittest.TestCase):
    def test_churn(self):
        client = TestClient(week12_challenge.app)
        r1 = client.post("/predict_churn", json={"age": 55, "income": 20000})
        self.assertEqual(r1.json()["churn"], 1)
        r2 = client.post("/predict_churn", json={"age": 30, "income": 50000})
        self.assertEqual(r2.json()["churn"], 0)

if __name__ == '__main__':
    unittest.main()
import unittest
from fastapi.testclient import TestClient
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day88_app

class TestDay88(unittest.TestCase):
    def test_fastapi_fallback(self):
        client = TestClient(day88_app.app)
        res = client.post("/predict", json={
            "age": 60.0,
            "tenure": 12.0,
            "monthly_charges": 120.0,
            "contract_type": "month-to-month"
        })
        self.assertEqual(res.status_code, 200)
        self.assertIn("prediction", res.json())

if __name__ == '__main__':
    unittest.main()
import unittest
from fastapi.testclient import TestClient
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day79_assignment

class TestDay79(unittest.TestCase):
    def test_health(self):
        client = TestClient(day79_assignment.app)
        res = client.get("/health")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.json()["status"], "ok")

if __name__ == '__main__':
    unittest.main()

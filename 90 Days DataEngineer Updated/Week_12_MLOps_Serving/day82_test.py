import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day82_assignment

class TestDay82(unittest.TestCase):
    def test_dockerfile(self):
        self.assertIn("FROM", day82_assignment.DOCKERFILE_TEMPLATE)
        self.assertIn("uvicorn", day82_assignment.DOCKERFILE_TEMPLATE)

if __name__ == '__main__':
    unittest.main()
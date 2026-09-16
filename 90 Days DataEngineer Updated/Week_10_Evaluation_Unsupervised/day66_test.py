import unittest
from sklearn.pipeline import Pipeline
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day66_assignment

class TestDay66(unittest.TestCase):
    def test_pipe(self):
        pipe = day66_assignment.build_scaling_pipeline()
        self.assertIsInstance(pipe, Pipeline)
        self.assertEqual(pipe.steps[0][0], "scaler")

if __name__ == '__main__':
    unittest.main()
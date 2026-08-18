import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day65_assignment

class TestDay65(unittest.TestCase):
    def test_tune(self):
        X = np.random.rand(20, 2)
        y = np.random.choice([0, 1], 20)
        grid = {"max_depth": [2, 3]}
        params, score = day65_assignment.tune_decision_tree(X, y, grid)
        self.assertIn("max_depth", params)

if __name__ == '__main__':
    unittest.main()
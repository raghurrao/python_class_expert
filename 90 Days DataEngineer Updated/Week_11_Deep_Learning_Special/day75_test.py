import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day75_assignment

class TestDay75(unittest.TestCase):
    def test_rec(self):
        sim = np.array([
            [1.0, 0.8, 0.2],
            [0.8, 1.0, 0.1],
            [0.2, 0.1, 1.0]
        ])
        recs = day75_assignment.recommend_similar_items(sim, 0, 1)
        self.assertEqual(recs[0], 1)

if __name__ == '__main__':
    unittest.main()
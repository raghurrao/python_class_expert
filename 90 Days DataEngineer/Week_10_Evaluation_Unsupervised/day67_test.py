import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day67_assignment

class TestDay67(unittest.TestCase):
    def test_kmeans(self):
        X = np.array([[1.0, 1.0], [1.5, 1.0], [10.0, 10.0], [10.5, 10.0]])
        model, labels, centers = day67_assignment.run_kmeans(X, 2)
        self.assertEqual(len(centers), 2)
        self.assertNotEqual(labels[0], labels[2])

if __name__ == '__main__':
    unittest.main()
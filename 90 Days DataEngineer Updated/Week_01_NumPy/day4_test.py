import unittest
import numpy as np
import sys
import os

# Adjust path to import the assignment module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day4_assignment

class TestDay4NumPy(unittest.TestCase):

    def test_exercise_1_standardize_matrix(self):
        X = np.array([
            [1.0, 10.0],
            [2.0, 20.0],
            [3.0, 30.0]
        ])
        
        standardized = day4_assignment.standardize_matrix(X)
        
        self.assertIsInstance(standardized, np.ndarray)
        self.assertEqual(standardized.shape, X.shape)
        
        # Verify columns have mean = 0 and std = 1
        np.testing.assert_allclose(np.mean(standardized, axis=0), np.zeros(2), atol=1e-5)
        np.testing.assert_allclose(np.std(standardized, axis=0), np.ones(2), atol=1e-5)

    def test_exercise_2_add_bias_to_rows(self):
        features = np.array([
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0]
        ])
        bias = np.array([10.0, 20.0])
        
        result = day4_assignment.add_bias_to_rows(features, bias)
        
        self.assertIsInstance(result, np.ndarray)
        self.assertEqual(result.shape, features.shape)
        
        expected = np.array([
            [11.0, 12.0, 13.0],
            [24.0, 25.0, 26.0]
        ])
        np.testing.assert_allclose(result, expected)

    def test_exercise_3_compute_pairwise_distances(self):
        # 3 points in 2D space
        coords = np.array([
            [0.0, 0.0],
            [3.0, 0.0],
            [0.0, 4.0]
        ])
        
        # Distances:
        # P0-P1: 3
        # P0-P2: 4
        # P1-P2: sqrt(3^2 + 4^2) = 5
        D = day4_assignment.compute_pairwise_distances(coords)
        
        self.assertIsInstance(D, np.ndarray)
        self.assertEqual(D.shape, (3, 3))
        
        expected = np.array([
            [0.0, 3.0, 4.0],
            [3.0, 0.0, 5.0],
            [4.0, 5.0, 0.0]
        ])
        np.testing.assert_allclose(D, expected, rtol=1e-5)

if __name__ == '__main__':
    unittest.main()

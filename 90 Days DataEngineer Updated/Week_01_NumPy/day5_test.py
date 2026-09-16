import unittest
import numpy as np
import sys
import os

# Adjust path to import the assignment module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day5_assignment

class TestDay5NumPy(unittest.TestCase):

    def test_exercise_1_filter_outliers(self):
        # A normal sequence with a few outliers (1000 and -500)
        prices = np.array([10.0, 12.0, 11.0, 1000.0, 9.0, 13.0, -500.0, 11.0, 12.0, 10.0])
        
        filtered = day5_assignment.filter_outliers(prices)
        
        self.assertIsInstance(filtered, np.ndarray)
        # Check that outlier values are removed
        self.assertNotIn(1000.0, filtered)
        self.assertNotIn(-500.0, filtered)
        # Check normal values remain
        self.assertIn(10.0, filtered)
        self.assertIn(12.0, filtered)

    def test_exercise_2_relu_activation(self):
        X = np.array([
            [1.5, -2.0, 3.0],
            [-0.5, 0.0, 2.5]
        ])
        
        result = day5_assignment.relu_activation(X)
        
        # Verify in-place modification
        self.assertTrue(id(result) == id(X), "The array must be modified in-place.")
        
        expected = np.array([
            [1.5, 0.0, 3.0],
            [0.0, 0.0, 2.5]
        ])
        np.testing.assert_array_equal(result, expected)

    def test_exercise_3_find_points_in_circle(self):
        coords = np.array([
            [0.5, 0.5],   # Dist^2 = 0.5 (Inside radius 1)
            [1.0, 1.0],   # Dist^2 = 2.0 (Outside radius 1)
            [0.0, 0.9],   # Dist^2 = 0.81 (Inside radius 1)
            [-0.5, -0.5], # Dist^2 = 0.5 (Inside radius 1)
            [2.0, 0.0]    # Dist^2 = 4.0 (Outside radius 1)
        ])
        
        indices = day5_assignment.find_points_in_circle(coords, radius=1.0)
        
        self.assertIsInstance(indices, np.ndarray)
        self.assertEqual(indices.ndim, 1, "Indices array must be 1D.")
        np.testing.assert_array_equal(indices, np.array([0, 2, 3]))

if __name__ == '__main__':
    unittest.main()

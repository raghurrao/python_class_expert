import unittest
import numpy as np
import sys
import os

# Adjust path to import the assignment module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day2_assignment

class TestDay2NumPy(unittest.TestCase):

    def test_exercise_1_reshape_sensor_data(self):
        sensor_readings = np.arange(120)  # 0 to 119
        reshaped = day2_assignment.reshape_sensor_data(sensor_readings)
        
        self.assertIsInstance(reshaped, np.ndarray, "Output must be a numpy array.")
        self.assertEqual(reshaped.shape, (10, 4, 3), "Shape must be (10, 4, 3).")
        self.assertEqual(reshaped[0, 0, 0], 0)
        self.assertEqual(reshaped[9, 3, 2], 119)

    def test_exercise_2_combine_features(self):
        student_ids = np.array([101, 102, 103])
        math_scores = np.array([90, 85, 95])
        verbal_scores = np.array([88, 92, 80])
        
        combined = day2_assignment.combine_features(student_ids, math_scores, verbal_scores)
        
        self.assertIsInstance(combined, np.ndarray, "Output must be a numpy array.")
        self.assertEqual(combined.shape, (3, 3), "Shape must be (3, 3).")
        
        # Verify columns
        np.testing.assert_array_equal(combined[:, 0], student_ids)
        np.testing.assert_array_equal(combined[:, 1], math_scores)
        np.testing.assert_array_equal(combined[:, 2], verbal_scores)

    def test_exercise_3_split_dataset(self):
        dataset = np.arange(50).reshape(10, 5)  # 10 rows, 5 columns
        train, test = day2_assignment.split_dataset(dataset, split_index=7)
        
        self.assertIsInstance(train, np.ndarray, "Train set must be a numpy array.")
        self.assertIsInstance(test, np.ndarray, "Test set must be a numpy array.")
        
        self.assertEqual(train.shape, (7, 5), "Train shape must be (7, 5).")
        self.assertEqual(test.shape, (3, 5), "Test shape must be (3, 5).")
        
        # Check values
        np.testing.assert_array_equal(train, dataset[:7, :])
        np.testing.assert_array_equal(test, dataset[7:, :])

if __name__ == '__main__':
    unittest.main()

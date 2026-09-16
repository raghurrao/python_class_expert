import unittest
import numpy as np
import sys
import os

# Adjust path to import the assignment module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day1_assignment

class TestDay1NumPy(unittest.TestCase):

    def test_exercise_1_temperature_analysis(self):
        # Sample input
        temps_f = np.array([72.5, 81.0, 68.4, 90.5, 75.2, 59.0, 85.1, 79.8, 92.4, 62.1])
        
        # Call function
        celsius, count, mean_hot = day1_assignment.analyze_temperatures(temps_f)
        
        # Verify type
        self.assertIsInstance(celsius, np.ndarray, "celsius_temperatures must be a numpy ndarray.")
        
        # Verify conversion value (72.5 F -> 22.5 C)
        np.testing.assert_allclose(celsius[0], 22.5, rtol=1e-5, err_msg="Temperature conversion is incorrect.")
        
        # Verify count (above 25 C)
        self.assertEqual(count, 5, "Count of hot days (>25 C) is incorrect.")
        
        # Verify mean of hot days
        hot_temps = celsius[celsius > 25.0]
        expected_mean = np.mean(hot_temps)
        self.assertAlmostEqual(mean_hot, expected_mean, places=4, msg="Mean temperature of hot days is incorrect.")
        
        # Test edge case: no hot days
        cold_f = np.array([32.0, 50.0]) # 0 C, 10 C
        _, cold_count, cold_mean = day1_assignment.analyze_temperatures(cold_f)
        self.assertEqual(cold_count, 0)
        self.assertEqual(cold_mean, 0.0, "Mean of hot days should be 0.0 if no day exceeds 25 C.")

    def test_exercise_2_min_max_scaling(self):
        data = np.array([12.0, 45.0, 78.0, 2.0, 99.0, 34.0, 54.0, 21.0])
        scaled = day1_assignment.min_max_scale(data)
        
        # Verification
        self.assertIsInstance(scaled, np.ndarray, "Output must be a numpy ndarray.")
        self.assertAlmostEqual(np.min(scaled), 0.0, places=5)
        self.assertAlmostEqual(np.max(scaled), 1.0, places=5)
        self.assertAlmostEqual(scaled[3], 0.0, places=5) # 2.0 -> 0.0
        self.assertAlmostEqual(scaled[4], 1.0, places=5) # 99.0 -> 1.0
        
        # Test boundary case: all same numbers
        flat_data = np.ones(5) * 10
        flat_scaled = day1_assignment.min_max_scale(flat_data)
        np.testing.assert_array_equal(flat_scaled, np.zeros(5), err_msg="If min == max, return zeros.")

    def test_exercise_3_column_wise_normalization(self):
        features = np.array([
            [10.0, 200.0, 0.5],
            [12.0, 180.0, 0.7],
            [8.0, 220.0, 0.4],
            [15.0, 190.0, 0.9],
            [11.0, 210.0, 0.6]
        ])
        
        normalized = day1_assignment.normalize_columns(features)
        
        # Verification
        self.assertIsInstance(normalized, np.ndarray, "Output must be a numpy ndarray.")
        self.assertEqual(normalized.shape, features.shape, "Output shape must match input shape.")
        
        # Each column's maximum should be 1.0
        np.testing.assert_array_almost_equal(np.max(normalized, axis=0), np.array([1.0, 1.0, 1.0]), decimal=5)
        
        # Verify specific element calculation: col 0 max is 15, row 0 col 0 is 10 -> 10/15 = 0.66667
        self.assertAlmostEqual(normalized[0, 0], 10.0/15.0, places=5)
        # Verify col 1 max is 220, row 0 col 1 is 200 -> 200/220 = 0.90909
        self.assertAlmostEqual(normalized[0, 1], 200.0/220.0, places=5)

if __name__ == '__main__':
    unittest.main()

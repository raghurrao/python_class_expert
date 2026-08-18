import unittest
import numpy as np
import sys
import os

# Adjust path to import the assignment module
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day3_assignment

class TestDay3NumPy(unittest.TestCase):

    def test_exercise_1_log_transform_features(self):
        features = np.array([0, 1, 2, 9])
        transformed = day3_assignment.log_transform_features(features)
        
        self.assertIsInstance(transformed, np.ndarray)
        np.testing.assert_allclose(transformed, np.log1p(features), rtol=1e-5)

    def test_exercise_2_softmax_rows(self):
        scores = np.array([
            [1.0, 2.0, 3.0],
            [1.0, 1.0, 1.0]
        ])
        softmaxed = day3_assignment.softmax_rows(scores)
        
        self.assertIsInstance(softmaxed, np.ndarray)
        self.assertEqual(softmaxed.shape, scores.shape)
        
        # Verify row sums are equal to 1.0
        np.testing.assert_allclose(np.sum(softmaxed, axis=1), np.array([1.0, 1.0]), rtol=1e-5)
        
        # Verify specific calculations
        e_scores1 = np.exp(scores[0])
        exp_row1 = e_scores1 / np.sum(e_scores1)
        np.testing.assert_allclose(softmaxed[0], exp_row1, rtol=1e-5)
        
        e_scores2 = np.exp(scores[1])
        exp_row2 = e_scores2 / np.sum(e_scores2)
        np.testing.assert_allclose(softmaxed[1], exp_row2, rtol=1e-5)

    def test_exercise_3_predict_class(self):
        probabilities = np.array([
            [0.1, 0.7, 0.2],  # class 1 is max
            [0.8, 0.1, 0.1],  # class 0 is max
            [0.3, 0.3, 0.4]   # class 2 is max
        ])
        
        predictions = day3_assignment.predict_class(probabilities)
        
        self.assertIsInstance(predictions, np.ndarray)
        self.assertEqual(predictions.shape, (3,))
        np.testing.assert_array_equal(predictions, np.array([1, 0, 2]))

if __name__ == '__main__':
    unittest.main()

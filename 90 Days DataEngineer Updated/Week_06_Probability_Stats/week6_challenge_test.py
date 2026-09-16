import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import week6_challenge

class TestWeek6Challenge(unittest.TestCase):
    def test_prediction(self):
        probs = {"buy": (0.8, 0.1), "meeting": (0.1, 0.7)}
        self.assertTrue(week6_challenge.naive_bayes_predict(probs, 0.5, ["buy"]))
        self.assertFalse(week6_challenge.naive_bayes_predict(probs, 0.5, ["meeting"]))

if __name__ == '__main__':
    unittest.main()
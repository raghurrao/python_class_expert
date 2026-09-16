import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day36_assignment

class TestDay36(unittest.TestCase):
    def test_bayes(self):
        val = day36_assignment.bayes_spam_probability(0.5, 0.8, 0.2)
        self.assertEqual(val, 0.8)

if __name__ == '__main__':
    unittest.main()
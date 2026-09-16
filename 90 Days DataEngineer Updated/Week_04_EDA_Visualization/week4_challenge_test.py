import unittest
import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import week4_challenge

class TestWeek4Challenge(unittest.TestCase):
    def test_summary(self):
        df = pd.DataFrame({"A": [1, 2, None], "B": [4, 5, 6]})
        summary = week4_challenge.generate_eda_summary(df)
        self.assertEqual(summary["row_count"], 3)
        self.assertEqual(summary["null_count"], 1)

if __name__ == '__main__':
    unittest.main()
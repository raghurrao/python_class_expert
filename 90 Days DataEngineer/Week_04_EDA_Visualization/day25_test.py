import unittest
import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day25_assignment

class TestDay25(unittest.TestCase):
    def test_corr(self):
        df = pd.DataFrame({"A": [1, 2, 3], "B": [2, 4, 6]}) # Perfect correlation
        corr = day25_assignment.calculate_correlation_matrix(df)
        self.assertAlmostEqual(corr.loc["A", "B"], 1.0)

if __name__ == '__main__':
    unittest.main()
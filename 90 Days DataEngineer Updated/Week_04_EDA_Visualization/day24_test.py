import unittest
import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day24_assignment

class TestDay24(unittest.TestCase):
    def test_outlier_clip(self):
        df = pd.DataFrame({"val": [10.0, 11.0, 12.0, 100.0, -50.0]})
        cleaned = day24_assignment.detect_and_clip_outliers(df, "val")
        self.assertLess(cleaned["val"].max(), 100.0)

if __name__ == '__main__':
    unittest.main()

import unittest
import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day11_assignment

class TestDay11(unittest.TestCase):
    def test_parse_and_extract_dates(self):
        df = pd.DataFrame({"date": ["2026-08-18", "2025-01-01"]})
        result = day11_assignment.parse_and_extract_dates(df, "date")
        self.assertIn("year", result.columns)
        self.assertIn("month", result.columns)
        self.assertIn("day", result.columns)
        self.assertEqual(result["year"].values[0], 2026)
        self.assertEqual(result["month"].values[1], 1)

if __name__ == '__main__':
    unittest.main()

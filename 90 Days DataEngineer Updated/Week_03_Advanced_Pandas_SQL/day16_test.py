import unittest
import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day16_assignment

class TestDay16(unittest.TestCase):
    def test_pivot_sales_data(self):
        df = pd.DataFrame({
            "category": ["A", "A", "B"],
            "region": ["North", "South", "North"],
            "sales": [10, 20, 5]
        })
        pivoted = day16_assignment.pivot_sales_data(df)
        self.assertEqual(pivoted.loc["A", "North"], 10)
        self.assertEqual(pivoted.loc["A", "South"], 20)

if __name__ == '__main__':
    unittest.main()

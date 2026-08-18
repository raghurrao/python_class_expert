import unittest
import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day12_assignment

class TestDay12(unittest.TestCase):
    def test_aggregate_sales_data(self):
        df = pd.DataFrame({
            "category": ["A", "A", "B"],
            "sales": [10.0, 20.0, 5.0]
        })
        aggregated = day12_assignment.aggregate_sales_data(df)
        self.assertIn("total_sales", aggregated.columns)
        self.assertIn("average_sales", aggregated.columns)
        # Category A total_sales should be 30.0, average_sales 15.0
        row_a = aggregated.loc["A" if "A" in aggregated.index else aggregated['category']=="A"]
        self.assertEqual(row_a["total_sales"].values[0] if hasattr(row_a, "values") else row_a["total_sales"], 30.0)

if __name__ == '__main__':
    unittest.main()

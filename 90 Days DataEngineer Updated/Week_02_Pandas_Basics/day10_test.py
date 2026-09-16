import unittest
import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day10_assignment

class TestDay10(unittest.TestCase):
    def test_filter_high_value_customers(self):
        df = pd.DataFrame({
            "status": ["active", "active", "inactive"],
            "order_value": [150.0, 50.0, 200.0]
        })
        filtered = day10_assignment.filter_high_value_customers(df, 100.0)
        self.assertEqual(len(filtered), 1)
        self.assertEqual(filtered["order_value"].values[0], 150.0)

if __name__ == '__main__':
    unittest.main()

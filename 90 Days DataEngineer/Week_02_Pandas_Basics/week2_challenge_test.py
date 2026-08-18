import unittest
import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import week2_challenge

class TestWeek2Challenge(unittest.TestCase):
    def test_pipeline(self):
        df = pd.DataFrame({
            "transaction_id": [1, 1, 2, 3],
            "customer_id": [101, 101, 102, None],
            "sales_amount": [100.0, 100.0, 50.0, None]
        })
        summary = week2_challenge.clean_and_pipeline_transactions(df)
        # customer_id -1 should have total_amount = 0.0, transaction_count = 1
        row_val = summary.loc[-1]
        self.assertEqual(row_val["total_amount"], 0.0)
        self.assertEqual(row_val["transaction_count"], 1)

if __name__ == '__main__':
    unittest.main()

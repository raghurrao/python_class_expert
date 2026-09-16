import unittest
import pandas as pd
import sqlite3
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import week3_challenge

class TestWeek3Challenge(unittest.TestCase):
    def setUp(self):
        self.csv = "cust.csv"
        self.db = "trans.db"
        
        pd.DataFrame({"customer_id": [1, 2], "name": ["A", "B"]}).to_csv(self.csv, index=False)
        
        conn = sqlite3.connect(self.db)
        conn.execute("CREATE TABLE transactions (customer_id INTEGER, spend REAL)")
        conn.execute("INSERT INTO transactions VALUES (1, 50.0), (1, 20.0), (2, 80.0)")
        conn.commit()
        conn.close()

    def tearDown(self):
        for f in [self.csv, self.db]:
            if os.path.exists(f):
                os.remove(f)

    def test_pipeline(self):
        res = week3_challenge.run_analytics_pipeline(self.csv, self.db)
        # customer A spend should be 70, B should be 80
        val_a = res.loc[res['name']=='A', 'spend'].values[0] if 'name' in res.columns else res.loc['A', 'spend']
        self.assertEqual(val_a, 70.0)

if __name__ == '__main__':
    unittest.main()

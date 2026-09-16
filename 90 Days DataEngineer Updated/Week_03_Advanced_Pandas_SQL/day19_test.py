import unittest
import sqlite3
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day19_assignment

class TestDay19(unittest.TestCase):
    def setUp(self):
        self.db_path = "test_day19.db"
        conn = sqlite3.connect(self.db_path)
        conn.execute("CREATE TABLE sales (day INTEGER, revenue REAL)")
        conn.execute("INSERT INTO sales VALUES (1, 100), (2, 150), (3, 200)")
        conn.commit()
        conn.close()

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_query(self):
        df = day19_assignment.query_rolling_sales(self.db_path)
        self.assertEqual(len(df), 3)
        self.assertEqual(df.loc[df["day"]==2, "cumulative_revenue"].values[0], 250.0)
        self.assertEqual(df.loc[df["day"]==3, "cumulative_revenue"].values[0], 450.0)

if __name__ == '__main__':
    unittest.main()

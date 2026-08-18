import unittest
import sqlite3
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day18_assignment

class TestDay18(unittest.TestCase):
    def setUp(self):
        self.db_path = "test_day18.db"
        conn = sqlite3.connect(self.db_path)
        conn.execute("CREATE TABLE employees (department TEXT, salary REAL)")
        conn.execute("INSERT INTO employees VALUES ('HR', 5000), ('HR', 6000), ('IT', 8000)")
        conn.commit()
        conn.close()

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_query(self):
        df = day18_assignment.query_department_salaries(self.db_path)
        self.assertEqual(len(df), 2)
        hr_val = df.loc[df["department"]=="HR", "average_salary"].values[0]
        self.assertEqual(hr_val, 5500.0)

if __name__ == '__main__':
    unittest.main()

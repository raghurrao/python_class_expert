import unittest
import os
import sqlite3
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day17_assignment

class TestDay17(unittest.TestCase):
    def setUp(self):
        self.db_path = "test_day17.db"

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_db_creation(self):
        data = [(1, "Alice", 50000.0), (2, "Bob", 60000.0)]
        day17_assignment.create_and_populate_db(self.db_path, data)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        rows = cursor.fetchall()
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0][1], "Alice")
        conn.close()

if __name__ == '__main__':
    unittest.main()

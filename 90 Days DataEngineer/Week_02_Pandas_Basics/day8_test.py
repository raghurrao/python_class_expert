import unittest
import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day8_assignment

class TestDay8(unittest.TestCase):
    def setUp(self):
        self.csv_path = "mock_data.csv"
        df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
        df.to_csv(self.csv_path, index=False)

    def tearDown(self):
        if os.path.exists(self.csv_path):
            os.remove(self.csv_path)

    def test_load_and_inspect_data(self):
        df, shape, cols, head = day8_assignment.load_and_inspect_data(self.csv_path)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(shape, (2, 2))
        self.assertEqual(list(cols), ["A", "B"])
        self.assertEqual(len(head), 2)

if __name__ == '__main__':
    unittest.main()

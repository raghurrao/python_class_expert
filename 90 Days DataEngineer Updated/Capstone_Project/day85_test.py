import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import generate_data
import day85_eda

class TestDay85(unittest.TestCase):
    def setUp(self):
        self.csv = "temp_churn.csv"
        generate_data.generate_mock_churn_data(self.csv, size=100)

    def tearDown(self):
        if os.path.exists(self.csv):
            os.remove(self.csv)

    def test_eda(self):
        rows, mean_c, churn = day85_eda.run_capstone_eda(self.csv)
        self.assertEqual(rows, 100)
        self.assertTrue(20.0 <= mean_c <= 150.0)
        self.assertTrue(0.0 <= churn <= 1.0)

if __name__ == '__main__':
    unittest.main()
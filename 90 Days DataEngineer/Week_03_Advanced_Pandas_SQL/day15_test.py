import unittest
import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day15_assignment

class TestDay15(unittest.TestCase):
    def test_merge_customer_orders(self):
        c = pd.DataFrame({"customer_id": [1, 2], "name": ["Alice", "Bob"]})
        o = pd.DataFrame({"order_id": [101, 102], "customer_id": [1, 3]})
        merged = day15_assignment.merge_customer_orders(c, o)
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged["name"].values[0], "Alice")

if __name__ == '__main__':
    unittest.main()

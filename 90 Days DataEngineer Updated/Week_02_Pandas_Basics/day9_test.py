import unittest
import pandas as pd
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day9_assignment

class TestDay9(unittest.TestCase):
    def test_clean_customer_data(self):
        df = pd.DataFrame({
            "id": [1, 1, 2],
            "age": [30.0, 30.0, np.nan],
            "phone": [123, 123, 456]
        })
        cleaned = day9_assignment.clean_customer_data(df)
        self.assertEqual(len(cleaned), 2)  # duplicates dropped
        self.assertFalse(cleaned["age"].isna().any())  # median imputed
        self.assertEqual(cleaned.loc[cleaned["id"]==2, "age"].values[0], 30.0) # median is 30
        self.assertEqual(cleaned["phone"].dtype, object)  # converted to string/object

if __name__ == '__main__':
    unittest.main()

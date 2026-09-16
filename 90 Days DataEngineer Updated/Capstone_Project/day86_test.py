import unittest
import pandas as pd
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day86_pipeline

class TestDay86(unittest.TestCase):
    def test_preprocessor(self):
        df = pd.DataFrame({
            "age": [20.0, 40.0],
            "tenure": [12, 24],
            "monthly_charges": [50.0, 100.0],
            "contract_type": ["month-to-month", "two-year"]
        })
        preprocessor = day86_pipeline.build_preprocessing_pipeline()
        X_trans = preprocessor.fit_transform(df)
        # Expected shape: 2 samples, 3 scaled numeric + 2 categorical categories = 5 columns
        self.assertEqual(X_trans.shape, (2, 5))

if __name__ == '__main__':
    unittest.main()
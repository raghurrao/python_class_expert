import unittest
import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import generate_data
import day87_training

class TestDay87(unittest.TestCase):
    def setUp(self):
        self.csv = "temp_train.csv"
        self.model_path = "temp_model.pkl"
        generate_data.generate_mock_churn_data(self.csv, size=100)

    def tearDown(self):
        for f in [self.csv, self.model_path]:
            if os.path.exists(f): os.remove(f)

    def test_training(self):
        df = pd.read_csv(self.csv)
        model = day87_training.train_and_serialize_best_model(df, self.model_path)
        self.assertTrue(os.path.exists(self.model_path))
        self.assertTrue(hasattr(model, "predict"))

if __name__ == '__main__':
    unittest.main()
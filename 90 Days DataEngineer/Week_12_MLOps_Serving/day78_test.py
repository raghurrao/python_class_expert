import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day78_assignment

class TestDay78(unittest.TestCase):
    def setUp(self):
        self.path = "test_model.pkl"

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def test_save_load(self):
        model = "dummy_model_string"
        day78_assignment.save_model(model, self.path)
        loaded = day78_assignment.load_model(self.path)
        self.assertEqual(model, loaded)

if __name__ == '__main__':
    unittest.main()
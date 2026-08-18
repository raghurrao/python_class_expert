import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day74_assignment

class TestDay74(unittest.TestCase):
    def test_nlp(self):
        docs = ["hello world", "data science is great"]
        matrix, model = day74_assignment.extract_tfidf_features(docs)
        self.assertEqual(matrix.shape[0], 2)
        self.assertIn("hello", model.get_feature_names_out())

if __name__ == '__main__':
    unittest.main()
import unittest
from sklearn.pipeline import Pipeline
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import week10_challenge

class TestWeek10Challenge(unittest.TestCase):
    def test_clustering(self):
        pipe = week10_challenge.build_clustering_pipeline(2, 3)
        self.assertIsInstance(pipe, Pipeline)
        self.assertEqual(pipe.steps[0][0], "pca")

if __name__ == '__main__':
    unittest.main()
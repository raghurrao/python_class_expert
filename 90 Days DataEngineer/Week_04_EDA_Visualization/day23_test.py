import unittest
import pandas as pd
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day23_assignment

class TestDay23(unittest.TestCase):
    def test_plot(self):
        df = pd.DataFrame({"val": [1, 2, 2, 3, 4]})
        out = "test_dist.png"
        if os.path.exists(out): os.remove(out)
        day23_assignment.plot_distributions(df, "val", out)
        self.assertTrue(os.path.exists(out))
        if os.path.exists(out): os.remove(out)

if __name__ == '__main__':
    unittest.main()
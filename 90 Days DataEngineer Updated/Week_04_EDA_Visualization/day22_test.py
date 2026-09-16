import unittest
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day22_assignment

class TestDay22(unittest.TestCase):
    def test_plot(self):
        fn = "test_trend.png"
        if os.path.exists(fn): os.remove(fn)
        day22_assignment.plot_pricing_trends(fn)
        self.assertTrue(os.path.exists(fn))
        if os.path.exists(fn): os.remove(fn)

if __name__ == '__main__':
    unittest.main()

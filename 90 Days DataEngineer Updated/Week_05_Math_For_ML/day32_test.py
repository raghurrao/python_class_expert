import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day32_assignment

class TestDay32(unittest.TestCase):
    def test_gradient(self):
        grad = day32_assignment.compute_quadratic_gradient(2.0, 1.0)
        # df/dx = 6(2) - 4(1) = 8
        # df/dy = 4(1) - 4(2) = -4
        np.testing.assert_array_equal(grad, np.array([8.0, -4.0]))

if __name__ == '__main__':
    unittest.main()
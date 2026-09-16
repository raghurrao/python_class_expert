import unittest
import numpy as np
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day29_assignment

class TestDay29(unittest.TestCase):
    def test_solve(self):
        A = np.array([[2, 1], [1, 3]])
        b = np.array([5, 5]) # Solution should be x = [2, 1]
        x = day29_assignment.solve_linear_system(A, b)
        np.testing.assert_allclose(x, np.array([2.0, 1.0]), rtol=1e-5)

if __name__ == '__main__':
    unittest.main()
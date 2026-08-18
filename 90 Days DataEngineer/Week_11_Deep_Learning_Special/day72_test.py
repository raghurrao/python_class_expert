import unittest
import torch
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day72_assignment

class TestDay72(unittest.TestCase):
    def test_mlp(self):
        model = day72_assignment.build_model(5, 10, 2)
        x = torch.randn(3, 5)
        out = model(x)
        self.assertEqual(out.shape, (3, 2))

if __name__ == '__main__':
    unittest.main()
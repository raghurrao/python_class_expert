import unittest
import torch
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import day71_assignment

class TestDay71(unittest.TestCase):
    def test_pytorch(self):
        res = day71_assignment.create_and_sum_tensors([1, 2], [3, 4])
        self.assertTrue(torch.is_tensor(res))
        self.assertEqual(res[0].item(), 4)

if __name__ == '__main__':
    unittest.main()
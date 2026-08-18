import unittest
import torch
import torch.nn as nn
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import week11_challenge

class TestWeek11Challenge(unittest.TestCase):
    def test_step(self):
        model = nn.Linear(5, 2)
        opt = torch.optim.SGD(model.parameters(), lr=0.1)
        crit = nn.MSELoss()
        x = torch.randn(3, 5)
        y = torch.randn(3, 2)
        loss = week11_challenge.train_one_step(model, opt, crit, x, y)
        self.assertTrue(loss > 0)

if __name__ == '__main__':
    unittest.main()
import torch
import torch.nn as nn

class SimpleMLP(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
        super(SimpleMLP, self).__init__()
        self.linear1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.linear2 = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, x):
        out = self.linear1(x)
        out = self.relu(out)
        out = self.linear2(out)
        return out

def build_model(input_dim: int, hidden_dim: int, output_dim: int) -> SimpleMLP:
    return SimpleMLP(input_dim, hidden_dim, output_dim)
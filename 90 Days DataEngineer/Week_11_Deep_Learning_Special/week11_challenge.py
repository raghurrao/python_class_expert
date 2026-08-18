import torch
import torch.nn as nn

def train_one_step(model: nn.Module, optimizer: torch.optim.Optimizer, criterion: nn.Module, x: torch.Tensor, y: torch.Tensor) -> float:
    """
    Run one backpropagation step of training on batch x, y.
    Return the loss value.
    """
    model.train()
    optimizer.zero_grad()
    outputs = model(x)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()
    return float(loss.item())
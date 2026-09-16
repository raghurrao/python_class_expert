# Day 72: Deep Learning (Multi-Layer Perceptron)

Yesterday we learned about Tensors. Today we build our first Neural Network, specifically a Multi-Layer Perceptron (MLP).

---

## 1. What is an MLP?
An MLP is the simplest type of deep neural network. It consists of:
1. **Input Layer:** Takes in the features of your data.
2. **Hidden Layer(s):** Where the "deep learning" happens. Each neuron connects to all neurons in the previous layer.
3. **Output Layer:** Gives the final prediction (e.g., a single number for regression, or probabilities for classification).

### Activation Functions (ReLU)
If we just stack linear equations on top of each other ($y = mx + b$), the whole network just collapses mathematically into one giant linear equation. It wouldn't be able to learn curved, complex patterns.
We fix this by applying a non-linear **Activation Function** after every hidden layer. The most popular is **ReLU (Rectified Linear Unit)**, which simply turns all negative numbers to 0 and leaves positive numbers alone.

---

## 2. Core Concepts & Operations

### Building a Network in PyTorch
In PyTorch, we define neural networks as Python classes that inherit from `torch.nn.Module`. 

```python
import torch
import torch.nn as nn

# Define the network architecture
class SimpleMLP(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
        # Always call super() first
        super(SimpleMLP, self).__init__()
        
        # Define the layers
        self.linear1 = nn.Linear(input_dim, hidden_dim) # From Input -> Hidden
        self.relu = nn.ReLU()                           # Activation Function
        self.linear2 = nn.Linear(hidden_dim, output_dim) # From Hidden -> Output
        
    def forward(self, x):
        # This defines how data flows through the network
        out = self.linear1(x)
        out = self.relu(out)
        out = self.linear2(out)
        return out

# Initialize the network
# E.g., Predicting house price (1 output) based on 10 features, with 32 hidden neurons
model = SimpleMLP(input_dim=10, hidden_dim=32, output_dim=1)

# Pass dummy data through it (Batch of 5 samples, 10 features each)
dummy_data = torch.randn(5, 10)
predictions = model(dummy_data)

print(predictions.shape) # Output will be [5, 1] (5 predictions)
```

---

## 3. Reference Documentation
* [PyTorch nn.Module](https://pytorch.org/docs/stable/generated/torch.nn.Module.html)
* [Multilayer perceptron (Wikipedia)](https://en.wikipedia.org/wiki/Multilayer_perceptron)

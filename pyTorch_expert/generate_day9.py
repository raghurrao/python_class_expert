import json

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Day 9 \u2014 The `torch.nn` Module\n",
                "\n",
                "## 1. Learning Objectives\n",
                "- Replace manual tensor math with `nn.Linear`.\n",
                "- Build simple models quickly using `nn.Sequential`.\n",
                "- Build robust, custom models by subclassing `nn.Module`.\n",
                "- Understand how PyTorch manages parameters automatically."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Prerequisites\n",
                "- Neural Network structure (Day 8).\n",
                "- Basic Python Object-Oriented Programming (Classes and Inheritance)."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import torch\n",
                "import torch.nn as nn"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Concept Explanation\n",
                "Writing `X @ W + b` and manually initializing weight tensors with `requires_grad=True` every time is tedious and error-prone.\n",
                "\n",
                "PyTorch provides `torch.nn`, a library of pre-built neural network layers. \n",
                "- `nn.Linear(in_features, out_features)` replaces `X @ W + b`.\n",
                "- `nn.ReLU()` replaces `torch.relu()`.\n",
                "\n",
                "Most importantly, PyTorch provides `nn.Module`. Every custom neural network you build will inherit from `nn.Module`. It automatically registers your weights and biases as \"parameters\" so the optimizer can find and update them."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 8. Simple Example 1: `nn.Sequential`\n",
                "`nn.Sequential` is the easiest way to build a network where data flows in a straight line from layer to layer."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# A network that takes 10 features, maps to 32 hidden neurons, then outputs 1 prediction.\n",
                "simple_model = nn.Sequential(\n",
                "    nn.Linear(in_features=10, out_features=32),\n",
                "    nn.ReLU(),\n",
                "    nn.Linear(in_features=32, out_features=1)\n",
                ")\n",
                "\n",
                "dummy_x = torch.randn(5, 10) # 5 samples, 10 features\n",
                "predictions = simple_model(dummy_x) # Notice we call the model like a function\n",
                "\n",
                "print(\"Predictions shape:\", predictions.shape)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 9. Simple Example 2: Subclassing `nn.Module`\n",
                "`nn.Sequential` is great, but what if your network needs multiple inputs, or skips layers (ResNets)? You must use `nn.Module`. This is the **standard PyTorch way**."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "class MyCustomNetwork(nn.Module):\n",
                "    def __init__(self):\n",
                "        # ALWAYS call the super init first\n",
                "        super(MyCustomNetwork, self).__init__()\n",
                "        \n",
                "        # Define your layers here\n",
                "        self.layer1 = nn.Linear(10, 32)\n",
                "        self.relu = nn.ReLU()\n",
                "        self.layer2 = nn.Linear(32, 1)\n",
                "        \n",
                "    def forward(self, x):\n",
                "        # Define the forward pass logic here\n",
                "        x = self.layer1(x)\n",
                "        x = self.relu(x)\n",
                "        x = self.layer2(x)\n",
                "        return x\n",
                "\n",
                "# Instantiate the model\n",
                "custom_model = MyCustomNetwork()\n",
                "predictions2 = custom_model(dummy_x)\n",
                "print(\"Custom Model Predictions shape:\", predictions2.shape)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 10. Experiment: Inspecting Parameters\n",
                "Because we inherited from `nn.Module`, PyTorch knows about our layers."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "print(\"Total layers with parameters:\", len(list(custom_model.parameters())))\n",
                "\n",
                "# Let's look at the shape of the first parameter (Weight of layer1)\n",
                "print(\"Layer 1 weight shape:\", list(custom_model.parameters())[0].shape)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 11. Practice Exercise 1: Build a Deep Network\n",
                "Using the `nn.Module` class structure, build a network for an image dataset. The flattened images have `28 * 28 = 784` features.\n",
                "The network should have:\n",
                "1. Hidden layer with 128 neurons.\n",
                "2. ReLU activation.\n",
                "3. Hidden layer with 64 neurons.\n",
                "4. ReLU activation.\n",
                "5. Output layer with 10 neurons (representing 10 digit classes)."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Write your code here"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# SOLUTION\n",
                "class DigitClassifier(nn.Module):\n",
                "    def __init__(self):\n",
                "        super().__init__()\n",
                "        self.fc1 = nn.Linear(784, 128)\n",
                "        self.fc2 = nn.Linear(128, 64)\n",
                "        self.fc3 = nn.Linear(64, 10)\n",
                "        self.relu = nn.ReLU()\n",
                "        \n",
                "    def forward(self, x):\n",
                "        x = self.relu(self.fc1(x))\n",
                "        x = self.relu(self.fc2(x))\n",
                "        x = self.fc3(x) # Usually no activation on final output before loss function\n",
                "        return x\n",
                "\n",
                "model = DigitClassifier()\n",
                "print(model)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 13. Debugging Challenge\n",
                "A developer wrote this model, but calling `list(bad_model.parameters())` returns an empty list `[]`. \n",
                "Because of this, the optimizer won't be able to update the weights. Find the bug."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "class BadModel(nn.Module):\n",
                "    def __init__(self):\n",
                "        # super().__init__() is missing!\n",
                "        self.layer = nn.Linear(10, 2)\n",
                "        \n",
                "    def forward(self, x):\n",
                "        return self.layer(x)\n",
                "\n",
                "# bad_model = BadModel()\n",
                "# print(list(bad_model.parameters())) # Uncomment to see error"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Solution:** The developer forgot to call `super().__init__()` (or `super(BadModel, self).__init__()`) inside the `__init__` method. Without this, the `nn.Module` internals are never initialized, and it fails to track the assigned layers."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 17. Interview Questions\n",
                "1. **When should you use `nn.Sequential` vs subclassing `nn.Module`?**\n",
                "   *Answer*: Use `nn.Sequential` for simple, straight-line feedforward networks. Subclass `nn.Module` when you need complex logic in the forward pass, like multiple inputs, residual connections (skip connections), or dynamic loops.\n",
                "2. **Why do we call the model like a function `model(x)` instead of `model.forward(x)`?**\n",
                "   *Answer*: `nn.Module` implements the `__call__` python magic method. Calling `model(x)` not only runs `forward(x)`, but it also triggers PyTorch's \"hooks\" which are necessary for things like Autograd and hardware synchronization."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 19. Day Summary\n",
                "- `nn.Linear(in, out)` handles the Weight and Bias tensor creation and math automatically.\n",
                "- `nn.Sequential` is the fast way to stack layers.\n",
                "- Subclassing `nn.Module` with `__init__` and `forward` is the professional way to build networks.\n",
                "- Always call `super().__init__()`!"
            ]
        }
    ],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 4
}

with open("Day_09_torch_nn.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Created Day_09_torch_nn.ipynb")

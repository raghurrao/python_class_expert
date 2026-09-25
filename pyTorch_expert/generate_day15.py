import json

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Day 15 \u2014 Overfitting & Regularization\n",
                "\n",
                "## 1. Learning Objectives\n",
                "- Diagnose Overfitting and Underfitting from loss curves.\n",
                "- Implement **Dropout** (`nn.Dropout`).\n",
                "- Implement **Weight Decay** (L2 Regularization) via the Optimizer.\n",
                "- Understand the concept of **Early Stopping**.\n",
                "- Conceptualize Data Augmentation."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Prerequisites\n",
                "- Train/Validation tracking (Day 13).\n",
                "- `torch.nn` layer stacking (Day 9)."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import torch\n",
                "import torch.nn as nn\n",
                "import torch.optim as optim\n",
                "import matplotlib.pyplot as plt"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Concept Explanation\n",
                "**Underfitting**: The model is too simple (or hasn't trained long enough) to learn the patterns. Both Train and Validation loss are high.\n",
                "\n",
                "**Overfitting**: The model is too complex and has memorized the exact training data, including the noise. \n",
                "- Train loss keeps going down to 0.\n",
                "- Validation loss goes down initially, but then starts **going back up**.\n",
                "\n",
                "**Regularization** refers to techniques we use to prevent Overfitting."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. Technique 1: Dropout\n",
                "Dropout randomly turns off a percentage of neurons in a layer during training. This prevents the network from relying too heavily on any single neuron and forces it to learn redundant, robust features.\n",
                "We use `nn.Dropout(p=0.5)`."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# 8. Simple Example: Dropout in Action\n",
                "dropout_layer = nn.Dropout(p=0.5)\n",
                "dummy_inputs = torch.ones(1, 10)\n",
                "\n",
                "print(\"Original:\", dummy_inputs)\n",
                "print(\"During Training (model.train()):\", dropout_layer(dummy_inputs))\n",
                "\n",
                "# Notice that the active neurons are scaled up by 1/(1-p) to maintain the overall magnitude of the signal!\n",
                "dropout_layer.eval()\n",
                "print(\"During Evaluation (model.eval()):\", dropout_layer(dummy_inputs))"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 5. Technique 2: Weight Decay\n",
                "Weight Decay (L2 Regularization) mathematically penalizes large weights. If a weight gets too large, it dominates the network. By keeping weights small, the network is smoother and less prone to overfitting.\n",
                "\n",
                "In PyTorch, you don't add this to the Loss Function manually. You simply pass `weight_decay` to the optimizer."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "model = nn.Linear(10, 2)\n",
                "# AdamW is Adam with mathematically correct Weight Decay\n",
                "optimizer = optim.AdamW(model.parameters(), lr=0.001, weight_decay=1e-4)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 6. Technique 3: Early Stopping\n",
                "If the Validation Loss starts going back up, stop training! Revert the model's weights back to the epoch where Validation Loss was at its lowest."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 11. Practice Exercise 1: Build a Regularized Model\n",
                "Build an `nn.Module` with 3 Linear Layers. Add a `ReLU` and a `Dropout(p=0.3)` layer after the first and second Linear layers. Do NOT add Dropout after the final layer."
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
                "class RegularizedModel(nn.Module):\n",
                "    def __init__(self):\n",
                "        super().__init__()\n",
                "        self.fc1 = nn.Linear(100, 64)\n",
                "        self.fc2 = nn.Linear(64, 32)\n",
                "        self.fc3 = nn.Linear(32, 10)\n",
                "        self.relu = nn.ReLU()\n",
                "        self.dropout = nn.Dropout(p=0.3)\n",
                "        \n",
                "    def forward(self, x):\n",
                "        x = self.dropout(self.relu(self.fc1(x)))\n",
                "        x = self.dropout(self.relu(self.fc2(x)))\n",
                "        x = self.fc3(x)\n",
                "        return x\n",
                "\n",
                "my_model = RegularizedModel()\n",
                "print(my_model)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 13. Debugging Challenge\n",
                "A student added Dropout to their model, but now their validation accuracy is terrible and fluctuates wildly every time they run the validation loop. Find the bug."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# student_model = RegularizedModel()\n",
                "# \n",
                "# --- Validation Loop ---\n",
                "# with torch.no_grad():\n",
                "#     val_preds = student_model(val_x)\n",
                "#     # ... calculate metrics"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Solution:** They forgot to call `student_model.eval()`! Because `eval()` was not called, the Dropout layers continued to randomly turn off neurons during the validation phase, causing random and terrible predictions. This is exactly why `model.eval()` exists."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 17. Interview Questions\n",
                "1. **What does `model.eval()` actually do under the hood?**\n",
                "   *Answer*: It toggles the internal `training` boolean flag on every module in the network to `False`. Layers like `nn.Dropout` and `nn.BatchNorm2d` check this flag during the forward pass. If `False`, Dropout acts as an identity function (does nothing).\n",
                "2. **Why do we scale up the active neurons during training in PyTorch's Dropout implementation?**\n",
                "   *Answer*: If we drop 50% of neurons, the total sum of the signals going to the next layer is halved. If we train like this, but evaluate with 100% of neurons on, the next layer will be overwhelmed by signals that are twice as large. Scaling the remaining neurons by `1/(1-p)` during training ensures the expected sum remains constant between train and eval modes."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 19. Day Summary\n",
                "- Overfitting = Train Loss goes down, Val Loss goes up.\n",
                "- `nn.Dropout` prevents neurons from co-adapting.\n",
                "- `weight_decay` in the optimizer penalizes massive weight values.\n",
                "- `model.eval()` is absolutely mandatory if your model contains Dropout."
            ]
        }
    ],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 4
}

with open("Day_15_Overfitting_Regularization.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Created Day_15_Overfitting_Regularization.ipynb")

import json

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Day 23 \u2014 `torch.nn.Conv2d` & CNN Architectures\n",
                "\n",
                "## 1. Learning Objectives\n",
                "- Build a real Convolutional Neural Network using `nn.Conv2d`.\n",
                "- Master the `in_channels` and `out_channels` arguments.\n",
                "- Combine Convolutions, Activations, and Pooling in `nn.Sequential`.\n",
                "- Calculate the exact tensor shape required to transition from Convolutional layers to Linear layers."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Prerequisites\n",
                "- CNN Fundamentals (Day 22)\n",
                "- `nn.Module` (Day 9)"
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
                "## 3. Concept Explanation: `in_channels` and `out_channels`\n",
                "When you create an `nn.Linear(in_features, out_features)`, you are mapping 1D vectors.\n",
                "When you create an `nn.Conv2d(in_channels, out_channels, kernel_size)`, you are mapping entire 3D feature maps.\n",
                "\n",
                "- **`in_channels`**: How many \"layers\" deep is the input image? (e.g., Grayscale = 1, RGB = 3).\n",
                "- **`out_channels`**: How many different kernels/filters do you want this layer to learn? (e.g., if `out_channels=16`, the layer learns 16 different 3x3 edge detectors, producing a 16-channel feature map).\n",
                "- **`kernel_size`**: Usually 3 (for a 3x3 square)."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 8. Simple Example: Building a CNN\n",
                "Let's build a standard CNN for a 32x32 RGB image (like CIFAR-10)."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "class SimpleCNN(nn.Module):\n",
                "    def __init__(self):\n",
                "        super().__init__()\n",
                "        \n",
                "        # Block 1: Input is [Batch, 3, 32, 32]\n",
                "        self.conv1 = nn.Conv2d(in_channels=3, out_channels=16, kernel_size=3, padding=1)\n",
                "        self.relu1 = nn.ReLU()\n",
                "        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)\n",
                "        # After pool1, spatial dimensions are halved: 32 -> 16. Shape: [Batch, 16, 16, 16]\n",
                "        \n",
                "        # Block 2\n",
                "        # Notice that in_channels here MUST match the out_channels of the previous layer!\n",
                "        self.conv2 = nn.Conv2d(in_channels=16, out_channels=32, kernel_size=3, padding=1)\n",
                "        self.relu2 = nn.ReLU()\n",
                "        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)\n",
                "        # After pool2, spatial dimensions are halved again: 16 -> 8. Shape: [Batch, 32, 8, 8]\n",
                "        \n",
                "        # Transition to Linear (Fully Connected) Classifier\n",
                "        # We must flatten the [32, 8, 8] tensor into a 1D vector. \n",
                "        # The math is: 32 channels * 8 height * 8 width = 2048 features.\n",
                "        self.fc1 = nn.Linear(32 * 8 * 8, 256)\n",
                "        self.fc2 = nn.Linear(256, 10) # 10 Output classes\n",
                "        \n",
                "    def forward(self, x):\n",
                "        # Feature Extraction\n",
                "        x = self.pool1(self.relu1(self.conv1(x)))\n",
                "        x = self.pool2(self.relu2(self.conv2(x)))\n",
                "        \n",
                "        # Flatten: keep batch dimension (0), flatten the rest (-1)\n",
                "        x = x.view(x.size(0), -1)\n",
                "        \n",
                "        # Classification\n",
                "        x = torch.relu(self.fc1(x))\n",
                "        x = self.fc2(x)\n",
                "        return x\n",
                "\n",
                "model = SimpleCNN()\n",
                "dummy_img = torch.randn(1, 3, 32, 32)\n",
                "out = model(dummy_img)\n",
                "print(\"Output shape:\", out.shape)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 9. Code Walkthrough: Cleaner Code with `nn.Sequential`\n",
                "The `__init__` and `forward` pass above are very messy. In Computer Vision, we heavily rely on `nn.Sequential` to group layers into logical \"Blocks\"."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "class CleanCNN(nn.Module):\n",
                "    def __init__(self):\n",
                "        super().__init__()\n",
                "        self.features = nn.Sequential(\n",
                "            # Block 1\n",
                "            nn.Conv2d(3, 16, 3, padding=1),\n",
                "            nn.ReLU(),\n",
                "            nn.MaxPool2d(2, 2),\n",
                "            \n",
                "            # Block 2\n",
                "            nn.Conv2d(16, 32, 3, padding=1),\n",
                "            nn.ReLU(),\n",
                "            nn.MaxPool2d(2, 2)\n",
                "        )\n",
                "        \n",
                "        self.classifier = nn.Sequential(\n",
                "            nn.Linear(32 * 8 * 8, 256),\n",
                "            nn.ReLU(),\n",
                "            nn.Linear(256, 10)\n",
                "        )\n",
                "\n",
                "    def forward(self, x):\n",
                "        x = self.features(x)\n",
                "        x = x.view(x.size(0), -1) # Flatten\n",
                "        x = self.classifier(x)\n",
                "        return x"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 11. Practice Exercise 1: The Transition Math\n",
                "You are building a CNN for a `64x64` RGB image.\n",
                "- Block 1: Conv2d(out=32, pad=1), ReLU, MaxPool(2,2)\n",
                "- Block 2: Conv2d(out=64, pad=1), ReLU, MaxPool(2,2)\n",
                "- Block 3: Conv2d(out=128, pad=1), ReLU, MaxPool(2,2)\n",
                "\n",
                "Write the correct `in_features` for the first Linear layer in the classifier."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# SOLUTION:\n",
                "# Initial: 64x64\n",
                "# After Block 1 MaxPool: 32x32\n",
                "# After Block 2 MaxPool: 16x16\n",
                "# After Block 3 MaxPool: 8x8\n",
                "# Channels after Block 3 = 128\n",
                "# \n",
                "# Math: 128 * 8 * 8 = 8192\n",
                "# \n",
                "# self.fc1 = nn.Linear(8192, 512)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 13. Debugging Challenge\n",
                "A student gets this error when creating their model:\n",
                "`RuntimeError: mat1 and mat2 shapes cannot be multiplied (64x2048 and 4096x256)`\n",
                "\n",
                "They are using a batch size of 64. What did they do wrong in their `__init__` function?"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Solution:** They calculated the transition math incorrectly. The tensor flattened to a size of `2048` features, but their `nn.Linear` was defined as `nn.Linear(4096, 256)`. They need to change their code to `nn.Linear(2048, 256)`."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 17. Interview Questions\n",
                "1. **What is the purpose of stacking multiple Convolutional layers?**\n",
                "   *Answer*: The first layer learns very simple, low-level features (like edges and colors). The second layer combines those edges to find mid-level features (like circles or textures). Deep layers combine those into high-level semantic features (like \"dog ears\" or \"car wheels\").\n",
                "2. **Why do we increase the number of channels (e.g., 16 -> 32 -> 64) as we go deeper into the network?**\n",
                "   *Answer*: As spatial dimensions shrink via Pooling, we lose spatial resolution. We increase the number of channels to preserve and expand the *semantic* representation capacity of the network."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 19. Day Summary\n",
                "- `nn.Conv2d` expects `[Batch, Channels, Height, Width]`.\n",
                "- `in_channels` of a Conv layer must match the `out_channels` of the previous layer.\n",
                "- Group layers into `self.features` and `self.classifier` using `nn.Sequential` for clean code.\n",
                "- The trickiest part of CNN design is calculating `Channels * Height * Width` before the Linear layer."
            ]
        }
    ],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 4
}

with open("Day_23_Conv2d.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Created Day_23_Conv2d.ipynb")

import json

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Day 21 \u2014 Project: Fashion-MNIST Image Classifier\n",
                "\n",
                "## 1. Learning Objectives\n",
                "- Synthesize all knowledge from Phase 3 into a complete Computer Vision pipeline.\n",
                "- Download and use `torchvision.datasets`.\n",
                "- Flatten images to work with a Linear (Fully Connected) Neural Network.\n",
                "- Train the model using the GPU.\n",
                "- Evaluate performance using a Confusion Matrix.\n",
                "- Save the final model as a `.pth` checkpoint."
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
                "import torchvision\n",
                "import torchvision.transforms as transforms\n",
                "from torch.utils.data import DataLoader\n",
                "import matplotlib.pyplot as plt\n",
                "import numpy as np"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Step 1: Device Configuration\n",
                "Always start by defining the device."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')\n",
                "print(f\"Using device: {device}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Step 2: Dataset & DataLoader\n",
                "We will use `torchvision` to download the Fashion-MNIST dataset. These are 28x28 grayscale images of clothing items (10 classes). \n",
                "We must transform them into PyTorch Tensors."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# 1. Define Transform\n",
                "transform = transforms.Compose([\n",
                "    transforms.ToTensor(), # Converts PIL Image to PyTorch Tensor (C, H, W) and scales to [0, 1]\n",
                "    transforms.Normalize((0.5,), (0.5,)) # Standardize to mean 0.5, std 0.5\n",
                "])\n",
                "\n",
                "# 2. Download Datasets\n",
                "# (Setting download=True downloads it to a './data' folder)\n",
                "train_dataset = torchvision.datasets.FashionMNIST(root='./data', train=True, transform=transform, download=True)\n",
                "test_dataset = torchvision.datasets.FashionMNIST(root='./data', train=False, transform=transform, download=True)\n",
                "\n",
                "# 3. Create DataLoaders\n",
                "batch_size = 64\n",
                "train_loader = DataLoader(dataset=train_dataset, batch_size=batch_size, shuffle=True)\n",
                "test_loader = DataLoader(dataset=test_dataset, batch_size=batch_size, shuffle=False)\n",
                "\n",
                "print(f\"Training samples: {len(train_dataset)}\")\n",
                "print(f\"Testing samples: {len(test_dataset)}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Step 3: Define the Neural Network\n",
                "Because we haven't learned CNNs yet (that's Phase 4!), we will use a standard `nn.Linear` network. \n",
                "This means we must FLATTEN the `[Batch, 1, 28, 28]` images into `[Batch, 784]` before feeding them to the layers."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "class FashionClassifier(nn.Module):\n",
                "    def __init__(self):\n",
                "        super().__init__()\n",
                "        # 28 * 28 = 784\n",
                "        self.fc1 = nn.Linear(784, 256)\n",
                "        self.fc2 = nn.Linear(256, 128)\n",
                "        self.fc3 = nn.Linear(128, 10) # 10 classes output\n",
                "        \n",
                "        self.relu = nn.ReLU()\n",
                "        self.dropout = nn.Dropout(p=0.3)\n",
                "        \n",
                "    def forward(self, x):\n",
                "        # 1. Flatten the spatial dimensions: [Batch, 1, 28, 28] -> [Batch, 784]\n",
                "        x = x.view(x.size(0), -1) \n",
                "        \n",
                "        # 2. Forward pass\n",
                "        x = self.dropout(self.relu(self.fc1(x)))\n",
                "        x = self.dropout(self.relu(self.fc2(x)))\n",
                "        x = self.fc3(x) # Raw logits out (CrossEntropyLoss handles the Softmax)\n",
                "        return x\n",
                "\n",
                "# Send model to GPU immediately\n",
                "model = FashionClassifier().to(device)\n",
                "print(model)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Step 4: Loss, Optimizer, and Training Loop\n",
                "**Your task:** Complete the training loop. Make sure to send `images` and `labels` to the `device`!"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "criterion = nn.CrossEntropyLoss()\n",
                "optimizer = optim.AdamW(model.parameters(), lr=0.001)\n",
                "\n",
                "epochs = 5\n",
                "train_losses = []\n",
                "\n",
                "for epoch in range(epochs):\n",
                "    model.train()\n",
                "    running_loss = 0.0\n",
                "    \n",
                "    for images, labels in train_loader:\n",
                "        # 1. SEND DATA TO GPU\n",
                "        images = images.to(device)\n",
                "        labels = labels.to(device)\n",
                "        \n",
                "        # 2. Forward, Loss, Zero, Backward, Step\n",
                "        outputs = model(images)\n",
                "        loss = criterion(outputs, labels)\n",
                "        \n",
                "        optimizer.zero_grad()\n",
                "        loss.backward()\n",
                "        optimizer.step()\n",
                "        \n",
                "        running_loss += loss.item()\n",
                "        \n",
                "    avg_loss = running_loss / len(train_loader)\n",
                "    train_losses.append(avg_loss)\n",
                "    print(f\"Epoch [{epoch+1}/{epochs}] | Loss: {avg_loss:.4f}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Step 5: Evaluation & Confusion Matrix\n",
                "Now we evaluate the model on the `test_loader`."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "model.eval()\n",
                "correct = 0\n",
                "total = 0\n",
                "all_preds = []\n",
                "all_labels = []\n",
                "\n",
                "with torch.no_grad():\n",
                "    for images, labels in test_loader:\n",
                "        images = images.to(device)\n",
                "        labels = labels.to(device)\n",
                "        \n",
                "        outputs = model(images)\n",
                "        \n",
                "        # Get the index of the max logit\n",
                "        _, predicted = torch.max(outputs.data, 1)\n",
                "        \n",
                "        total += labels.size(0)\n",
                "        correct += (predicted == labels).sum().item()\n",
                "        \n",
                "        all_preds.extend(predicted.cpu().numpy())\n",
                "        all_labels.extend(labels.cpu().numpy())\n",
                "\n",
                "print(f\"\\nTest Accuracy: {(100 * correct / total):.2f}%\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Step 6: Save the Model\n",
                "We want to save this trained checkpoint so we don't have to retrain."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "checkpoint = {\n",
                "    'model_state': model.state_dict(),\n",
                "    'optimizer_state': optimizer.state_dict(),\n",
                "    'epochs_trained': epochs\n",
                "}\n",
                "torch.save(checkpoint, 'fashion_mnist_checkpoint.pth')\n",
                "print(\"Model saved to 'fashion_mnist_checkpoint.pth'\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## Phase 3 Conclusion\n",
                "Congratulations! You've built a robust, professional-grade Deep Learning pipeline. \n",
                "\n",
                "However, note that flattening a 2D image into a 1D vector (`x.view(x.size(0), -1)`) destroys all spatial information (like the fact that a sleeve is next to a collar). To achieve true Computer Vision mastery, we must preserve spatial structure. \n",
                "\n",
                "In **Phase 4**, we introduce **Convolutional Neural Networks (CNNs)**."
            ]
        }
    ],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 4
}

with open("Day_21_Project.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Created Day_21_Project.ipynb")

import json

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Day 18 \u2014 Model Saving & Loading\n",
                "\n",
                "## 1. Learning Objectives\n",
                "- Understand what a `state_dict` is.\n",
                "- Learn the PyTorch Best Practices for saving models.\n",
                "- Save and load a trained model using `torch.save` and `torch.load`.\n",
                "- Save checkpoints (including optimizer states) to resume training later."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Prerequisites\n",
                "- `nn.Module` (Day 9)\n",
                "- Optimizers (Day 11)"
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
                "import os"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Concept Explanation\n",
                "Once you train a model for 5 days on a GPU, you don't want to lose it when you close your script. You must save it to your hard drive.\n",
                "\n",
                "There are two ways to save a model in PyTorch:\n",
                "1. **Save the entire model (Not Recommended)**: Saves the architecture code AND the weights using Python's `pickle`. It is fragile; if you move your code to another folder, the model might fail to load.\n",
                "2. **Save only the `state_dict` (Highly Recommended)**: Saves ONLY the weights (parameters). You must instantiate the `nn.Module` class first, and then load the weights into it. This is robust and standard practice."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. What is a `state_dict`?\n",
                "A `state_dict` is simply a Python dictionary that maps each layer's name to its parameter tensor."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "class SimpleModel(nn.Module):\n",
                "    def __init__(self):\n",
                "        super().__init__()\n",
                "        self.layer1 = nn.Linear(3, 2)\n",
                "        self.layer2 = nn.Linear(2, 1)\n",
                "        \n",
                "model = SimpleModel()\n",
                "\n",
                "print(\"Model's state_dict:\")\n",
                "for param_tensor in model.state_dict():\n",
                "    print(param_tensor, \"\\t\", model.state_dict()[param_tensor].size())"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 8. Simple Example: Saving and Loading (The Right Way)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# --- SAVING ---\n",
                "# Extension is usually .pt or .pth\n",
                "save_path = \"model_weights.pth\"\n",
                "torch.save(model.state_dict(), save_path)\n",
                "print(f\"Saved to {save_path}\")\n",
                "\n",
                "# --- LOADING ---\n",
                "# 1. You MUST create an instance of the model first\n",
                "loaded_model = SimpleModel()\n",
                "\n",
                "# 2. Load the dictionary from disk\n",
                "weights_dict = torch.load(save_path)\n",
                "\n",
                "# 3. Inject the weights into the model\n",
                "loaded_model.load_state_dict(weights_dict)\n",
                "\n",
                "# 4. Put into eval mode if you are going to use it for inference\n",
                "loaded_model.eval()\n",
                "print(\"Model loaded successfully!\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 9. Advanced Example: Saving Checkpoints\n",
                "What if your computer crashes on Epoch 50 of 100? If you just save the model weights, you lose the Optimizer's internal state (e.g., Adam's momentum buffers), meaning you can't resume training smoothly.\n",
                "\n",
                "**Best Practice for Checkpoints**: Save a dictionary containing the epoch, model state, optimizer state, and current loss."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "optimizer = optim.Adam(model.parameters(), lr=0.01)\n",
                "epoch = 50\n",
                "loss = 0.45\n",
                "\n",
                "# Save Checkpoint\n",
                "checkpoint = {\n",
                "    'epoch': epoch,\n",
                "    'model_state_dict': model.state_dict(),\n",
                "    'optimizer_state_dict': optimizer.state_dict(),\n",
                "    'loss': loss\n",
                "}\n",
                "torch.save(checkpoint, \"checkpoint_epoch_50.pth\")\n",
                "print(\"Checkpoint saved!\")\n",
                "\n",
                "# Load Checkpoint\n",
                "loaded_checkpoint = torch.load(\"checkpoint_epoch_50.pth\")\n",
                "\n",
                "# Restore states\n",
                "model.load_state_dict(loaded_checkpoint['model_state_dict'])\n",
                "optimizer.load_state_dict(loaded_checkpoint['optimizer_state_dict'])\n",
                "resumed_epoch = loaded_checkpoint['epoch']\n",
                "\n",
                "print(f\"Ready to resume training from Epoch {resumed_epoch}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 11. Practice Exercise 1: Cleanup\n",
                "Write a quick python script using the `os` module to delete the two `.pth` files we just created so we don't clutter the directory."
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
                "if os.path.exists(\"model_weights.pth\"):\n",
                "    os.remove(\"model_weights.pth\")\n",
                "if os.path.exists(\"checkpoint_epoch_50.pth\"):\n",
                "    os.remove(\"checkpoint_epoch_50.pth\")\n",
                "print(\"Cleanup complete.\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 13. Debugging Challenge\n",
                "You train a massive model using PyTorch and save it using `torch.save(model.state_dict(), \"huge_model.pth\")`.\n",
                "You send `huge_model.pth` to your coworker. They run `loaded_model = torch.load(\"huge_model.pth\")` and then try to run inference, but they get an error saying \"dict object is not callable\". Why?"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Solution:** The `.pth` file only contains a python dictionary mapping string names to numbers (the weights). The coworker forgot that they must first instantiate the exact same `nn.Module` python class in their code, and then use `model.load_state_dict(torch.load(\"huge_model.pth\"))`."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 17. Interview Questions\n",
                "1. **Why is it recommended to save `state_dict` rather than the entire model using `torch.save(model)`?**\n",
                "   *Answer*: Saving the entire model pickles the python class structure. If you refactor your code, change a file name, or move the model class to a different module, PyTorch won't be able to find the class definitions when loading, and it will break. `state_dict` is purely data (tensors) and is extremely robust.\n",
                "2. **Why do we need to save the optimizer's state dictionary when creating a checkpoint?**\n",
                "   *Answer*: Optimizers like Adam maintain internal moving averages of gradients (momentum) for every single weight. If you resume training with a fresh optimizer, it starts from scratch, which can cause a sudden, massive spike in loss and destabilize training."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 19. Day Summary\n",
                "- Use `model.state_dict()` to extract weights.\n",
                "- Use `torch.save()` to write to `.pth`.\n",
                "- Use `model.load_state_dict(torch.load(...))` to read them back.\n",
                "- Always save a \"Checkpoint Dictionary\" containing the epoch, model dict, and optimizer dict if you plan to resume training."
            ]
        }
    ],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 4
}

with open("Day_18_Model_Saving_Loading.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Created Day_18_Model_Saving_Loading.ipynb")

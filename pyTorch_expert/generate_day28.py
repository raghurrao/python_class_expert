import json

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Day 28 \u2014 RNNs, LSTMs & Sequence Data\n",
                "\n",
                "## 1. Learning Objectives\n",
                "- Understand how to handle data where *order matters* (Time Series, Text).\n",
                "- Learn the PyTorch Sequence shape: `[Batch, Sequence_Length, Features]`.\n",
                "- Understand the internal **Hidden State**.\n",
                "- Implement `nn.RNN` and `nn.LSTM` layers."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Prerequisites\n",
                "- Linear Layers (Day 9)\n",
                "- Tensor Shapes (Day 4)"
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
                "## 3. Concept Explanation: The Sequence Problem\n",
                "If I pass the sentence \"The dog bit the man\" into a Linear Layer or a CNN, it treats the words as independent inputs. It would think \"The man bit the dog\" means the exact same thing.\n",
                "\n",
                "For Text, Audio, and Stock Prices, **order matters**. \n",
                "\n",
                "**Recurrent Neural Networks (RNNs)** solve this by reading the sequence one step at a time, and maintaining a \"Memory\" (called the **Hidden State**) of what it read in the past."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. The Sequence Shape (`[Batch, Seq_Len, Features]`)\n",
                "If we have a batch of 32 sentences, each sentence is exactly 10 words long, and each word is represented by a vector of 50 numbers (an embedding), our shape is `[32, 10, 50]`."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# 8. Simple Example: Using nn.RNN\n",
                "# Let's create dummy data: 1 sequence, 5 time steps, 3 features per step\n",
                "dummy_sequence = torch.randn(1, 5, 3)\n",
                "\n",
                "# IMPORTANT: batch_first=True tells PyTorch our shape is [Batch, Seq, Feature]\n",
                "# PyTorch's default is actually [Seq, Batch, Feature] for legacy performance reasons!\n",
                "rnn = nn.RNN(input_size=3, hidden_size=10, batch_first=True)\n",
                "\n",
                "# The RNN returns TWO things:\n",
                "# 1. out: The output at EVERY time step\n",
                "# 2. hidden: The final \"memory\" state at the very end of the sequence\n",
                "out, hidden = rnn(dummy_sequence)\n",
                "\n",
                "print(\"Output shape (all steps):\", out.shape)   # [1, 5, 10]\n",
                "print(\"Hidden shape (final step):\", hidden.shape) # [1, 1, 10]"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 9. Code Walkthrough: Classification with RNNs\n",
                "If you want to classify the *entire sentence* (e.g., Sentiment Analysis: Positive/Negative), you usually ignore the outputs from steps 1, 2, 3, and 4. You only care about what the RNN thought at the **very last step**, after it has read the whole sentence."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "class RNNClassifier(nn.Module):\n",
                "    def __init__(self):\n",
                "        super().__init__()\n",
                "        self.rnn = nn.RNN(input_size=3, hidden_size=10, batch_first=True)\n",
                "        # Linear layer takes the final hidden state and predicts 2 classes\n",
                "        self.fc = nn.Linear(10, 2) \n",
                "        \n",
                "    def forward(self, x):\n",
                "        out, hidden = self.rnn(x)\n",
                "        \n",
                "        # hidden is shape [num_layers, Batch, Hidden_Size]\n",
                "        # We squeeze the num_layers dimension out to get [Batch, Hidden_Size]\n",
                "        final_memory = hidden.squeeze(0)\n",
                "        \n",
                "        return self.fc(final_memory)\n",
                "\n",
                "model = RNNClassifier()\n",
                "print(\"Prediction shape:\", model(dummy_sequence).shape)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 10. Experiment: LSTMs\n",
                "Vanilla RNNs are terrible at remembering things that happened a long time ago in the sequence (the **Vanishing Gradient** problem). \n",
                "\n",
                "**LSTMs (Long Short-Term Memory)** networks are complex RNNs with internal \"gates\" that allow them to choose what to remember and what to forget. They return `out, (hidden, cell)`."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "lstm = nn.LSTM(input_size=3, hidden_size=10, batch_first=True)\n",
                "\n",
                "out, (hidden, cell) = lstm(dummy_sequence)\n",
                "\n",
                "print(\"LSTM Output shape:\", out.shape)\n",
                "print(\"LSTM Hidden shape:\", hidden.shape) # Short term memory\n",
                "print(\"LSTM Cell shape:\", cell.shape)     # Long term memory"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 11. Practice Exercise 1: Build an LSTM\n",
                "Write an `LSTMClassifier` class. \n",
                "The LSTM should have `input_size=20`, `hidden_size=64`, and `num_layers=2` (this stacks two LSTMs on top of each other!). Ensure `batch_first=True`.\n",
                "The Linear layer should output 5 classes. \n",
                "In the forward pass, extract the `hidden` state of the *last* layer to pass into the Linear layer."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# SOLUTION\n",
                "class LSTMClassifier(nn.Module):\n",
                "    def __init__(self):\n",
                "        super().__init__()\n",
                "        self.lstm = nn.LSTM(input_size=20, hidden_size=64, num_layers=2, batch_first=True)\n",
                "        self.fc = nn.Linear(64, 5)\n",
                "        \n",
                "    def forward(self, x):\n",
                "        out, (hidden, cell) = self.lstm(x)\n",
                "        \n",
                "        # hidden is shape [num_layers, batch, hidden_size] -> [2, Batch, 64]\n",
                "        # We only want the hidden state of the LAST layer (index -1)\n",
                "        final_layer_hidden = hidden[-1, :, :]\n",
                "        \n",
                "        return self.fc(final_layer_hidden)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 13. Debugging Challenge\n",
                "A student defines `nn.RNN(10, 20)` and passes in a batch of `[32, 5, 10]` sequence data. PyTorch throws an error about shape mismatch. Why?"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Solution:** By default, PyTorch RNNs expect the shape `[Sequence_Length, Batch_Size, Features]`. The student passed `[Batch, Seq, Features]`. They must either transpose their data OR pass `batch_first=True` when defining the RNN."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 17. Interview Questions\n",
                "1. **What is the \"Vanishing Gradient\" problem in RNNs?**\n",
                "   *Answer*: When an RNN processes a long sequence (e.g., 100 words), during backpropagation, the gradients are multiplied over and over at each time step. Because these gradients are usually less than 1, multiplying them 100 times shrinks them to zero. The network completely fails to learn dependencies between word 1 and word 100.\n",
                "2. **How does an LSTM solve this?**\n",
                "   *Answer*: LSTMs have a separate \"Cell State\" that runs straight down the entire sequence with only minor linear interactions (gates). Gradients can flow backwards through this cell state unimpeded, effectively acting as an \"express highway\" for error signals."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 19. Day Summary\n",
                "- Sequence data is 3D: `[Batch, Seq_Length, Features]`.\n",
                "- **ALWAYS pass `batch_first=True`** to `nn.RNN` or `nn.LSTM` to keep your sanity.\n",
                "- RNNs/LSTMs return the output at *every* step, AND the final `hidden` memory state.\n",
                "- For classification, we usually only care about the final `hidden` state."
            ]
        }
    ],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 4
}

with open("Day_28_RNN_LSTM.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Created Day_28_RNN_LSTM.ipynb")

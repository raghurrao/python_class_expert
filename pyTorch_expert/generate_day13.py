import json

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Day 13 \u2014 Validation & Evaluation\n",
                "\n",
                "## 1. Learning Objectives\n",
                "- Reiterate the necessity of Train vs Validation vs Test splits.\n",
                "- Learn how to safely turn off gradients during evaluation.\n",
                "- Calculate Accuracy, Precision, Recall, and F1-Score from scratch.\n",
                "- Understand and interpret a Confusion Matrix."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Prerequisites\n",
                "- Day 10 (Classification Loss functions)\n",
                "- Day 12 (Training Loops)"
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
                "Training Loss just tells us how well the model memorized the training data. To know if it actually learned general patterns, we evaluate it on a **Validation Set** during training, and a **Test Set** at the very end.\n",
                "\n",
                "When evaluating, we must tell PyTorch two things:\n",
                "1. `model.eval()`: Tells layers like Dropout and BatchNorm to behave in evaluation mode (more on these later).\n",
                "2. `with torch.no_grad():`: Stops the autograd engine to save memory and compute."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 5. Intuition & Math: Metrics\n",
                "If 99% of your emails are normal, and 1% are spam, a model that always guesses \"normal\" is 99% accurate. But it's completely useless! Accuracy is not enough.\n",
                "\n",
                "- **True Positive (TP)**: Model predicted Spam, and it was Spam.\n",
                "- **False Positive (FP)**: Model predicted Spam, but it was Normal.\n",
                "- **False Negative (FN)**: Model predicted Normal, but it was Spam.\n",
                "- **True Negative (TN)**: Model predicted Normal, and it was Normal.\n",
                "\n",
                "**Precision** = $\\frac{TP}{TP + FP}$ (Out of all predicted spams, how many were actually spam?)\n",
                "**Recall** = $\\frac{TP}{TP + FN}$ (Out of all actual spams, how many did we catch?)\n",
                "**F1-Score** = Harmonic mean of Precision and Recall. Use this for imbalanced datasets."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# 8. Simple Example: Calculating Metrics\n",
                "# Let's say 1 = Spam, 0 = Normal\n",
                "true_labels = torch.tensor([1, 0, 1, 1, 0, 0, 1, 0, 0, 0])\n",
                "predictions = torch.tensor([1, 0, 0, 1, 1, 0, 1, 0, 0, 0])\n",
                "\n",
                "# Compute TP, FP, FN, TN\n",
                "TP = ((predictions == 1) & (true_labels == 1)).sum().float()\n",
                "FP = ((predictions == 1) & (true_labels == 0)).sum().float()\n",
                "FN = ((predictions == 0) & (true_labels == 1)).sum().float()\n",
                "TN = ((predictions == 0) & (true_labels == 0)).sum().float()\n",
                "\n",
                "accuracy = (TP + TN) / len(true_labels)\n",
                "precision = TP / (TP + FP)\n",
                "recall = TP / (TP + FN)\n",
                "f1 = 2 * (precision * recall) / (precision + recall)\n",
                "\n",
                "print(f\"Accuracy: {accuracy:.2f}\")\n",
                "print(f\"Precision: {precision:.2f}\")\n",
                "print(f\"Recall: {recall:.2f}\")\n",
                "print(f\"F1 Score: {f1:.2f}\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 10. Experiment: The Confusion Matrix\n",
                "A Confusion Matrix is just a 2x2 grid (for binary classification) showing `[[TN, FP], [FN, TP]]`."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "confusion_matrix = torch.tensor([\n",
                "    [TN, FP],\n",
                "    [FN, TP]\n",
                "])\n",
                "print(\"Confusion Matrix:\\n\", confusion_matrix)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 11. Practice Exercise 1: Model Evaluation Mode\n",
                "Below is a tiny evaluation loop. Add the two missing critical PyTorch commands needed for evaluation. Also, when returning to training, how do you put the model back into training mode?"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# dummy_model = nn.Linear(10, 2)\n",
                "# val_x = torch.randn(5, 10)\n",
                "\n",
                "# Fix this evaluation block:\n",
                "# val_preds = dummy_model(val_x)\n",
                "# ... then go back to training mode"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# SOLUTION\n",
                "dummy_model = nn.Linear(10, 2)\n",
                "val_x = torch.randn(5, 10)\n",
                "\n",
                "dummy_model.eval() # 1. Set to eval mode\n",
                "with torch.no_grad(): # 2. Turn off gradients\n",
                "    val_preds = dummy_model(val_x)\n",
                "    \n",
                "dummy_model.train() # 3. Back to training mode!"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 17. Interview Questions\n",
                "1. **What is the difference between `model.eval()` and `torch.no_grad()`?**\n",
                "   *Answer*: `torch.no_grad()` turns off the autograd engine so gradients aren't computed, saving memory. `model.eval()` changes the forward-pass behavior of specific layers (like turning off Dropout or using running statistics for BatchNorm) so predictions are deterministic.\n",
                "2. **If your model is detecting cancer (where missing a cancer case is fatal), which metric should you optimize: Precision or Recall?**\n",
                "   *Answer*: Recall. High recall means very few False Negatives (missed cancer cases). You accept more False Positives (scaring a healthy patient) to ensure you catch all real cases."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 19. Day Summary\n",
                "- Never use Accuracy for imbalanced datasets. Use F1-Score, Precision, or Recall.\n",
                "- ALWAYS use `model.eval()` and `with torch.no_grad():` when running your validation loop.\n",
                "- ALWAYS remember to call `model.train()` before the next training epoch starts."
            ]
        }
    ],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 4
}

with open("Day_13_Validation_Evaluation.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Created Day_13_Validation_Evaluation.ipynb")

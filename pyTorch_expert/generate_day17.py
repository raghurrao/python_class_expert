import json

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Day 17 \u2014 Dataset & DataLoader\n",
                "\n",
                "## 1. Learning Objectives\n",
                "- Understand the problem of loading massive datasets into memory.\n",
                "- Create a custom `torch.utils.data.Dataset`.\n",
                "- Use `torch.utils.data.DataLoader` for mini-batching.\n",
                "- Understand `batch_size`, `shuffle`, and `num_workers`."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Prerequisites\n",
                "- Object-Oriented Python (subclassing).\n",
                "- Training Loops (Day 12)."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import torch\n",
                "from torch.utils.data import Dataset, DataLoader"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Concept Explanation\n",
                "Up until now, we've passed our entire dataset `X_train` into the model at once (`model(X_train)`). This is called **Full Batch Gradient Descent**.\n",
                "\n",
                "If you have 10 million images, this will instantly crash your GPU (Out of Memory error). We must process the data in small chunks (e.g., 32 images at a time). This is called **Mini-Batch Gradient Descent**.\n",
                "\n",
                "PyTorch provides two classes to handle this:\n",
                "1. **`Dataset`**: Tells PyTorch *where* your data is and *how to load a single item*.\n",
                "2. **`DataLoader`**: Takes a `Dataset` and automatically batches, shuffles, and loads the data in parallel."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 8. Simple Example: Custom Dataset\n",
                "To create a custom dataset, you subclass `Dataset` and MUST implement 3 magic methods:\n",
                "- `__init__`: Setup (e.g., load a CSV file or list of image paths).\n",
                "- `__len__`: Returns the total number of samples.\n",
                "- `__getitem__`: Fetches exactly ONE sample and its label at a specific index."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "class DummyImageDataset(Dataset):\n",
                "    def __init__(self, num_samples):\n",
                "        # Normally, you'd load file paths here, not the actual images\n",
                "        self.num_samples = num_samples\n",
                "        \n",
                "    def __len__(self):\n",
                "        # How big is the dataset?\n",
                "        return self.num_samples\n",
                "    \n",
                "    def __getitem__(self, idx):\n",
                "        # How do I get the item at index `idx`?\n",
                "        # Here we just generate a random tensor to simulate an image\n",
                "        image = torch.randn(3, 32, 32)\n",
                "        label = torch.randint(0, 10, (1,)).item() # Random class 0-9\n",
                "        return image, label\n",
                "\n",
                "my_dataset = DummyImageDataset(num_samples=100)\n",
                "print(\"Total samples:\", len(my_dataset))\n",
                "\n",
                "# Fetch one item\n",
                "img, lbl = my_dataset[0]\n",
                "print(\"Single image shape:\", img.shape)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 9. Code Walkthrough: DataLoader\n",
                "Now we wrap our dataset in a `DataLoader`. \n",
                "- `batch_size`: How many items to return at once.\n",
                "- `shuffle`: Should the data be randomized? (ALWAYS `True` for training, `False` for validation/testing).\n",
                "- `num_workers`: How many CPU cores to use for background loading. (0 means main thread)."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "train_loader = DataLoader(dataset=my_dataset, batch_size=16, shuffle=True, num_workers=0)\n",
                "\n",
                "# Let's see what a batch looks like\n",
                "for batch_images, batch_labels in train_loader:\n",
                "    print(\"Batch Images Shape:\", batch_images.shape)\n",
                "    print(\"Batch Labels Shape:\", batch_labels.shape)\n",
                "    break # Just look at the first batch"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "Notice that the `DataLoader` automatically took 16 individual `[3, 32, 32]` images from the dataset and stacked them into a single `[16, 3, 32, 32]` tensor!"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 11. Practice Exercise 1: Modifying the Training Loop\n",
                "Rewrite the standard 5-step training loop to use a `DataLoader`. \n",
                "\n",
                "*Hint: You need a nested loop. An outer loop for `epochs`, and an inner loop iterating through the `train_loader`.*"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Write your pseudo-code or code here"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# SOLUTION\n",
                "# for epoch in range(epochs):\n",
                "#     model.train()\n",
                "#     \n",
                "#     # Iterate over mini-batches\n",
                "#     for images, labels in train_loader:\n",
                "#         # The standard 5 steps happen PER BATCH\n",
                "#         preds = model(images)\n",
                "#         loss = criterion(preds, labels)\n",
                "#         optimizer.zero_grad()\n",
                "#         loss.backward()\n",
                "#         optimizer.step()"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 13. Debugging Challenge\n",
                "A student sets `num_workers=8` on their Windows laptop, but the script crashes immediately with a multiprocessing error. Why?"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Solution:** On Windows, Python's multiprocessing requires the main code execution to be protected by an `if __name__ == '__main__':` block. If this is missing in a `.py` script, setting `num_workers > 0` will cause an infinite recursive crash. When in doubt on Windows or in Jupyter, set `num_workers=0`."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 17. Interview Questions\n",
                "1. **Why do we shuffle the training data, but not the validation data?**\n",
                "   *Answer*: We shuffle training data to prevent the model from learning the order of the dataset (e.g., all cats then all dogs) and getting stuck in a local minimum. We don't shuffle validation data because the order doesn't matter for evaluation, and keeping it static makes debugging/comparing predictions easier.\n",
                "2. **What happens if your dataset length is 100, and your batch size is 32?**\n",
                "   *Answer*: The DataLoader will yield three batches of 32, and one final batch of 4. If your model specifically requires a fixed batch size (rare, but happens), you can pass `drop_last=True` to the DataLoader to discard the final incomplete batch."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 19. Day Summary\n",
                "- `Dataset`: Defines how to get *one* data point (`__getitem__`).\n",
                "- `DataLoader`: Groups data points into mini-batches, handles shuffling, and multiprocessing.\n",
                "- The training loop now consists of two loops: Epochs (outer) and Batches (inner)."
            ]
        }
    ],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 4
}

with open("Day_17_Dataset_DataLoader.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Created Day_17_Dataset_DataLoader.ipynb")

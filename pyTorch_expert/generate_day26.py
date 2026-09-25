import json

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Day 26 \u2014 Custom Image Datasets\n",
                "\n",
                "## 1. Learning Objectives\n",
                "- Break free from `torchvision.datasets`.\n",
                "- Write a custom `torch.utils.data.Dataset` that reads `.jpg` or `.png` files from a folder.\n",
                "- Integrate `PIL.Image` and `transforms.v2` into `__getitem__`.\n",
                "- Understand how to map string labels (e.g., \"cat\", \"dog\") to integer classes (0, 1)."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Prerequisites\n",
                "- Dataset & DataLoader (Day 17)\n",
                "- Data Augmentation (Day 25)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import torch\n",
                "from torch.utils.data import Dataset, DataLoader\n",
                "from torchvision.transforms import v2\n",
                "from PIL import Image\n",
                "import os\n",
                "import glob"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Concept Explanation: The Custom Dataset Reality\n",
                "In the real world, nobody hands you a perfectly formatted `torchvision` dataset. Your boss will hand you a folder called `medical_scans/` containing subfolders like `healthy/` and `tumor/`, filled with thousands of messy `.jpg` files.\n",
                "\n",
                "We must write a Python class that:\n",
                "1. Scans the folder and makes a massive list of every file path.\n",
                "2. Remembers which label belongs to which file path.\n",
                "3. In `__getitem__`, opens the image from the hard drive, applies the transforms, and returns the Tensor and the Label."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. Simulating a Real-World Directory Structure\n",
                "First, let's pretend we have a directory structure that looks like this:\n",
                "```text\n",
                "my_dataset/\n",
                "    cats/\n",
                "        cat_01.jpg\n",
                "        cat_02.jpg\n",
                "    dogs/\n",
                "        dog_01.jpg\n",
                "        dog_02.jpg\n",
                "```\n",
                "\n",
                "For this notebook, we will just simulate having lists of these file paths."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Simulated file paths (In reality, you'd use glob.glob('my_dataset/*/*.jpg'))\n",
                "simulated_filepaths = [\n",
                "    \"my_dataset/cats/cat_01.jpg\",\n",
                "    \"my_dataset/cats/cat_02.jpg\",\n",
                "    \"my_dataset/dogs/dog_01.jpg\",\n",
                "    \"my_dataset/dogs/dog_02.jpg\"\n",
                "]"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 8. Simple Example: The Custom Image Dataset Class\n",
                "Let's write the class. Pay special attention to how we extract the label from the folder name!"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "class CustomImageDataset(Dataset):\n",
                "    def __init__(self, filepaths, transform=None):\n",
                "        self.filepaths = filepaths\n",
                "        self.transform = transform\n",
                "        \n",
                "        # Create a dictionary to map string folder names to integer labels\n",
                "        self.class_to_idx = {\"cats\": 0, \"dogs\": 1}\n",
                "        \n",
                "    def __len__(self):\n",
                "        return len(self.filepaths)\n",
                "    \n",
                "    def __getitem__(self, idx):\n",
                "        # 1. Get the path\n",
                "        img_path = self.filepaths[idx]\n",
                "        \n",
                "        # 2. Extract the label from the path (e.g., split \"my_dataset/cats/cat_01.jpg\")\n",
                "        # path.split('/') -> ['my_dataset', 'cats', 'cat_01.jpg'] -> index 1 is 'cats'\n",
                "        class_name = img_path.split('/')[-2]\n",
                "        label = self.class_to_idx[class_name]\n",
                "        \n",
                "        # 3. Open the image (Normally we do Image.open(img_path).convert('RGB'))\n",
                "        # Since these files don't actually exist on our drive, we'll simulate opening a PIL image.\n",
                "        # REAL CODE: image = Image.open(img_path).convert('RGB')\n",
                "        image = Image.new('RGB', (224, 224), color = (73, 109, 137))\n",
                "        \n",
                "        # 4. Apply transforms\n",
                "        if self.transform:\n",
                "            image = self.transform(image)\n",
                "            \n",
                "        return image, label"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 9. Code Walkthrough: Testing the Dataset\n",
                "Let's create the transform, instantiate the dataset, and test it."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "my_transform = v2.Compose([\n",
                "    v2.Resize((128, 128)),\n",
                "    v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)])\n",
                "])\n",
                "\n",
                "my_dataset = CustomImageDataset(simulated_filepaths, transform=my_transform)\n",
                "\n",
                "# Fetch item at index 2 (which should be 'my_dataset/dogs/dog_01.jpg')\n",
                "img_tensor, label = my_dataset[2]\n",
                "\n",
                "print(\"Image Tensor Shape:\", img_tensor.shape)\n",
                "print(\"Label Integer (1 = Dog):\", label)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 11. Practice Exercise 1: `ImageFolder` Shortcut\n",
                "Writing the class above is a great exercise to understand how things work under the hood. However, if your data is perfectly organized in folders like the example above (`dataset_root/class_name/image.jpg`), PyTorch has a built-in shortcut that does exactly what we just wrote.\n",
                "\n",
                "Look up `torchvision.datasets.ImageFolder` and write the single line of code required to create a dataset using it."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# SOLUTION\n",
                "# Assuming your root directory is 'my_dataset/'\n",
                "# easy_dataset = torchvision.datasets.ImageFolder(root='my_dataset/', transform=my_transform)\n",
                "# \n",
                "# To see how it mapped the classes, you would check:\n",
                "# print(easy_dataset.class_to_idx)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 13. Debugging Challenge\n",
                "You wrote a custom dataset. During training, your dataloader runs fine for the first 100 batches, but then suddenly crashes with `RuntimeError: stack expects each tensor to be equal size, but got [3, 224, 224] at entry 0 and [1, 224, 224] at entry 15`.\n",
                "\n",
                "What is the bug in your dataset, and how do you fix it?"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Solution:** You forgot to add `.convert('RGB')` when opening the image in `__getitem__`. Most of your images are standard RGB (3 channels), but the dataloader stumbled upon a Grayscale image (1 channel). The `DataLoader` cannot stack a batch of images if they have different channel dimensions. \n",
                "Always use `Image.open(img_path).convert('RGB')` to force all images into 3 channels."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 17. Interview Questions\n",
                "1. **Why don't we load all the images into memory in the `__init__` function of the Dataset?**\n",
                "   *Answer*: If your dataset is 50GB of images, loading them all in `__init__` will instantly crash your system's RAM. The `__init__` function should only store a lightweight list of file paths. The `__getitem__` function loads images one-by-one from the hard drive *on-demand*.\n",
                "2. **If `torchvision.datasets.ImageFolder` exists, why ever write a custom dataset class?**\n",
                "   *Answer*: `ImageFolder` requires a very specific directory structure. In real life, you might have a single massive folder of images, and a `.csv` file containing the labels, bounding boxes, or patient ages. A custom dataset is the only way to read from that `.csv` file."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 19. Day Summary\n",
                "- Custom Datasets only store file paths in `__init__`.\n",
                "- `__getitem__` is where you read from the disk (`Image.open`), convert to RGB, apply transforms, and return the tensor.\n",
                "- Never forget `.convert('RGB')` to prevent channel mismatch crashes.\n",
                "- If your files are organized perfectly into class folders, just use `torchvision.datasets.ImageFolder`."
            ]
        }
    ],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 4
}

with open("Day_26_Custom_Datasets.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Created Day_26_Custom_Datasets.ipynb")

import json

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Day 25 \u2014 Advanced Data Augmentation\n",
                "\n",
                "## 1. Learning Objectives\n",
                "- Understand how Data Augmentation acts as the ultimate regularizer.\n",
                "- Use the modern `torchvision.transforms.v2` API.\n",
                "- Apply Random Crops, Flips, and Color Jittering.\n",
                "- Properly separate Train Transforms from Validation/Test Transforms."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Prerequisites\n",
                "- Overfitting & Regularization (Day 15)\n",
                "- Datasets & Transforms (Day 21)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import torch\n",
                "import torchvision\n",
                "import matplotlib.pyplot as plt\n",
                "\n",
                "# We use transforms.v2 because it is the modern, faster, and more capable API\n",
                "from torchvision.transforms import v2"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Concept Explanation: Data Augmentation\n",
                "In Day 15, we learned that Neural Networks love to memorize training data (Overfitting). \n",
                "\n",
                "If you only have 1,000 pictures of dogs, the network might memorize that \"a dog is a brown thing exactly in the center of the image.\" \n",
                "**Data Augmentation** solves this by slightly altering the images every single time they are loaded. \n",
                "If we randomly flip the image horizontally, randomly zoom in a bit, and randomly change the brightness, the network never sees the exact same image twice! It is forced to learn what a dog *actually* looks like, rather than memorizing the exact pixel layout."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 8. Simple Example: Building a Transform Pipeline\n",
                "We use `v2.Compose` to string together multiple random alterations."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# This pipeline is for the TRAINING data\n",
                "train_transforms = v2.Compose([\n",
                "    # 1. Randomly flip the image horizontally 50% of the time\n",
                "    v2.RandomHorizontalFlip(p=0.5),\n",
                "    \n",
                "    # 2. Randomly rotate by up to 15 degrees\n",
                "    v2.RandomRotation(degrees=15),\n",
                "    \n",
                "    # 3. Randomly change brightness, contrast, and saturation\n",
                "    v2.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),\n",
                "    \n",
                "    # 4. Mandatory: Convert PIL Image to PyTorch Tensor [C, H, W] in range [0., 1.]\n",
                "    v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)]),\n",
                "    \n",
                "    # 5. Mandatory: Normalize according to ImageNet stats (if using transfer learning)\n",
                "    v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])\n",
                "])"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 9. Code Walkthrough: Train vs Validation\n",
                "**CRITICAL RULE**: You NEVER augment the Validation or Test sets. \n",
                "You want your evaluation metrics to be measured on clean, un-distorted images. The only things the Test set needs are the resizing, tensor conversion, and normalization."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# This pipeline is for the VALIDATION/TEST data\n",
                "test_transforms = v2.Compose([\n",
                "    # NO flips, NO rotations, NO jitters.\n",
                "    v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)]),\n",
                "    v2.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])\n",
                "])\n",
                "\n",
                "# Usage in Datasets:\n",
                "# train_dataset = torchvision.datasets.CIFAR10(root='./data', train=True, transform=train_transforms)\n",
                "# test_dataset = torchvision.datasets.CIFAR10(root='./data', train=False, transform=test_transforms)"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 11. Practice Exercise 1: Exploring Augmentations\n",
                "Look up the PyTorch documentation for `torchvision.transforms.v2.RandomResizedCrop`. \n",
                "Write a quick definition of what it does, and why it is considered one of the most powerful single augmentations."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Solution**: `RandomResizedCrop(size)` selects a random rectangular area of the image (with a random aspect ratio and scale), crops it out, and then resizes that cropped area back to the requested `size`. \n",
                "\n",
                "It is powerful because it acts as multiple augmentations in one: Translation (it moves the subject around), Scaling (zooming in/out), and Aspect Ratio distortion. It forces the network to recognize the object regardless of its size, shape, or position in the frame."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 13. Debugging Challenge\n",
                "You run inference on a picture of a dog you downloaded from Google using your perfectly trained model. The model is 99% confident it is a \"Car\". \n",
                "\n",
                "Here is your inference code:\n",
                "```python\n",
                "from PIL import Image\n",
                "img = Image.open('my_dog.jpg')\n",
                "\n",
                "infer_transform = v2.Compose([\n",
                "    v2.Resize((224, 224)),\n",
                "    v2.Compose([v2.ToImage(), v2.ToDtype(torch.float32, scale=True)])\n",
                "])\n",
                "\n",
                "tensor_img = infer_transform(img).unsqueeze(0)\n",
                "pred = model(tensor_img)\n",
                "```\n",
                "Why did it fail so terribly?"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "**Solution:** You forgot the `v2.Normalize` step in your inference pipeline! \n",
                "If the model was trained on normalized images (mean=0.485, etc.), its weights are mathematically tuned to expect inputs in that exact numeric distribution (usually between -2 and +2). By feeding it raw `[0, 1]` tensors, the math is entirely thrown off, resulting in garbage predictions. Your inference transform MUST match your training normalization exactly."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 17. Interview Questions\n",
                "1. **Should you apply Data Augmentation to Medical Images (like X-Rays)?**\n",
                "   *Answer*: You must be very careful. Flipping a chest X-Ray horizontally puts the heart on the right side of the body, which is a rare medical condition (Dextrocardia). Rotating an X-Ray by 90 degrees creates a physically impossible image. Only apply augmentations that preserve the physical reality of the dataset.\n",
                "2. **Why do we use `transforms.v2` instead of `transforms`?**\n",
                "   *Answer*: The older `transforms` API was designed strictly for PIL Images. The `v2` API is designed to work seamlessly with PyTorch Tensors, supports batched transformations on the GPU, and can simultaneously transform bounding boxes and segmentation masks along with the images."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 19. Day Summary\n",
                "- Data Augmentation forces models to learn general features rather than memorizing pixels.\n",
                "- Always separate `train_transforms` (heavy augmentation) from `test_transforms` (no augmentation, only resizing and normalization).\n",
                "- **Never forget to apply the exact same `v2.Normalize` to your inference images!**"
            ]
        }
    ],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 4
}

with open("Day_25_Data_Augmentation.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Created Day_25_Data_Augmentation.ipynb")

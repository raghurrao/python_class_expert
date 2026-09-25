import json

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Day 30 \u2014 Grand Finale & Mastery\n",
                "\n",
                "## 1. Welcome to the End\n",
                "Congratulations! You have completed the 30-Day PyTorch Expert Course. \n",
                "Over the past 29 days, you have transitioned from basic Python to manipulating high-dimensional tensors, building custom Neural Networks, debugging complex errors, processing Computer Vision datasets, and exporting models for production.\n",
                "\n",
                "Today, there are no tutorials. There is only a single, massive project specification. It is up to you to build it from scratch."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. The Capstone Project: End-to-End Image Classification Pipeline\n",
                "\n",
                "**The Scenario**:\n",
                "A hospital has hired you to build a Computer Vision pipeline that can classify X-Rays into one of three categories: `Normal`, `Viral_Pneumonia`, and `Covid_19`. \n",
                "\n",
                "They have provided you with a simulated dataset folder (which you will generate in Step 1). You must build a complete PyTorch application to train the model and export it for their C++ server."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Step 1: Setup (Run this cell to generate dummy data)"
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "import os\n",
                "import torch\n",
                "from PIL import Image\n",
                "\n",
                "# Create a fake directory structure with blank images\n",
                "dirs = ['hospital_data/train/Normal', 'hospital_data/train/Pneumonia', 'hospital_data/train/Covid',\n",
                "        'hospital_data/val/Normal', 'hospital_data/val/Pneumonia', 'hospital_data/val/Covid']\n",
                "\n",
                "for d in dirs:\n",
                "    os.makedirs(d, exist_ok=True)\n",
                "    for i in range(10): # 10 dummy images per class\n",
                "        img = Image.new('RGB', (256, 256), color = (torch.randint(0,255).item(), torch.randint(0,255).item(), torch.randint(0,255).item()))\n",
                "        img.save(f\"{d}/scan_{i}.jpg\")\n",
                "        \n",
                "print(\"Dummy hospital data generated in './hospital_data/'\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "### Step 2: Your Mission (The Requirements)\n",
                "\n",
                "Create a new python cell (or multiple cells) below and write the entire pipeline. You must meet the following criteria:\n",
                "\n",
                "1. **Device**: The script must automatically use CUDA if available, else CPU.\n",
                "2. **Transforms**:\n",
                "    * **Train**: Resize to 256, RandomCrop to 224, RandomHorizontalFlip(p=0.5), Convert to Tensor, Normalize (ImageNet stats).\n",
                "    * **Val**: Resize to 256, CenterCrop to 224, Convert to Tensor, Normalize (ImageNet stats).\n",
                "3. **DataLoaders**: Use `ImageFolder` and `DataLoader`. Set a batch size of 8. Shuffle the training data.\n",
                "4. **Model**: Import a pretrained `vgg16` from `torchvision.models`. \n",
                "    * Freeze all feature extraction layers.\n",
                "    * Replace the final classification layer (`classifier[6]`) with a new layer that outputs exactly 3 classes.\n",
                "5. **Optimization**:\n",
                "    * Use `CrossEntropyLoss`.\n",
                "    * Use the `AdamW` optimizer (learning rate = 0.001, weight_decay = 1e-4). Only pass the parameters of the new final layer to the optimizer.\n",
                "6. **Training Loop**:\n",
                "    * Train for exactly 2 epochs.\n",
                "    * Track both Training Loss and Validation Accuracy.\n",
                "    * Remember `optimizer.zero_grad()`, `loss.backward()`, and `optimizer.step()`.\n",
                "    * Remember `model.train()` and `model.eval()`.\n",
                "7. **Export**:\n",
                "    * At the end of training, use `torch.jit.script` to compile the model.\n",
                "    * Save the compiled model as `hospital_vgg16_production.pt`."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# ==========================================\n",
                "# WRITE YOUR MASTERPIECE HERE\n",
                "# ==========================================\n"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. What's Next?\n",
                "You are now highly proficient in PyTorch. Where do you go from here?\n",
                "\n",
                "1. **Read PyTorch Source Code**: Start reading implementations on GitHub. Look at how HuggingFace writes their Transformers.\n",
                "2. **Learn NLP**: We focused heavily on Computer Vision. Dive deep into Transformers, `nn.Transformer`, Attention Mechanisms, and Large Language Models (LLMs).\n",
                "3. **Learn Advanced CNNs**: Study Object Detection (YOLO, Faster R-CNN) and Image Segmentation (U-Net).\n",
                "4. **Distributed Training**: Learn `torch.nn.parallel.DistributedDataParallel` to train models across 8+ GPUs simultaneously.\n",
                "\n",
                "Thank you for taking this 30-day journey. Now, go build the future."
            ]
        }
    ],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 4
}

with open("Day_30_Grand_Finale.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Created Day_30_Grand_Finale.ipynb")

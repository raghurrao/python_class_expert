import json

notebook = {
    "cells": [
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "# Day 29 \u2014 TorchScript, ONNX & Production\n",
                "\n",
                "## 1. Learning Objectives\n",
                "- Understand the limitations of Python in production environments.\n",
                "- Use `torch.jit.trace` to convert a model to TorchScript.\n",
                "- Use `torch.jit.script` for models with control flow (if/else).\n",
                "- Export a model to ONNX format for cross-platform deployment."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 2. Prerequisites\n",
                "- Model Saving & Loading (Day 18)\n",
                "- CNN Architectures (Day 23)"
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
                "import os"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 3. Concept Explanation: The Production Problem\n",
                "Python is slow, requires a heavy runtime environment, and is hard to deploy on mobile phones or embedded IoT devices. \n",
                "If you want to run your model in a high-performance C++ server or an iOS app, you cannot use standard `.pth` files (which require Python to read).\n",
                "\n",
                "**TorchScript** is a way to compile your PyTorch model into a serialized format that is completely decoupled from Python. It can be loaded natively in C++ using `libtorch`."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 4. Method 1: Tracing (`torch.jit.trace`)\n",
                "Tracing works by passing a dummy tensor through your model. PyTorch records every single mathematical operation that occurs during the forward pass and saves that exact path as a static graph."
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
                "        self.fc = nn.Linear(10, 2)\n",
                "        \n",
                "    def forward(self, x):\n",
                "        return torch.relu(self.fc(x))\n",
                "\n",
                "model = SimpleModel()\n",
                "model.eval() # ALWAYS put in eval mode before tracing!\n",
                "\n",
                "# 1. Create a dummy input matching your expected data shape\n",
                "dummy_input = torch.randn(1, 10)\n",
                "\n",
                "# 2. Trace the model\n",
                "traced_model = torch.jit.trace(model, dummy_input)\n",
                "\n",
                "# 3. Save the traced model\n",
                "traced_model.save(\"traced_model.pt\")\n",
                "print(\"Model successfully traced and saved!\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 5. Method 2: Scripting (`torch.jit.script`)\n",
                "Tracing has a fatal flaw: it ignores Python control flow (like `if` statements or `for` loops). If your `forward` method has an `if` statement, tracing will only record the branch that the dummy tensor happened to take. \n",
                "\n",
                "To capture control flow, you must use **Scripting**. Scripting actually parses your Python source code and compiles it."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "class ControlFlowModel(nn.Module):\n",
                "    def __init__(self):\n",
                "        super().__init__()\n",
                "        self.fc = nn.Linear(10, 2)\n",
                "        \n",
                "    def forward(self, x):\n",
                "        # TRACING WOULD FAIL HERE\n",
                "        if x.sum() > 0:\n",
                "            return self.fc(x)\n",
                "        else:\n",
                "            return -self.fc(x)\n",
                "\n",
                "cf_model = ControlFlowModel()\n",
                "cf_model.eval()\n",
                "\n",
                "# Script the model directly (no dummy input required!)\n",
                "scripted_model = torch.jit.script(cf_model)\n",
                "scripted_model.save(\"scripted_model.pt\")\n",
                "print(\"Model successfully scripted and saved!\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 6. ONNX (Open Neural Network Exchange)\n",
                "ONNX is an open format built to represent machine learning models. If you export to ONNX, you can load your model in TensorFlow, Caffe2, TensorRT, or ONNX Runtime (which is highly optimized for production)."
            ]
        },
        {
            "cell_type": "code",
            "execution_count": None,
            "metadata": {},
            "outputs": [],
            "source": [
                "# Exporting to ONNX\n",
                "onnx_model = SimpleModel()\n",
                "onnx_model.eval()\n",
                "onnx_dummy = torch.randn(1, 10)\n",
                "\n",
                "torch.onnx.export(\n",
                "    onnx_model,               # model being run\n",
                "    onnx_dummy,               # model input\n",
                "    \"model.onnx\",             # where to save the model\n",
                "    export_params=True,       # store the trained parameter weights inside the model file\n",
                "    opset_version=11,         # the ONNX version to export the model to\n",
                "    input_names = ['input'],  # the model's input names\n",
                "    output_names = ['output'] # the model's output names\n",
                ")\n",
                "print(\"Model successfully exported to ONNX format!\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 11. Practice Exercise 1: Cleanup\n",
                "Write a script to delete the `traced_model.pt`, `scripted_model.pt`, and `model.onnx` files."
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
                "files = [\"traced_model.pt\", \"scripted_model.pt\", \"model.onnx\"]\n",
                "for f in files:\n",
                "    if os.path.exists(f):\n",
                "        os.remove(f)\n",
                "print(\"Cleanup complete.\")"
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 17. Interview Questions\n",
                "1. **When should you use `torch.jit.trace` vs `torch.jit.script`?**\n",
                "   *Answer*: You should prefer `trace` because it is highly optimized and guaranteed to execute exactly the math you gave it. However, if your forward pass contains data-dependent control flow (like sequence-length checks or dynamic `if` statements), you MUST use `script`, because `trace` will silently hardcode whatever path the dummy tensor took.\n",
                "2. **Why MUST you call `model.eval()` before tracing/exporting?**\n",
                "   *Answer*: If you leave the model in `train()` mode, layers like `Dropout` will continue to randomly drop neurons, and `BatchNorm` will continue to update its running statistics based on the single input you give it. Your compiled model will behave randomly and incorrectly in production."
            ]
        },
        {
            "cell_type": "markdown",
            "metadata": {},
            "source": [
                "## 19. Day Summary\n",
                "- Production models (C++, Mobile) require decoupling from Python.\n",
                "- `torch.jit.trace` records operations using a dummy tensor.\n",
                "- `torch.jit.script` compiles Python code (needed for control flow).\n",
                "- `torch.onnx.export` allows moving PyTorch models into entirely different ML frameworks.\n",
                "- **ALWAYS call `model.eval()` first!**"
            ]
        }
    ],
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 4
}

with open("Day_29_TorchScript.ipynb", "w", encoding="utf-8") as f:
    json.dump(notebook, f, indent=2)

print("Created Day_29_TorchScript.ipynb")

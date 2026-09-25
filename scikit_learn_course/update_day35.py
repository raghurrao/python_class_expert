import json

def create_markdown_cell(source):
    if isinstance(source, str):
        source = [source]
    return {
        "cell_type": "markdown",
        "metadata": {},
        "source": [s + "\n" if not s.endswith("\n") else s for s in source]
    }

def create_code_cell(source):
    if isinstance(source, str):
        source = [source]
    return {
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [s + "\n" if not s.endswith("\n") else s for s in source]
    }

day35_cells = [
    create_markdown_cell("# BONUS CONTENT"),
    create_markdown_cell("# Day 35 — Neural Networks (MLPClassifier)"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Understand the concept of a Multi-Layer Perceptron (MLP).\n- Train a basic Neural Network natively within Scikit-Learn.\n- Recognize when to use Scikit-Learn for Neural Networks and when to graduate to PyTorch or TensorFlow."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 5 (Pipelines).\n- Day 8 (Linear Regression / Math)."),
    
    create_markdown_cell("## 3. Concept: The Multi-Layer Perceptron\nUp until now, our models have been \"Shallow\" Learning. A Linear Regression draws a single line. A Random Forest builds trees. \n\nA **Neural Network (Multi-Layer Perceptron)** tries to mimic the human brain. \n- **Input Layer**: The raw features of your dataset.\n- **Hidden Layers**: Layers of \"neurons\". Each neuron takes the data from the previous layer, applies some complex mathematical warping (like a ReLU activation function), and passes it forward.\n- **Output Layer**: The final prediction.\n\nBecause the data is warped mathematically layer after layer, Neural Networks can learn unimaginably complex, non-linear relationships that traditional algorithms fail to see."),
    
    create_markdown_cell("## 4. Concept: Scikit-Learn's Limitations\nScikit-learn is the king of traditional Machine Learning. However, it is **not** designed for Deep Learning. \n`MLPClassifier` does not support GPUs. It does not support convolutions (for images) or LSTMs (for text). \n\nSo why use it? It is absolutely fantastic as a lightweight, extremely fast Neural Network baseline for tabular data, and it plugs perfectly into standard Scikit-learn `Pipeline` and `GridSearchCV` ecosystems."),
    
    create_markdown_cell("## 5. Scikit-learn API\n```python\nfrom sklearn.neural_network import MLPClassifier\n\n# hidden_layer_sizes=(100, 50) means 2 hidden layers.\n# The first has 100 neurons, the second has 50 neurons.\nmlp = MLPClassifier(hidden_layer_sizes=(100, 50), max_iter=1000)\n```"),
    
    create_markdown_cell("## 6. Simple Example: Training an MLP\nLet's generate a complex, non-linear dataset (two moons) and let the Neural Network try to untangle them."),
    create_code_cell([
        "import pandas as pd",
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "from sklearn.datasets import make_moons",
        "from sklearn.model_selection import train_test_split",
        "from sklearn.preprocessing import StandardScaler",
        "from sklearn.neural_network import MLPClassifier",
        "from sklearn.metrics import classification_report",
        "",
        "# 1. Generate Non-Linear Data",
        "X, y = make_moons(n_samples=1000, noise=0.2, random_state=42)",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)",
        "",
        "plt.scatter(X[:, 0], X[:, 1], c=y, cmap='coolwarm', alpha=0.5)",
        "plt.title('Non-Linear Moon Dataset')",
        "plt.show()",
        "",
        "# 2. SCALE THE DATA (Neural Networks will completely fail if data is unscaled!)",
        "scaler = StandardScaler()",
        "X_train_scaled = scaler.fit_transform(X_train)",
        "X_test_scaled = scaler.transform(X_test)",
        "",
        "# 3. Train the Neural Network",
        "# 3 hidden layers: 64 neurons, then 32 neurons, then 16 neurons.",
        "mlp = MLPClassifier(hidden_layer_sizes=(64, 32, 16), max_iter=1000, random_state=42)",
        "",
        "print('Training Neural Network...')",
        "mlp.fit(X_train_scaled, y_train)",
        "print('Training Complete!')",
        "",
        "# 4. Evaluate",
        "y_pred = mlp.predict(X_test_scaled)",
        "print('\\n--- MLP Classification Report ---')",
        "print(classification_report(y_test, y_pred))"
    ]),
    
    create_markdown_cell("## 7. Code Walkthrough\n- We used `make_moons` to create a dataset that cannot be separated by a straight line.\n- We **MUST scale the data**. Neural networks use Gradient Descent to learn weights. If features have vastly different scales, the gradients explode and the network learns nothing.\n- We passed `hidden_layer_sizes=(64, 32, 16)`. The network pushed the raw data into 64 neurons, warped it, passed it to 32 neurons, warped it again, passed it to 16 neurons, and then finally made a 0 or 1 prediction. \n- It successfully achieved high accuracy on a complex dataset."),
    
    create_markdown_cell("## 8. Experiment: Accessing the Weights\nLet's peek inside the brain of the Neural Network. It learned mathematical matrices (weights) connecting every neuron together."),
    create_code_cell([
        "print(f'Number of layers (including input/output): {mlp.n_layers_}')",
        "",
        "print('\\nShape of the Weight Matrices:')",
        "for i, weight_matrix in enumerate(mlp.coefs_):",
        "    print(f'Weights connecting Layer {i} to Layer {i+1}: {weight_matrix.shape}')"
    ]),
    create_markdown_cell("> - Notice the first matrix is `(2, 64)`. It connects the 2 original features (X, Y coordinates) to the first hidden layer of 64 neurons.\n> - The final matrix is `(16, 1)`. It takes the output of the 16 neurons and squashes them down into 1 final prediction!"),
    
    create_markdown_cell("## 9. Pipeline Integration\nBecause `MLPClassifier` is a native Scikit-Learn object, we can completely automate the mandatory scaling step by putting it in a Pipeline!"),
    create_code_cell([
        "from sklearn.pipeline import Pipeline",
        "from sklearn.model_selection import cross_val_score",
        "",
        "nn_pipe = Pipeline([",
        "    ('scaler', StandardScaler()),",
        "    ('mlp', MLPClassifier(hidden_layer_sizes=(32, 16), max_iter=1000, random_state=42))",
        "])",
        "",
        "scores = cross_val_score(nn_pipe, X, y, cv=5, scoring='accuracy')",
        "print(f'Neural Network 5-Fold Accuracy: {scores.mean() * 100:.1f}%')"
    ]),
    
    create_markdown_cell("## 10. The Graduation Point\nYou have now learned to build Neural Networks in Scikit-learn. \nHowever, if you want to build a Neural Network that can recognize faces in images, generate text like ChatGPT, or translate languages, Scikit-learn is no longer sufficient. \n\n**To continue your Machine Learning journey, your next logical step is to learn PyTorch or TensorFlow.**"),
    
    create_markdown_cell("## 11. Summary of Bonus Day 35\n- **Multi-Layer Perceptrons (MLPs)** are basic neural networks consisting of input, hidden, and output layers.\n- They are exceptionally good at learning complex non-linear patterns.\n- You **MUST scale your data** (e.g., `StandardScaler`) before training an MLP, or it will fail to converge.\n- Scikit-learn's `MLPClassifier` is great for tabular data and Pipelines, but does not support GPUs or Deep Learning architectures. For that, you need PyTorch or TensorFlow.")
]

notebook = {
    "cells": day35_cells,
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 5
}

filename = "Day_35_Neural_Networks_MLP.ipynb"
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Created {filename} successfully!")

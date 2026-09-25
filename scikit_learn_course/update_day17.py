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

day17_cells = [
    create_markdown_cell("# PHASE 3 — CLASSIFICATION"),
    create_markdown_cell("# Day 17 — K-Nearest Neighbors (KNN)"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Explain how K-Nearest Neighbors (KNN) classifies data without learning any mathematical equations.\n- Understand the concept of distance metrics (Euclidean Distance).\n- Tune the `n_neighbors` ($K$) hyperparameter to control overfitting/underfitting.\n- Recognize why feature scaling is absolutely mandatory for distance-based algorithms."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 15 (Classification Concepts).\n- Day 4 (Preprocessing / Scaling)."),
    
    create_markdown_cell("## 3. Concept: The Lazy Learner\nLogistic Regression spends time during `.fit()` running complex calculus (gradient descent) to find the perfect equation (line). \n\n**K-Nearest Neighbors (KNN)** is called a \"Lazy Learner\". During `.fit()`, it does absolutely no math. It simply memorizes the training data. \nWhen you ask it to predict a new data point, it looks at the $K$ closest training points (its \"neighbors\") and takes a majority vote. \nIf $K=3$, and the 3 closest neighbors are 2 Cats and 1 Dog, the model predicts Cat."),
    
    create_markdown_cell("## 4. Why Does This Matter?\nKNN is incredibly intuitive and naturally handles non-linear, complex decision boundaries without needing polynomial features. It is heavily used in Recommendation Systems (e.g., \"People who liked this movie also liked...\") where similarity is the main driver."),
    
    create_markdown_cell("## 5. Intuition\nImagine you move to a new neighborhood and want to know if it's safe. \nYou don't build a mathematical regression model of the city. You simply ask your 5 closest neighbors. \nIf 4 of them say it's safe, and 1 says it's dangerous, you assume it's safe. \nThis is exactly what KNN does."),
    
    create_markdown_cell("## 6. Mathematical Foundation\nHow does it define \"closest\"? It calculates the physical distance between data points. The most common metric is **Euclidean Distance** (the Pythagorean theorem in multi-dimensional space):\n\n$$ d(p, q) = \\sqrt{(p_1 - q_1)^2 + (p_2 - q_2)^2 + ... + (p_n - q_n)^2} $$\n\nBecause it calculates distance, **Features with larger scales will dominate the math**. \nIf Feature 1 is Age (0-100) and Feature 2 is Salary (0-150,000), the Salary difference will completely overwrite the Age difference. **You MUST scale your data.**"),
    
    create_markdown_cell("## 7. Scikit-learn API\n```python\nfrom sklearn.neighbors import KNeighborsClassifier\nmodel = KNeighborsClassifier(n_neighbors=5)\n```"),
    
    create_markdown_cell("## 8. Simple Example\nLet's generate a dataset with a crescent moon shape. Logistic Regression will fail because it tries to draw a straight line. Let's see how KNN handles it."),
    create_code_cell([
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "from sklearn.datasets import make_moons",
        "from sklearn.linear_model import LogisticRegression",
        "from sklearn.neighbors import KNeighborsClassifier",
        "from sklearn.model_selection import train_test_split",
        "from sklearn.metrics import accuracy_score",
        "",
        "# 1. Generate Non-Linear Data (Moons)",
        "X, y = make_moons(n_samples=300, noise=0.2, random_state=42)",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)",
        "",
        "# 2. Train Logistic Regression (Straight Line)",
        "log_reg = LogisticRegression()",
        "log_reg.fit(X_train, y_train)",
        "",
        "# 3. Train KNN (K=5)",
        "knn = KNeighborsClassifier(n_neighbors=5)",
        "knn.fit(X_train, y_train)",
        "",
        "print(f'Logistic Regression Accuracy: {accuracy_score(y_test, log_reg.predict(X_test)):.2f}')",
        "print(f'KNN (K=5) Accuracy:           {accuracy_score(y_test, knn.predict(X_test)):.2f}')"
    ]),
    
    create_markdown_cell("## 9. Code Walkthrough\n- `make_moons` generates a classic non-linear classification dataset shaped like two intertwining crescents.\n- Logistic Regression completely failed (low accuracy) because a straight line cannot separate two curved moons.\n- KNN effortlessly achieved high accuracy because it just looks at local neighborhoods, ignoring the global shape."),
    
    create_markdown_cell("## 10. Experiment\nLet's visualize the decision boundaries to prove *why* KNN succeeded."),
    create_code_cell([
        "from matplotlib.colors import ListedColormap",
        "",
        "def plot_decision_boundary(model, X, y, title):",
        "    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5",
        "    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5",
        "    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))",
        "    Z = model.predict(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)",
        "    plt.contourf(xx, yy, Z, alpha=0.3, cmap=ListedColormap(['#FFAAAA', '#AAAAFF']))",
        "    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=ListedColormap(['red', 'blue']), edgecolor='k')",
        "    plt.title(title)",
        "",
        "plt.figure(figsize=(12, 5))",
        "plt.subplot(1, 2, 1)",
        "plot_decision_boundary(log_reg, X, y, 'Logistic Regression (Linear)')",
        "plt.subplot(1, 2, 2)",
        "plot_decision_boundary(knn, X, y, 'KNN (K=5) (Non-Linear)')",
        "plt.show()"
    ]),
    create_markdown_cell("> As you can see, Logistic Regression is permanently stuck as a straight line. KNN gracefully curves to encapsulate the blue points."),
    
    create_markdown_cell("## 11. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "knn_k1 = KNeighborsClassifier(n_neighbors=1)",
        "knn_k1.fit(X_train, y_train)",
        "",
        "knn_k300 = KNeighborsClassifier(n_neighbors=len(X_train))",
        "knn_k300.fit(X_train, y_train)"
    ]),
    create_markdown_cell("> **Question:** What happens to the decision boundary if `K=1`? What happens if `K` equals the total number of training samples?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print('If K=1: The model perfectly memorizes the training data (Massive Overfitting). The decision boundary will be incredibly jagged and capture every single noise point.')",
        "print('If K=N: The model just takes a global majority vote. It will always predict whichever class is most common in the entire dataset, ignoring features entirely (Massive Underfitting).')"
    ]),
    
    create_markdown_cell("## 12. Coding Exercise\nProve that `K=1` overfits. Train a KNN with `n_neighbors=1` and plot its decision boundary using the `plot_decision_boundary` function we defined in Section 10."),
    create_code_cell([
        "# YOUR CODE HERE",
        "knn_1 = KNeighborsClassifier(n_neighbors=1)",
        "knn_1.fit(X_train, y_train)",
        "",
        "plt.figure(figsize=(6, 5))",
        "plot_decision_boundary(knn_1, X, y, 'KNN (K=1) (Severe Overfitting)')",
        "plt.show()",
        "print('Notice the tiny islands of red floating in the blue sea. The model memorized the noise!')"
    ]),
    
    create_markdown_cell("## 13. Debugging Challenge\nA data scientist is using KNN to classify houses as Cheap (0) or Expensive (1). \nFeature 1: Square Footage (1000 - 5000)\nFeature 2: Distance to city center in miles (0.1 - 5.0)\n\nThe model is completely ignoring Feature 2. Why?"),
    create_code_cell([
        "# Conceptual Bug",
        "print('Error: The model is acting as if Distance to city center doesn\\'t exist.')",
        "print('Why? Because Square Footage is in the thousands, and Distance is less than 5.')",
        "print('In Euclidean math: sqrt((5000-2000)^2 + (5-1)^2) is completely dominated by the 3000^2.')"
    ]),
    create_markdown_cell("> **Rule:** Because KNN relies purely on mathematical distance, you MUST use `StandardScaler` so that all features contribute equally to the distance calculation."),
    
    create_markdown_cell("## 14. Model Evaluation\nHow do we choose $K$? \nAs $K$ gets smaller (e.g., 1), the model becomes more complex (Overfitting/High Variance).\nAs $K$ gets larger (e.g., 50), the model becomes simpler (Underfitting/High Bias).\nWe use Cross-Validation to find the \"Goldilocks\" $K$ (usually an odd number to prevent voting ties)."),
    
    create_markdown_cell("## 15. Real-World Example\nSpotify's \"Discover Weekly\" relies heavily on concepts derived from KNN. If you listen to a specific set of artists, Spotify plots you in a massive multi-dimensional space. To find new songs for you, it simply finds the $K$ closest users in that space (people with identical music tastes) and recommends whatever they recently liked that you haven't heard yet."),
    
    create_markdown_cell("## 16. Mini Project\nBuild a Pipeline that correctly applies `StandardScaler` and `KNeighborsClassifier(n_neighbors=7)`. \nTest it on a new dataset where scaling actually matters!"),
    create_code_cell([
        "from sklearn.pipeline import Pipeline",
        "from sklearn.preprocessing import StandardScaler",
        "from sklearn.datasets import make_classification",
        "",
        "# Create data where Feature 0 is tiny and Feature 1 is massive",
        "X_scale, y_scale = make_classification(n_samples=200, n_features=2, n_redundant=0, weights=[0.5], random_state=42)",
        "X_scale[:, 1] = X_scale[:, 1] * 1000 # Make Feature 1 artificially massive",
        "",
        "X_tr, X_te, y_tr, y_te = train_test_split(X_scale, y_scale, test_size=0.3, random_state=42)",
        "",
        "# 1. Unscaled KNN (Bad)",
        "bad_knn = KNeighborsClassifier(n_neighbors=7)",
        "bad_knn.fit(X_tr, y_tr)",
        "print(f'Unscaled Accuracy: {accuracy_score(y_te, bad_knn.predict(X_te)):.2f}')",
        "",
        "# 2. Scaled KNN Pipeline (Good)",
        "good_knn = Pipeline([",
        "    ('scaler', StandardScaler()),",
        "    ('knn', KNeighborsClassifier(n_neighbors=7))",
        "])",
        "good_knn.fit(X_tr, y_tr)",
        "print(f'Scaled Accuracy:   {accuracy_score(y_te, good_knn.predict(X_te)):.2f}')"
    ]),
    
    create_markdown_cell("## 17. Common Mistakes\n- **Not Scaling Data**: The most fatal error in KNN.\n- **Choosing an even K**: If K=4, and the vote is 2 to 2, the model breaks the tie randomly, which adds instability. Always use odd K (3, 5, 7).\n- **High Dimensionality**: KNN suffers from the \"Curse of Dimensionality\". If you have 500 features, \"distance\" loses its mathematical meaning, and KNN's accuracy will plummet. (We use Random Forests for wide datasets)."),
    
    create_markdown_cell("## 18. Interview Questions\n- **Beginner**: Why is KNN called a \"Lazy Learner\"?\n- **Intermediate**: Explain why you must scale data before using KNN.\n- **Advanced**: Explain the \"Curse of Dimensionality\" and why KNN performs poorly on datasets with hundreds of features."),
    
    create_markdown_cell("## 19. Knowledge Check\n- What hyperparameter controls the complexity of the model? (`n_neighbors` or K)\n- As K increases, does the model Overfit or Underfit? (Underfit)"),
    
    create_markdown_cell("## 20. Summary\n- **KNN** classifies points by taking a majority vote of its closest neighbors.\n- It natively handles non-linear patterns.\n- Smaller K = Overfitting. Larger K = Underfitting.\n- You MUST use `StandardScaler`.\n- Struggles with datasets containing hundreds of features."),
    
    create_markdown_cell("## 21. Homework\nLoad the `load_wine` dataset. Build a `StandardScaler` + `KNN` pipeline. Loop through $K = [1, 3, 5, 7, 9, 11]$ and print the accuracy for each to see how the performance changes as you adjust the hyperparameter!")
]

# Read existing notebook and update cells
filename = "Day_17_K_Nearest_Neighbors.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day17_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")

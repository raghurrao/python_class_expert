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

day18_cells = [
    create_markdown_cell("# PHASE 3 — CLASSIFICATION"),
    create_markdown_cell("# Day 18 — Support Vector Machines (SVM)"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Explain how Support Vector Machines classify data by finding the \"widest street\".\n- Understand what a Support Vector is.\n- Use the Kernel Trick (`linear` vs `rbf`) to separate complex, overlapping data.\n- Understand why SVMs absolutely require feature scaling."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 15 (Logistic Regression).\n- Day 4 (Preprocessing / Scaling)."),
    
    create_markdown_cell("## 3. Concept: The Widest Street\nLogistic Regression draws a line to separate two classes. But if the classes are far apart, you could draw *infinite* lines between them that perfectly separate the data. Which line is the best?\n\n**Support Vector Machines (SVM)** don't just draw a line; they draw a \"street\". \nTheir goal is to draw the **widest possible street** between the two classes. The line in the exact center of the street is the decision boundary."),
    
    create_markdown_cell("## 4. Why Does This Matter?\nBy maximizing the margin (the width of the street), SVMs create models that are highly confident and generalize exceptionally well to unseen data. Before Deep Learning took over, SVMs were widely considered the single most powerful algorithm in Machine Learning."),
    
    create_markdown_cell("## 5. Intuition\nImagine separating Red balls from Blue balls on a table using a wooden stick. \n- Logistic Regression just throws the stick down so that Reds are on one side and Blues on the other.\n- SVM carefully places the stick perfectly in the middle, pushing it as far away from the closest Red ball and the closest Blue ball as physically possible. \n\nThose closest balls that are touching the edges of the \"street\" are called **Support Vectors**. They are the only data points the model actually cares about!"),
    
    create_markdown_cell("## 6. Mathematical Foundation: The Kernel Trick\nWhat if the Red balls are entirely surrounded by a ring of Blue balls? You can't draw a straight line through them.\n\nSVMs use the **Kernel Trick**. Mathematically, it temporarily adds a 3rd dimension to your data (e.g., throwing the balls into the air). The Red balls might fly higher than the Blue balls. The SVM then slices a flat sheet of paper (a plane) between them in mid-air. When they fall back to the table, that flat slice looks like a perfect circle!\n\nThe most common kernel for non-linear data is the **RBF (Radial Basis Function) Kernel**."),
    
    create_markdown_cell("## 7. Scikit-learn API\n```python\nfrom sklearn.svm import SVC\nmodel = SVC(kernel='linear') # or kernel='rbf'\n```"),
    
    create_markdown_cell("## 8. Simple Example\nLet's generate a dataset with a circle of points inside another circle of points. A straight line will completely fail. Let's see how the RBF kernel handles it."),
    create_code_cell([
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "from sklearn.datasets import make_circles",
        "from sklearn.linear_model import LogisticRegression",
        "from sklearn.svm import SVC",
        "from sklearn.model_selection import train_test_split",
        "from sklearn.metrics import accuracy_score",
        "",
        "# 1. Generate Non-Linear Data (Circles)",
        "X, y = make_circles(n_samples=300, noise=0.1, factor=0.4, random_state=42)",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)",
        "",
        "# 2. Train Logistic Regression (Straight Line)",
        "log_reg = LogisticRegression()",
        "log_reg.fit(X_train, y_train)",
        "",
        "# 3. Train SVM with RBF Kernel (Non-Linear)",
        "svm_rbf = SVC(kernel='rbf', random_state=42)",
        "svm_rbf.fit(X_train, y_train)",
        "",
        "print(f'Logistic Regression Accuracy: {accuracy_score(y_test, log_reg.predict(X_test)):.2f}')",
        "print(f'SVM (RBF Kernel) Accuracy:    {accuracy_score(y_test, svm_rbf.predict(X_test)):.2f}')"
    ]),
    
    create_markdown_cell("## 9. Code Walkthrough\n- `make_circles` generates a dataset where Class 1 is clustered in the center, and Class 0 forms a ring around it.\n- Logistic Regression (accuracy ~50%) just guessed, because a straight line can't capture a circle.\n- `SVC(kernel='rbf')` mathematically projected the data into a higher dimension, sliced it, and perfectly separated the classes (accuracy ~100%)."),
    
    create_markdown_cell("## 10. Experiment\nLet's visualize the decision boundaries using the same plotting function from yesterday."),
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
        "plot_decision_boundary(svm_rbf, X, y, 'SVM with RBF Kernel (Non-Linear)')",
        "plt.show()"
    ]),
    create_markdown_cell("> Look at the SVM! The RBF kernel perfectly drew a circular boundary around the inner cluster. A \"Linear\" kernel would have looked exactly like the Logistic Regression plot."),
    
    create_markdown_cell("## 11. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "svm_linear = SVC(kernel='linear', C=1.0)",
        "svm_linear.fit(X_train, y_train)",
        "",
        "svm_c_huge = SVC(kernel='linear', C=100000.0)",
        "svm_c_huge.fit(X_train, y_train)"
    ]),
    create_markdown_cell("> **Question:** The `C` hyperparameter controls the \"strictness\" of the street. If `C` is huge, the model is utterly terrified of making a single mistake on the training data. Will a huge `C` lead to Overfitting or Underfitting?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print('A huge C leads to severe Overfitting (High Variance).')",
        "print('The model will make the street incredibly narrow, and draw absurd, jagged lines just to ensure not a single training point is on the wrong side.')",
        "print('A small C creates a wider street, allowing a few mistakes (violations) on the training set, but generalizing much better to new data.')"
    ]),
    
    create_markdown_cell("## 12. Coding Exercise\nProve that SVMs absolutely require feature scaling. \nTake the `X_train` from earlier and artificially multiply the first column by 10,000. \nTrain an `SVC(kernel='rbf')` on this unscaled data. Then build a Pipeline with `StandardScaler` + `SVC` and train it on the same data. Compare their accuracies on `X_test`."),
    create_code_cell([
        "# YOUR CODE HERE",
        "from sklearn.pipeline import Pipeline",
        "from sklearn.preprocessing import StandardScaler",
        "",
        "X_train_bad = X_train.copy()",
        "X_train_bad[:, 0] = X_train_bad[:, 0] * 10000",
        "X_test_bad = X_test.copy()",
        "X_test_bad[:, 0] = X_test_bad[:, 0] * 10000",
        "",
        "# Unscaled (Bad)",
        "bad_svm = SVC(kernel='rbf', random_state=42)",
        "bad_svm.fit(X_train_bad, y_train)",
        "print('Unscaled SVM Accuracy:', accuracy_score(y_test, bad_svm.predict(X_test_bad)))",
        "",
        "# Scaled (Good)",
        "good_svm = Pipeline([",
        "    ('scaler', StandardScaler()),",
        "    ('svm', SVC(kernel='rbf', random_state=42))",
        "])",
        "good_svm.fit(X_train_bad, y_train)",
        "print('Scaled SVM Accuracy:  ', accuracy_score(y_test, good_svm.predict(X_test_bad)))"
    ]),
    
    create_markdown_cell("## 13. Debugging Challenge\nA Machine Learning engineer trained an `SVC(kernel='rbf')` model. They want to check the `.predict_proba()` of a patient having cancer, but the code crashed saying: `AttributeError: predict_proba is not available when probability=False`. Why?"),
    create_code_cell([
        "# Buggy conceptual code",
        "try:",
        "    # model = SVC(kernel='rbf')",
        "    # model.fit(X_train, y_train)",
        "    # probs = model.predict_proba(X_test)",
        "    print('Error: SVMs do not natively output probabilities. They output geometric distances.')",
        "except Exception as e:",
        "    print('Error:', e)"
    ]),
    create_markdown_cell("> **Hint:** Because SVM is purely geometric (measuring distance to the street), it doesn't naturally understand \"probability\". \n> **Rule:** If you absolutely need `.predict_proba()` from an SVM, you MUST pass `probability=True` when instantiating the model (e.g., `SVC(probability=True)`). Note: This makes training much slower!"),
    
    create_markdown_cell("## 14. Model Evaluation\nWhen should you use SVMs?\n- **Small to Medium Datasets**: SVMs are mathematically intense. They scale horribly with large datasets (e.g., > 100,000 rows) and will take hours to train.\n- **High Dimensionality**: SVMs handle datasets with huge amounts of features very well.\n- **Non-Linear Data**: The RBF kernel is magic for complex shapes."),
    
    create_markdown_cell("## 15. Real-World Example\nBefore Convolutional Neural Networks (CNNs), SVMs were the gold standard for Image Recognition (like identifying handwritten digits for the post office). An image is just a grid of pixels (features). A 28x28 pixel image has 784 features. SVMs naturally handle this high dimensionality and can draw complex boundaries to separate the number '4' from the number '9'."),
    
    create_markdown_cell("## 16. Mini Project\nLet's prove the SVM handles dimensionality well. Generate a dataset with 500 features using `make_classification(n_samples=200, n_features=500, random_state=42)`. \nBuild a pipeline with `StandardScaler` and `SVC(kernel='linear')`. Print the accuracy."),
    create_code_cell([
        "from sklearn.datasets import make_classification",
        "",
        "X_wide, y_wide = make_classification(n_samples=200, n_features=500, random_state=42)",
        "X_tr_w, X_te_w, y_tr_w, y_te_w = train_test_split(X_wide, y_wide, test_size=0.3, random_state=42)",
        "",
        "wide_pipe = Pipeline([",
        "    ('scaler', StandardScaler()),",
        "    ('svm', SVC(kernel='linear', random_state=42))",
        "])",
        "",
        "wide_pipe.fit(X_tr_w, y_tr_w)",
        "print('Accuracy on 500-feature dataset:', accuracy_score(y_te_w, wide_pipe.predict(X_te_w)))",
        "print('Even with massive dimensionality, the SVM finds the \"widest street\" efficiently!')"
    ]),
    
    create_markdown_cell("## 17. Common Mistakes\n- **Not using StandardScaler**: As we proved in Section 12, SVM relies entirely on measuring distance. If features aren't scaled, it breaks entirely.\n- **Using SVM on 1 Million rows**: The training time will be astronomical. Use Random Forests or Gradient Boosting instead.\n- **Not setting `probability=True`**: Crashing your deployment pipeline because the API couldn't find `.predict_proba()`."),
    
    create_markdown_cell("## 18. Interview Questions\n- **Beginner**: What does the SVM try to maximize between the two classes? (Answer: The Margin / Width of the street).\n- **Intermediate**: What is a Support Vector? (Answer: The data points closest to the decision boundary that dictate exactly where the boundary is drawn).\n- **Advanced**: Explain the Kernel Trick in your own words."),
    
    create_markdown_cell("## 19. Knowledge Check\n- What is the most common Kernel used for non-linear data? (RBF)\n- Does a high `C` parameter cause Overfitting or Underfitting? (Overfitting)"),
    
    create_markdown_cell("## 20. Summary\n- **SVMs** classify by finding the widest street (margin) between classes.\n- **Support Vectors** are the edge points touching the street.\n- The **Kernel Trick** (RBF) projects data to higher dimensions to slice complex shapes.\n- You MUST use `StandardScaler`.\n- Excellent for high-feature datasets, terrible for millions of rows."),
    
    create_markdown_cell("## 21. Homework\nLoad the `load_wine` dataset. Build a pipeline with `StandardScaler` and `SVC(kernel='rbf')`. Print the `classification_report`. Then, train a second model with `SVC(kernel='linear')` and compare the accuracies. Which kernel works best for the wine data?")
]

# Read existing notebook and update cells
filename = "Day_18_Support_Vector_Machines.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day18_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")

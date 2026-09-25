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

day2_cells = [
    create_markdown_cell("# PHASE 1 — MACHINE LEARNING FOUNDATIONS"),
    create_markdown_cell("# Day 02 — Scikit learn API and ML Workflow"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Understand the core Scikit-learn objects: Estimators, Predictors, and Transformers.\n- Explain the difference between `.fit()`, `.predict()`, `.transform()`, and `.fit_transform()`.\n- Build your first complete end-to-end Machine Learning workflow."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 1 Concepts (X, y, supervised vs unsupervised learning).\n- Basic Numpy and Pandas."),
    
    create_markdown_cell("## 3. Concept\nScikit-learn is built around a beautifully consistent Object-Oriented API.\n\n1. **Estimators**: Any object that can learn from data (e.g., `LogisticRegression`, `MinMaxScaler`). They all implement `.fit(X, y)`.\n2. **Predictors**: Estimators that can make predictions (e.g., Models). They implement `.predict(X)` and `.score(X, y)`.\n3. **Transformers**: Estimators that can modify or filter data (e.g., Scalers). They implement `.transform(X)` and `.fit_transform(X)`."),
    
    create_markdown_cell("## 4. Why Does This Matter?\nIf you learn the API for one model (like Linear Regression), you automatically know how to use almost every other model in Scikit-learn (Random Forests, SVMs, Neural Networks). The API consistency drastically reduces the learning curve."),
    
    create_markdown_cell("## 5. Intuition\nThink of the `.fit()` method as **\"studying for the exam.\"** The model looks at the data (X) and the answers (y) and learns the rules.\n\nThink of `.predict()` as **\"taking the exam.\"** The model is given new data (X_test) and has to output the answers (predictions).\n\nThink of `.transform()` as **\"translating the exam paper.\"** It changes the data into a format that is easier for the model to understand (like scaling numbers)."),
    
    create_markdown_cell("## 6. Mathematical Foundation\nWhen we call `.fit(X, y)` on a model, we are minimizing a **Loss Function** $L(y, f(X, \\theta))$.\n\nFor example, in Ordinary Least Squares (OLS), `.fit()` solves:\n\n$$ \\hat{\\theta} = \\arg\\min_{\\theta} \\sum_{i=1}^{N} (y_i - X_i \\theta)^2 $$\n\nThe `.predict(X)` step simply computes:\n\n$$ \\hat{y} = X \\hat{\\theta} $$"),
    
    create_markdown_cell("## 7. Scikit-learn API\nThe ML Workflow looks like this:\n1. Prepare `X` and `y`.\n2. Initialize the model: `model = ModelClass(hyperparameters)`\n3. Train: `model.fit(X_train, y_train)`\n4. Predict: `predictions = model.predict(X_test)`\n5. Evaluate: `score = model.score(X_test, y_test)`"),
    
    create_markdown_cell("## 8. Simple Example\nLet's build a complete workflow on the classic Breast Cancer dataset."),
    create_code_cell([
        "from sklearn.datasets import load_breast_cancer",
        "from sklearn.model_selection import train_test_split",
        "from sklearn.ensemble import RandomForestClassifier",
        "",
        "# 1. Load Data",
        "data = load_breast_cancer()",
        "X, y = data.data, data.target",
        "",
        "# 2. Split Data (More on this in Day 3!)",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)",
        "",
        "# 3. Initialize Estimator/Predictor",
        "model = RandomForestClassifier(n_estimators=100, random_state=42)",
        "",
        "# 4. Fit (Learn)",
        "model.fit(X_train, y_train)",
        "",
        "# 5. Predict",
        "y_pred = model.predict(X_test)",
        "",
        "# 6. Evaluate",
        "accuracy = model.score(X_test, y_test)",
        "print(f'Test Accuracy: {accuracy * 100:.2f}%')"
    ]),
    
    create_markdown_cell("## 9. Code Walkthrough\n- `load_breast_cancer()`: Loads real-world data.\n- `train_test_split(...)`: Randomly divides data so we test on data the model hasn't seen.\n- `RandomForestClassifier(...)`: We initialize our predictor. (Parameters like `n_estimators` are set before fitting).\n- `.fit(...)`: The algorithm studies the training data.\n- `.predict(...)`: Generates predictions on the test set.\n- `.score(...)`: Automatically compares `y_pred` with `y_test` and returns accuracy."),
    
    create_markdown_cell("## 10. Experiment\nChange `test_size=0.2` to `test_size=0.5`. What happens to the Test Accuracy? Why?"),
    create_code_cell([
        "X_train_half, X_test_half, y_train_half, y_test_half = train_test_split(X, y, test_size=0.5, random_state=42)",
        "model.fit(X_train_half, y_train_half)",
        "print(f'Test Accuracy (50% split): {model.score(X_test_half, y_test_half) * 100:.2f}%')"
    ]),
    create_markdown_cell("> **Note**: Accuracy usually drops because the model has less data to learn from!"),
    
    create_markdown_cell("## 11. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "from sklearn.preprocessing import StandardScaler",
        "scaler = StandardScaler()",
        "X_scaled = scaler.fit_transform(X_train)",
        "X_test_scaled = scaler.transform(X_test)"
    ]),
    create_markdown_cell("> **Question:** Why do we use `.fit_transform()` on the training data, but ONLY `.transform()` on the test data?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print('Answer: We use `.fit()` on the training data so the scaler learns the mean and variance of the training set.')",
        "print('We ONLY `.transform()` the test set because we must pretend the test set is completely unseen. If we fit on the test set, we cause Data Leakage!')"
    ]),
    
    create_markdown_cell("## 12. Coding Exercise\nBuild an ML workflow for regression. \n1. Load `make_regression`.\n2. Split it using `train_test_split`.\n3. Train a `LinearRegression` model.\n4. Score it."),
    create_code_cell([
        "from sklearn.datasets import make_regression",
        "from sklearn.linear_model import LinearRegression",
        "from sklearn.model_selection import train_test_split",
        "",
        "# YOUR CODE HERE",
        "X_reg, y_reg = make_regression(n_samples=500, n_features=3, noise=10, random_state=42)",
        "X_train_r, X_test_r, y_train_r, y_test_r = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42)",
        "reg_model = LinearRegression()",
        "reg_model.fit(X_train_r, y_train_r)",
        "print(f'Regression R^2 Score: {reg_model.score(X_test_r, y_test_r):.4f}')"
    ]),
    
    create_markdown_cell("## 13. Debugging Challenge\nThe code below throws an error. Diagnose and fix it!"),
    create_code_cell([
        "from sklearn.ensemble import RandomForestClassifier",
        "from sklearn.datasets import make_classification",
        "",
        "X_bug, y_bug = make_classification(n_samples=100, random_state=42)",
        "model_bug = RandomForestClassifier()",
        "",
        "# Uncomment to see error:",
        "# predictions_bug = model_bug.predict(X_bug)",
        "# model_bug.fit(X_bug, y_bug)"
    ]),
    create_markdown_cell("> **Hint:** Look at the order of the method calls. Can you take an exam before studying?"),
    
    create_markdown_cell("## 14. Model Evaluation\nThe `.score()` method is convenient, but what metric is it actually using?\n- For Classifiers (like `LogisticRegression`): It returns **Accuracy**.\n- For Regressors (like `LinearRegression`): It returns **$R^2$ (Coefficient of Determination)**."),
    
    create_markdown_cell("## 15. Real-World Example\nIn production, you don't just train a model and throw it away. The `.fit()` step happens offline (maybe once a week). The `.predict()` step happens in real-time on a web server every time a user requests a prediction."),
    
    create_markdown_cell("## 16. Mini Project\nWrite a function `train_and_evaluate(model, X, y)` that:\n1. Splits the data (80/20).\n2. Fits the provided model.\n3. Returns the test score."),
    create_code_cell([
        "def train_and_evaluate(model, X, y):",
        "    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)",
        "    model.fit(X_train, y_train)",
        "    return model.score(X_test, y_test)",
        "",
        "# Test your function",
        "from sklearn.tree import DecisionTreeClassifier",
        "score = train_and_evaluate(DecisionTreeClassifier(), X, y)",
        "print(f'Decision Tree Score: {score:.4f}')"
    ]),
    
    create_markdown_cell("## 17. Common Mistakes\n- **Calling `.predict()` before `.fit()`**: Throws a `NotFittedError`.\n- **Fitting a Transformer on the test set**: Causes data leakage. Never call `scaler.fit(X_test)`.\n- **Passing `y` to `predict()`**: `.predict(X)` only takes features, not targets!"),
    
    create_markdown_cell("## 18. Interview Questions\n- **Beginner**: What is the difference between an Estimator and a Transformer in Scikit-learn?\n- **Intermediate**: Why must you use `.transform()` instead of `.fit_transform()` on test data?"),
    
    create_markdown_cell("## 19. Knowledge Check\n- Which method calculates the internal parameters? (`fit`)\n- Which method outputs predictions? (`predict`)\n- Which method changes data format? (`transform`)"),
    
    create_markdown_cell("## 20. Summary\n- **Estimator**: `.fit(X, y)` - Learns from data.\n- **Predictor**: `.predict(X)` - Makes predictions.\n- **Transformer**: `.transform(X)` - Modifies data.\n- The workflow is always: Initialize -> Fit on Train -> Transform/Predict on Test."),
    
    create_markdown_cell("## 21. Homework\nLoad the `load_wine()` dataset from `sklearn.datasets`. Split the data, train a `LogisticRegression(max_iter=10000)` model, and report the accuracy score.")
]

# Read existing notebook and update cells
filename = "Day_02_Scikit_learn_API_and_ML_Workflow.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day2_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")

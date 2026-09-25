import json
import os

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

day31_cells = [
    create_markdown_cell("# BONUS CONTENT"),
    create_markdown_cell("# Day 31 — Advanced Ensembling (XGBoost)"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Differentiate between **Bagging** (Random Forests) and **Boosting** (Gradient Boosting).\n- Understand why XGBoost dominates Kaggle tabular data competitions.\n- Install and use the `XGBClassifier` seamlessly inside a Scikit-Learn Pipeline."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 12 & 13 (Decision Trees & Ensembles)."),
    
    create_markdown_cell("## 3. Concept: Bagging vs. Boosting\nIn Day 13, we learned about **Bagging** (Bootstrap Aggregating) via Random Forests. \n- **Bagging**: You build 100 deep, complex Decision Trees in *parallel*. Each tree gets a random subset of data. They all vote. If one tree makes a mistake, the others overrule it.\n\n**Boosting** is entirely different.\n- **Boosting**: You build 100 very shallow, weak Decision Trees *sequentially*. Tree 1 is built. It makes mistakes. Tree 2 is built specifically to fix the mistakes of Tree 1. Tree 3 is built to fix the mistakes of Tree 2. \nThey don't overrule each other; they act as a relay race, constantly correcting the team's errors."),
    
    create_markdown_cell("## 4. Concept: XGBoost (eXtreme Gradient Boosting)\nScikit-learn has built-in Gradient Boosting models (`GradientBoostingClassifier`), but a team of researchers built an external library called **XGBoost**. \nXGBoost is heavily optimized for speed, handles missing data automatically, and has mathematically advanced regularization to prevent overfitting. \nFor years, if a dataset was tabular (rows and columns, not images or text), XGBoost was the algorithm that won 1st place in almost every Kaggle competition."),
    
    create_markdown_cell("## 5. Third-Party Integration\nXGBoost is not part of Scikit-learn. You must install it separately (`pip install xgboost`).\nHowever, the developers were smart. They built a \"wrapper\" class called `XGBClassifier` that perfectly mimics the Scikit-learn API. \nIt has `.fit()`, `.predict()`, and can be placed natively inside a `Pipeline` or a `GridSearchCV`!"),
    
    create_markdown_cell("## 6. Simple Example: Training XGBoost\nLet's generate some classification data and train an XGBoost model. *Note: You must have xgboost installed in your environment to run this cell!*"),
    create_code_cell([
        "import numpy as np",
        "from sklearn.datasets import make_classification",
        "from sklearn.model_selection import train_test_split",
        "from sklearn.metrics import classification_report",
        "",
        "# Try importing xgboost. If not installed, this will fail gracefully.",
        "try:",
        "    from xgboost import XGBClassifier",
        "    print('XGBoost is installed and ready!')",
        "except ImportError:",
        "    print('XGBoost is not installed. Please run `pip install xgboost` in your terminal.')",
        "",
        "# 1. Generate Data",
        "X, y = make_classification(n_samples=2000, n_features=20, n_informative=10, random_state=42)",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)",
        "",
        "# 2. Initialize and Train XGBoost",
        "# n_estimators: How many trees in the sequence",
        "# learning_rate: How aggressively each tree tries to fix the previous tree's mistakes",
        "# max_depth: Keep it shallow! Usually 3 to 7.",
        "xgb_model = XGBClassifier(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)",
        "",
        "xgb_model.fit(X_train, y_train)",
        "",
        "# 3. Evaluate",
        "y_pred = xgb_model.predict(X_test)",
        "print('\\n--- XGBoost Classification Report ---')",
        "print(classification_report(y_test, y_pred))"
    ]),
    
    create_markdown_cell("## 7. Code Walkthrough\n- `n_estimators=100`: We built 100 sequential trees.\n- `learning_rate=0.1`: The \"shrinkage\". If Tree 1 makes an error, Tree 2 doesn't immediately overcompensate 100%. It steps 10% of the way towards the fix. This requires more trees, but results in massive stability.\n- `max_depth=5`: Unlike Random Forests that grow huge deep trees, Boosting relies on small trees. "),
    
    create_markdown_cell("## 8. Experiment: Scikit-learn Compatibility\nBecause `XGBClassifier` follows the API rules, we can seamlessly drop it into a Scikit-learn Pipeline and Cross-Validate it just like we did in Day 26!"),
    create_code_cell([
        "from sklearn.pipeline import Pipeline",
        "from sklearn.preprocessing import StandardScaler",
        "from sklearn.model_selection import cross_val_score",
        "",
        "# Build a Pipeline containing an external library!",
        "advanced_pipe = Pipeline([",
        "    ('scaler', StandardScaler()),",
        "    ('classifier', XGBClassifier(n_estimators=50, max_depth=4, random_state=42, n_jobs=-1))",
        "])",
        "",
        "# Cross validate it using Scikit-Learn's native function",
        "scores = cross_val_score(advanced_pipe, X, y, cv=5, scoring='accuracy')",
        "",
        "print(f'XGBoost 5-Fold Mean Accuracy: {scores.mean() * 100:.2f}%')",
        "print(f'XGBoost 5-Fold Standard Dev:  ±{scores.std() * 100:.2f}%')"
    ]),
    create_markdown_cell("> It works perfectly! You can mix and match Scikit-learn preprocessors with third-party models as long as they follow the `.fit()` and `.predict()` standards."),
    
    create_markdown_cell("## 9. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "rf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)",
        "xgb = XGBClassifier(n_estimators=100, learning_rate=0.1, random_state=42, n_jobs=-1)"
    ]),
    create_markdown_cell("> **Question:** Both models are asked to build 100 trees. Since Random Forests build trees in parallel, they can assign 25 trees to each of your 4 CPU cores and finish extremely quickly.\n> Can XGBoost do this?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print('No, XGBoost cannot build the trees in parallel.')",
        "print('Why? Because Tree 2 literally cannot be built until Tree 1 is finished, so it knows what mistakes to fix!')",
        "print('\\nHowever, XGBoost IS incredibly fast because it multithreads the internal math of building EACH individual tree (like parallelizing the Gini impurity calculations).')"
    ]),
    
    create_markdown_cell("## 10. Summary of Bonus Day 31\n- **Boosting** builds shallow trees sequentially to fix previous mistakes.\n- **XGBoost** is an industry standard third-party library that dominates tabular data.\n- It perfectly integrates with Scikit-learn `Pipeline` and `GridSearchCV` interfaces.")
]

notebook = {
    "cells": day31_cells,
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 5
}

filename = "Day_31_Advanced_Ensembling_XGBoost.ipynb"
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Created {filename} successfully!")

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

day32_cells = [
    create_markdown_cell("# BONUS CONTENT"),
    create_markdown_cell("# Day 32 — Handling Imbalanced Data (SMOTE)"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Explain the severe dangers of Highly Imbalanced Datasets.\n- Use **SMOTE** (Synthetic Minority Over-sampling Technique) to generate fake data that balances the classes.\n- Use `imblearn.pipeline` to prevent data leakage while oversampling during Cross Validation."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 16 (Classification Metrics: Precision, Recall, F1).\n- Day 26 (Cross Validation & Pipelines)."),
    
    create_markdown_cell("## 3. Concept: The Imbalance Problem\nSuppose you are building a model to detect rare cancer. Out of 10,000 patients in your dataset, only 10 have the cancer (0.1%).\nIf you train a Logistic Regression model on this data, the model will just learn to predict \"Healthy\" 100% of the time. \nIt will achieve a **99.9% Accuracy** and effectively be the most useless model in the world because its Recall is 0. \n\nMachine learning models are lazy. If one class completely dominates the dataset, the math just favors the majority class."),
    
    create_markdown_cell("## 4. Concept: SMOTE\nHow do we fix this? We could just duplicate the 10 cancer patients over and over (Oversampling), but that leads to massive overfitting. \nInstead, we use **SMOTE**. \n\nSMOTE looks at the 10 cancer patients, draws imaginary lines between them in the mathematical space, and generates *brand new, synthetic* cancer patients along those lines. \nIt literally fabricates fake data that perfectly mimics the minority class until both classes have exactly 5,000 rows!"),
    
    create_markdown_cell("## 5. Third-Party Integration\nSMOTE is not built into Scikit-learn. It belongs to a sister library called `imbalanced-learn`. \n*(You can install it via `pip install imbalanced-learn`)*."),
    
    create_markdown_cell("## 6. Simple Example: The Lazy Model\nLet's generate a highly imbalanced dataset and prove that a basic model completely ignores the minority class."),
    create_code_cell([
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "from sklearn.datasets import make_classification",
        "from sklearn.model_selection import train_test_split",
        "from sklearn.linear_model import LogisticRegression",
        "from sklearn.metrics import classification_report",
        "",
        "# Try importing imblearn. If not installed, this will fail gracefully.",
        "try:",
        "    from imblearn.over_sampling import SMOTE",
        "    from imblearn.pipeline import Pipeline as ImbPipeline",
        "    print('imbalanced-learn is installed and ready!')",
        "except ImportError:",
        "    print('imbalanced-learn is not installed. Please run `pip install imbalanced-learn` in your terminal.')",
        "",
        "# 1. Generate Highly Imbalanced Data (99% Class 0, 1% Class 1)",
        "X, y = make_classification(n_samples=5000, n_features=2, n_informative=2, n_redundant=0, ",
        "                           weights=[0.99, 0.01], random_state=42)",
        "",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)",
        "",
        "print('Original Class distribution in Training Set:')",
        "unique, counts = np.unique(y_train, return_counts=True)",
        "print(dict(zip(unique, counts)))",
        "",
        "# 2. Train a standard model",
        "lazy_model = LogisticRegression()",
        "lazy_model.fit(X_train, y_train)",
        "",
        "print('\\n--- Lazy Model Report ---')",
        "print(classification_report(y_test, lazy_model.predict(X_test)))"
    ]),
    create_markdown_cell("> Look at the Recall for Class 1. It's terrible (or even 0). The model is completely broken despite high overall accuracy!"),
    
    create_markdown_cell("## 7. Experiment: Visualizing SMOTE\nLet's apply SMOTE to the training data. We will visually plot what SMOTE actually does to the 2D space."),
    create_code_cell([
        "smote = SMOTE(random_state=42)",
        "X_smote, y_smote = smote.fit_resample(X_train, y_train)",
        "",
        "print('New Class distribution after SMOTE:')",
        "unique, counts = np.unique(y_smote, return_counts=True)",
        "print(dict(zip(unique, counts)))",
        "",
        "fig, axes = plt.subplots(1, 2, figsize=(12, 5))",
        "",
        "axes[0].scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='coolwarm', alpha=0.6)",
        "axes[0].set_title('Original Highly Imbalanced Data (Few red dots)')",
        "",
        "axes[1].scatter(X_smote[:, 0], X_smote[:, 1], c=y_smote, cmap='coolwarm', alpha=0.1)",
        "axes[1].set_title('After SMOTE (Red class artificially boosted)')",
        "",
        "plt.show()"
    ]),
    create_markdown_cell("> As you can see, SMOTE generated thousands of fake \"Red\" data points perfectly interspersed among the original real Red data points!"),
    
    create_markdown_cell("## 8. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "smote_model = LogisticRegression()",
        "smote_model.fit(X_smote, y_smote)",
        "",
        "y_pred_smote = smote_model.predict(X_test)"
    ]),
    create_markdown_cell("> **Question:** We trained the model on `X_smote` (where the classes are 50/50). We are predicting on `X_test`. \n> Did we run SMOTE on `X_test`? Should we?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print('NO! You NEVER run SMOTE on the Test data.')",
        "print('The Test Data must always represent the REAL WORLD. In the real world, the disease is 1% rare. We only oversample the TRAINING data to force the model to pay attention.')",
        "",
        "print('\\n--- SMOTE Model Report on Real-World Test Data ---')",
        "print(classification_report(y_test, y_pred_smote))"
    ]),
    create_markdown_cell("> The Recall for Class 1 jumped massively! The model is now actively finding the minority class. (Yes, Precision dropped, meaning more false alarms, but in medical detection, catching the disease is the priority)."),
    
    create_markdown_cell("## 9. The Cross-Validation Leakage Trap\nIf you run SMOTE on your entire `X` array, and then use Scikit-learn's `cross_val_score(cv=5)`, you will cause massive Data Leakage. The fake data generated by SMOTE will bleed across the Training and Test folds!\n\nTo fix this, `imbalanced-learn` provides its own special `Pipeline`. You MUST use `imblearn.pipeline.Pipeline`, NOT `sklearn.pipeline.Pipeline`! \n\nThe `imblearn` pipeline is smart enough to apply SMOTE *only* to the training folds during cross-validation."),
    
    create_markdown_cell("## 10. Coding Exercise\nBuild an `imblearn` pipeline containing `SMOTE` and a `RandomForestClassifier`. \nRun `cross_val_score(cv=3)` on the pipeline using the RAW `X` and `y` arrays (not the smote ones). Print the F1-Score!"),
    create_code_cell([
        "# YOUR CODE HERE",
        "from sklearn.model_selection import cross_val_score",
        "from sklearn.ensemble import RandomForestClassifier",
        "",
        "# Notice we are using ImbPipeline from imblearn, not sklearn!",
        "safe_pipe = ImbPipeline([",
        "    ('smote', SMOTE(random_state=42)),",
        "    ('rf', RandomForestClassifier(random_state=42))",
        "])",
        "",
        "# We score using 'f1_macro' to fairly evaluate both classes",
        "scores = cross_val_score(safe_pipe, X, y, cv=3, scoring='f1_macro')",
        "",
        "print(f'Leak-Free SMOTE Pipeline F1-Macro: {scores.mean():.3f}')"
    ]),
    
    create_markdown_cell("## 11. Summary of Bonus Day 32\n- **Imbalanced Data** breaks models because the math ignores the minority class to achieve high overall accuracy.\n- **SMOTE** synthesizes fake mathematical data to balance the classes.\n- **NEVER oversample the Test Set**. The test set must mimic reality.\n- **Use `imblearn.pipeline`** to prevent data leakage during Cross Validation.")
]

notebook = {
    "cells": day32_cells,
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 5
}

filename = "Day_32_Handling_Imbalanced_Data_SMOTE.ipynb"
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Created {filename} successfully!")

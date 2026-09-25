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

day33_cells = [
    create_markdown_cell("# BONUS CONTENT"),
    create_markdown_cell("# Day 33 — Custom Transformers"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Understand the limitations of Scikit-learn's built-in transformers.\n- Write your own Python classes that inherit from `BaseEstimator` and `TransformerMixin`.\n- Execute arbitrary Pandas code (like custom math or outlier removal) natively inside a `Pipeline`."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 5 (Pipelines).\n- Day 28 (Feature Engineering)."),
    
    create_markdown_cell("## 3. Concept: The Pipeline Limitation\nIn Day 28, we did Feature Engineering (e.g., `df['Square_Footage'] = df['Width'] * df['Length']`). \nWe did this globally, *before* we passed the data into a Pipeline or Cross Validation. \n\nWhile this usually works for simple math, what if your Feature Engineering requires calculating the `mean()` of a column to subtract from another? If you do this globally, you cause Data Leakage (the mean calculation saw the test data).\nTo perfectly lock your custom Pandas code inside the Pipeline, you must build a **Custom Transformer**."),
    
    create_markdown_cell("## 4. Concept: Duck Typing\nScikit-learn Pipelines don't care *what* object you put inside them, as long as the object quacks like a duck. \nSpecifically, the object must have a `.fit()` method and a `.transform()` method. \nIf we write our own Python class with those two methods, the `Pipeline` will gladly accept it and execute it!"),
    
    create_markdown_cell("## 5. Scikit-learn API\nTo ensure our custom class perfectly mimics Scikit-learn, we inherit from two base classes:\n```python\nfrom sklearn.base import BaseEstimator, TransformerMixin\n\nclass MyTransformer(BaseEstimator, TransformerMixin):\n    def fit(self, X, y=None):\n        return self\n        \n    def transform(self, X):\n        # Do custom Pandas stuff here\n        return X\n```"),
    
    create_markdown_cell("## 6. Simple Example: The Math Transformer\nLet's write a Custom Transformer that takes a DataFrame with `Width` and `Length`, and automatically returns a DataFrame with a brand new `Square_Footage` column."),
    create_code_cell([
        "import pandas as pd",
        "import numpy as np",
        "from sklearn.base import BaseEstimator, TransformerMixin",
        "",
        "# 1. Define the Custom Class",
        "class AreaEngineer(BaseEstimator, TransformerMixin):",
        "    def __init__(self):",
        "        pass",
        "        ",
        "    def fit(self, X, y=None):",
        "        # We don't need to learn any math from the data, so just return self",
        "        return self",
        "        ",
        "    def transform(self, X):",
        "        # X will be passed in as a Pandas DataFrame or Numpy Array",
        "        # We'll assume X is a DataFrame for simplicity",
        "        X_new = X.copy()",
        "        X_new['Square_Footage'] = X_new['Width'] * X_new['Length']",
        "        return X_new",
        "",
        "print('Custom Transformer Class defined!')"
    ]),
    
    create_markdown_cell("## 7. Code Walkthrough\n- We created `AreaEngineer`.\n- `fit()`: Required by Scikit-learn, but we don't need it. We just `return self`.\n- `transform()`: We create a copy of the incoming data, do our arbitrary Pandas math (`Width * Length`), and return the modified DataFrame."),
    
    create_markdown_cell("## 8. Experiment: Putting it in a Pipeline\nNow let's prove that Scikit-learn accepts our custom class natively."),
    create_code_cell([
        "from sklearn.pipeline import Pipeline",
        "from sklearn.preprocessing import StandardScaler",
        "from sklearn.linear_model import LinearRegression",
        "",
        "# Create some raw data",
        "X_raw = pd.DataFrame({",
        "    'Width': [10, 20, 15],",
        "    'Length': [20, 40, 30]",
        "})",
        "y = np.array([200, 800, 450])",
        "",
        "# Build a Pipeline containing our custom class!",
        "custom_pipe = Pipeline([",
        "    ('area_creator', AreaEngineer()),",
        "    ('scaler', StandardScaler()),",
        "    ('model', LinearRegression())",
        "])",
        "",
        "# Run fit! The pipeline will automatically route the data through AreaEngineer.",
        "custom_pipe.fit(X_raw, y)",
        "",
        "print('Pipeline executed successfully using the Custom Transformer!')"
    ]),
    create_markdown_cell("> It worked! The Pipeline routed `X_raw` into `AreaEngineer.transform()`, which added the column. Then it routed that 3-column DataFrame into `StandardScaler.fit_transform()`, and finally into `LinearRegression.fit()`."),
    
    create_markdown_cell("## 9. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "class OutlierRemover(BaseEstimator, TransformerMixin):",
        "    def fit(self, X, y=None):",
        "        return self",
        "        ",
        "    def transform(self, X):",
        "        # Drop rows where 'Price' is > 1000",
        "        return X[X['Price'] <= 1000]"
    ]),
    create_markdown_cell("> **Question:** The engineer above wrote a custom transformer to delete outliers. If they put this inside a `Pipeline` and run `.fit(X, y)`, the pipeline will pass `X` into `transform()`, and `X` will lose 5 rows.\n> What happens to `y` when it reaches the `LinearRegression.fit(X, y)` step at the end of the Pipeline?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print('CRASH: ValueError: Found input variables with inconsistent numbers of samples.')",
        "print('\\nWhy? Scikit-learn Pipelines ONLY transform X. They NEVER transform y.')",
        "print('If your Custom Transformer deletes 5 rows from X, y still has all of its original rows.')",
        "print('When the algorithm tries to align X and y at the very end, the lengths don\\'t match, and the code explodes.')"
    ]),
    create_markdown_cell("> **Rule:** You can NEVER drop rows inside a Scikit-learn Pipeline. Pipelines are strictly for modifying/adding/scaling columns."),
    
    create_markdown_cell("## 10. Real-World Example\n**Text Preprocessing**: When dealing with raw Tweets, you often need to remove emojis, strip URLs, and lowercase everything. There is no `StandardScaler` for this. Data scientists write custom `TweetCleaner(BaseEstimator, TransformerMixin)` classes that run Regex functions on the text, and place them as the very first step in their production NLP pipelines."),
    
    create_markdown_cell("## 11. Coding Exercise\nWrite a custom transformer called `ThresholdBinarizer`. \nIts `__init__` should take a `threshold` argument (e.g., `threshold=5`). \nIts `transform` method should return a DataFrame where every value is converted to `1` if it is greater than the threshold, and `0` otherwise. \nTest it on a small DataFrame!"),
    create_code_cell([
        "# YOUR CODE HERE",
        "class ThresholdBinarizer(BaseEstimator, TransformerMixin):",
        "    def __init__(self, threshold=0):",
        "        self.threshold = threshold",
        "        ",
        "    def fit(self, X, y=None):",
        "        return self",
        "        ",
        "    def transform(self, X):",
        "        # Returns 1 if > threshold, else 0",
        "        return (X > self.threshold).astype(int)",
        "",
        "# Test it",
        "test_df = pd.DataFrame({'A': [1, 5, 10], 'B': [-2, 7, 0]})",
        "binarizer = ThresholdBinarizer(threshold=4)",
        "print('Original:\\n', test_df)",
        "print('\\nBinarized:\\n', binarizer.fit_transform(test_df))"
    ]),
    
    create_markdown_cell("## 12. Summary of Bonus Day 33\n- You can inject arbitrary Python/Pandas logic into Scikit-learn by inheriting from `BaseEstimator` and `TransformerMixin`.\n- You must implement a `.fit()` method that returns `self`.\n- You must implement a `.transform()` method that modifies and returns `X`.\n- Custom Transformers cannot drop rows because they cannot modify `y`.")
]

notebook = {
    "cells": day33_cells,
    "metadata": {},
    "nbformat": 4,
    "nbformat_minor": 5
}

filename = "Day_33_Custom_Transformers.ipynb"
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Created {filename} successfully!")

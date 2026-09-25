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

day15_cells = [
    create_markdown_cell("# PHASE 3 — CLASSIFICATION"),
    create_markdown_cell("# Day 15 — Logistic Regression"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Explain the fundamental difference between Regression and Classification.\n- Understand why Linear Regression fails at Classification.\n- Explain the Sigmoid function and how it maps outputs to probabilities.\n- Implement `LogisticRegression` to classify data.\n- Understand the decision boundary threshold (default 0.5)."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 8 (Linear Regression)."),
    
    create_markdown_cell("## 3. Concept: Regression vs Classification\nUntil today, we have only predicted **Continuous Numbers** (House Prices, Salaries). This is **Regression**.\nToday, we start predicting **Categories** (Spam vs Not Spam, Sick vs Healthy, Dog vs Cat). This is **Classification**.\n\nIn binary classification, we mathematically represent the two categories as `0` and `1`."),
    
    create_markdown_cell("## 4. Why Does Linear Regression Fail?\nImagine predicting if a Tumor is Malignant (`1`) or Benign (`0`) based on its Size.\nIf you use Linear Regression, the line might predict `y = 0.5` for a medium tumor. That makes sense. \nBut if you have a massive tumor in your dataset, the line will tilt upwards sharply. Suddenly, Linear Regression might predict `y = 3.2` for a very large tumor, or `y = -1.5` for a very small one.\n\nWhat does a \"probability\" of 3.2 mean? It is mathematically invalid. We need a function that is strictly bounded between `0` and `1`."),
    
    create_markdown_cell("## 5. Intuition\n**Logistic Regression** is just Linear Regression in disguise. \nIt calculates the exact same line: $z = \\beta_0 + \\beta_1x_1$. \nBut before returning the answer, it feeds $z$ into a special mathematical crushing machine called the **Sigmoid Function**.\n\nThe Sigmoid function takes *any* number (from $-\\infty$ to $+\\infty$) and crushes it into a probability between `0.0` and `1.0`."),
    
    create_markdown_cell("## 6. Mathematical Foundation\nThe Sigmoid function equation:\n$$ \\sigma(z) = \\frac{1}{1 + e^{-z}} $$\n\nWhere $z$ is the output of standard Linear Regression.\n\nOnce the model outputs a probability (e.g., `0.85`), it applies a **Decision Boundary** (usually `0.5`). \n- If Probability >= 0.5: Predict Class 1\n- If Probability < 0.5: Predict Class 0"),
    
    create_markdown_cell("## 7. Scikit-learn API\n```python\nfrom sklearn.linear_model import LogisticRegression\nmodel = LogisticRegression()\n```"),
    
    create_markdown_cell("## 8. Simple Example\nLet's generate a dataset where students study for a certain number of hours, and they either Pass (1) or Fail (0)."),
    create_code_cell([
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "from sklearn.linear_model import LinearRegression, LogisticRegression",
        "",
        "# 1. Generate Data",
        "np.random.seed(42)",
        "X_hours = np.sort(10 * np.random.rand(30, 1), axis=0)",
        "y_pass = (X_hours > 5).astype(int).ravel() # Pass if hours > 5",
        "# Add some noise so it's not a perfectly clean split",
        "y_pass[13:17] = [1, 0, 1, 0]",
        "",
        "# 2. Train Linear Regression (Wrong Approach)",
        "lin_reg = LinearRegression()",
        "lin_reg.fit(X_hours, y_pass)",
        "",
        "# 3. Train Logistic Regression (Correct Approach)",
        "log_reg = LogisticRegression()",
        "log_reg.fit(X_hours, y_pass)"
    ]),
    
    create_markdown_cell("## 9. Code Walkthrough\n- We created data `X_hours` (0 to 10 hours) and `y_pass` (0 or 1).\n- We trained both a Linear and Logistic model to see how they differ conceptually."),
    
    create_markdown_cell("## 10. Experiment\nLet's plot both models. Notice how the Linear Regression line shoots off into infinity, while the Logistic Regression line forms a beautiful 'S' curve (the Sigmoid curve)."),
    create_code_cell([
        "X_plot = np.linspace(0, 10, 100).reshape(-1, 1)",
        "",
        "plt.figure(figsize=(10, 5))",
        "plt.scatter(X_hours, y_pass, color='black', zorder=5, label='Data (0=Fail, 1=Pass)')",
        "",
        "# Plot Linear Regression",
        "plt.plot(X_plot, lin_reg.predict(X_plot), color='red', linestyle='--', label='Linear Regression')",
        "",
        "# Plot Logistic Regression (predict_proba returns probabilities)",
        "plt.plot(X_plot, log_reg.predict_proba(X_plot)[:, 1], color='blue', linewidth=3, label='Logistic Regression (Sigmoid)')",
        "",
        "plt.axhline(0.5, color='gray', linestyle=':', label='Decision Boundary (0.5)')",
        "plt.xlabel('Hours Studied')",
        "plt.ylabel('Probability of Passing')",
        "plt.legend()",
        "plt.show()"
    ]),
    create_markdown_cell("> Notice the red dashed line predicts a probability of `1.2` for 10 hours of study. The blue solid line caps perfectly at `1.0`."),
    
    create_markdown_cell("## 11. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "student_hours = np.array([[4.5], [6.5]])",
        "preds = log_reg.predict(student_hours)",
        "probs = log_reg.predict_proba(student_hours)"
    ]),
    create_markdown_cell("> **Question:** What is the difference between `.predict()` and `.predict_proba()`?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print('Predictions:', preds)",
        "print('Probabilities:\\n', probs)",
        "print('\\nWhy? `.predict()` outputs the final hard class (0 or 1).')",
        "print('`.predict_proba()` outputs the exact decimal probabilities for BOTH classes [Prob_Class_0, Prob_Class_1].')"
    ]),
    
    create_markdown_cell("## 12. Coding Exercise\nA pharmaceutical company wants to be extremely cautious. They only want to predict a tumor is Malignant (1) if the model is **90% sure**, not 50% sure. \nHow do you change the decision boundary? \nWrite code to get the probabilities for `student_hours`, and manually create an array of predictions using a `0.90` threshold."),
    create_code_cell([
        "# YOUR CODE HERE",
        "custom_threshold = 0.90",
        "probs_class_1 = log_reg.predict_proba(student_hours)[:, 1]",
        "custom_preds = (probs_class_1 >= custom_threshold).astype(int)",
        "",
        "print('Default (0.5) Preds:', log_reg.predict(student_hours))",
        "print('Custom (0.9) Preds: ', custom_preds)"
    ]),
    
    create_markdown_cell("## 13. Debugging Challenge\nA student tried to build a pipeline with Logistic Regression but got an error saying: `ConvergenceWarning: lbfgs failed to converge`. Why?"),
    create_code_cell([
        "# Buggy conceptual code",
        "try:",
        "    # df = pd.read_csv('massive_dataset.csv')",
        "    # bad_model = LogisticRegression()",
        "    # bad_model.fit(df[['Income', 'Age']], df['Defaulted'])",
        "    print('Error: LBFGS failed to converge. Increase max_iter or SCALE YOUR DATA.')",
        "except Exception as e:",
        "    print('Error:', e)"
    ]),
    create_markdown_cell("> **Hint:** Logistic Regression uses an optimization algorithm called gradient descent (LBFGS). If your features have wildly different scales (Income is 100,000, Age is 25), the algorithm gets confused and fails to find the bottom of the math bowl. \n> **Rule:** You MUST use `StandardScaler` before Logistic Regression."),
    
    create_markdown_cell("## 14. Model Evaluation\nHow do we evaluate Logistic Regression? We can't use RMSE anymore because the target isn't continuous. \nThe simplest metric is **Accuracy**: `(Correct Predictions) / (Total Predictions)`.\nWe will learn much more advanced metrics tomorrow."),
    
    create_markdown_cell("## 15. Real-World Example\nBanks use Logistic Regression for Credit Card Fraud detection. Because Logistic Regression outputs probabilities via `.predict_proba()`, the bank doesn't just block a transaction if it predicts `1`. If the probability of fraud is `0.99`, they block it. If the probability is `0.60`, they might let it go through but send the user an SMS alert. The probability is highly actionable business intelligence."),
    
    create_markdown_cell("## 16. Mini Project\nBuild a proper Pipeline that scales data and applies Logistic Regression. Train it on `X_hours` and `y_pass`. Score it using `.score()` (which calculates Accuracy for classification models)."),
    create_code_cell([
        "from sklearn.pipeline import Pipeline",
        "from sklearn.preprocessing import StandardScaler",
        "",
        "log_pipe = Pipeline([",
        "    ('scaler', StandardScaler()),",
        "    ('model', LogisticRegression(random_state=42))",
        "])",
        "",
        "log_pipe.fit(X_hours, y_pass)",
        "accuracy = log_pipe.score(X_hours, y_pass) # Notice .score() now returns Accuracy, not R^2!",
        "print(f'Pipeline Accuracy: {accuracy * 100:.1f}%')"
    ]),
    
    create_markdown_cell("## 17. Common Mistakes\n- **Not using predict_proba()**: Developers often just use `.predict()` and lose the valuable confidence/probability data.\n- **Not scaling data**: Results in the dreaded `ConvergenceWarning`.\n- **Using Linear Regression for classes**: Produces invalid probabilities > 1 or < 0."),
    
    create_markdown_cell("## 18. Interview Questions\n- **Beginner**: Why is it called Logistic *Regression* if it's used for Classification?\n- **Intermediate**: Explain the role of the Sigmoid function in Logistic Regression.\n- **Advanced**: How would you modify the predictions of a Logistic Regression model if the cost of a False Positive is extremely high? (Answer: Raise the decision boundary threshold above 0.5)."),
    
    create_markdown_cell("## 19. Knowledge Check\n- What function crushes outputs between 0 and 1? (Sigmoid)\n- What method returns the raw probabilities? (`.predict_proba()`)"),
    
    create_markdown_cell("## 20. Summary\n- **Classification** predicts categories (0 or 1).\n- **Logistic Regression** is the foundation of classification.\n- It feeds a linear equation into a **Sigmoid Function** to generate probabilities.\n- The default **Decision Boundary** is 0.5.\n- Always use `StandardScaler` to prevent convergence issues."),
    
    create_markdown_cell("## 21. Homework\nLoad the `load_breast_cancer` dataset from Scikit-learn (`from sklearn.datasets import load_breast_cancer`). Build a Logistic Regression pipeline. What is its accuracy on predicting breast cancer?")
]

# Read existing notebook and update cells
filename = "Day_15_Logistic_Regression.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day15_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")

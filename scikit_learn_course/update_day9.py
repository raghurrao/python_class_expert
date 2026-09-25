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

day9_cells = [
    create_markdown_cell("# PHASE 2 — REGRESSION"),
    create_markdown_cell("# Day 09 — Regression Evaluation"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Calculate and interpret MAE, MSE, RMSE, and $R^2$.\n- Explain the mathematical difference between these metrics.\n- Understand when MAE is better than RMSE (and vice versa) based on outliers.\n- Understand the concept of Adjusted $R^2$ for multiple regression."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 8 (Linear Regression)."),
    
    create_markdown_cell("## 3. Concept\nIn regression, our predictions are almost never 100% perfectly accurate. There is always an error (or residual): $e_i = y_i - \\hat{y}_i$.\n\nTo evaluate a model, we aggregate these errors into a single score. However, *how* we aggregate them drastically changes how the model is penalized for being wrong.\n\n- **MAE** (Mean Absolute Error): The average absolute distance from the truth.\n- **MSE** (Mean Squared Error): The average squared distance.\n- **RMSE** (Root Mean Squared Error): The square root of MSE, bringing it back to the original units.\n- **$R^2$**: The proportion of variance in the target explained by the model."),
    
    create_markdown_cell("## 4. Why Does This Matter?\nIf you are predicting House Prices, being off by $10,000 on a $500,000 house is not a big deal. Being off by $500,000 on a $500,000 house is disastrous. \nDifferent metrics punish large errors (outliers) differently. Choosing the wrong metric leads to selecting the wrong model for your business problem."),
    
    create_markdown_cell("## 5. Intuition\n- **MAE**: \"On average, my house price predictions are off by $15,000.\"\n- **RMSE**: \"On average, my predictions are off by roughly $18,000, but I am penalizing huge misses more heavily.\"\n- **$R^2$**: \"My model explains 85% of the reasons why some houses are more expensive than others.\""),
    
    create_markdown_cell("## 6. Mathematical Foundation\n**MAE** = $\\frac{1}{n} \\sum |y_i - \\hat{y}_i|$\n\n**MSE** = $\\frac{1}{n} \\sum (y_i - \\hat{y}_i)^2$\n\n**RMSE** = $\\sqrt{MSE}$\n\n**$R^2$** = $1 - \\frac{\\sum (y_i - \\hat{y}_i)^2}{\\sum (y_i - \\bar{y})^2}$ (where $\\bar{y}$ is the mean of the true targets).\n\nNotice that MSE and RMSE *square* the error. If an error is $10$, squaring it makes it $100$. This means RMSE violently punishes the model if it makes a few massive mistakes, whereas MAE treats all mistakes linearly."),
    
    create_markdown_cell("## 7. Scikit-learn API\nScikit-learn provides these functions inside the `metrics` module:\n\n```python\nfrom sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score\nmae = mean_absolute_error(y_true, y_pred)\nmse = mean_squared_error(y_true, y_pred)\nrmse = mean_squared_error(y_true, y_pred, squared=False) # or np.sqrt(mse)\nr2 = r2_score(y_true, y_pred)\n```"),
    
    create_markdown_cell("## 8. Simple Example\nLet's generate data with ONE massive outlier and see how it affects MAE vs RMSE."),
    create_code_cell([
        "import numpy as np",
        "from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score",
        "",
        "# True values (House Prices in thousands)",
        "y_true = np.array([100, 100, 100, 100, 1000]) # 1000 is a massive mansion",
        "",
        "# Model A: Predicts perfectly on normal houses, but completely misses the mansion",
        "y_pred_A = np.array([100, 100, 100, 100, 0])",
        "",
        "# Model B: Mediocre predictions on everything",
        "y_pred_B = np.array([300, 300, 300, 300, 700])",
        "",
        "print('Model A:')",
        "print(f'MAE:  {mean_absolute_error(y_true, y_pred_A):.2f}')",
        "print(f'RMSE: {np.sqrt(mean_squared_error(y_true, y_pred_A)):.2f}')",
        "",
        "print('\\nModel B:')",
        "print(f'MAE:  {mean_absolute_error(y_true, y_pred_B):.2f}')",
        "print(f'RMSE: {np.sqrt(mean_squared_error(y_true, y_pred_B)):.2f}')"
    ]),
    
    create_markdown_cell("## 9. Code Walkthrough\n- **Model A** has a much lower MAE (200 vs 220). So according to MAE, Model A is better.\n- **Model B** has a much lower RMSE (223 vs 447). So according to RMSE, Model B is better.\n\nWhy? Because Model A missed the mansion by $1,000! RMSE squared that $1,000 to $1,000,000, violently punishing Model A. Model B missed the normal houses by $200 and the mansion by $300, but RMSE didn't care as much because none of those misses were as massively extreme as $1,000."),
    
    create_markdown_cell("## 10. Experiment\nWhen is MAE better than RMSE?\nIf your dataset has bizarre outliers (like a data entry error where someone typed $15,000,000 instead of $150,000), RMSE will force your model to bend towards the error to avoid the massive squared penalty. \n\n**Use MAE** when you want to ignore outliers.\n**Use RMSE** when large errors are completely unacceptable to your business."),
    create_code_cell([
        "# Example of $R^2$",
        "print(f'Model A R^2: {r2_score(y_true, y_pred_A):.4f}')",
        "print(f'Model B R^2: {r2_score(y_true, y_pred_B):.4f}')"
    ]),
    
    create_markdown_cell("## 11. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "y_actual = np.array([10, 20, 30, 40])",
        "y_predict = np.array([10, 20, 30, 40])",
        "perfect_r2 = r2_score(y_actual, y_predict)",
        "",
        "y_mean_predict = np.array([25, 25, 25, 25])",
        "mean_r2 = r2_score(y_actual, y_mean_predict)"
    ]),
    create_markdown_cell("> **Question:** What is the exact value of `perfect_r2`? What is the exact value of `mean_r2`?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print('Perfect R^2:', perfect_r2)",
        "print('Mean Prediction R^2:', mean_r2)",
        "print('\\nWhy? A perfect model explains 100% (1.0) of the variance. A model that just predicts the average explains 0% (0.0) of the variance.')"
    ]),
    
    create_markdown_cell("## 12. Coding Exercise\nWrite a function `evaluate_regression(y_true, y_pred)` that prints the MAE, MSE, RMSE, and $R^2$ neatly formatted to 2 decimal places."),
    create_code_cell([
        "# YOUR CODE HERE",
        "def evaluate_regression(y_t, y_p):",
        "    mae = mean_absolute_error(y_t, y_p)",
        "    mse = mean_squared_error(y_t, y_p)",
        "    rmse = np.sqrt(mse)",
        "    r2 = r2_score(y_t, y_p)",
        "    print(f'MAE:  {mae:.2f}')",
        "    print(f'MSE:  {mse:.2f}')",
        "    print(f'RMSE: {rmse:.2f}')",
        "    print(f'R^2:  {r2:.2f}')",
        "",
        "# Test it",
        "evaluate_regression(y_true, y_pred_A)"
    ]),
    
    create_markdown_cell("## 13. Debugging Challenge\nThe junior data scientist tried to evaluate their model, but got a wildly negative $R^2$ score. Find the bug!"),
    create_code_cell([
        "# Buggy code",
        "try:",
        "    y_true_bug = np.array([1, 2, 3, 4, 5])",
        "    y_pred_bug = np.array([1.1, 2.1, 2.9, 4.2, 5.0])",
        "    ",
        "    # THE BUG IS HERE:",
        "    bad_r2 = r2_score(y_pred_bug, y_true_bug)",
        "    print('R^2:', bad_r2)",
        "except Exception as e:",
        "    print('Error:', e)"
    ]),
    create_markdown_cell("> **Hint:** Scikit-learn metrics ALWAYS expect the true labels first, then the predictions: `metric(y_true, y_pred)`. Reversing them calculates the variance of the *predictions*, not the truth, which ruins the math!"),
    
    create_markdown_cell("## 14. Model Evaluation (Adjusted R-Squared)\n$R^2$ has a fatal flaw: if you add 1,000 completely random, useless features to your dataset, $R^2$ will technically go up (or stay flat) simply due to random chance correlations. It never goes down.\n\n**Adjusted $R^2$** penalizes you for adding useless features:\n\n$$ R^2_{adj} = 1 - \\left( \\frac{(1 - R^2)(n - 1)}{n - p - 1} \\right) $$\nWhere $n$ is sample size and $p$ is the number of features. Scikit-learn doesn't have a built-in function for this, but it's easy to calculate manually!"),
    
    create_markdown_cell("## 15. Real-World Example\nIn ride-sharing apps (like Uber/Lyft), predicting ETA is a regression task. \nIf the RMSE is huge, it means occasionally the app predicts a 5-minute wait, but the driver arrives in 30 minutes. This ruins user trust! Therefore, ride-sharing companies optimize heavily for RMSE to avoid massive edge-case failures, rather than just MAE."),
    
    create_markdown_cell("## 16. Mini Project\nCalculate the Adjusted $R^2$ for Model A. Assume the dataset had 5 samples ($n=5$) and 2 features ($p=2$)."),
    create_code_cell([
        "n = len(y_true)",
        "p = 2",
        "r2_A = r2_score(y_true, y_pred_A)",
        "",
        "adj_r2 = 1 - ( (1 - r2_A) * (n - 1) / (n - p - 1) )",
        "print(f'R^2: {r2_A:.4f}')",
        "print(f'Adjusted R^2: {adj_r2:.4f}')",
        "print('Notice how Adjusted R^2 is lower, heavily penalizing the model because we used 2 features for only 5 rows of data!')"
    ]),
    
    create_markdown_cell("## 17. Common Mistakes\n- **Comparing MAE to RMSE directly**: MAE will almost always be lower than RMSE. You cannot compare them to each other. You must compare MAE of Model A to MAE of Model B.\n- **Passing strings to regression metrics**: Regression metrics require continuous numbers. You cannot calculate MSE on `['cat', 'dog']`.\n- **Swapping `y_true` and `y_pred`**: Always `y_true` first."),
    
    create_markdown_cell("## 18. Interview Questions\n- **Beginner**: What does an $R^2$ of 0 mean?\n- **Intermediate**: Why might RMSE be a better metric than MAE when predicting the dosage of a dangerous medication?\n- **Advanced**: Why does $R^2$ naturally increase as you add more features, and how does Adjusted $R^2$ fix this?"),
    
    create_markdown_cell("## 19. Knowledge Check\n- Which metric squares the errors before averaging? (MSE / RMSE)\n- Which metric treats all errors linearly? (MAE)"),
    
    create_markdown_cell("## 20. Summary\n- **MAE**: Easy to interpret. Resilient to outliers.\n- **RMSE**: Punishes large errors. Sensitive to outliers.\n- **$R^2$**: Percentage of variance explained.\n- **Adjusted $R^2$**: Fixes $R^2$'s vulnerability to useless features."),
    
    create_markdown_cell("## 21. Homework\nWrite a loop that calculates RMSE and MAE for an array. Then, inject a massive outlier into the array (e.g., change one prediction to be wrong by 1,000,000) and observe how RMSE explodes compared to MAE.")
]

# Read existing notebook and update cells
filename = "Day_09_Regression_Evaluation.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day9_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")

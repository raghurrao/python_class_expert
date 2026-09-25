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

day8_cells = [
    create_markdown_cell("# PHASE 2 — REGRESSION"),
    create_markdown_cell("# Day 08 — Linear Regression"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Define what regression is and when to use it.\n- Understand the mathematics of a linear relationship (coefficients and intercepts).\n- Implement `LinearRegression` using Scikit-learn.\n- Build a simplified Linear Regression model from scratch using NumPy to understand Ordinary Least Squares (OLS)."),
    
    create_markdown_cell("## 2. Prerequisites\n- Phase 1 (Data Splitting, Preprocessing, Pipelines)."),
    
    create_markdown_cell("## 3. Concept\n**Regression** is a supervised learning task where the goal is to predict a *continuous numerical value* (e.g., house price, temperature, sales revenue) rather than a discrete class.\n\n**Linear Regression** assumes that the relationship between the features ($X$) and the target ($y$) is linear. Visually, this means we are trying to draw the 'line of best fit' through our data points."),
    
    create_markdown_cell("## 4. Why Does This Matter?\nLinear Regression is arguably the most famous and widely used statistical model in history. While deep neural networks get the hype, linear models are preferred in many industries (like finance and medicine) because they are incredibly fast, highly interpretable, and computationally cheap."),
    
    create_markdown_cell("## 5. Intuition\nImagine you are predicting House Price based on Square Footage.\n- The **Intercept** (or bias) is the base price of the house even if the square footage is 0 (think of it as the price of the land).\n- The **Coefficient** (or weight) is how much the price increases for *every additional 1 square foot*.\n\nTo draw the best line, the model tries to minimize the **Loss Function**—which is the total distance between the actual data points and the line itself."),
    
    create_markdown_cell("## 6. Mathematical Foundation\nThe equation for Linear Regression is:\n\n$$ \\hat{y} = \\beta_0 + \\beta_1x_1 + \\beta_2x_2 + ... + \\beta_nx_n $$\n\nWhere:\n- $\\hat{y}$ is the predicted value.\n- $\\beta_0$ is the intercept.\n- $\\beta_1 ... \\beta_n$ are the coefficients (weights) for each feature.\n- $x_1 ... x_n$ are the features.\n\n**Ordinary Least Squares (OLS)** is the method used to find the best $\\beta$ values. It minimizes the Sum of Squared Errors (SSE):\n\n$$ SSE = \\sum_{i=1}^{n} (y_i - \\hat{y}_i)^2 $$"),
    
    create_markdown_cell("## 7. Scikit-learn API\nUsing Linear Regression is as simple as importing it from the `linear_model` module.\n\n```python\nfrom sklearn.linear_model import LinearRegression\nmodel = LinearRegression()\nmodel.fit(X_train, y_train)\n```"),
    
    create_markdown_cell("## 8. Simple Example\nLet's generate a dataset mapping Years of Experience to Salary."),
    create_code_cell([
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "from sklearn.linear_model import LinearRegression",
        "from sklearn.model_selection import train_test_split",
        "",
        "# Generate synthetic data",
        "np.random.seed(42)",
        "X = 2 * np.random.rand(100, 1) # Years of Experience (0 to 20 years, scaled by 10 later)",
        "X = X * 10",
        "y = 30000 + 5000 * X + np.random.randn(100, 1) * 10000 # Salary with noise",
        "",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)",
        "",
        "# Train model",
        "lin_reg = LinearRegression()",
        "lin_reg.fit(X_train, y_train)",
        "",
        "print(f'Intercept (β0): {lin_reg.intercept_[0]:.2f}')",
        "print(f'Coefficient (β1): {lin_reg.coef_[0][0]:.2f}')"
    ]),
    
    create_markdown_cell("## 9. Code Walkthrough\n- We created data where Salary $\\approx 30,000 + 5,000 \\times \\text{Experience}$.\n- We added random noise so the data isn't a perfectly straight line.\n- We trained `LinearRegression()`.\n- Notice the model's learned `intercept_` is very close to 30,000, and its `coef_` is very close to 5,000. It successfully discovered the hidden math!"),
    
    create_markdown_cell("## 10. Experiment\nLet's visualize the Line of Best Fit against our test data."),
    create_code_cell([
        "y_pred = lin_reg.predict(X_test)",
        "",
        "plt.scatter(X_test, y_test, color='blue', label='Actual Data')",
        "plt.plot(X_test, y_pred, color='red', linewidth=2, label='Regression Line')",
        "plt.xlabel('Years of Experience')",
        "plt.ylabel('Salary ($)')",
        "plt.title('Linear Regression: Experience vs Salary')",
        "plt.legend()",
        "plt.show()"
    ]),
    
    create_markdown_cell("## 11. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "# Suppose the learned intercept is 32000 and the coefficient is 4800.",
        "new_developer_experience = np.array([[5]])",
        "# prediction = lin_reg.predict(new_developer_experience)"
    ]),
    create_markdown_cell("> **Question:** Using the math equation $y = \\beta_0 + \\beta_1x$, what exact numerical value will the model predict for a developer with 5 years of experience?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "predicted_salary = 32000 + (4800 * 5)",
        "print(f'Manual Math Prediction: {predicted_salary}')",
        "print(f'Model Prediction: {lin_reg.predict(np.array([[5]]))[0][0]:.2f} (Will be slightly different because the actual params are slightly different)')"
    ]),
    
    create_markdown_cell("## 12. Coding Exercise (From Scratch!)\nScikit-learn hides the math. Let's build Ordinary Least Squares (OLS) from scratch using NumPy. \nThe mathematical solution (Normal Equation) for finding the optimal weights $\\theta$ is:\n\n$$ \\hat{\\theta} = (X^T X)^{-1} X^T y $$"),
    create_code_cell([
        "# YOUR CODE HERE",
        "# To calculate intercept, we must add a column of 1s to X_train",
        "X_b = np.c_[np.ones((80, 1)), X_train]",
        "",
        "# Normal Equation: theta = inverse(X_b.T @ X_b) @ X_b.T @ y_train",
        "theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)",
        "",
        "print('NumPy Intercept:', theta_best[0][0])",
        "print('NumPy Coefficient:', theta_best[1][0])",
        "print('\\nCompare these to Scikit-learn results from Section 8. They are IDENTICAL!')"
    ]),
    
    create_markdown_cell("## 13. Debugging Challenge\nThe junior data scientist tried to fit a model, but their code crashed. Find the bug!"),
    create_code_cell([
        "# Buggy code",
        "try:",
        "    X_buggy = np.array([1, 2, 3, 4, 5])",
        "    y_buggy = np.array([2, 4, 6, 8, 10])",
        "    ",
        "    model_buggy = LinearRegression()",
        "    # THE BUG IS HERE:",
        "    model_buggy.fit(X_buggy, y_buggy)",
        "except Exception as e:",
        "    print('Error:', e)"
    ]),
    create_markdown_cell("> **Hint:** Scikit-learn features (`X`) must always be a 2D array, even if you only have 1 feature. You need `X.reshape(-1, 1)`."),
    
    create_markdown_cell("## 14. Model Evaluation\nHow do we know if our line is good? We use $R^2$ (Coefficient of Determination), which `lin_reg.score()` calculates by default.\nAn $R^2$ of 1.0 is perfect. An $R^2$ of 0.0 means your model is no better than simply predicting the average salary for everyone."),
    create_code_cell([
        "r2 = lin_reg.score(X_test, y_test)",
        "print(f'R^2 Score: {r2:.4f}')"
    ]),
    
    create_markdown_cell("## 15. Real-World Example\nIn Real Estate, Linear Regression is heavily used. However, linear models struggle with non-linear relationships. For instance, house price increases with square footage, but eventually plateaus (a 20,000 sqft mansion isn't necessarily twice as expensive as a 10,000 sqft mansion). Linear Regression would incorrectly assume it keeps going up forever at the same rate."),
    
    create_markdown_cell("## 16. Mini Project\nTrain a Multiple Linear Regression model (multiple features) using `make_regression`."),
    create_code_cell([
        "from sklearn.datasets import make_regression",
        "",
        "X_multi, y_multi = make_regression(n_samples=500, n_features=3, noise=15.0, random_state=42)",
        "X_tr, X_te, y_tr, y_te = train_test_split(X_multi, y_multi, test_size=0.2, random_state=42)",
        "",
        "multi_model = LinearRegression()",
        "multi_model.fit(X_tr, y_tr)",
        "",
        "print('Intercept:', multi_model.intercept_)",
        "print('Coefficients:', multi_model.coef_)",
        "print('R^2 Score:', multi_model.score(X_te, y_te))"
    ]),
    
    create_markdown_cell("## 17. Common Mistakes\n- **Extrapolation**: Predicting values way outside your training data. If you train on houses between 1,000-3,000 sqft, predicting the price of a 100,000 sqft warehouse will result in garbage.\n- **Collinearity**: If two features are highly correlated (e.g., 'Square Feet' and 'Square Meters' are both in the dataset), the coefficients will become unstable and meaningless."),
    
    create_markdown_cell("## 18. Interview Questions\n- **Beginner**: What does the intercept represent in Linear Regression?\n- **Intermediate**: What is Ordinary Least Squares minimizing?\n- **Advanced**: Why does multi-collinearity harm the interpretability of Linear Regression coefficients?"),
    
    create_markdown_cell("## 19. Knowledge Check\n- What shape does Scikit-learn expect `X` to be? (2D array)\n- In $y = \\beta_0 + \\beta_1x$, what is $\\beta_1$? (The coefficient/weight)"),
    
    create_markdown_cell("## 20. Summary\n- Linear Regression finds the line of best fit.\n- It minimizes the Sum of Squared Errors (OLS).\n- It is highly interpretable (you can read the coefficients to see exactly how features impact predictions).\n- Use `lin_reg.coef_` and `lin_reg.intercept_` to view the math."),
    
    create_markdown_cell("## 21. Homework\nLoad the `fetch_california_housing` dataset from `sklearn.datasets`. Extract just one feature (`MedInc` - Median Income). Split the data, train a `LinearRegression` model to predict `MedHouseVal` (House Value), and plot the line of best fit over a scatter plot of the data.")
]

# Read existing notebook and update cells
filename = "Day_08_Linear_Regression.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day8_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")

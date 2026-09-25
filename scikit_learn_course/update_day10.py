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

day10_cells = [
    create_markdown_cell("# PHASE 2 — REGRESSION"),
    create_markdown_cell("# Day 10 — Regularization"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Define Overfitting, Underfitting, Bias, and Variance.\n- Understand why standard Linear Regression often fails on complex datasets.\n- Apply L1 (Lasso) and L2 (Ridge) Regularization.\n- Explain how Regularization shrinks coefficients and performs automatic feature selection."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 8 (Linear Regression & Coefficients)."),
    
    create_markdown_cell("## 3. Concept\nIf you give a Linear Regression model 100 features and only 50 rows of data, it will solve the math perfectly. It will draw a line that hits every single training data point ($R^2 = 1.0$). \nHowever, this line will be insanely jagged and complex. When you test it on new data, the predictions will be completely wrong. \n\nThis is **Overfitting** (High Variance): The model memorized the noise in the training data.\nThe opposite is **Underfitting** (High Bias): The model is too simple to capture the underlying pattern.\n\n**Regularization** is the act of mathematically forcing the model to be simpler by punishing large coefficients."),
    
    create_markdown_cell("## 4. Why Does This Matter?\nIn the real world, datasets have hundreds of features (e.g., genetic data might have 20,000 features). Standard Linear Regression will overfit immediately and wildly. Regularization is mandatory to keep the model constrained, robust, and capable of generalizing to unseen data."),
    
    create_markdown_cell("## 5. Intuition\nImagine telling a dog to fetch a ball. \n- **Underfitting (High Bias)**: The dog ignores you and just sits there. It learned nothing.\n- **Overfitting (High Variance)**: The dog remembers that last time you threw the ball, you scratched your nose. So now, the dog refuses to fetch unless you scratch your nose. It learned useless, specific noise.\n- **Regularization**: You put a leash on the dog. It can still run to get the ball, but it can't run wildly into the neighbor's yard. You are *restricting* its complexity."),
    
    create_markdown_cell("## 6. Mathematical Foundation\nStandard OLS minimizes: $Loss = \\sum (y - \\hat{y})^2$\n\n**Ridge (L2 Regularization)** adds a penalty equal to the *square* of the magnitude of coefficients:\n$$ Loss = \\sum (y - \\hat{y})^2 + \\alpha \\sum \\beta_j^2 $$\nEffect: Shrinks all coefficients towards zero, but never exactly zero. Prevents huge weights.\n\n**Lasso (L1 Regularization)** adds a penalty equal to the *absolute value* of the coefficients:\n$$ Loss = \\sum (y - \\hat{y})^2 + \\alpha \\sum |\\beta_j| $$\nEffect: Can shrink coefficients **exactly to zero**. This performs automatic Feature Selection!\n\n**ElasticNet**: A mix of both L1 and L2.\n\n*Note: $\\alpha$ (alpha) controls how strict the leash is. Higher $\\alpha$ = smaller coefficients.*"),
    
    create_markdown_cell("## 7. Scikit-learn API\nScikit-learn provides `Ridge`, `Lasso`, and `ElasticNet` in the `linear_model` module.\n\n```python\nfrom sklearn.linear_model import Ridge, Lasso, ElasticNet\nmodel = Ridge(alpha=1.0)\n```"),
    
    create_markdown_cell("## 8. Simple Example\nLet's intentionally overfit a dataset with 10 rows and 15 useless features, and see how Ridge and Lasso fix it."),
    create_code_cell([
        "import numpy as np",
        "import pandas as pd",
        "import matplotlib.pyplot as plt",
        "from sklearn.linear_model import LinearRegression, Ridge, Lasso",
        "from sklearn.model_selection import train_test_split",
        "from sklearn.metrics import mean_squared_error",
        "",
        "# 1. Create a dataset where n_features is close to n_samples to cause overfitting",
        "np.random.seed(42)",
        "X = np.random.rand(20, 15) # 20 rows, 15 features",
        "y = 3 * X[:, 0] + 1.5 * X[:, 1] + np.random.randn(20) * 2.0 # Only first 2 features matter!",
        "",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)",
        "",
        "# 2. Train Standard Linear Regression",
        "lin_reg = LinearRegression()",
        "lin_reg.fit(X_train, y_train)",
        "",
        "# 3. Train Ridge and Lasso",
        "ridge_reg = Ridge(alpha=1.0)",
        "ridge_reg.fit(X_train, y_train)",
        "",
        "lasso_reg = Lasso(alpha=0.1)",
        "lasso_reg.fit(X_train, y_train)",
        "",
        "print('--- Test Set RMSE ---')",
        "print(f'Standard LR: {np.sqrt(mean_squared_error(y_test, lin_reg.predict(X_test))):.2f}')",
        "print(f'Ridge LR:    {np.sqrt(mean_squared_error(y_test, ridge_reg.predict(X_test))):.2f}')",
        "print(f'Lasso LR:    {np.sqrt(mean_squared_error(y_test, lasso_reg.predict(X_test))):.2f}')"
    ]),
    
    create_markdown_cell("## 9. Code Walkthrough\n- We engineered data where only Feature 0 and Feature 1 actually affect `y`. Features 2-14 are pure noise.\n- **Standard LR** memorized the noise (Overfitting). When it saw the test set, it failed catastrophically (massive RMSE).\n- **Ridge** and **Lasso** constrained the coefficients, preventing the model from giving too much weight to the noise features, resulting in much better (lower) test RMSE."),
    
    create_markdown_cell("## 10. Experiment\nLet's look at the actual coefficients the models learned to understand *how* they prevented overfitting."),
    create_code_cell([
        "print('Standard LR Coefficients:\\n', np.round(lin_reg.coef_, 2))",
        "print('\\nRidge Coefficients (Shrinkage):\\n', np.round(ridge_reg.coef_, 2))",
        "print('\\nLasso Coefficients (Selection):\\n', np.round(lasso_reg.coef_, 2))"
    ]),
    create_markdown_cell("> Look at Lasso! It forced almost all the noisy feature coefficients to exactly `0.0`. It automatically selected only the most important features!"),
    
    create_markdown_cell("## 11. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "model_alpha_0 = Ridge(alpha=0.0)",
        "model_alpha_huge = Ridge(alpha=1000000.0)"
    ]),
    create_markdown_cell("> **Question:** What happens to the coefficients in `model_alpha_0`? What happens to the coefficients in `model_alpha_huge`?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print('If alpha=0, Ridge is exactly equal to Standard Linear Regression (no penalty).')",
        "print('If alpha is huge, the penalty is so severe that Ridge will force all coefficients to essentially 0, resulting in severe Underfitting.')"
    ]),
    
    create_markdown_cell("## 12. Coding Exercise\nTrain an `ElasticNet` model on the same data. ElasticNet uses a parameter called `l1_ratio`. \nIf `l1_ratio=1.0`, it acts exactly like Lasso. If `l1_ratio=0.0`, it acts exactly like Ridge. \nSet it to `0.5` to get a 50/50 mix."),
    create_code_cell([
        "# YOUR CODE HERE",
        "from sklearn.linear_model import ElasticNet",
        "",
        "elastic = ElasticNet(alpha=0.1, l1_ratio=0.5)",
        "elastic.fit(X_train, y_train)",
        "print('ElasticNet RMSE:', np.sqrt(mean_squared_error(y_test, elastic.predict(X_test))))",
        "print('ElasticNet Coefs:', np.round(elastic.coef_, 2))"
    ]),
    
    create_markdown_cell("## 13. Debugging Challenge\nThe junior data scientist tried to apply Ridge regression to a real dataset, but the model performed terribly because they forgot a crucial preprocessing step. What is it?"),
    create_code_cell([
        "# Buggy conceptual code",
        "try:",
        "    # df = pd.read_csv('housing.csv')",
        "    # X_train, X_test, y_train, y_test = train_test_split(X, y)",
        "    # bad_model = Ridge(alpha=1.0)",
        "    # bad_model.fit(X_train, y_train)",
        "    print('Error: The model learned terrible weights because the data was NOT SCALED.')",
        "except Exception as e:",
        "    print('Error:', e)"
    ]),
    create_markdown_cell("> **Hint:** Regularization punishes large coefficients. If Feature 1 is measured in millimeters (value=10,000) and Feature 2 is measured in kilometers (value=0.01), Feature 2 will naturally need a massive coefficient just to have an effect. Ridge will unfairly punish Feature 2 just because of its units! \n> **Rule:** You MUST use `StandardScaler` before using Ridge, Lasso, or ElasticNet."),
    
    create_markdown_cell("## 14. Model Evaluation (Bias-Variance Tradeoff)\nAs you increase $\\alpha$:\n- **Variance decreases**: The model becomes less sensitive to noise (less overfitting).\n- **Bias increases**: The model becomes stiffer and simpler (more underfitting).\nYour goal as a Data Scientist is to find the \"Goldilocks\" $\\alpha$ value that balances this tradeoff. We will learn how to automate finding this value in Phase 5."),
    
    create_markdown_cell("## 15. Real-World Example\nIn Genetics, researchers often have data on 20,000 genes (features) for only 500 patients (samples) to predict a disease marker. Standard regression is mathematically impossible here ($p > n$). They use **Lasso Regression**, which forces 19,950 useless genes to exactly 0, leaving only the 50 genes most heavily associated with the disease. Lasso acts as an automated biological feature selector."),
    
    create_markdown_cell("## 16. Mini Project\nBuild a Pipeline that correctly scales data before applying Lasso Regression. Train it on the `X` and `y` from Section 8."),
    create_code_cell([
        "from sklearn.pipeline import Pipeline",
        "from sklearn.preprocessing import StandardScaler",
        "",
        "lasso_pipe = Pipeline([",
        "    ('scaler', StandardScaler()),",
        "    ('lasso', Lasso(alpha=0.1, random_state=42))",
        "])",
        "",
        "lasso_pipe.fit(X_train, y_train)",
        "pipe_rmse = np.sqrt(mean_squared_error(y_test, lasso_pipe.predict(X_test)))",
        "print(f'Pipeline Lasso RMSE: {pipe_rmse:.2f}')",
        "print('Pipeline Lasso Coefs:', np.round(lasso_pipe.named_steps['lasso'].coef_, 2))"
    ]),
    
    create_markdown_cell("## 17. Common Mistakes\n- **Not Scaling Data**: As mentioned in the debugging challenge, Regularization is highly sensitive to the scale of features.\n- **Setting Alpha too high**: The model will collapse and predict a flat line (high bias).\n- **Using Ridge when you want Feature Selection**: Ridge shrinks coefficients *close* to zero, but rarely *exactly* zero. If you want to eliminate features, you must use Lasso (L1)."),
    
    create_markdown_cell("## 18. Interview Questions\n- **Beginner**: What is the difference between Overfitting and Underfitting?\n- **Intermediate**: Explain the difference between L1 (Lasso) and L2 (Ridge) regularization.\n- **Advanced**: Why does L1 regularization tend to produce sparse solutions (coefficients of exactly 0) while L2 does not? (Hint: Think about the geometry of absolute values vs squares)."),
    
    create_markdown_cell("## 19. Knowledge Check\n- Which regularization technique performs automatic feature selection? (Lasso / L1)\n- What parameter controls the strength of the penalty? (`alpha`)"),
    
    create_markdown_cell("## 20. Summary\n- **Overfitting**: Memorizing noise. **Underfitting**: Failing to learn patterns.\n- **Ridge (L2)**: Shrinks coefficients. Good for preventing overfitting.\n- **Lasso (L1)**: Shrinks coefficients to exactly zero. Good for feature selection.\n- **ElasticNet**: Combines both.\n- **Always scale your data** before using regularization."),
    
    create_markdown_cell("## 21. Homework\nGenerate a regression dataset using `make_regression(n_samples=50, n_features=100, noise=10)`. Notice that $p > n$. Try fitting a standard `LinearRegression` and a `Lasso` model. Compare their test RMSE scores. Note how standard LR completely fails.")
]

# Read existing notebook and update cells
filename = "Day_10_Regularization.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day10_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")

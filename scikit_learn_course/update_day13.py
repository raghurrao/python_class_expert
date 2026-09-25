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

day13_cells = [
    create_markdown_cell("# PHASE 2 — REGRESSION"),
    create_markdown_cell("# Day 13 — Ensemble Learning (Random Forests)"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Understand the concept of Ensemble Learning (Wisdom of the Crowd).\n- Explain how Bagging (Bootstrap Aggregating) works.\n- Implement a `RandomForestRegressor` to fix the overfitting problems of single Decision Trees.\n- Tune the hyperparameters `n_estimators` and `max_depth`."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 12 (Decision Trees)."),
    
    create_markdown_cell("## 3. Concept\nYesterday, we learned that a single Decision Tree is wildly unstable. If you change even one row of training data, the entire structure of the tree might change, leading to massive Overfitting.\n\n**Ensemble Learning** is the idea that combining multiple weak, unstable models creates one incredibly strong, stable model. It's the mathematical version of the \"Wisdom of the Crowd.\"\n\nA **Random Forest** is simply an ensemble of hundreds of Decision Trees."),
    
    create_markdown_cell("## 4. Why Does This Matter?\nRandom Forest is widely considered the \"Swiss Army Knife\" of Machine Learning. If you are handed a tabular dataset and only have 5 minutes to get a decent prediction, you run a Random Forest. It is incredibly robust to outliers, requires no scaling, handles non-linear data, and doesn't overfit easily."),
    
    create_markdown_cell("## 5. Intuition\nImagine you want to guess the exact number of jellybeans in a massive jar. \n- A single person (Decision Tree) will likely be wildly wrong (high variance).\n- If you ask 1,000 random people, some will guess way too high, and some way too low. \n- But if you **average** all 1,000 guesses, the final answer will be shockingly close to the truth.\n\nA Random Forest trains 1,000 Decision Trees and simply takes the mathematical average of all their predictions."),
    
    create_markdown_cell("## 6. Mathematical Foundation (Bagging)\nIf all 100 trees in the forest saw the exact same data, they would all build the exact same tree, rendering the average useless. \n\nRandom Forests use a mathematical trick called **Bagging (Bootstrap Aggregating)**:\n1. **Bootstrap**: The algorithm randomly samples rows from your dataset *with replacement* to create 100 slightly different, \"fake\" datasets.\n2. **Feature Randomness**: At every split, each tree is only allowed to look at a random subset of features (e.g., it can only choose between Age or Salary, but not Education).\n3. **Aggregate**: Train 100 trees on these random subsets, then average their predictions.\n\nThis guarantees every tree is fundamentally unique, making their average incredibly powerful and resistant to overfitting."),
    
    create_markdown_cell("## 7. Scikit-learn API\n```python\nfrom sklearn.ensemble import RandomForestRegressor\nmodel = RandomForestRegressor(n_estimators=100, max_depth=5, random_state=42)\n```\n`n_estimators` is the number of trees in the forest. Default is 100."),
    
    create_markdown_cell("## 8. Simple Example\nLet's generate a highly noisy, non-linear dataset. We will compare a single Decision Tree against a Random Forest of 100 trees."),
    create_code_cell([
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "from sklearn.tree import DecisionTreeRegressor",
        "from sklearn.ensemble import RandomForestRegressor",
        "from sklearn.metrics import mean_squared_error",
        "from sklearn.model_selection import train_test_split",
        "",
        "# 1. Generate noisy sine wave data",
        "np.random.seed(42)",
        "X = np.sort(5 * np.random.rand(80, 1), axis=0)",
        "y = np.sin(X).ravel() + np.random.randn(80) * 0.2",
        "",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)",
        "",
        "# 2. Train a single Unconstrained Tree",
        "tree = DecisionTreeRegressor(random_state=42)",
        "tree.fit(X_train, y_train)",
        "",
        "# 3. Train a Random Forest (100 trees)",
        "forest = RandomForestRegressor(n_estimators=100, random_state=42)",
        "forest.fit(X_train, y_train)",
        "",
        "print('Single Tree RMSE:  ', np.sqrt(mean_squared_error(y_test, tree.predict(X_test))))",
        "print('Random Forest RMSE:', np.sqrt(mean_squared_error(y_test, forest.predict(X_test))))"
    ]),
    
    create_markdown_cell("## 9. Code Walkthrough\n- We created a Sine wave with heavy noise.\n- The single `DecisionTreeRegressor` got a higher RMSE because it memorized the noise on the training set.\n- The `RandomForestRegressor` combined 100 trees, smoothing out the noise and generalizing better to the unseen test set."),
    
    create_markdown_cell("## 10. Experiment\nLet's visualize exactly *why* the Random Forest scored better."),
    create_code_cell([
        "X_plot = np.linspace(0, 5, 500).reshape(-1, 1)",
        "",
        "plt.figure(figsize=(12, 5))",
        "plt.scatter(X, y, color='blue', alpha=0.4, label='Data')",
        "plt.plot(X_plot, tree.predict(X_plot), color='red', alpha=0.7, label='Single Tree (Overfit)')",
        "plt.plot(X_plot, forest.predict(X_plot), color='green', linewidth=3, label='Random Forest (Smoothed)')",
        "plt.legend()",
        "plt.title('Decision Tree vs Random Forest')",
        "plt.show()"
    ]),
    create_markdown_cell("> Notice the red line zigs and zags violently. The green line is much smoother! By averaging 100 jagged trees, the Random Forest creates a beautiful, smooth approximation of the true Sine wave."),
    
    create_markdown_cell("## 11. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "forest_10 = RandomForestRegressor(n_estimators=10, random_state=42)",
        "forest_1000 = RandomForestRegressor(n_estimators=1000, random_state=42)"
    ]),
    create_markdown_cell("> **Question:** Which model will take longer to train? Does increasing `n_estimators` from 10 to 1,000 increase the risk of overfitting?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print('The 1,000 tree model takes 100x longer to train.')",
        "print('However, unlike max_depth, increasing n_estimators ALMOST NEVER causes overfitting! Averaging more trees just makes the prediction strictly more stable.')"
    ]),
    
    create_markdown_cell("## 12. Coding Exercise\nTrain a `RandomForestRegressor` but this time constrain the depth of the 100 trees inside it by passing `max_depth=2`. Plot it against `X_plot`."),
    create_code_cell([
        "# YOUR CODE HERE",
        "forest_constrained = RandomForestRegressor(n_estimators=100, max_depth=2, random_state=42)",
        "forest_constrained.fit(X_train, y_train)",
        "",
        "plt.scatter(X, y, color='blue', alpha=0.4)",
        "plt.plot(X_plot, forest_constrained.predict(X_plot), color='orange', linewidth=3)",
        "plt.title('Random Forest (max_depth=2)')",
        "plt.show()",
        "print('Notice how constraining the depth of the trees inside the forest creates an extremely smooth, conservative staircase!')"
    ]),
    
    create_markdown_cell("## 13. Debugging Challenge\nA Junior Developer tried to use Random Forest to predict next month's sales, which are expected to be \$200,000. The highest historical month in the training data was \$150,000. \nThe Random Forest keeps predicting \$150,000 and the developer thinks there is a bug in Scikit-learn. What is actually happening?"),
    create_code_cell([
        "try:",
        "    historical_sales = np.array([[1], [2], [3], [4], [5]])",
        "    historical_revenue = np.array([50, 75, 100, 125, 150])",
        "    ",
        "    rf = RandomForestRegressor(n_estimators=10, random_state=42)",
        "    rf.fit(historical_sales, historical_revenue)",
        "    ",
        "    future_month = np.array([[6]])",
        "    print('Predicted Revenue for Month 6:', rf.predict(future_month))",
        "except Exception as e:",
        "    print('Error:', e)"
    ]),
    create_markdown_cell("> **Hint:** Remember Day 12. A Random Forest is just an average of Decision Trees. Can a Decision Tree predict a number higher than what it saw in the training data? (No!). \n> Random Forests CANNOT extrapolate outside the bounds of the training data. If you need extrapolation (trending upwards infinitely), you MUST use a Linear Model."),
    
    create_markdown_cell("## 14. Model Evaluation (Feature Importance)\nBecause Random Forests randomly subset features across hundreds of trees, they naturally discover which features are useless and which are critical. You can extract this using `.feature_importances_`. This is incredibly valuable for business stakeholders who want to know *why* the model makes predictions."),
    
    create_markdown_cell("## 15. Real-World Example\nIn e-commerce, predicting Customer Lifetime Value (CLV) is critical. The data is messy, non-linear, has massive outliers, and missing values. A standard Linear Regression would crash or produce terrible predictions. A Random Forest naturally handles the non-linear interactions, ignores the extreme outliers, and provides a stable prediction of how much a user will spend over their lifetime."),
    
    create_markdown_cell("## 16. Mini Project\nTrain a Random Forest on a dataset with 5 features (only the first 1 matters). Use `.feature_importances_` to prove the forest figured this out."),
    create_code_cell([
        "X_multi = np.random.rand(100, 5)",
        "y_multi = 10 * X_multi[:, 0] + np.random.randn(100) # Only feature 0 matters!",
        "",
        "rf_feat = RandomForestRegressor(n_estimators=50, random_state=42)",
        "rf_feat.fit(X_multi, y_multi)",
        "",
        "importances = rf_feat.feature_importances_",
        "for i, imp in enumerate(importances):",
        "    print(f'Feature {i} Importance: {imp:.3f}')",
        "print('The Forest correctly identified that Feature 0 holds ~95%+ of the predictive power!')"
    ]),
    
    create_markdown_cell("## 17. Common Mistakes\n- **Extrapolation**: Using Random Forests for time-series forecasting where the target is trending upwards into unseen numbers.\n- **Not tuning `max_depth`**: While `n_estimators` won't cause overfitting, if you leave `max_depth` unconstrained, the forest can still slightly overfit on extremely noisy datasets. \n- **Worrying about scaling**: Random Forests do not need `StandardScaler`!"),
    
    create_markdown_cell("## 18. Interview Questions\n- **Beginner**: What is the difference between a Decision Tree and a Random Forest?\n- **Intermediate**: Explain the two random steps in 'Bagging' (Bootstrap Aggregating) that ensure trees in a Random Forest are diverse.\n- **Advanced**: Why does increasing `n_estimators` to infinity not cause overfitting in a Random Forest?"),
    
    create_markdown_cell("## 19. Knowledge Check\n- What property allows you to see which features were most useful? (`.feature_importances_`)\n- Does a Random Forest require scaled data? (No)"),
    
    create_markdown_cell("## 20. Summary\n- **Random Forest** = Ensemble of Decision Trees.\n- Uses **Bagging** to ensure diversity (Random Rows + Random Features).\n- Averaging predictions drastically reduces variance (Overfitting).\n- It cannot extrapolate outside the training data range.\n- Provides feature importance out of the box."),
    
    create_markdown_cell("## 21. Homework\nLoad the `fetch_california_housing` dataset. Train a `LinearRegression` and a `RandomForestRegressor(n_estimators=50)`. Compare their Test RMSE scores. The Random Forest should obliterate the Linear Regression because house prices are highly non-linear.")
]

# Read existing notebook and update cells
filename = "Day_13_Ensemble_Learning.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day13_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")

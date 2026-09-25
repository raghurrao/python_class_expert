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

day12_cells = [
    create_markdown_cell("# PHASE 2 — REGRESSION"),
    create_markdown_cell("# Day 12 — Decision Trees (Regression)"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Explain how a Decision Tree performs regression without calculating any lines or coefficients.\n- Implement a `DecisionTreeRegressor`.\n- Understand why trees are incredibly prone to overfitting.\n- Control overfitting using hyperparameters like `max_depth` and `min_samples_split`.\n- Visualize a tree structure."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 8 (Linear Regression).\n- Day 10 (Overfitting vs Underfitting)."),
    
    create_markdown_cell("## 3. Concept\nUnlike Linear Regression, a **Decision Tree** does not calculate a line of best fit. It does not use $\\beta$ coefficients. It does not care if the data is linear or curved.\n\nInstead, a Decision Tree plays a game of \"20 Questions\". It looks at the features and repeatedly splits the data into two groups. \nFor example: *\"Is Square Footage > 2000?\"* If Yes, go left. If No, go right. \nAt the very bottom of the tree (the **Leaf Node**), the model predicts the **average** value of all the training samples that ended up in that leaf."),
    
    create_markdown_cell("## 4. Why Does This Matter?\nDecision Trees are the foundation of modern tabular machine learning. While a single tree is rarely used in production, combining hundreds of trees (Ensemble Learning) results in algorithms like Random Forest and XGBoost, which dominate Kaggle competitions and real-world finance/marketing applications."),
    
    create_markdown_cell("## 5. Intuition\nImagine predicting a person's Salary based on Age and Education.\n- Root Node: Is Education = Masters?\n  - If No: Predict \$50,000.\n  - If Yes: Node 2: Is Age > 30?\n    - If No: Predict \$70,000.\n    - If Yes: Predict \$120,000.\n\nNotice that the predictions are completely discrete blocks. A regression tree looks like a set of stairs, not a smooth line."),
    
    create_markdown_cell("## 6. Mathematical Foundation\nHow does the tree decide *where* to split? It iterates through every possible feature, and every possible threshold, and calculates the **Mean Squared Error (MSE)** of the two resulting splits.\n\nIt chooses the split that mathematically minimizes the MSE the most (i.e., creates the two groups with the lowest variance).\n\n$$ MSE = \\frac{1}{n_{left}} \\sum_{i \\in left} (y_i - \\bar{y}_{left})^2 + \\frac{1}{n_{right}} \\sum_{i \\in right} (y_i - \\bar{y}_{right})^2 $$"),
    
    create_markdown_cell("## 7. Scikit-learn API\n```python\nfrom sklearn.tree import DecisionTreeRegressor\nmodel = DecisionTreeRegressor(max_depth=3, random_state=42)\n```"),
    
    create_markdown_cell("## 8. Simple Example\nLet's go back to the curved parabola data from Day 11. Can a Decision Tree learn a curve without us having to mathematically engineer Polynomial Features?"),
    create_code_cell([
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "from sklearn.tree import DecisionTreeRegressor",
        "from sklearn.metrics import mean_squared_error",
        "",
        "# 1. Generate curved data (same as Day 11)",
        "np.random.seed(42)",
        "X = 6 * np.random.rand(100, 1) - 3",
        "y = 0.5 * X**2 + X + 2 + np.random.randn(100, 1)",
        "",
        "# 2. Train an UNCONSTRAINED tree",
        "tree_unconstrained = DecisionTreeRegressor(random_state=42)",
        "tree_unconstrained.fit(X, y)",
        "",
        "# 3. Train a CONSTRAINED tree (max_depth=3)",
        "tree_constrained = DecisionTreeRegressor(max_depth=3, random_state=42)",
        "tree_constrained.fit(X, y)"
    ]),
    
    create_markdown_cell("## 9. Code Walkthrough\n- We imported `DecisionTreeRegressor`.\n- `tree_unconstrained`: We let the tree grow as deep as it wants. It will keep asking questions until every single leaf has only 1 data point in it.\n- `tree_constrained`: We told the tree to stop growing after 3 questions (`max_depth=3`)."),
    
    create_markdown_cell("## 10. Experiment\nLet's visualize the unconstrained vs constrained tree. This is the most important visual in all of Machine Learning for understanding Overfitting!"),
    create_code_cell([
        "X_plot = np.linspace(-3, 3, 500).reshape(-1, 1)",
        "",
        "plt.figure(figsize=(14, 5))",
        "",
        "plt.subplot(1, 2, 1)",
        "plt.scatter(X, y, color='blue', alpha=0.5)",
        "plt.plot(X_plot, tree_unconstrained.predict(X_plot), color='red', linewidth=1.5)",
        "plt.title('Unconstrained (Overfit - Memorized Noise)')",
        "",
        "plt.subplot(1, 2, 2)",
        "plt.scatter(X, y, color='blue', alpha=0.5)",
        "plt.plot(X_plot, tree_constrained.predict(X_plot), color='green', linewidth=3)",
        "plt.title('Max Depth = 3 (Good Fit)')",
        "",
        "plt.show()"
    ]),
    create_markdown_cell("> **Notice:** The unconstrained tree (red) violently zigs and zags to perfectly hit every single outlier point. The constrained tree (green) looks like a staircase that follows the general mathematical trend."),
    
    create_markdown_cell("## 11. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "from sklearn.tree import plot_tree",
        "small_tree = DecisionTreeRegressor(max_depth=1, random_state=42)",
        "small_tree.fit(X, y)"
    ]),
    create_markdown_cell("> **Question:** If `max_depth=1`, how many total leaf nodes will the tree have? How many unique numerical values can this model predict in total?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "plt.figure(figsize=(6,3))",
        "plot_tree(small_tree, filled=True, rounded=True)",
        "plt.show()",
        "print('Why? max_depth=1 means exactly 1 split. This creates exactly 2 leaf nodes.')",
        "print('Therefore, this model can only EVER output 2 unique predictions, no matter what data you feed it!')"
    ]),
    
    create_markdown_cell("## 12. Coding Exercise\nAnother way to prevent overfitting is `min_samples_split`. \nTrain a tree with `min_samples_split=20` (meaning a node cannot split unless it has at least 20 samples inside it). Plot its predictions over `X_plot`."),
    create_code_cell([
        "# YOUR CODE HERE",
        "tree_min_samples = DecisionTreeRegressor(min_samples_split=20, random_state=42)",
        "tree_min_samples.fit(X, y)",
        "",
        "plt.scatter(X, y, color='blue', alpha=0.5)",
        "plt.plot(X_plot, tree_min_samples.predict(X_plot), color='orange', linewidth=3)",
        "plt.title('min_samples_split = 20')",
        "plt.show()"
    ]),
    
    create_markdown_cell("## 13. Debugging Challenge\nA data scientist trained a Decision Tree Regressor and got an $R^2$ score of exactly 1.0 (100% accuracy) on their training data. They told their boss the model is perfect. Why are they about to get fired?"),
    create_code_cell([
        "# Buggy evaluation logic",
        "perfect_r2 = tree_unconstrained.score(X, y)",
        "print('Training R^2:', perfect_r2)"
    ]),
    create_markdown_cell("> **Hint:** An unconstrained tree will ALWAYS get 1.0 on the training data because it grows until every leaf contains exactly 1 sample, meaning its prediction is just the exact value of that sample. \n> They tested the model on the data it memorized! They needed to use a Test Set!"),
    
    create_markdown_cell("## 14. Model Evaluation\nDecision Trees require absolutely zero scaling. Because they split by asking \"Is X > 5?\", it doesn't matter if X is 5, 500, or 0.05. The split logic remains mathematically identical. You do NOT need `StandardScaler` for Decision Trees!"),
    
    create_markdown_cell("## 15. Real-World Example\nIn Real Estate pricing, geographic location (Latitude/Longitude) is highly non-linear. Linear regression fails completely because moving slightly north might increase price (towards a city) but moving further north might decrease price (into the mountains). A Decision Tree solves this beautifully by carving the map into small rectangular bounding boxes (leaves)."),
    
    create_markdown_cell("## 16. Mini Project\nProve that Decision Trees don't care about scaling. Train `tree1` on `X`. Train `tree2` on `X * 1000`. Compare their predictions on a test point."),
    create_code_cell([
        "tree1 = DecisionTreeRegressor(max_depth=2, random_state=42)",
        "tree1.fit(X, y)",
        "",
        "tree2 = DecisionTreeRegressor(max_depth=2, random_state=42)",
        "tree2.fit(X * 1000, y)",
        "",
        "pred1 = tree1.predict([[2.5]])",
        "pred2 = tree2.predict([[2500]]) # Scaled test point",
        "",
        "print('Prediction 1 (Unscaled):', pred1[0])",
        "print('Prediction 2 (Scaled):  ', pred2[0])",
        "print('Notice they are mathematically identical!')"
    ]),
    
    create_markdown_cell("## 17. Common Mistakes\n- **Forgetting to constrain the tree**: If you don't set `max_depth`, `min_samples_leaf`, or `min_samples_split`, you are guaranteed to overfit.\n- **Extrapolation**: Decision Trees cannot predict values outside their training range. If the highest salary in your training set is \$100k, a Decision Tree can NEVER predict \$101k, no matter what features you give it. (Unlike Linear Regression, which will extrapolate the line upward forever)."),
    
    create_markdown_cell("## 18. Interview Questions\n- **Beginner**: Why doesn't a Decision Tree draw a smooth line?\n- **Intermediate**: Do you need to use `StandardScaler` on data before feeding it to a Decision Tree? Why or why not?\n- **Advanced**: Explain why a Decision Tree Regressor is fundamentally incapable of extrapolation outside the bounds of the training target variable."),
    
    create_markdown_cell("## 19. Knowledge Check\n- What hyperparameter limits how many levels deep the tree can grow? (`max_depth`)\n- If a tree has `max_depth=2`, how many leaf nodes does it have? (4)"),
    
    create_markdown_cell("## 20. Summary\n- **Decision Trees** predict by splitting data into smaller and smaller groups.\n- They model non-linear relationships natively (no PolynomialFeatures required).\n- They are massively prone to **Overfitting**.\n- You constrain them using **hyperparameters** (`max_depth`).\n- They do not require data scaling."),
    
    create_markdown_cell("## 21. Homework\nLoad the `fetch_california_housing` dataset. Train an unconstrained `DecisionTreeRegressor` and a constrained one (`max_depth=5`). Compare their Train $R^2$ vs Test $R^2$. Observe how the unconstrained tree gets 1.0 on Train but terrible scores on Test.")
]

# Read existing notebook and update cells
filename = "Day_12_Decision_Trees.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day12_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")

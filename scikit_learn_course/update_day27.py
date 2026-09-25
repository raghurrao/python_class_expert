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

day27_cells = [
    create_markdown_cell("# PHASE 5 — ADVANCED WORKFLOWS & PRODUCTION"),
    create_markdown_cell("# Day 27 — Hyperparameter Tuning"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Differentiate between **Parameters** and **Hyperparameters**.\n- Use **GridSearchCV** to automatically test hundreds of model settings.\n- Use **RandomizedSearchCV** to save time when grids become too large.\n- Understand why tuning *must* be combined with Cross-Validation."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 26 (Cross Validation).\n- Day 18 (Support Vector Machines - `C`, `gamma`, `kernel`)."),
    
    create_markdown_cell("## 3. Concept: Parameters vs. Hyperparameters\n- **Parameters**: The math the model learns *by itself* during `.fit()`. (e.g., The slope $m$ and intercept $b$ in Linear Regression, or the position of a Centroid in K-Means).\n- **Hyperparameters**: The settings the human sets *before* calling `.fit()`. (e.g., $K=5$ in KNN, or `max_depth=3` in a Decision Tree).\n\nHow do you know if $K=5$ is better than $K=15$? You have to test it. **Hyperparameter Tuning** is the process of writing code to test all possible combinations of settings to find the absolute best model."),
    
    create_markdown_cell("## 4. Concept: GridSearchCV\n`GridSearchCV` is a brute-force approach. You give it a dictionary of settings (a grid). \nIf you pass `kernel = ['linear', 'rbf']` and `C = [0.1, 1, 10]`, there are $2 \\times 3 = 6$ possible combinations.\n\n`GridSearchCV` will:\n1. Build 6 different models.\n2. Run a 5-Fold Cross Validation on EVERY model to see how good it is.\n3. Return the single best model.\n*(Math check: 6 combinations * 5 folds = 30 total models trained!)*"),
    
    create_markdown_cell("## 5. Scikit-learn API\n```python\nfrom sklearn.model_selection import GridSearchCV\n# Define the grid\nparam_grid = {'C': [0.1, 1, 10]}\n# Create the searcher\ngrid = GridSearchCV(estimator=SVC(), param_grid=param_grid, cv=5)\n# Run the brute force search\ngrid.fit(X, y)\n```"),
    
    create_markdown_cell("## 6. Simple Example: Tuning an SVM\nLet's generate some classification data. We will tune an SVM to find the perfect combination of `C` (Regularization), `gamma` (RBF radius), and `kernel` type."),
    create_code_cell([
        "import pandas as pd",
        "from sklearn.datasets import make_classification",
        "from sklearn.model_selection import train_test_split, GridSearchCV",
        "from sklearn.svm import SVC",
        "from sklearn.preprocessing import StandardScaler",
        "",
        "# 1. Generate and scale data",
        "X, y = make_classification(n_samples=500, n_features=10, n_informative=5, random_state=42)",
        "scaler = StandardScaler()",
        "X_scaled = scaler.fit_transform(X) # Note: we scale the whole X for this simple example, but see Section 11 for the strict Pipeline method!",
        "",
        "# 2. Define the Hyperparameter Grid",
        "param_grid = {",
        "    'kernel': ['linear', 'rbf'],",
        "    'C': [0.1, 1, 10, 100],",
        "    'gamma': ['scale', 'auto', 0.1, 1] # Only affects 'rbf'",
        "}",
        "",
        "# 3. Set up GridSearchCV",
        "# 2 * 4 * 4 = 32 combinations. cv=5 means 160 total models will be trained!",
        "grid_search = GridSearchCV(estimator=SVC(), param_grid=param_grid, cv=5, scoring='accuracy', n_jobs=-1)",
        "",
        "# 4. Run the Search",
        "grid_search.fit(X_scaled, y)",
        "",
        "print('Brute force search complete!')"
    ]),
    
    create_markdown_cell("## 7. Code Walkthrough\n- We defined a dictionary `param_grid`. The keys MUST exactly match the arguments you would normally pass into `SVC(C=1)`. \n- We passed `n_jobs=-1` to `GridSearchCV`. This tells Scikit-learn to use ALL of your computer's CPU cores to train the 160 models simultaneously, speeding up the search significantly.\n- It ran `cv=5` on every single combination to ensure the results weren't just \"Luck of the Draw\"."),
    
    create_markdown_cell("## 8. Experiment: Accessing the Results\nNow that it is done, let's ask `grid_search` what the best settings were, and what the best score was."),
    create_code_cell([
        "print('Best Hyperparameters found:')",
        "print(grid_search.best_params_)",
        "",
        "print(f'\\nBest Cross-Validated Accuracy: {grid_search.best_score_ * 100:.2f}%')",
        "",
        "# You can immediately use the grid object to predict on new data! ",
        "# It automatically uses the best model it found.",
        "predictions = grid_search.predict(X_scaled[:5])",
        "print(f'\\nPredictions for first 5 rows: {predictions}')"
    ]),
    create_markdown_cell("> The grid searched 32 configurations and mathematically proved that an `rbf` kernel with `C=10` and `gamma=scale` is the optimal setup for this specific dataset."),
    
    create_markdown_cell("## 9. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "from sklearn.ensemble import RandomForestClassifier",
        "",
        "rf_grid = {",
        "    'n_estimators': [10, 50, 100, 200, 500],",
        "    'max_depth': [None, 5, 10, 15, 20],",
        "    'min_samples_split': [2, 5, 10, 20],",
        "    'min_samples_leaf': [1, 2, 5, 10]",
        "}"
    ]),
    create_markdown_cell("> **Question:** If we pass this `rf_grid` to `GridSearchCV(cv=5)`, how many models will your computer have to train?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "combinations = 5 * 5 * 4 * 4",
        "total_fits = combinations * 5",
        "print(f'Combinations: {combinations}')",
        "print(f'Total Models to train: {total_fits}')",
        "print('\\nTraining 2,000 Random Forests could take hours. Brute force does not scale well!')"
    ]),
    
    create_markdown_cell("## 10. Concept: RandomizedSearchCV\nWhen your grid is massive, you use `RandomizedSearchCV`. \nInstead of testing all 400 combinations, you tell it `n_iter=20`. It will pick 20 random combinations out of the 400, run CV on those 20, and return the best one.\n\n*Why does this work?* In most ML problems, only 1 or 2 hyperparameters actually matter (e.g., `max_depth`). The others are minor tweaks. Randomly sampling 20 combinations is mathematically highly likely to stumble upon the optimal zone for the important hyperparameters, saving you hours of computation!"),
    
    create_markdown_cell("## 11. Coding Exercise\nRun a `RandomizedSearchCV` on the `RandomForestClassifier` using the massive `rf_grid` above. \nSet `n_iter=10` and `cv=3` (this means it will only train 30 models total). \nPrint the `best_params_`."),
    create_code_cell([
        "# YOUR CODE HERE",
        "from sklearn.model_selection import RandomizedSearchCV",
        "",
        "rf_random = RandomizedSearchCV(",
        "    estimator=RandomForestClassifier(random_state=42), ",
        "    param_distributions=rf_grid, ",
        "    n_iter=10, ",
        "    cv=3, ",
        "    random_state=42, ",
        "    n_jobs=-1",
        ")",
        "",
        "rf_random.fit(X, y)",
        "print('Best Random Forest Params:', rf_random.best_params_)",
        "print(f'Best Random Forest Score:  {rf_random.best_score_ * 100:.2f}%')"
    ]),
    
    create_markdown_cell("## 12. Debugging Challenge\nA developer builds a Pipeline with `StandardScaler` and `SVC`. They want to tune the SVM's `C` parameter. They write:\n`param_grid = {'C': [0.1, 1, 10]}` and pass the Pipeline into `GridSearchCV`. \nIt crashes with a `ValueError: Invalid parameter C for estimator Pipeline`. Why?"),
    create_code_cell([
        "# Conceptual Bug",
        "print('Error: The Pipeline doesn\\'t know which step the parameter belongs to.')",
        "print('Does `C` belong to the scaler? Or the SVM?')",
        "print('To fix this, you MUST prefix the parameter with the step name and two underscores.')",
        "print('Correct code: param_grid = {\\'svm__C\\': [0.1, 1, 10]}')"
    ]),
    create_markdown_cell("> **Rule:** When tuning a Pipeline, you must use the `stepname__parametername` syntax in your grid dictionary!"),
    
    create_markdown_cell("## 13. Real-World Example\n**Kaggle Competitions**: In machine learning competitions, the difference between 1st place ($10,000 prize) and 2nd place is often 0.001% accuracy. Competitors spend weeks building massive Grids and letting `GridSearchCV` run on cloud servers with 128 CPU cores to find the absolute mathematical limit of their models."),
    
    create_markdown_cell("## 14. Mini Project\nLet's tune a Pipeline the correct, leak-free way. \nBuild a Pipeline with `StandardScaler` (named `scaler`) and `SVC` (named `svc`). \nCreate a grid to tune `svc__C` and `svc__kernel`. \nRun `GridSearchCV` on the pipeline!"),
    create_code_cell([
        "from sklearn.pipeline import Pipeline",
        "",
        "pipe = Pipeline([",
        "    ('scaler', StandardScaler()),",
        "    ('svc', SVC(random_state=42))",
        "])",
        "",
        "# Note the double underscores connecting the step name to the parameter!",
        "pipe_grid = {",
        "    'svc__C': [0.1, 1, 10],",
        "    'svc__kernel': ['linear', 'rbf']",
        "}",
        "",
        "pipe_search = GridSearchCV(pipe, param_grid=pipe_grid, cv=5, n_jobs=-1)",
        "pipe_search.fit(X, y)",
        "",
        "print('Best Pipeline Params:', pipe_search.best_params_)",
        "print(f'Best Pipeline Score:  {pipe_search.best_score_ * 100:.2f}%')"
    ]),
    
    create_markdown_cell("## 15. Common Mistakes\n- **Tuning without CV**: If you just run a massive loop of hyperparameters and check the accuracy on a single `X_test`, you are committing severe Data Leakage. The loop will eventually stumble upon a setting that performs flawlessly on that specific `X_test` by pure random chance. This is why `GridSearchCV` has CV built-in natively.\n- **Forgetting `__` in Pipelines**: The number one syntax error when combining Phase 2 (Pipelines) with Phase 5 (Tuning).\n- **Exploding Grids**: Adding 5 lists of 10 items to a grid results in $10^5 = 100,000$ combinations. Your computer will crash."),
    
    create_markdown_cell("## 16. Interview Questions\n- **Beginner**: What is the difference between a parameter and a hyperparameter? (Answer: Parameters are learned by the model from the data (like weights). Hyperparameters are manually set by the engineer before training (like tree depth)).\n- **Intermediate**: Why would you use `RandomizedSearchCV` instead of `GridSearchCV`? (Answer: When the parameter grid is too large. Randomized Search saves massive amounts of computation time while still usually finding a near-optimal setup).\n- **Advanced**: How do you pass a hyperparameter grid to a Pipeline? (Answer: You must use a double underscore `__` to map the hyperparameter to the specific step name in the pipeline, e.g., `rf__max_depth`)."),
    
    create_markdown_cell("## 17. Knowledge Check\n- Does `GridSearchCV` use Cross Validation internally? (Yes, the `cv` parameter is required/defaults to 5).\n- What argument speeds up training by using all CPU cores? (`n_jobs=-1`)"),
    
    create_markdown_cell("## 18. Summary\n- **GridSearchCV** brute-forces every combination of hyperparameters in a dictionary.\n- It runs **K-Fold CV** on every single combination to find the true best model.\n- **RandomizedSearchCV** samples a random subset of a massive grid to save time.\n- To tune a **Pipeline**, you must use the `stepname__paramname` syntax."),
    
    create_markdown_cell("## 19. Homework\nLoad the `load_iris` dataset. Use `RandomizedSearchCV` to tune a `DecisionTreeClassifier`. Tune `max_depth` (1 to 10) and `min_samples_split` (2 to 20). Set `n_iter=5`. What were the best parameters it found?")
]

# Read existing notebook and update cells
filename = "Day_27_Hyperparameter_Tuning.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day27_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")

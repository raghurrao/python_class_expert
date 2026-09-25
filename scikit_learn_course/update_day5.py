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

day5_cells = [
    create_markdown_cell("# PHASE 1 — MACHINE LEARNING FOUNDATIONS"),
    create_markdown_cell("# Day 05 — Pipelines"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Construct a `Pipeline` to chain multiple Scikit-learn steps together.\n- Explain how Pipelines automatically prevent data leakage.\n- Explain how Pipelines prevent training/inference mismatch.\n- Simplify messy ML code into a clean, elegant workflow."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 2 (Scikit-learn API).\n- Day 4 (Preprocessing: Imputation and Scaling)."),
    
    create_markdown_cell("## 3. Concept\nA **Pipeline** sequentially applies a list of transformers and a final estimator. \nInstead of manually saving an Imputer, manually calling `imputer.transform(X)`, then manually saving a Scaler, and manually calling `scaler.transform(X)`, a Pipeline bundles all these steps into a single object.\n\nYou treat the entire Pipeline as if it were a single model. You call `pipeline.fit(X, y)` and it automatically executes every step in the correct order."),
    
    create_markdown_cell("## 4. Why Does This Matter?\nPipelines are arguably the most important feature in Scikit-learn for production ML because they prevent three massive problems:\n1. **Data Leakage**: During cross-validation, pipelines ensure that scaling/imputing happens *after* the split on every single fold.\n2. **Inconsistent Preprocessing**: Doing step A then step B in training, but accidentally doing step B then step A in testing.\n3. **Training/Inference Mismatch**: Deploying the model but forgetting to deploy the exact scaler object alongside it. A Pipeline bundles everything together into one deployable artifact."),
    
    create_markdown_cell("## 5. Intuition\nThink of an assembly line in a car factory.\n- Step 1 (Imputer): Put on the wheels.\n- Step 2 (Scaler): Paint the car.\n- Step 3 (Model): Drive the car.\n\nWithout an assembly line (Pipeline), you have to manually carry the car from station to station. If you forget to paint the test car before trying to drive it, the car fails inspection. The Pipeline automates the conveyor belt."),
    
    create_markdown_cell("## 6. Mathematical Foundation\nMathematically, a Pipeline represents function composition. If we have an Imputer $I$, a Scaler $S$, and a Model $M$, predicting $\\hat{y}$ on raw data $X$ requires:\n\n$$ \\hat{y} = M(S(I(X))) $$\n\nThe Pipeline abstracts this so you only ever have to compute:\n\n$$ \\hat{y} = Pipeline(X) $$"),
    
    create_markdown_cell("## 7. Scikit-learn API\nUsing `Pipeline` from `sklearn.pipeline` requires passing a list of tuples. Each tuple contains a string name (that you make up) and the estimator object:\n\n```python\nPipeline([\n    ('step1_name', Transformer1()),\n    ('step2_name', Transformer2()),\n    ('model_name', Estimator())\n])\n```"),
    
    create_markdown_cell("## 8. Simple Example\nLet's recreate yesterday's numeric processing (Imputation + Scaling) combined with a Logistic Regression model, but this time using a Pipeline."),
    create_code_cell([
        "import numpy as np",
        "from sklearn.pipeline import Pipeline",
        "from sklearn.impute import SimpleImputer",
        "from sklearn.preprocessing import StandardScaler",
        "from sklearn.linear_model import LogisticRegression",
        "from sklearn.model_selection import train_test_split",
        "",
        "# 1. Create messy data",
        "X = np.array([[25.0], [np.nan], [30.0], [45.0], [50.0], [np.nan], [22.0], [60.0]])",
        "y = np.array([0, 1, 0, 1, 1, 0, 0, 1])",
        "",
        "# 2. Split",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)",
        "",
        "# 3. Build the Pipeline",
        "pipe = Pipeline([",
        "    ('imputer', SimpleImputer(strategy='mean')), # Step 1",
        "    ('scaler', StandardScaler()),              # Step 2",
        "    ('classifier', LogisticRegression())       # Step 3",
        "])",
        "",
        "# 4. Fit the ENTIRE pipeline at once",
        "pipe.fit(X_train, y_train)",
        "",
        "# 5. Predict using the ENTIRE pipeline",
        "predictions = pipe.predict(X_test)",
        "print('Predictions:', predictions)"
    ]),
    
    create_markdown_cell("## 9. Code Walkthrough\n- `pipe = Pipeline(...)`: We define the chronological steps of our workflow.\n- `pipe.fit(X_train, y_train)`: Under the hood, this does:\n  1. `X_imp = imputer.fit_transform(X_train)`\n  2. `X_scaled = scaler.fit_transform(X_imp)`\n  3. `classifier.fit(X_scaled, y_train)`\n- `pipe.predict(X_test)`: Under the hood, this does:\n  1. `X_imp = imputer.transform(X_test)` (Note: ONLY `.transform()`!)\n  2. `X_scaled = scaler.transform(X_imp)`\n  3. `return classifier.predict(X_scaled)`\n  \nNotice how the Pipeline safely protects the test set from `.fit_transform()` leakage automatically!"),
    
    create_markdown_cell("## 10. Experiment\nWe can access individual steps inside the pipeline using the `.named_steps` dictionary. Let's look at what the imputer learned."),
    create_code_cell([
        "learned_mean = pipe.named_steps['imputer'].statistics_",
        "print('The imputer learned this mean from the training data:', learned_mean)",
        "",
        "learned_coef = pipe.named_steps['classifier'].coef_",
        "print('The logistic regression learned this coefficient:', learned_coef)"
    ]),
    
    create_markdown_cell("## 11. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "from sklearn.pipeline import make_pipeline",
        "pipe2 = make_pipeline(",
        "    SimpleImputer(strategy='median'),",
        "    StandardScaler(),",
        "    LogisticRegression()",
        ")"
    ]),
    create_markdown_cell("> **Question:** What is the difference between `Pipeline` and `make_pipeline`? If we didn't provide string names in `make_pipeline`, what name will it assign to `StandardScaler`? \n\n**Think before running the next cell!**"),
    create_code_cell([
        "print(list(pipe2.named_steps.keys()))",
        "print('\\nWhy? `make_pipeline` is a shortcut that automatically generates names for the steps by lowercasing the class name (e.g., StandardScaler -> standardscaler).')"
    ]),
    
    create_markdown_cell("## 12. Coding Exercise\nBuild a pipeline using `make_pipeline` that:\n1. Fills missing values with the constant value `-1`.\n2. Uses `MinMaxScaler`.\n3. Trains a `DecisionTreeClassifier`.\nFit it on `X_train` and score it on `X_test`."),
    create_code_cell([
        "# YOUR CODE HERE",
        "from sklearn.pipeline import make_pipeline",
        "from sklearn.tree import DecisionTreeClassifier",
        "from sklearn.preprocessing import MinMaxScaler",
        "",
        "my_pipe = make_pipeline(",
        "    SimpleImputer(strategy='constant', fill_value=-1),",
        "    MinMaxScaler(),",
        "    DecisionTreeClassifier(random_state=42)",
        ")",
        "my_pipe.fit(X_train, y_train)",
        "score = my_pipe.score(X_test, y_test)",
        "print('Pipeline Score:', score)"
    ]),
    
    create_markdown_cell("## 13. Debugging Challenge\nThe pipeline below crashes with a `TypeError`. Why?"),
    create_code_cell([
        "# Buggy code",
        "try:",
        "    bad_pipe = Pipeline([",
        "        ('model', LogisticRegression()),",
        "        ('scaler', StandardScaler())",
        "    ])",
        "    # bad_pipe.fit(X_train, y_train) # This would crash",
        "except Exception as e:",
        "    print('Error:', e)"
    ]),
    create_markdown_cell("> **Hint:** Look at the order of the steps. What does `LogisticRegression` output? Can a Scaler scale the output of a predictor? (No, the predictor must always be the **last** step in the Pipeline)."),
    
    create_markdown_cell("## 14. Model Evaluation\nWhen we score a pipeline (`pipe.score(X, y)`), the pipeline pushes `X` through all the transformers, and then calls the `.score()` method of the final estimator. It is perfectly identical to evaluating the model on manually preprocessed data, just much safer."),
    
    create_markdown_cell("## 15. Real-World Example\nIn production, you serialize (save) the entire `Pipeline` object using a library like `joblib`. \nWhen the Web API receives new user data, it simply calls `loaded_pipeline.predict(user_data)`. \nIf you didn't use a pipeline, your backend software engineer would have to perfectly rewrite your Imputation and Scaling logic in the web server code, which almost always introduces bugs!"),
    
    create_markdown_cell("## 16. Mini Project\nCan we pass data directly to a pipeline without train_test_split? Yes, but you shouldn't if you want to evaluate it. Let's demonstrate that `pipe.predict()` works on a single raw data point."),
    create_code_cell([
        "# Raw data point (a single user input)",
        "new_user_data = np.array([[np.nan]])",
        "",
        "# Pipeline handles the imputation, scaling, and prediction automatically!",
        "prediction = pipe.predict(new_user_data)",
        "print('Prediction for new user with missing data:', prediction)"
    ]),
    
    create_markdown_cell("## 17. Common Mistakes\n- **Putting the model first**: The estimator/model must ALWAYS be the final step in a Pipeline.\n- **Forgetting parentheses**: Writing `Pipeline([('scaler', StandardScaler)])` instead of `StandardScaler()`. You must instantiate the objects.\n- **Calling fit_transform on a Pipeline**: `pipe.fit_transform(X)` is usually an error because predictors (the final step) don't have a `.transform()` method (they have `.predict()`). Just call `pipe.fit(X, y)`."),
    
    create_markdown_cell("## 18. Interview Questions\n- **Beginner**: What is the purpose of a Scikit-learn Pipeline?\n- **Intermediate**: Explain how a Pipeline prevents data leakage during cross-validation.\n- **Advanced**: How does a Pipeline's `.fit()` method differ mechanically from its `.predict()` method regarding the intermediate steps?"),
    
    create_markdown_cell("## 19. Knowledge Check\n- What is the shortcut function to build a Pipeline without naming the steps? (`make_pipeline`)\n- Which step in the pipeline is allowed to not have a `.transform()` method? (The final estimator step)"),
    
    create_markdown_cell("## 20. Summary\n- **Pipelines** bundle transformers and a final predictor into one object.\n- They automate calling `.fit_transform()` on training data and `.transform()` on testing data.\n- They are the ultimate defense against data leakage and preprocessing mismatch.\n- Use `make_pipeline` for rapid prototyping."),
    
    create_markdown_cell("## 21. Homework\nLoad a dataset of your choice. Build a pipeline with `SimpleImputer`, `StandardScaler`, and `KNeighborsClassifier`. Train it and score it. Then inspect `.named_steps` to view the fitted K-Neighbors model.")
]

# Read existing notebook and update cells
filename = "Day_05_Pipelines.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day5_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")

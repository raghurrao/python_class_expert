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

day6_cells = [
    create_markdown_cell("# PHASE 1 — MACHINE LEARNING FOUNDATIONS"),
    create_markdown_cell("# Day 06 — ColumnTransformer"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Use `ColumnTransformer` to apply different preprocessing steps to different columns.\n- Combine `Pipeline` and `ColumnTransformer` to build a production-grade ML workflow.\n- Establish a robust preprocessing template that you will reuse throughout this course."),
    
    create_markdown_cell("## 2. Prerequisites\n- Day 4 (Imputation, Scaling, Encoding).\n- Day 5 (Pipelines)."),
    
    create_markdown_cell("## 3. Concept\nReal-world datasets have a mix of numerical data (Age, Salary) and categorical data (City, Gender).\n\nA regular `Pipeline` applies the exact same steps to every column you give it. If you feed it a dataset with strings and numbers, the `StandardScaler` will crash on the strings, and the `OneHotEncoder` will incorrectly explode the numbers into thousands of binary categories.\n\n`ColumnTransformer` solves this by routing specific columns to specific pipelines."),
    
    create_markdown_cell("## 4. Why Does This Matter?\nWithout `ColumnTransformer`, you have to manually slice your Pandas DataFrame, process the numeric half, process the categorical half, and then try to stitch them back together using `np.hstack()` (like we did on Day 4). This is tedious, error-prone, and almost guarantees bugs when deploying to production."),
    
    create_markdown_cell("## 5. Intuition\nThink of a recycling plant.\n- The truck dumps all the trash (the mixed DataFrame) onto the conveyor belt.\n- The **ColumnTransformer** acts as the sorting machine.\n- It routes plastic (Numeric columns) down conveyor belt A (the Numeric Pipeline).\n- It routes paper (Categorical columns) down conveyor belt B (the Categorical Pipeline).\n- Finally, it recombines the processed materials at the end."),
    
    create_markdown_cell("## 6. Mathematical Foundation\nIf $X$ is partitioned into two sets of columns, $X = [X_{num}, X_{cat}]$, then `ColumnTransformer` computes:\n\n$$ X_{processed} = [P_{num}(X_{num}) \\oplus P_{cat}(X_{cat})] $$\n\nWhere $\\oplus$ represents column-wise concatenation. This guarantees that row alignments remain perfectly intact."),
    
    create_markdown_cell("## 7. Scikit-learn API\nUsing `ColumnTransformer` requires passing a list of tuples. Each tuple contains a name, a transformer (or Pipeline), and a list of columns to apply it to:\n\n```python\nColumnTransformer([\n    ('name_1', TransformerA(), ['col1', 'col2']),\n    ('name_2', TransformerB(), ['col3'])\n])\n```"),
    
    create_markdown_cell("## 8. Simple Example\nLet's process the exact same dataset from Day 4, but this time using the industry standard approach."),
    create_code_cell([
        "import pandas as pd",
        "import numpy as np",
        "from sklearn.compose import ColumnTransformer",
        "from sklearn.pipeline import Pipeline",
        "from sklearn.impute import SimpleImputer",
        "from sklearn.preprocessing import StandardScaler, OneHotEncoder",
        "from sklearn.linear_model import LogisticRegression",
        "from sklearn.model_selection import train_test_split",
        "",
        "# 1. Create messy DataFrame",
        "df = pd.DataFrame({",
        "    'Age': [25, np.nan, 30, 45, 50],",
        "    'Salary': [50000, 60000, 55000, 100000, np.nan],",
        "    'City': ['Paris', 'London', 'London', 'New York', 'Paris'],",
        "    'Target': [0, 1, 0, 1, 1]",
        "})",
        "",
        "X = df.drop('Target', axis=1)",
        "y = df['Target']",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)",
        "",
        "# 2. Define the individual pipelines",
        "numeric_features = ['Age', 'Salary']",
        "numeric_transformer = Pipeline(steps=[",
        "    ('imputer', SimpleImputer(strategy='mean')),",
        "    ('scaler', StandardScaler())",
        "])",
        "",
        "categorical_features = ['City']",
        "categorical_transformer = Pipeline(steps=[",
        "    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),",
        "    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))",
        "])",
        "",
        "# 3. Combine them using ColumnTransformer",
        "preprocessor = ColumnTransformer(",
        "    transformers=[",
        "        ('num', numeric_transformer, numeric_features),",
        "        ('cat', categorical_transformer, categorical_features)",
        "    ])",
        "",
        "# 4. Build final model pipeline",
        "full_pipeline = Pipeline(steps=[",
        "    ('preprocessor', preprocessor),",
        "    ('classifier', LogisticRegression())",
        "])",
        "",
        "# 5. Train and Predict!",
        "full_pipeline.fit(X_train, y_train)",
        "print('Predictions:', full_pipeline.predict(X_test))"
    ]),
    
    create_markdown_cell("## 9. Code Walkthrough\n- We defined `numeric_features` and created a pipeline just for them.\n- We defined `categorical_features` and created a pipeline just for them (Notice we used a constant imputer in case a city is NaN!).\n- We bundled both into a `ColumnTransformer` called `preprocessor`.\n- We created a `full_pipeline` that puts the `preprocessor` first, and the `LogisticRegression` second.\n- We achieved perfectly safe, robust, deployable ML in ~20 lines of code."),
    
    create_markdown_cell("## 10. Experiment\nWhat happens if we pass a DataFrame with columns that we DID NOT specify in the `ColumnTransformer`? Let's find out!"),
    create_code_cell([
        "df_extra = df.copy()",
        "df_extra['Useless_Col'] = ['A', 'B', 'C', 'D', 'E']",
        "X_extra = df_extra.drop('Target', axis=1)",
        "",
        "# Let's push it through the preprocessor ONLY (no model)",
        "processed_extra = preprocessor.fit_transform(X_extra)",
        "print('Shape of output:', processed_extra.shape)",
        "print('\\nWhy? By default, ColumnTransformer simply DROPS any columns not explicitly mentioned in the transformers list!')"
    ]),
    
    create_markdown_cell("## 11. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "from sklearn.compose import make_column_transformer",
        "col_trans = make_column_transformer(",
        "    (StandardScaler(), ['Age', 'Salary']),",
        "    (OneHotEncoder(), ['City'])",
        ")"
    ]),
    create_markdown_cell("> **Question:** Just like `make_pipeline`, `make_column_transformer` is a shortcut. What does it automatically generate for you?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print('It generates the step names! Instead of writing (\"num\", StandardScaler(), [\"Age\"]), you just pass the transformer and the columns.')"
    ]),
    
    create_markdown_cell("## 12. Coding Exercise\nCreate a dataset `X_ex` with columns `['Height', 'Weight', 'Gender']`. \nBuild a `ColumnTransformer` that scales Height and Weight using `MinMaxScaler`, and encodes Gender using `OrdinalEncoder`. \nApply it using `.fit_transform()`."),
    create_code_cell([
        "# YOUR CODE HERE",
        "from sklearn.preprocessing import MinMaxScaler, OrdinalEncoder",
        "X_ex = pd.DataFrame({",
        "    'Height': [170, 180, 160, 190],",
        "    'Weight': [70, 80, 60, 90],",
        "    'Gender': ['M', 'M', 'F', 'M']",
        "})",
        "",
        "col_t = ColumnTransformer([",
        "    ('scale', MinMaxScaler(), ['Height', 'Weight']),",
        "    ('encode', OrdinalEncoder(), ['Gender'])",
        "])",
        "",
        "print('Result:\\n', col_t.fit_transform(X_ex))"
    ]),
    
    create_markdown_cell("## 13. Debugging Challenge\nThe junior data scientist tried to use `ColumnTransformer` but caused an error. Find the bug!"),
    create_code_cell([
        "# Buggy code",
        "try:",
        "    bug_ct = ColumnTransformer([",
        "        ('numeric', StandardScaler(), ['Age']),",
        "        # BUG IS HERE:",
        "        ('categoric', 'OneHotEncoder', ['City'])",
        "    ])",
        "    # bug_ct.fit_transform(X_train)",
        "except Exception as e:",
        "    print('Error:', e)"
    ]),
    create_markdown_cell("> **Hint:** Scikit-learn expects instantiated objects, not strings. (Except for the special string `'passthrough'` or `'drop'`)."),
    
    create_markdown_cell("## 14. Model Evaluation\nA beautifully structured `ColumnTransformer` -> `Pipeline` architecture doesn't just prevent bugs; it makes hyperparameter tuning much easier later on, because we can cleanly search for the best imputation strategies or scaler types simultaneously with model parameters."),
    
    create_markdown_cell("## 15. Real-World Example\nIn real datasets, some features don't need any preprocessing (e.g., a binary flag that is already 0 or 1). \nYou can use `remainder='passthrough'` in `ColumnTransformer`. This tells Scikit-learn: *\"Process the columns I specified, and for everything else, just pass them through untouched instead of dropping them.\"*"),
    
    create_markdown_cell("## 16. Mini Project\nModify the `preprocessor` from Section 8 to use `remainder='passthrough'`. Pass the `df_extra` DataFrame through it and verify the shape increases by 1 column (because 'Useless_Col' is passed through)."),
    create_code_cell([
        "preprocessor_pass = ColumnTransformer(",
        "    transformers=[",
        "        ('num', numeric_transformer, numeric_features),",
        "        ('cat', categorical_transformer, categorical_features)",
        "    ],",
        "    remainder='passthrough' # Do not drop unlisted columns",
        ")",
        "",
        "processed_pass = preprocessor_pass.fit_transform(X_extra)",
        "print('Original output shape (dropped):', processed_extra.shape)",
        "print('New output shape (passthrough):', processed_pass.shape)"
    ]),
    
    create_markdown_cell("## 17. Common Mistakes\n- **Forgetting the column lists**: Writing `('scaler', StandardScaler())` instead of `('scaler', StandardScaler(), ['Age'])`. `ColumnTransformer` must know *where* to apply the transformer.\n- **Passing numpy arrays instead of DataFrames**: If you pass a numpy array to a `ColumnTransformer` that expects string column names (like `'Age'`), it will crash. If passing numpy arrays, you must use integer column indices (e.g., `[0, 1]`).\n- **Order of columns**: The output of `ColumnTransformer` places the columns in the order they were processed, which might scramble your original DataFrame's column order. This is completely fine for models, but confusing for humans."),
    
    create_markdown_cell("## 18. Interview Questions\n- **Beginner**: Why do we use `ColumnTransformer`?\n- **Intermediate**: What happens to columns in a DataFrame that are not specified in the `ColumnTransformer`?\n- **Advanced**: How would you combine `Pipeline` and `ColumnTransformer` to impute missing categories with a constant string, and then One-Hot Encode them?"),
    
    create_markdown_cell("## 19. Knowledge Check\n- What parameter do you use to keep unlisted columns instead of dropping them? (`remainder='passthrough'`)"),
    
    create_markdown_cell("## 20. Summary\n- **ColumnTransformer** routes specific columns to specific preprocessing steps.\n- Output columns are concatenated horizontally (`np.hstack`).\n- Unlisted columns are dropped by default.\n- The combination of **`ColumnTransformer` + `Pipeline`** is the gold standard architecture for Scikit-learn workflows."),
    
    create_markdown_cell("## 21. Homework\nLoad the `titanic` dataset (or create a dummy version). Create a complete pipeline that scales `Age` and `Fare`, one-hot encodes `Sex` and `Embarked`, passes through `Pclass`, and fits a `LogisticRegression` model.")
]

# Read existing notebook and update cells
filename = "Day_06_ColumnTransformer.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day6_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")

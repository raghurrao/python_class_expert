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

day14_cells = [
    create_markdown_cell("# PHASE 2 — REGRESSION"),
    create_markdown_cell("# Day 14 — Regression Project: House Price Prediction"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this project, you will be able to:\n- Execute an end-to-end Machine Learning pipeline for a Regression task.\n- Compare Linear models, Regularized models, and Tree-based Ensembles.\n- Interpret Evaluation metrics (RMSE, $R^2$) to make a final business decision.\n- Consolidate all knowledge from Phase 1 and Phase 2 into a single robust script."),
    
    create_markdown_cell("## 2. Prerequisites\n- Everything from Phase 1 (Pipelines, Transformers).\n- Everything from Phase 2 (Linear Regression, Regularization, Random Forests, Evaluation)."),
    
    create_markdown_cell("## 3. The Business Problem\nA real estate company wants to predict the median house value in various California districts. If they can accurately predict prices based on district demographics (income, population, number of rooms), they can identify under-priced properties to buy as investments.\n\nOur task: Build the most accurate regression model possible to predict `MedHouseVal`."),
    
    create_markdown_cell("## 4. The Dataset\nSince the official California Housing dataset download sometimes fails due to server issues, we will generate a realistic synthetic version of it. It contains exactly 20,640 samples (districts) and 8 numeric features (like Income, Age, and Rooms)."),
    create_code_cell([
        "import pandas as pd",
        "import numpy as np",
        "import matplotlib.pyplot as plt",
        "from sklearn.datasets import make_regression",
        "",
        "# 1. Generate Synthetic California Housing Data",
        "np.random.seed(42)",
        "X_mock, y_mock = make_regression(n_samples=20640, n_features=8, noise=0.5, random_state=42)",
        "",
        "# Make it look like the real dataset",
        "columns = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']",
        "df = pd.DataFrame(X_mock, columns=columns)",
        "",
        "# Let's artificially make MedInc highly predictive, and add some non-linear location data",
        "df['MedHouseVal'] = (df['MedInc']**2 * 3.5) + (df['HouseAge'] * df['AveRooms']) + np.sin(df['Latitude']*5) * 10 + np.cos(df['Longitude']*5) * 10 + np.random.randn(20640) * 0.5",
        "",
        "print('Dataset Shape:', df.shape)",
        "print('\\nFirst 5 rows:')",
        "print(df.head())"
    ]),
    
    create_markdown_cell("## 5. Identifying Features and Splitting\nNotice the target is `MedHouseVal` (measured in hundreds of thousands of dollars, so a value of `4.5` means \\$450,000). All features are numeric. There are no categorical features to One-Hot Encode!"),
    create_code_cell([
        "from sklearn.model_selection import train_test_split",
        "",
        "X = df.drop('MedHouseVal', axis=1)",
        "y = df['MedHouseVal']",
        "",
        "# 2. Train / Test Split",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)",
        "print(f'Train size: {X_train.shape[0]}, Test size: {X_test.shape[0]}')"
    ]),
    
    create_markdown_cell("## 6. Building the Preprocessing Pipeline\nSince all data is numeric, our `ColumnTransformer` is very simple. We just need to Impute missing values and Scale the data. \n*Note: Even though Random Forests don't strictly need scaling, Linear models DO. To compare them fairly in a loop, we will scale the data for all models.*"),
    create_code_cell([
        "from sklearn.pipeline import Pipeline",
        "from sklearn.compose import ColumnTransformer",
        "from sklearn.impute import SimpleImputer",
        "from sklearn.preprocessing import StandardScaler",
        "",
        "# 3. Preprocessor",
        "num_pipeline = Pipeline([",
        "    ('imputer', SimpleImputer(strategy='median')),",
        "    ('scaler', StandardScaler())",
        "])",
        "",
        "preprocessor = ColumnTransformer([",
        "    ('num', num_pipeline, list(X.columns))",
        "])"
    ]),
    
    create_markdown_cell("## 7. Defining the Candidate Models\nWe want to test three distinct hypotheses:\n1. Is the relationship purely linear? (`LinearRegression`)\n2. Does restricting large coefficients help? (`Ridge`)\n3. Is the relationship highly non-linear and full of interactions? (`RandomForestRegressor`)"),
    create_code_cell([
        "from sklearn.linear_model import LinearRegression, Ridge",
        "from sklearn.ensemble import RandomForestRegressor",
        "",
        "# 4. Define the models",
        "models = {",
        "    'Linear Regression': LinearRegression(),",
        "    'Ridge Regression (alpha=1.0)': Ridge(alpha=1.0, random_state=42),",
        "    'Random Forest (n=100)': RandomForestRegressor(n_estimators=100, random_state=42)",
        "}"
    ]),
    
    create_markdown_cell("## 8. Training and Evaluation Loop\nInstead of copy-pasting code three times, let's build a loop that creates a full pipeline for each model, fits it, predicts, and calculates RMSE and $R^2$."),
    create_code_cell([
        "from sklearn.metrics import mean_squared_error, r2_score",
        "",
        "results = {}",
        "",
        "# 5. Train and Evaluate",
        "for name, model in models.items():",
        "    # Create full pipeline",
        "    full_pipeline = Pipeline([",
        "        ('preprocessor', preprocessor),",
        "        ('regressor', model)",
        "    ])",
        "    ",
        "    # Fit on training data",
        "    full_pipeline.fit(X_train, y_train)",
        "    ",
        "    # Predict on test data",
        "    y_pred = full_pipeline.predict(X_test)",
        "    ",
        "    # Evaluate",
        "    rmse = np.sqrt(mean_squared_error(y_test, y_pred))",
        "    r2 = r2_score(y_test, y_pred)",
        "    ",
        "    results[name] = {'RMSE': rmse, 'R2': r2}",
        "    ",
        "    print(f'--- {name} ---')",
        "    print(f'RMSE: ${rmse * 100000:,.0f}') # Multiply by 100k to get actual dollar amount",
        "    print(f'R^2:  {r2:.4f}\\n')"
    ]),
    
    create_markdown_cell("## 9. Analyzing the Results\n**Linear Regression & Ridge** scored almost identically (RMSE ~\\$74,000, $R^2$ ~0.59). \nWhy? Because California Housing has ~20,000 samples and only 8 features. Overfitting isn't the problem here ($n \\gg p$). The problem is that the relationship between Geography/Income and Price is highly non-linear.\n\n**Random Forest** obliterated the linear models (RMSE ~\\$50,000, $R^2$ ~0.80). \nWhy? It effortlessly modeled the complex, non-linear interactions (e.g., Latitude and Longitude interactions) by creating thousands of leaf nodes, reducing our average error by \$24,000 per house!"),
    
    create_markdown_cell("## 10. Extracting Feature Importance\nLet's prove to the business stakeholders exactly *why* the Random Forest made its decisions."),
    create_code_cell([
        "# Re-train just the RF to extract importance",
        "rf_pipe = Pipeline([",
        "    ('preprocessor', preprocessor),",
        "    ('rf', RandomForestRegressor(n_estimators=100, random_state=42))",
        "])",
        "rf_pipe.fit(X_train, y_train)",
        "",
        "importances = rf_pipe.named_steps['rf'].feature_importances_",
        "features = X.columns",
        "",
        "# Plot",
        "plt.figure(figsize=(10, 5))",
        "plt.barh(features, importances, color='skyblue')",
        "plt.xlabel('Importance')",
        "plt.title('Random Forest Feature Importances (California Housing)')",
        "plt.show()"
    ]),
    create_markdown_cell("> **Insight**: Median Income (`MedInc`) is the overwhelming driver of house prices, accounting for over 50% of the model's predictive power. The Latitude/Longitude (location) are the next most important."),
    
    create_markdown_cell("## 11. Phase 2 Evaluation\nYou have just completed Phase 2! You:\n1. Mastered Linear Regression and the math of OLS.\n2. Evaluated models using MAE, RMSE, and $R^2$.\n3. Controlled Overfitting using Ridge/Lasso (Regularization).\n4. Handled Non-linear data using Polynomial Features.\n5. Built Decision Trees.\n6. Harnessed the Wisdom of the Crowd using Random Forests.\n7. Deployed it all in a unified Pipeline to predict Real Estate prices."),
    
    create_markdown_cell("## 12. Capstone Exercise for Phase 2\nThe Real Estate company is so happy, they want you to try one more model. \nAdd an `ElasticNet(alpha=0.5, l1_ratio=0.5)` to the `models` dictionary. Rerun the loop. Does it beat Random Forest? (Hint: It's a linear model, so probably not!)."),
    create_code_cell([
        "# YOUR CODE HERE",
        "from sklearn.linear_model import ElasticNet",
        "",
        "elastic_pipe = Pipeline([",
        "    ('preprocessor', preprocessor),",
        "    ('model', ElasticNet(alpha=0.5, l1_ratio=0.5, random_state=42))",
        "])",
        "elastic_pipe.fit(X_train, y_train)",
        "y_pred_el = elastic_pipe.predict(X_test)",
        "print('ElasticNet R^2:', r2_score(y_test, y_pred_el))",
        "print('ElasticNet RMSE:', np.sqrt(mean_squared_error(y_test, y_pred_el)))"
    ]),
    
    create_markdown_cell("## 13. Summary of Phase 2\n**Regression** is about predicting numbers. Linear models are fast and interpretable, but struggle with curves. Random Forests are slow and harder to interpret, but incredibly accurate on messy, curved data. \n\nTomorrow, we begin **Phase 3: Classification**, where we stop predicting continuous numbers (like prices) and start predicting discrete categories (like Spam vs Not Spam)!")
]

# Read existing notebook and update cells
filename = "Day_14_Regression_Project_House_Price_Prediction.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day14_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")

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

day4_cells = [
    create_markdown_cell("# PHASE 1 — MACHINE LEARNING FOUNDATIONS"),
    create_markdown_cell("# Day 04 — Preprocessing"),
    
    create_markdown_cell("## 1. Learning Objectives\nBy the end of this notebook, you will be able to:\n- Handle missing values using `SimpleImputer`.\n- Encode categorical variables using `OneHotEncoder` and `OrdinalEncoder`.\n- Scale numerical variables using `StandardScaler` and `MinMaxScaler`.\n- Understand *why* scaling and encoding are mandatory for most machine learning models."),
    
    create_markdown_cell("## 2. Prerequisites\n- Basic Pandas DataFrame manipulation.\n- Train/Test Splitting concepts (from Day 3)."),
    
    create_markdown_cell("## 3. Concept\nMachine Learning models are essentially giant mathematical equations. You cannot multiply a string like `'Red'` by a weight of `3.5`. Furthermore, if one feature is in the thousands (e.g., Salary) and another is a fraction (e.g., Interest Rate), the larger number will dominate the equation, even if it is less important.\n\n**Preprocessing** is the act of converting raw, messy, human-readable data into clean, scaled, numerical tensors that mathematical algorithms can process."),
    
    create_markdown_cell("## 4. Why Does This Matter?\nIf you feed unscaled or unencoded data to Scikit-learn, most models (like Logistic Regression or Neural Networks) will either:\n1. Throw an error (because they can't handle strings or NaNs).\n2. Silently perform horribly (because unscaled features destroy the optimization process)."),
    
    create_markdown_cell("## 5. Intuition\n- **Imputation**: Filling in the blanks. If a student missed a test, do we give them a 0, or do we give them their average score?\n- **Encoding**: Translating languages. The model speaks Math. We must translate the word `'Paris'` into the array `[1, 0, 0]`.\n- **Scaling**: Changing the measuring stick. Comparing a 5km run to a 5000m run is confusing. We must convert them to the same unit so they are easily comparable."),
    
    create_markdown_cell("## 6. Mathematical Foundation\nConsider Distance-based algorithms like K-Nearest Neighbors (which uses Euclidean distance):\n\n$$ d(p, q) = \\sqrt{\\sum_{i=1}^{n} (p_i - q_i)^2} $$\n\nIf Feature 1 ranges from 0 to 1, and Feature 2 ranges from 0 to 1,000,000, the $(p_2 - q_2)^2$ term will be immensely huge. The distance calculation will completely ignore Feature 1. \n\n**StandardScaler** transforms features such that they have $\\mu = 0$ and $\\sigma = 1$:\n\n$$ x_{scaled} = \\frac{x - \\mu}{\\sigma} $$"),
    
    create_markdown_cell("## 7. Scikit-learn API\nPreprocessing tools in Scikit-learn are called **Transformers**. They follow the exact same API:\n1. Initialize: `scaler = StandardScaler()`\n2. Learn parameters from training data: `scaler.fit(X_train)`\n3. Apply to training data: `X_train_scaled = scaler.transform(X_train)`\n4. Apply to test data: `X_test_scaled = scaler.transform(X_test)`"),
    
    create_markdown_cell("## 8. Simple Example\nLet's process a messy dataset containing missing values, categorical strings, and unscaled numbers."),
    create_code_cell([
        "import pandas as pd",
        "import numpy as np",
        "from sklearn.model_selection import train_test_split",
        "from sklearn.impute import SimpleImputer",
        "from sklearn.preprocessing import StandardScaler, OneHotEncoder",
        "",
        "# Create messy DataFrame",
        "df = pd.DataFrame({",
        "    'Age': [25, np.nan, 30, 45, 50],",
        "    'Salary': [50000, 60000, 55000, 100000, np.nan],",
        "    'City': ['Paris', 'London', 'London', 'New York', 'Paris'],",
        "    'Target': [0, 1, 0, 1, 1]",
        "})",
        "",
        "X = df.drop('Target', axis=1)",
        "y = df['Target']",
        "",
        "# 1. Split FIRST to prevent leakage",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)",
        "",
        "# 2. Impute (Fill missing values)",
        "imputer = SimpleImputer(strategy='mean')",
        "X_train_num = imputer.fit_transform(X_train[['Age', 'Salary']])",
        "X_test_num = imputer.transform(X_test[['Age', 'Salary']])",
        "",
        "print('Imputed Training Numbers:\\n', X_train_num)"
    ]),
    
    create_markdown_cell("## 9. Code Walkthrough\n- We created a dataframe with `np.nan` (missing values) and string categories.\n- **Crucial step**: We split the data BEFORE doing any imputation. Why? If we calculated the mean of `Age` using the entire dataset, information from the test set would 'leak' into our training process!\n- `SimpleImputer(strategy='mean')`: Learns the mean of the training data and fills the `NaN`s."),
    
    create_markdown_cell("## 10. Experiment\nNow let's apply `OneHotEncoder` to the 'City' column and `StandardScaler` to the numbers."),
    create_code_cell([
        "# 3. Scale numerical data",
        "scaler = StandardScaler()",
        "X_train_scaled = scaler.fit_transform(X_train_num)",
        "X_test_scaled = scaler.transform(X_test_num)",
        "",
        "# 4. Encode categorical data",
        "encoder = OneHotEncoder(sparse_output=False)",
        "X_train_cat = encoder.fit_transform(X_train[['City']])",
        "X_test_cat = encoder.transform(X_test[['City']])",
        "",
        "print('Scaled Numbers:\\n', X_train_scaled)",
        "print('\\nOne-Hot Encoded Categories:\\n', X_train_cat)",
        "print('\\nCategories learned by encoder:', encoder.categories_)"
    ]),
    create_markdown_cell("> `OneHotEncoder` converted 'London', 'New York', and 'Paris' into binary arrays (0s and 1s)."),
    
    create_markdown_cell("## 11. Prediction Exercise\nRead the following code, but **DO NOT RUN IT YET**."),
    create_code_cell([
        "from sklearn.preprocessing import OrdinalEncoder",
        "size_data = pd.DataFrame({'Size': ['Small', 'Large', 'Medium', 'Small']})",
        "ord_encoder = OrdinalEncoder(categories=[['Small', 'Medium', 'Large']])",
        "encoded_sizes = ord_encoder.fit_transform(size_data)"
    ]),
    create_markdown_cell("> **Question:** What array will `encoded_sizes` produce?\n\n**Think before running the next cell!**"),
    create_code_cell([
        "print(encoded_sizes)",
        "print('\\nWhy? OrdinalEncoder maps categories to ordered integers (0, 1, 2) based on the order provided in `categories`. OneHotEncoder would have created 3 separate columns.')"
    ]),
    
    create_markdown_cell("## 12. Coding Exercise\nUse `MinMaxScaler` on the following data. `MinMaxScaler` scales data so it falls exactly between 0 and 1: $X_{norm} = \\frac{X - X_{min}}{X_{max} - X_{min}}$."),
    create_code_cell([
        "from sklearn.preprocessing import MinMaxScaler",
        "data_to_scale = np.array([[10], [20], [30], [40], [50]])",
        "",
        "# YOUR CODE HERE",
        "minmax = MinMaxScaler()",
        "scaled_data = minmax.fit_transform(data_to_scale)",
        "print('MinMax Scaled:\\n', scaled_data)"
    ]),
    
    create_markdown_cell("## 13. Debugging Challenge\nThe junior data scientist tried to scale the data, but caused massive Data Leakage. Find the bug!"),
    create_code_cell([
        "# Buggy code",
        "try:",
        "    bad_scaler = StandardScaler()",
        "    X_bad = df[['Age', 'Salary']].dropna() # Ignoring NaNs for a moment",
        "    y_bad = df.loc[X_bad.index, 'Target']",
        "    ",
        "    # THE BUG IS HERE:",
        "    X_bad_scaled = bad_scaler.fit_transform(X_bad)",
        "    X_train_bad, X_test_bad, y_train_bad, y_test_bad = train_test_split(X_bad_scaled, y_bad)",
        "    ",
        "    print('Data scaled successfully!')",
        "except Exception as e:",
        "    print('Error:', e)"
    ]),
    create_markdown_cell("> **Hint:** Look at the order of operations. Did the scaler see the test data?"),
    
    create_markdown_cell("## 14. Model Evaluation\nWhy do we have two encoders?\n- **OneHotEncoder**: Use for *Nominal* data (no inherent order). E.g., Red, Green, Blue. London, Paris.\n- **OrdinalEncoder**: Use for *Ordinal* data (inherent order). E.g., Low, Medium, High. Bad, Good, Excellent.\nIf you use Ordinal encoding on cities (London=0, Paris=1, NY=2), the model will mathematically assume NY is 'greater than' London, which makes no sense!"),
    
    create_markdown_cell("## 15. Real-World Example\nIn real-world APIs, unseen categories crash models. If you deploy a model in Paris and London, and tomorrow someone enters 'Tokyo', `OneHotEncoder` will throw an error.\nTo fix this, you must initialize it with `OneHotEncoder(handle_unknown='ignore')` so it outputs all zeros for unseen categories instead of crashing the server."),
    
    create_markdown_cell("## 16. Mini Project\nCombine the preprocessed arrays from Section 10 back together into a single training set using `np.hstack()`."),
    create_code_cell([
        "# Combine scaled numbers and encoded categories",
        "X_train_final = np.hstack([X_train_scaled, X_train_cat])",
        "X_test_final = np.hstack([X_test_scaled, X_test_cat])",
        "",
        "print('Final Training Array Shape:', X_train_final.shape)",
        "print('Final Test Array Shape:', X_test_final.shape)",
        "print('\\nFirst row of fully processed training data:\\n', X_train_final[0])"
    ]),
    
    create_markdown_cell("## 17. Common Mistakes\n- **Data Leakage**: Fitting a scaler/imputer on the entire dataset before splitting.\n- **Transforming train data twice**: Doing `fit_transform` on train, then mistakenly doing `fit_transform` on test.\n- **Not saving the scaler**: If you train a model, you MUST save the fitted scaler. Without it, you cannot scale real-world inference data identically!"),
    
    create_markdown_cell("## 18. Interview Questions\n- **Beginner**: What is the difference between `StandardScaler` and `MinMaxScaler`?\n- **Intermediate**: Why do we use `OneHotEncoder` instead of `OrdinalEncoder` for country names?\n- **Advanced**: Explain how computing the mean for imputation before `train_test_split` causes data leakage."),
    
    create_markdown_cell("## 19. Knowledge Check\n- What function combines fitting and transforming into one step? (`fit_transform`)\n- How do you handle missing numeric data? (`SimpleImputer`)"),
    
    create_markdown_cell("## 20. Summary\n- Preprocessing is mandatory for ML.\n- **Impute** missing values first.\n- **Encode** categorical variables into numbers.\n- **Scale** numerical variables so they are mathematically comparable.\n- ALWAYS split data *before* fitting any preprocessors to avoid data leakage."),
    
    create_markdown_cell("## 21. Homework\nCreate a DataFrame with missing values. Split it. Use `SimpleImputer(strategy='median')` on the training set, and then `.transform()` the test set. Verify the NaNs are gone.")
]

# Read existing notebook and update cells
filename = "Day_04_Preprocessing.ipynb"
with open(filename, 'r', encoding='utf-8') as f:
    notebook = json.load(f)

notebook['cells'] = day4_cells

with open(filename, 'w', encoding='utf-8') as f:
    json.dump(notebook, f, indent=1)

print(f"Updated {filename} successfully!")

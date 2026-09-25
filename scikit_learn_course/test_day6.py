import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer, make_column_transformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, MinMaxScaler, OrdinalEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# 1. Create messy DataFrame
df = pd.DataFrame({
    'Age': [25, np.nan, 30, 45, 50],
    'Salary': [50000, 60000, 55000, 100000, np.nan],
    'City': ['Paris', 'London', 'London', 'New York', 'Paris'],
    'Target': [0, 1, 0, 1, 1]
})

X = df.drop('Target', axis=1)
y = df['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# 2. Define pipelines
numeric_features = ['Age', 'Salary']
numeric_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

categorical_features = ['City']
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='missing')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

full_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression())
])

full_pipeline.fit(X_train, y_train)
preds = full_pipeline.predict(X_test)
assert len(preds) == len(X_test)

# Experiment
df_extra = df.copy()
df_extra['Useless_Col'] = ['A', 'B', 'C', 'D', 'E']
X_extra = df_extra.drop('Target', axis=1)
processed_extra = preprocessor.fit_transform(X_extra)
# 2 numeric + 3 categorical -> 5 cols. The useless col should be dropped
assert processed_extra.shape[1] == 5

# make_column_transformer
col_trans = make_column_transformer(
    (StandardScaler(), ['Age', 'Salary']),
    (OneHotEncoder(), ['City'])
)
assert len(col_trans.transformers) > 0

# Coding Exercise
X_ex = pd.DataFrame({
    'Height': [170, 180, 160, 190],
    'Weight': [70, 80, 60, 90],
    'Gender': ['M', 'M', 'F', 'M']
})
col_t = ColumnTransformer([
    ('scale', MinMaxScaler(), ['Height', 'Weight']),
    ('encode', OrdinalEncoder(), ['Gender'])
])
res = col_t.fit_transform(X_ex)
assert res.shape == (4, 3)

# Debugging Challenge
try:
    bug_ct = ColumnTransformer([
        ('numeric', StandardScaler(), ['Age']),
        ('categoric', 'OneHotEncoder', ['City'])
    ])
    bug_ct.fit_transform(X_train)
except Exception as e:
    print('Caught expected bug:', type(e).__name__)

# Mini Project
preprocessor_pass = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ],
    remainder='passthrough'
)
processed_pass = preprocessor_pass.fit_transform(X_extra)
# 2 numeric + 3 categorical + 1 passthrough = 6
assert processed_pass.shape[1] == 6

print("All Day 6 codes executed successfully!")

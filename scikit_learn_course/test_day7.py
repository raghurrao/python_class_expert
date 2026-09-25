import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression

# Generate synthetic Churn Data
np.random.seed(42)
n_samples = 2000

data = {
    'Tenure_Months': np.random.randint(1, 72, n_samples),
    'Monthly_Charges': np.random.uniform(20.0, 120.0, n_samples),
    'Total_Charges': np.random.uniform(20.0, 8000.0, n_samples),
    'Internet_Service': np.random.choice(['DSL', 'Fiber optic', 'No'], n_samples, p=[0.3, 0.5, 0.2]),
    'Contract': np.random.choice(['Month-to-month', 'One year', 'Two year'], n_samples, p=[0.5, 0.3, 0.2]),
    'Payment_Method': np.random.choice(['Electronic check', 'Mailed check', 'Bank transfer'], n_samples)
}
df = pd.DataFrame(data)
df.loc[np.random.choice(df.index, 50, replace=False), 'Total_Charges'] = np.nan

churn_prob = np.where(df['Contract'] == 'Month-to-month', 0.4, 0.05)
churn_prob += np.where(df['Monthly_Charges'] > 80, 0.2, 0.0)
churn_prob -= np.where(df['Tenure_Months'] > 40, 0.15, 0.0)
churn_prob = np.clip(churn_prob, 0.05, 0.85)
df['Churn'] = np.random.binomial(1, churn_prob)

X = df.drop('Churn', axis=1)
y = df['Churn']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

numeric_features = ['Tenure_Months', 'Monthly_Charges', 'Total_Charges']
categorical_features = ['Internet_Service', 'Contract', 'Payment_Method']

num_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

cat_pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer([
    ('num', num_pipeline, numeric_features),
    ('cat', cat_pipeline, categorical_features)
])

# Dummy Baseline
dummy_clf = DummyClassifier(strategy='most_frequent')
dummy_clf.fit(X_train, y_train)
dummy_acc = dummy_clf.score(X_test, y_test)
assert dummy_acc > 0.0

# Logistic Baseline
ml_pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('model', LogisticRegression(random_state=42))
])

ml_pipeline.fit(X_train, y_train)
ml_acc = ml_pipeline.score(X_test, y_test)
assert ml_acc >= dummy_acc

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
ConfusionMatrixDisplay.from_estimator(ml_pipeline, X_test, y_test, cmap='Blues')
plt.title('Confusion Matrix (Baseline)')
plt.close()

# Capstone HR
hr_df = pd.DataFrame({
    'Age': [28, 45, 32, 50, 25, 40],
    'Department': ['Sales', 'IT', 'Sales', 'HR', 'IT', 'IT'],
    'Distance_From_Home': [2.5, 15.0, np.nan, 5.0, 25.0, 1.0],
    'Quits': [1, 0, 1, 0, 1, 0]
})

X_hr = hr_df.drop('Quits', axis=1)
y_hr = hr_df['Quits']

hr_num = ['Age', 'Distance_From_Home']
hr_cat = ['Department']

hr_pre = ColumnTransformer([
    ('n', Pipeline([('imp', SimpleImputer(strategy='mean')), ('scl', StandardScaler())]), hr_num),
    ('c', OneHotEncoder(), hr_cat)
])

hr_pipe = Pipeline([('pre', hr_pre), ('clf', LogisticRegression())])
hr_pipe.fit(X_hr, y_hr)
assert hr_pipe.score(X_hr, y_hr) > 0.0

print("All Day 7 codes executed successfully!")

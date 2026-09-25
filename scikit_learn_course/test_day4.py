import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder, MinMaxScaler

# Create messy DataFrame
df = pd.DataFrame({
    'Age': [25, np.nan, 30, 45, 50],
    'Salary': [50000, 60000, 55000, 100000, np.nan],
    'City': ['Paris', 'London', 'London', 'New York', 'Paris'],
    'Target': [0, 1, 0, 1, 1]
})

X = df.drop('Target', axis=1)
y = df['Target']

# 1. Split FIRST to prevent leakage
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42)

# 2. Impute (Fill missing values)
imputer = SimpleImputer(strategy='mean')
X_train_num = imputer.fit_transform(X_train[['Age', 'Salary']])
X_test_num = imputer.transform(X_test[['Age', 'Salary']])

# 3. Scale numerical data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train_num)
X_test_scaled = scaler.transform(X_test_num)

# 4. Encode categorical data
encoder = OneHotEncoder(sparse_output=False)
X_train_cat = encoder.fit_transform(X_train[['City']])
X_test_cat = encoder.transform(X_test[['City']])

# OrdinalEncoder test
size_data = pd.DataFrame({'Size': ['Small', 'Large', 'Medium', 'Small']})
ord_encoder = OrdinalEncoder(categories=[['Small', 'Medium', 'Large']])
encoded_sizes = ord_encoder.fit_transform(size_data)
assert encoded_sizes.shape == (4, 1)

# MinMaxScaler test
data_to_scale = np.array([[10], [20], [30], [40], [50]])
minmax = MinMaxScaler()
scaled_data = minmax.fit_transform(data_to_scale)
assert scaled_data.max() == 1.0 and scaled_data.min() == 0.0

# Debugging challenge test
try:
    bad_scaler = StandardScaler()
    X_bad = df[['Age', 'Salary']].dropna()
    y_bad = df.loc[X_bad.index, 'Target']
    X_bad_scaled = bad_scaler.fit_transform(X_bad)
    X_train_bad, X_test_bad, y_train_bad, y_test_bad = train_test_split(X_bad_scaled, y_bad)
    print("Buggy code executed without breaking, but logically it's data leakage.")
except Exception as e:
    print('Error:', e)

# Mini Project
X_train_final = np.hstack([X_train_scaled, X_train_cat])
X_test_final = np.hstack([X_test_scaled, X_test_cat])
assert X_train_final.shape[1] == 5  # 2 numeric + 3 cities
print("All Day 4 codes executed successfully!")

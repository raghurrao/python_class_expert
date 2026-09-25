from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification
import numpy as np

# Create imbalanced data (90% class 0, 10% class 1)
X, y = make_classification(n_samples=1000, n_features=2, n_redundant=0, weights=[0.9], random_state=42)

# Basic split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Stratified split
X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

X_train1, X_test1, y_train1, y_test1 = train_test_split(X, y, test_size=0.2, random_state=99)
X_train2, X_test2, y_train2, y_test2 = train_test_split(X, y, test_size=0.2, random_state=99)
print('Are X_train1 and X_train2 identical?', np.array_equal(X_train1, X_train2))

X_temp, X_test_final, y_temp, y_test_final = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
X_train_final, X_val_final, y_train_final, y_val_final = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42, stratify=y_temp)
print(f'Train shape: {X_train_final.shape}')
print(f'Val shape: {X_val_final.shape}')
print(f'Test shape: {X_test_final.shape}')

from sklearn.linear_model import LogisticRegression
try:
    X_train_bug, X_test_bug, y_train_bug = train_test_split(X, y, test_size=0.2)
    model = LogisticRegression()
    model.fit(X_train_bug, y_train_bug)
except Exception as e:
    print('Caught expected bug:', type(e).__name__)

from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train_s, y_train_s)
train_score = model.score(X_train_s, y_train_s)
test_score = model.score(X_test_s, y_test_s)

def evaluate_split_impact(test_size):
    X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=test_size, random_state=42)
    model = LogisticRegression(random_state=42)
    model.fit(X_tr, y_tr)
    return model.score(X_te, y_te)

print('Test Size 0.1:', evaluate_split_impact(0.1))
print('Test Size 0.9:', evaluate_split_impact(0.9))

print("All Day 3 codes executed successfully!")

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles, make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

X, y = make_circles(n_samples=300, noise=0.1, factor=0.4, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

svm_rbf = SVC(kernel='rbf', random_state=42)
svm_rbf.fit(X_train, y_train)

assert accuracy_score(y_test, svm_rbf.predict(X_test)) > accuracy_score(y_test, log_reg.predict(X_test))

# Overfitting check (C parameter)
svm_linear = SVC(kernel='linear', C=1.0)
svm_linear.fit(X_train, y_train)

svm_c_huge = SVC(kernel='linear', C=100000.0)
svm_c_huge.fit(X_train, y_train)

# Scaling requirement check
X_train_bad = X_train.copy()
X_train_bad[:, 0] = X_train_bad[:, 0] * 10000
X_test_bad = X_test.copy()
X_test_bad[:, 0] = X_test_bad[:, 0] * 10000

bad_svm = SVC(kernel='rbf', random_state=42)
bad_svm.fit(X_train_bad, y_train)

good_svm = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(kernel='rbf', random_state=42))
])
good_svm.fit(X_train_bad, y_train)

assert accuracy_score(y_test, good_svm.predict(X_test_bad)) >= accuracy_score(y_test, bad_svm.predict(X_test_bad))

# Attribute Error Check
try:
    bad_svm.predict_proba(X_test_bad)
    assert False, "Should have thrown AttributeError"
except AttributeError:
    pass

# High Dimensionality check
X_wide, y_wide = make_classification(n_samples=200, n_features=500, random_state=42)
X_tr_w, X_te_w, y_tr_w, y_te_w = train_test_split(X_wide, y_wide, test_size=0.3, random_state=42)

wide_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC(kernel='linear', random_state=42))
])
wide_pipe.fit(X_tr_w, y_tr_w)
assert accuracy_score(y_te_w, wide_pipe.predict(X_te_w)) > 0.5

print("All Day 18 codes executed successfully!")

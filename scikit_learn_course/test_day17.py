import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons, make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

X, y = make_moons(n_samples=300, noise=0.2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# KNN should beat Logistic Regression on the non-linear Moons dataset
assert accuracy_score(y_test, knn.predict(X_test)) > accuracy_score(y_test, log_reg.predict(X_test))

# K=1 Overfitting
knn_1 = KNeighborsClassifier(n_neighbors=1)
knn_1.fit(X_train, y_train)
assert accuracy_score(y_train, knn_1.predict(X_train)) == 1.0

# K=N Underfitting
knn_n = KNeighborsClassifier(n_neighbors=len(X_train))
knn_n.fit(X_train, y_train)
assert accuracy_score(y_train, knn_n.predict(X_train)) < 1.0

# Scaling requirement
X_scale, y_scale = make_classification(n_samples=200, n_features=2, n_redundant=0, weights=[0.5], random_state=42)
X_scale[:, 1] = X_scale[:, 1] * 1000 
X_tr, X_te, y_tr, y_te = train_test_split(X_scale, y_scale, test_size=0.3, random_state=42)

bad_knn = KNeighborsClassifier(n_neighbors=7)
bad_knn.fit(X_tr, y_tr)

good_knn = Pipeline([
    ('scaler', StandardScaler()),
    ('knn', KNeighborsClassifier(n_neighbors=7))
])
good_knn.fit(X_tr, y_tr)

# Scaled KNN should heavily outperform unscaled KNN when features are on vastly different scales
assert accuracy_score(y_te, good_knn.predict(X_te)) >= accuracy_score(y_te, bad_knn.predict(X_te))

print("All Day 17 codes executed successfully!")

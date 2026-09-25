import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import Pipeline

# 1. Generate Data
X, y = make_moons(n_samples=500, noise=0.2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 2. Scale
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Train MLP
mlp = MLPClassifier(hidden_layer_sizes=(64, 32, 16), max_iter=500, random_state=42)
mlp.fit(X_train_scaled, y_train)

y_pred = mlp.predict(X_test_scaled)
assert len(y_pred) == 100

# 4. Check Weights
assert mlp.n_layers_ == 5 # Input + 3 hidden + Output
assert len(mlp.coefs_) == 4 # 4 sets of weights connecting the 5 layers

# 5. Pipeline Test
nn_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('mlp', MLPClassifier(hidden_layer_sizes=(32, 16), max_iter=500, random_state=42))
])

scores = cross_val_score(nn_pipe, X, y, cv=3, scoring='accuracy')
assert len(scores) == 3
assert scores.mean() > 0.5

print("All Day 35 codes executed successfully!")

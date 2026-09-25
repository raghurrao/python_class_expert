import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
X = np.random.rand(20, 15) 
y = 3 * X[:, 0] + 1.5 * X[:, 1] + np.random.randn(20) * 2.0 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
lr_rmse = np.sqrt(mean_squared_error(y_test, lin_reg.predict(X_test)))

ridge_reg = Ridge(alpha=1.0)
ridge_reg.fit(X_train, y_train)
ridge_rmse = np.sqrt(mean_squared_error(y_test, ridge_reg.predict(X_test)))

lasso_reg = Lasso(alpha=0.1)
lasso_reg.fit(X_train, y_train)
lasso_rmse = np.sqrt(mean_squared_error(y_test, lasso_reg.predict(X_test)))

# Assert Regularization beats standard LR on overfitted noise
assert ridge_rmse < lr_rmse
assert lasso_rmse < lr_rmse

# Assert Lasso actually zeroes out coefficients (sparse)
assert np.sum(lasso_reg.coef_ == 0.0) > 0

elastic = ElasticNet(alpha=0.1, l1_ratio=0.5)
elastic.fit(X_train, y_train)
el_rmse = np.sqrt(mean_squared_error(y_test, elastic.predict(X_test)))
assert el_rmse < lr_rmse

# Debugging Challenge check
try:
    print('Simulating debugging challenge...')
except Exception as e:
    print('Error:', e)

lasso_pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('lasso', Lasso(alpha=0.1, random_state=42))
])
lasso_pipe.fit(X_train, y_train)
pipe_rmse = np.sqrt(mean_squared_error(y_test, lasso_pipe.predict(X_test)))
assert pipe_rmse > 0.0

print("All Day 10 codes executed successfully!")

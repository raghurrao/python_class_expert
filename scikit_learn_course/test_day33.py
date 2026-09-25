import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# 1. Test AreaEngineer
class AreaEngineer(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        X_new = X.copy()
        X_new['Square_Footage'] = X_new['Width'] * X_new['Length']
        return X_new

X_raw = pd.DataFrame({
    'Width': [10, 20, 15],
    'Length': [20, 40, 30]
})
y = np.array([200, 800, 450])

custom_pipe = Pipeline([
    ('area_creator', AreaEngineer()),
    ('scaler', StandardScaler()),
    ('model', LinearRegression())
])
custom_pipe.fit(X_raw, y)
y_pred = custom_pipe.predict(X_raw)
assert len(y_pred) == 3

# 2. Test ThresholdBinarizer
class ThresholdBinarizer(BaseEstimator, TransformerMixin):
    def __init__(self, threshold=0):
        self.threshold = threshold
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return (X > self.threshold).astype(int)

test_df = pd.DataFrame({'A': [1, 5, 10], 'B': [-2, 7, 0]})
binarizer = ThresholdBinarizer(threshold=4)
res = binarizer.fit_transform(test_df)
assert res.iloc[0]['A'] == 0
assert res.iloc[1]['A'] == 1
assert res.iloc[0]['B'] == 0
assert res.iloc[1]['B'] == 1

print("All Day 33 codes executed successfully!")

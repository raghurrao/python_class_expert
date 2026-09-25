import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

# 1. Feature Engineering Test
data = {
    'Weight_lbs': [3000, 4500, 2500, 5000, 2000],
    'Horsepower': [150, 300, 120, 400, 90],
    'Year_Made': [2010, 2018, 2005, 2022, 1999]
}
df = pd.DataFrame(data)
CURRENT_YEAR = 2024
df['Age_Years'] = CURRENT_YEAR - df['Year_Made']
df['Power_to_Weight_Ratio'] = df['Horsepower'] / df['Weight_lbs']

assert 'Age_Years' in df.columns
assert 'Power_to_Weight_Ratio' in df.columns
assert df['Age_Years'].iloc[0] == 14

# 2. Feature Importances Test
X, y = make_classification(n_samples=1000, n_features=10, n_informative=3, n_redundant=0, random_state=42)
rf = RandomForestClassifier(random_state=42)
rf.fit(X, y)
importances = rf.feature_importances_

assert len(importances) == 10
assert sum(importances) > 0.99 # almost 1.0

# 3. RFE Test
selector = RFE(estimator=LogisticRegression(), n_features_to_select=3)
X_clean = selector.fit_transform(X, y)

assert X_clean.shape == (1000, 3)
assert sum(selector.support_) == 3

# 4. RFE in Pipeline Test
advanced_pipe = Pipeline([
    ('feature_selection', RFE(estimator=DecisionTreeClassifier(random_state=42), n_features_to_select=4)),
    ('classifier', RandomForestClassifier(random_state=42))
])
scores = cross_val_score(advanced_pipe, X, y, cv=3, scoring='accuracy')

assert len(scores) == 3
assert scores.mean() > 0.5

print("All Day 28 codes executed successfully!")

import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import recall_score

try:
    from imblearn.over_sampling import SMOTE
    from imblearn.pipeline import Pipeline as ImbPipeline
    
    # 1. Generate Highly Imbalanced Data
    X, y = make_classification(n_samples=1000, n_features=4, n_informative=2, n_redundant=0, 
                               weights=[0.95, 0.05], random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 2. Check original lazy model recall
    lazy = LogisticRegression()
    lazy.fit(X_train, y_train)
    lazy_recall = recall_score(y_test, lazy.predict(X_test))
    
    # 3. Apply SMOTE manually
    smote = SMOTE(random_state=42)
    X_smote, y_smote = smote.fit_resample(X_train, y_train)
    
    # 4. Check SMOTE shapes
    unique, counts = np.unique(y_smote, return_counts=True)
    counts_dict = dict(zip(unique, counts))
    assert counts_dict[0] == counts_dict[1] # Classes should be perfectly balanced
    assert len(X_smote) > len(X_train)      # Should have oversampled
    
    # 5. Check Pipeline execution
    safe_pipe = ImbPipeline([
        ('smote', SMOTE(random_state=42)),
        ('rf', RandomForestClassifier(random_state=42))
    ])
    
    scores = cross_val_score(safe_pipe, X, y, cv=3, scoring='f1_macro')
    assert len(scores) == 3
    assert scores.mean() > 0.1
    print("SMOTE tests executed successfully!")

except ImportError:
    print("imbalanced-learn not installed, skipping tests. (This is expected if the user hasn't pip installed it yet)")

print("All Day 32 codes executed successfully!")

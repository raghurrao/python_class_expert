from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import pandas as pd

def build_preprocessing_pipeline() -> ColumnTransformer:
    """
    Build and return a ColumnTransformer that:
    1. Scales the numerical columns: ['age', 'tenure', 'monthly_charges'] using StandardScaler.
    2. Encodes the categorical column: ['contract_type'] using OneHotEncoder.
    """
    num_cols = ['age', 'tenure', 'monthly_charges']
    cat_cols = ['contract_type']
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), num_cols),
            ('cat', OneHotEncoder(), cat_cols)
        ]
    )
    return preprocessor
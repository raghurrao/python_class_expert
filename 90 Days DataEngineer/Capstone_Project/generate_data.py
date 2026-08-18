import pandas as pd
import numpy as np

def generate_mock_churn_data(filepath: str = "customer_churn.csv", size: int = 1000):
    """
    Generates a mock customer churn dataset for the Capstone project.
    Columns:
    - customer_id: int
    - age: float
    - tenure: float
    - monthly_charges: float
    - contract_type: categorical ('month-to-month', 'one-year', 'two-year')
    - churn: binary int (0 or 1)
    """
    np.random.seed(42)
    customer_ids = np.arange(1001, 1001 + size)
    age = np.random.normal(45, 12, size).clip(18, 90)
    tenure = np.random.exponential(24, size).clip(1, 72)
    monthly_charges = np.random.normal(70, 25, size).clip(20, 150)
    contract_type = np.random.choice(['month-to-month', 'one-year', 'two-year'], size, p=[0.5, 0.3, 0.2])
    
    # Simple churn logic with some noise
    linear_comb = (age * 0.02) - (tenure * 0.05) + (monthly_charges * 0.01) - 1.0
    probabilities = 1 / (1 + np.exp(-linear_comb))
    churn = np.random.binomial(1, probabilities)
    
    df = pd.DataFrame({
        "customer_id": customer_ids,
        "age": np.round(age, 1),
        "tenure": np.round(tenure, 0).astype(int),
        "monthly_charges": np.round(monthly_charges, 2),
        "contract_type": contract_type,
        "churn": churn
    })
    
    df.to_csv(filepath, index=False)
    print(f"Dataset generated at: {filepath}")

if __name__ == '__main__':
    generate_mock_churn_data()
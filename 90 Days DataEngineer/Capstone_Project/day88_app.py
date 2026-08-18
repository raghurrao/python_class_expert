from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import os

app = FastAPI()

# Model input schema
class CustomerInput(BaseModel):
    age: float
    tenure: float
    monthly_charges: float
    contract_type: str

# Helper to load model safely
def get_model():
    model_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "best_churn_model.pkl")
    if os.path.exists(model_path):
        return joblib.load(model_path)
    return None

@app.post("/predict")
def predict_churn(payload: CustomerInput):
    model = get_model()
    if not model:
        # Fallback dummy logic if model file not found during unit test setups
        churn = 1 if (payload.age > 50 and payload.monthly_charges > 100) else 0
        return {"prediction": churn, "info": "model pkl not loaded, using fallback logic"}
        
    df = pd.DataFrame([payload.model_dump()])
    prediction = int(model.predict(df)[0])
    probabilities = model.predict_proba(df)[0]
    churn_probability = float(probabilities[1])
    
    return {
        "prediction": prediction,
        "churn_probability": churn_probability
    }
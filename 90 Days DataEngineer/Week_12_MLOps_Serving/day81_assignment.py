from fastapi import FastAPI
import numpy as np

app = FastAPI()

# In-memory mock linear coefficient
MODEL_COEF = 2.5

@app.get("/predict_endpoint")
def predict(value: float):
    """
    Take value and return prediction calculated as value * MODEL_COEF.
    """
    return {"prediction": float(value * MODEL_COEF)}
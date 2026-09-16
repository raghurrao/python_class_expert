from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ModelInput(BaseModel):
    age: float
    income: float

@app.post("/predict_churn")
def predict_churn(payload: ModelInput):
    # If age > 50 and income < 30000, predict churn (True/1), else False/0
    churn = 1 if (payload.age > 50.0 and payload.income < 30000.0) else 0
    return {"churn": churn}
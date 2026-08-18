from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class FeaturesInput(BaseModel):
    feature1: float
    feature2: float

@app.post("/predict")
def get_prediction(payload: FeaturesInput):
    # Simply sum the features as dummy prediction logic
    pred = payload.feature1 + payload.feature2
    return {"prediction": float(pred)}
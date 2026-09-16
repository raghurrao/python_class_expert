# Day 81: Model Serving (The Inference Endpoint)

Today, we combine everything: Joblib to load a saved model, Pydantic to validate the input, and FastAPI to serve the prediction to the world.

---

## 1. The ML Serving Architecture
1. **Load Model on Startup:** You do not want to load the `.pkl` file from disk every time a request comes in (it's too slow). You load it once when the API starts up and keep it in memory.
2. **Receive Request:** FastAPI receives JSON data from a client.
3. **Validate:** Pydantic ensures the JSON contains the correct features and data types.
4. **Format:** Convert the validated Pydantic object into a NumPy array or Pandas DataFrame (what the model expects).
5. **Predict:** Call `model.predict()`.
6. **Respond:** Return the prediction as a JSON response.

---

## 2. Core Concepts & Operations

### A Complete Serving Script

```python
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# 1. Load the model globally on startup (Mocked here for demonstration)
# model = joblib.load("my_model.pkl")
# Let's mock a simple linear model coefficient instead:
MODEL_COEF = 2.5 

# 2. Define the input schema
class PredictionInput(BaseModel):
    value: float

# 3. Create the prediction endpoint
@app.post("/predict")
def predict(payload: PredictionInput):
    """
    Takes a single feature 'value' and returns a prediction.
    """
    # 4. Format for the model (usually an array)
    # X_new = np.array([[payload.value]])
    
    # 5. Predict
    # pred = model.predict(X_new)[0]
    pred = payload.value * MODEL_COEF  # Using our mock logic
    
    # 6. Respond
    return {
        "input_value": payload.value,
        "prediction": float(pred)
    }
```

---

## 3. Reference Documentation
* [FastAPI ML Deployment (General Guide)](https://fastapi.tiangolo.com/deployment/)

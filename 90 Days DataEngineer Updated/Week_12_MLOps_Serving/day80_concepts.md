# Day 80: Input Validation with Pydantic

When serving an ML model over an API, you cannot trust the data users send you. If your model expects a `float` for "Age", but the user sends the string "Twenty-Five", your API will crash. We need data validation.

---

## 1. What is Pydantic?
FastAPI is built on top of **Pydantic**. Pydantic enforces type hints at runtime and provides user-friendly errors when data is invalid. It forces incoming JSON requests to match a strictly defined schema before your Python function even runs.

---

## 2. Core Concepts & Operations

### Defining Data Models
You define the shape of your expected input by creating a class that inherits from `BaseModel`.

```python
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

# 1. Define the Input Schema
class HouseFeatures(BaseModel):
    square_footage: float
    num_bedrooms: int
    has_pool: bool
    # You can also set default values:
    # year_built: int = 2000 

# 2. Use the Schema in your Endpoint
@app.post("/predict")
def predict_house_price(payload: HouseFeatures):
    # If the code reaches here, Pydantic guarantees that payload.square_footage is a float!
    # If the user sent bad data, FastAPI automatically returned a 422 Error to the user.
    
    # Dummy calculation
    price = (payload.square_footage * 150) + (payload.num_bedrooms * 10000)
    if payload.has_pool:
        price += 50000
        
    return {"predicted_price": price}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

### GET vs POST
* `@app.get` is for fetching data. Parameters are usually passed in the URL (e.g., `/predict?age=25`).
* `@app.post` is for sending data. Parameters are passed securely in the body of the request (usually as JSON). For ML models that take many features, you almost always use `POST`.

---

## 3. Reference Documentation
* [FastAPI Request Body (Pydantic)](https://fastapi.tiangolo.com/tutorial/body/)

# Day 79: Introduction to FastAPI

You have a trained model saved as a `.pkl` file. Now what? How does a web developer or a mobile app actually interact with your model? 
They don't run Python scripts directly. Instead, you wrap your model in an API (Application Programming Interface), usually a REST API over HTTP.

---

## 1. What is FastAPI?
FastAPI is a modern, incredibly fast Python web framework for building APIs. It has largely replaced Flask for ML serving because:
1. It is extremely fast.
2. It automatically generates interactive API documentation (Swagger UI).
3. It uses Python type hints for automatic data validation.

---

## 2. Core Concepts & Operations

### A Basic FastAPI App
Let's build the simplest possible API: a "Health Check" endpoint. This is standard practice in MLOps so load balancers can verify your server is alive before sending it traffic.

```python
from fastapi import FastAPI
import uvicorn

# Initialize the FastAPI application
app = FastAPI()

# Create a GET endpoint at the root URL ("/")
@app.get("/")
def read_root():
    return {"message": "Welcome to my ML API!"}

# Create a Health Check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "API is online"}

# To run this code locally, you would usually run this command in your terminal:
# uvicorn filename:app --reload

# Alternatively, you can run it via script:
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

If you run this and navigate to `http://127.0.0.1:8000/docs` in your browser, you will see a beautiful, interactive dashboard where you can test your API endpoints immediately!

---

## 3. Reference Documentation
* [FastAPI Official Documentation](https://fastapi.tiangolo.com/)

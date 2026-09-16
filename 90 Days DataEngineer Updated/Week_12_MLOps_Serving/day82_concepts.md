# Day 82: Dockerizing Your API

"It works on my machine!" This is the most dreaded phrase in software engineering. A machine learning API that works perfectly on your Windows laptop might crash on a Linux production server due to different Python versions or missing dependencies. 

---

## 1. What is Docker?
Docker solves the "it works on my machine" problem by using **Containers**. A container packages up your code, your model file, your `requirements.txt`, and the exact operating system it needs to run, into a single, standardized box.

If a Docker container runs on your laptop, it is mathematically guaranteed to run exactly the same way on AWS, Google Cloud, or Azure.

---

## 2. Core Concepts & Operations

### The Dockerfile
A `Dockerfile` is a plain text file that contains the instructions for building your container image. 

Here is a standard, production-ready `Dockerfile` for a FastAPI application:

```dockerfile
# 1. Start from an official, lightweight Python image
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy just the requirements file first (for efficient caching)
COPY requirements.txt .

# 4. Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of your application code and model files into the container
COPY . .

# 6. Expose the port the app runs on
EXPOSE 8000

# 7. Define the command to run the FastAPI app using Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Basic Docker Commands
Assuming you have Docker installed on your computer, you build and run the image using the terminal:

```bash
# Build the image and tag it as 'my-ml-api'
# (The '.' means look for the Dockerfile in the current directory)
docker build -t my-ml-api .

# Run the container
# Map port 8000 on your local machine to port 8000 inside the container
docker run -p 8000:8000 my-ml-api
```
Once it's running, you can go to `http://localhost:8000/docs` to see your live API!

---

## 3. Reference Documentation
* [Dockerizing a Python Application](https://docs.docker.com/language/python/build-images/)
* [FastAPI in Containers](https://fastapi.tiangolo.com/deployment/docker/)
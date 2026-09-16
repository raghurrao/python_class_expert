# Write a simple text string representing a Dockerfile
# to serve a FastAPI app on port 8000.

DOCKERFILE_TEMPLATE = """
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "day79_assignment:app", "--host", "0.0.0.0", "--port", "8000"]
"""
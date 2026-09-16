FROM python:3.9-slim

WORKDIR /app

# Copy requirements from root or local setup
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run data generator and training script to produce the model file before startup
RUN python generate_data.py
RUN python -c "import pandas as pd; df = pd.read_csv('customer_churn.csv'); import day87_training; day87_training.train_and_serialize_best_model(df)"

EXPOSE 8000

CMD ["uvicorn", "day88_app:app", "--host", "0.0.0.0", "--port", "8000"]
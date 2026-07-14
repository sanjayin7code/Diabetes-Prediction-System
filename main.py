from fastapi import FastAPI
from schema import DiabetesInput
from predict import predict_diabetes

app = FastAPI(
    title="Diabetes Prediction API",
    description="Machine Learning API for Diabetes Prediction",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to Diabetes Prediction API",
        "status": "Running"
    }


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


@app.post("/predict")
def predict(data: DiabetesInput):
    result = predict_diabetes(data)
    return result
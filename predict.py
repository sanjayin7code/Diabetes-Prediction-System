import joblib
import numpy as np
from pathlib import Path

MODEL_PATH = Path(__file__).parent / "model" / "diabetes_model.joblib"
model = joblib.load(MODEL_PATH)


def predict_diabetes(data):

    # Gender Encoding
    gender_male = 1 if data.gender == "Male" else 0
    gender_other = 1 if data.gender == "Other" else 0

    # Smoking History Encoding
    smoking_current = 1 if data.smoking_history == "current" else 0
    smoking_ever = 1 if data.smoking_history == "ever" else 0
    smoking_former = 1 if data.smoking_history == "former" else 0
    smoking_never = 1 if data.smoking_history == "never" else 0
    smoking_not_current = 1 if data.smoking_history == "not current" else 0

    input_data = np.array([[
        data.age,
        data.hypertension,
        data.heart_disease,
        data.bmi,
        data.HbA1c_level,
        data.blood_glucose_level,
        gender_male,
        gender_other,
        smoking_current,
        smoking_ever,
        smoking_former,
        smoking_never,
        smoking_not_current
    ]])

    prediction = model.predict(input_data)[0]

    result = (
        "Diabetes Detected"
        if prediction == 1
        else "No Diabetes Detected"
    )

    confidence = None
    if hasattr(model, "predict_proba"):
        probability = model.predict_proba(input_data)[0]
        confidence = round(max(probability) * 100, 2)

    return {
        "prediction": result,
        "confidence": confidence
    }
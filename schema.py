from pydantic import BaseModel, Field
from typing import Literal


class DiabetesInput(BaseModel):
    gender: Literal["Female", "Male", "Other"]

    age: int = Field(..., ge=1, le=120)

    hypertension: int = Field(..., ge=0, le=1)

    heart_disease: int = Field(..., ge=0, le=1)

    smoking_history: Literal[
        "never",
        "former",
        "current",
        "ever",
        "not current"
    ]

    bmi: float = Field(..., gt=0)

    HbA1c_level: float = Field(..., gt=0)

    blood_glucose_level: int = Field(..., gt=0)
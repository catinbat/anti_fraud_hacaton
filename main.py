# -*- coding: utf-8 -*-
"""
Created on Mon May 12 11:40:42 2025

@author: Admin
"""
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Загрузка модели
model = joblib.load("catboost_final_model.joblib")

# Определение API и входных данных
app = FastAPI(title="CatBoost Classifier API")

class InputData(BaseModel):
    mean_percent_of_ordered_items: float
    DaysAfterRegistration: int
    count_items: int
    NmAge: int
    avg_unique_purchase: float

@app.post("/predict")
def predict(data: InputData):
    # Формируем массив признаков
    features = np.array([[
        data.mean_percent_of_ordered_items,
        data.DaysAfterRegistration,
        data.count_items,
        data.NmAge,
        data.avg_unique_purchase
    ]])

    # Предсказание
    prediction = model.predict(features)[0]
    proba = model.predict_proba(features)[0][1]

    return {
        "prediction": int(prediction),
        "probability": round(float(proba), 4)
    }

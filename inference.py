import joblib
import numpy as np
import pandas as pd

def load_model(model_name="xgb"):
    model = joblib.load(f"models/{model_name}.pkl")
    scaler = joblib.load("models/scaler.pkl")
    return model, scaler

def predict_price(model, scaler, input_dict: dict):
    df = pd.DataFrame([input_dict])
    df = pd.get_dummies(df)

    # 기존 훈련 컬럼 맞추기
    missing_cols = set(scaler.feature_names_in_) - set(df.columns)
    for c in missing_cols:
        df[c] = 0

    df = df[scaler.feature_names_in_]

    X_scaled = scaler.transform(df)
    pred = model.predict(X_scaled)[0]
    return pred

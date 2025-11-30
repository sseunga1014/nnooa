import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

from preprocess import load_data, preprocess

def evaluate(y_true, y_pred):
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    mae = mean_absolute_error(y_true, y_pred)
    return rmse, mae

def main():
    df = load_data("data/train.csv")
    X, y, scaler, columns = preprocess(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {
        "linear": LinearRegression(),
        "rf": RandomForestRegressor(n_estimators=200),
        "xgb": XGBRegressor(n_estimators=300, learning_rate=0.05)
    }

    for name, model in models.items():
        print(f"Training {name}...")
        model.fit(X_train, y_train)
        pred = model.predict(X_test)
        
        rmse, mae = evaluate(y_test, pred)
        print(f"{name} → RMSE: {rmse:.3f}, MAE: {mae:.3f}")

        # 모델 저장
        joblib.dump(model, f"models/{name}.pkl")

    # 스케일러 저장
    joblib.dump(scaler, "models/scaler.pkl")

if __name__ == "__main__":
    main()

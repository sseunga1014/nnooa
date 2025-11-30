import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(path: str):
    df = pd.read_csv(path)
    return df

def preprocess(df):
    # 숫자형 결측치 평균 대체
    df = df.fillna(df.mean(numeric_only=True))

    # 타깃 변수
    y = df['SalePrice']
    X = df.drop(['SalePrice'], axis=1)

    # 범주형 → 원핫인코딩
    X = pd.get_dummies(X, drop_first=True)

    # 스케일링
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X_scaled, y, scaler, X.columns

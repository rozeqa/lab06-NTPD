import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def train_and_predict():
    X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
    y = np.array([2, 4, 6, 8, 10, 12, 14, 16])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    model = LinearRegression()
    model.fit(X_train, y_train)

    preds = model.predict(X_test)

    return preds, y_test

def get_accuracy():
    preds, y_test = train_and_predict()
    return r2_score(y_test, preds)
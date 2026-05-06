import pytest
import numpy as np
from main import model

def test_predictions_not_none():
    """Test 1: Sprawdza, czy otrzymujemy jakąkolwiek predykcję[cite: 61]."""
    prediction = model.predict([[10.0]])
    assert prediction is not None, "Predykcja nie powinna być None[cite: 64]."

def test_predictions_length():
    """Test 2: Sprawdza, czy długość listy predykcji odpowiada liczbie próbek[cite: 67]."""
    input_data = [[1.0], [2.0], [3.0]]
    preds = model.predict(input_data)
    assert len(preds) == len(input_data), "Liczba predykcji musi być zgodna z liczbą próbek wejściowych."

def test_predictions_value_range():
    """Test 3: Sprawdza, czy wartości predykcji są sensowne dla regresji liniowej y=2x[cite: 72]."""
    test_val = 5.0
    prediction = model.predict([[test_val]])[0]
    # Sprawdzamy czy wynik jest blisko spodziewanego 10.0 (z tolerancją błędu)
    assert np.isclose(prediction, 10.0, atol=0.1), f"Błędna predykcja: {prediction} zamiast ~10.0"

def test_model_accuracy():
    """Test 4: Sprawdza, czy współczynnik modelu jest poprawny (zamiast accuracy dla regresji)[cite: 77]."""
    # W Twoim modelu y=2x, więc współczynnik (coef) powinien wynosić 2
    coef = model.coef_[0]
    assert np.isclose(coef, 2.0), f"Model nie nauczył się poprawnie trendu. Coef: {coef}"
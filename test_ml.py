import pytest
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import OneHotEncoder, LabelBinarizer
from ml.model import train_model, compute_model_metrics
from ml.data import apply_label


def test_train_model_returns_rf():
    """
    Test if the train_model function returns a RandomForestClassifier.
    """
    X_train = np.array([[1, 2], [3, 4]])
    y_train = np.array([0, 1])
    model = train_model(X_train, y_train)
    assert isinstance(model, RandomForestClassifier), "Expected model to be a RandomForestClassifier"


def test_compute_model_metrics_returns_correct_values():
    """
    Test if the compute_model_metrics function returns correct values.
    """
    y = np.array([0, 1, 1, 0])
    preds = np.array([0, 0, 1, 1])
    precision, recall, fbeta = compute_model_metrics(y, preds)
    assert precision == 0.5, "Expected precision to be 0.5"
    assert recall == 0.5, "Expected recall to be 0.5"
    assert fbeta == 0.5, "Expected fbeta to be 0.5"


def test_apply_label():
    """
    Test if the apply_label function returns correct labels.
    """
    assert apply_label([1]) == ">50K", "Expected label to be '>50K'"
    assert apply_label([0]) == "<=50K", "Expected label to be '<=50K'"

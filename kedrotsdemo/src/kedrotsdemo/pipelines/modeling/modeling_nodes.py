import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import pickle

def extract_single_series(df: pd.DataFrame) -> pd.Series:
    """Extract a single time series channel for modeling."""
    return df["channel_1"]

def train_forecasting_model(series: pd.Series) -> bytes:
    """Train a simple ARIMA model and return serialized model."""
    model = ARIMA(series, order=(1, 1, 1))
    fitted_model = model.fit()
    return pickle.dumps(fitted_model)

def forecast_from_model(model_bytes: bytes, steps: int = 10) -> pd.Series:
    """Forecast using the serialized model."""
    model = pickle.loads(model_bytes)
    forecast = model.forecast(steps=steps)
    return forecast

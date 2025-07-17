import pandas as pd
from your_project.pipelines.modeling import nodes as modeling_nodes

def test_extract_single_series():
    df = pd.DataFrame({"channel_1": [1, 2, 3], "channel_2": [4, 5, 6]})
    series = modeling_nodes.extract_single_series(df)
    assert isinstance(series, pd.Series)

def test_train_and_forecast_model():
    series = pd.Series([1, 2, 3, 4, 5])
    model_bytes = modeling_nodes.train_forecasting_model(series)
    forecast = modeling_nodes.forecast_from_model(model_bytes, steps=3)
    assert len(forecast) == 3

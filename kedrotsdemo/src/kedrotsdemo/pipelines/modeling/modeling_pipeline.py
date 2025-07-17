from kedro.pipeline import Pipeline, node, pipeline
from ..data_science.nodes import extract_single_series, train_forecasting_model, forecast_from_model

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=extract_single_series,
            inputs="time_series_cleaned",
            outputs="single_series",
            name="extract_series_node",
        ),
        node(
            func=train_forecasting_model,
            inputs="single_series",
            outputs="model_bytes",
            name="train_model_node",
        ),
        node(
            func=forecast_from_model,
            inputs="model_bytes",
            outputs="forecast_result",
            name="forecast_node",
        ),
    ])

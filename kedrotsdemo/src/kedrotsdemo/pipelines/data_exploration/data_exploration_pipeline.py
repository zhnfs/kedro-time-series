from kedro.pipeline import Pipeline, node, pipeline
from .nodes import load_and_describe_data, plot_time_series

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=load_and_describe_data,
            inputs="time_series_raw",
            outputs="time_series_cleaned",
            name="describe_data_node",
        ),
        node(
            func=plot_time_series,
            inputs="time_series_cleaned",
            outputs=None,
            name="plot_data_node",
        ),
    ])

import pandas as pd
from your_project.pipelines.data_exploration import nodes as eda_nodes

def test_load_and_describe_data():
    df = pd.DataFrame({"channel_1": [1, 2, 3], "channel_2": [4, 5, 6]})
    result = eda_nodes.load_and_describe_data(df)
    assert result.equals(df)

def test_plot_time_series(tmp_path):
    df = pd.DataFrame({"channel_1": [1, 2, 3], "channel_2": [3, 2, 1]})
    eda_nodes.plot_time_series(df)

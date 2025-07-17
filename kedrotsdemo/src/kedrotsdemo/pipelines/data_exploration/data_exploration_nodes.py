import logging
import pandas as pd
import matplotlib.pyplot as plt

logger = logging.getLogger(__name__)

def load_and_describe_data(df: pd.DataFrame) -> pd.DataFrame:
    """Logs basic data statistics and returns unchanged dataframe."""
    logger.info("Head of data:\n%s", df.head())
    logger.info("Data description:\n%s", df.describe())
    logger.info("Missing values:\n%s", df.isnull().sum())
    return df

def plot_time_series(df: pd.DataFrame) -> None:
    """Plots all time series channels."""
    plt.figure(figsize=(12, 6))
    for column in df.columns:
        plt.plot(df[column], label=column)
    plt.legend()
    plt.title("Time Series Channels")
    plt.xlabel("Time")
    plt.ylabel("Value")
    plt.grid()
    plt.tight_layout()
    plt.savefig("data/08_reporting/time_series_overview.png")

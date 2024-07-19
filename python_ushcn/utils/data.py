""""Functions for loading and preparing datasets."""

from pathlib import Path

import pandas as pd


daily_parquet_file_path = Path("/Users/richardlyon/ushcn-daily-2024-07-18.parquet")

monthly_parquet_file_path = Path("/Users/richardlyon/ushcn-monthly-2024-07-18.parquet")

stations_parquet_file_path = Path(
    "/Users/richardlyon/ghcnd-stations-2024-07-18.parquet"
)


def daily() -> pd.DataFrame:
    """Load the daily DataFrame from the parquet file."""
    df = pd.read_parquet(daily_parquet_file_path)
    df["date"] = pd.to_datetime(df["date"])

    return df


def monthly() -> pd.DataFrame:
    """Load the monthly DataFrame from the parquet file."""
    return pd.read_parquet(monthly_parquet_file_path)


def stations() -> pd.DataFrame:
    """Load the stations DataFrame from the parquet file."""
    df = pd.read_parquet(stations_parquet_file_path)
    df["station_id"] = (
        df["country_code"] + df["network_code"] + df["id_placeholder"] + df["coop_id"]
    ).str.upper()

    return df


def daily_tmax() -> pd.DataFrame:
    """Return a DataFrame containing the maximum daily temperature for each month.
    We clean the data by removing temperature readings over 60C, which are spuriously high.
    """
    df = pd.read_parquet(
        daily_parquet_file_path,
        columns=["date", "id", "tmax"],
        filters=[("tmax", "<=", 60.0)],
    )
    df["date"] = pd.to_datetime(df["date"])

    return df


def monthly_max_raw() -> pd.DataFrame:
    """Return a DataFrame containing the maximum monthly temperature for each station."""
    return pd.read_parquet(
        monthly_parquet_file_path,
        columns=["date", "id", "max_raw"],
        # filters=[("tmax", "<=", 60.0)],
    )

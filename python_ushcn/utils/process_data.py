"""
process_data.py

This module contains functions to process the USHCN data files and produce a Pandas DataFrame of the data.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List

import pandas as pd
from pandas import DataFrame

from python_ushcn import data_dir


@dataclass
class Measurement:
    value: float
    dm_flag: str
    qc_flag: str
    ds_flag: str

    @classmethod
    def from_string(cls, s: str):
        value_str = s[0:5].strip()
        if value_str == "-9999" or value_str == "":
            value = None
        else:
            value = float(value_str.strip()) / 100.0

        dm_flag = s[5] if len(s) > 5 and s[5].strip() else None
        qc_flag = s[6] if len(s) > 6 and s[6].strip() else None
        ds_flag = s[7] if len(s) > 7 and s[7].strip() else None

        return cls(value, dm_flag, qc_flag, ds_flag)


@dataclass
class WeatherData:
    country_code: str
    network_code: str
    observer_id: str
    codes: str
    year: int
    values: list[Measurement]

    @classmethod
    def from_line(cls, line: str):
        country_code = line[0:2]
        network_code = line[2]
        observer_id = line[3:12]
        year = int(line[12:16])
        codes = line[5:11]
        raw_values = [line[i:i + 8] for i in range(17, 132, 9)]
        values = [Measurement.from_string(s) for s in raw_values][0:12]
        return cls(country_code, network_code, observer_id, codes, year, values)


def process_data(data_dir: Path, element: str, dataset: str) -> List[WeatherData]:
    """Processes the data files in the given directory and return a list of WeatherData objects."""

    data_records = []
    dir_path = data_dir / element / dataset
    if dir_path.is_dir():
        data_records = [
            WeatherData.from_line(line)
            for file_path in dir_path.iterdir()
            if file_path.is_file()
            for line in file_path.open()
        ]

    return data_records


def create_dataframe(weather_data_list: List[WeatherData]) -> DataFrame:
    """Creates a DataFrame from the given list of WeatherData objects.

    Columns are a multi-index of observer_id and month. Rows are years. Values are the temperature.
    """
    data_records = []

    for wd in weather_data_list:
        for m in wd.values:
            data_records.append(
                {
                    # "country_code": wd.country_code,
                    # "network_code": wd.network_code,
                    "observer_id": wd.observer_id,
                    "year": wd.year,
                    "value": m.value,
                    # "dm_flag": m.dm_flag,
                    # "qc_flag": m.qc_flag,
                    # "ds_flag": m.ds_flag,
                }
            )

    df = pd.DataFrame(data_records)
    df["month"] = df.groupby("year").cumcount() + 1
    df["year"] = pd.to_datetime(df["year"], format="%Y")
    pivot_df = df.pivot(index="year", columns=["observer_id", "month"], values="value")

    return pivot_df


def get_data(element: str, dataset: str) -> DataFrame:
    """Returns a DataFrame of the weather data for the given element and dataset."""

    weather_data_list = process_data(data_dir(), element, dataset)
    df = create_dataframe(weather_data_list)

    return df


if __name__ == "__main__":
    df = get_data("max", "tob")
    print(df.head(30))

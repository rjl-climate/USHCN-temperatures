"""
deserialise.py

Download and process USHCN daily data and persist to a SQLITE database.

Sources:
https://www.ncei.noaa.gov/pub/data/ghcn/daily/
https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd_hcn.tar.gz

Stations
https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt

"""

import tarfile
from dataclasses import dataclass
from typing import List
import pandas as pd
import sqlite3
from tqdm import tqdm

import requests

from python_ushcn import data_dir, database_path, get_dir


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
    id: str
    year: int
    month: int
    element: str
    values: list[Measurement]

    @classmethod
    def from_line(cls, line: str):
        id = line[0:11]
        year = int(line[11:15])
        month = int(line[15:17])
        element = line[17:21]
        raw_values = [line[i : i + 8] for i in range(21, 300, 8)]
        values = [
            Measurement.from_string(s)
            for s in raw_values
            if len(s) > 0 and element in ["TMAX", "TMIN"]
        ]

        return cls(id, year, month, element, values)


def download_and_extract():
    """Download the USHCN daily data and extract it to a temporary directory for processing."""

    print("Downloading USHCN daily data...")

    # Create the directories
    temp_data_dir_path = get_dir("temp", do_create=True)
    tar_file_path = data_dir() / "ghcn_daily.tar.gz"

    # Download the file
    url = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd_hcn.tar.gz"
    response = requests.get(url)

    # Save the file
    with open(tar_file_path, "wb") as file:
        file.write(response.content)

    # Extract the file
    with tarfile.open(tar_file_path, "r:gz") as tar:
        tar.extractall(path=temp_data_dir_path)

    # Delete the tar file
    tar_file_path.unlink()


def deserialise() -> List[WeatherData]:
    """Deserialise the USHCN daily data files and return a list of WeatherData objects."""

    print("Deserialising USHCN daily data...")

    temp_data_dir_path = get_dir("temp") / "ghcnd_hcn"
    data_records = []

    if temp_data_dir_path.is_dir():
        data_records = [
            WeatherData.from_line(line)
            for file_path in tqdm(
                list(temp_data_dir_path.iterdir()), desc="Processing files"
            )
            if file_path.is_file()
            for line in file_path.open()
        ]

    # if temp_data_dir_path.is_dir():
    #     data_records = []
    #     for file_path in temp_data_dir_path.iterdir():
    #         print(f"processing {file_path}")
    #         if file_path.is_file():
    #             with file_path.open() as file:
    #                 for line in file:
    #                     data_records.append(WeatherData.from_line(line))
    #             break

    return data_records


def create_dataframe(weather_data_list: List[WeatherData]) -> pd.DataFrame:
    """Creates a DataFrame from the given list of WeatherData objects."""

    data_records = []

    for wd in weather_data_list:
        for m in wd.values:
            data_records.append(
                {
                    "id": wd.id,
                    "year": wd.year,
                    "month": wd.month,
                    "element": wd.element,
                    "value": m.value,
                }
            )

    df = pd.DataFrame(data_records)

    # df["month"] = df.groupby("year").cumcount() + 1
    # df["year"] = pd.to_datetime(df["year"], format="%Y")
    # pivot_df = df.pivot(index="year", columns=["element", "month"], values=["value"])

    return df


def save_to_sqlite(df: pd.DataFrame):
    database_filename = database_path()
    conn = sqlite3.connect(database_filename)
    df.to_sql("daily", conn, if_exists="replace", index=False)
    conn.close()


def process(download: bool = False):
    if download:
        download_and_extract()

    weather_data_list = deserialise()
    df = create_dataframe(weather_data_list)
    save_to_sqlite(df)

    # TODO: delete temporary files

    print(df)


if __name__ == "__main__":
    process()

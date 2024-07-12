"""
process_stations.py

Download and process USHCN daily data and persist to a SQLITE database.

Stations
https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt
"""

import sqlite3
from dataclasses import dataclass

import requests
import pandas as pd

from python_ushcn import database_path


@dataclass
class Station:
    id: str
    latitude: float
    longitude: float
    elevation: float
    state: str
    name: str

    @classmethod
    def from_line(cls, line: str):
        id = line[0:11]
        latitude = float(line[12:20])
        longitude = float(line[21:30])
        elevation = float(line[31:37])
        state = line[38:40].strip() or None
        name = line[41:71]

        return cls(id, latitude, longitude, elevation, state, name)


def process_stations():

    print("Processing USHCN station data...")

    # Download the data
    url = "https://www.ncei.noaa.gov/pub/data/ghcn/daily/ghcnd-stations.txt"
    response = requests.get(url)

    # Process the lines
    stations = [
        Station.from_line(line.decode("utf-8")) for line in response.iter_lines()
    ]

    # Filter out non-US stations and generate a DataFrame
    station_list = [
        {
            "id": s.id,
            "latitude": s.latitude,
            "longitude": s.longitude,
            "elevation": s.elevation,
            "state": s.state,
            "name": s.name,
        }
        for s in stations
        if s.id.startswith("US")
    ]

    df = pd.DataFrame(station_list)

    # Save to the database
    database_filename = database_path()
    conn = sqlite3.connect(database_filename)
    df.to_sql("stations", conn, if_exists="replace", index=False)
    conn.close()

    print("Finished processing USHCN station data.")


if __name__ == "__main__":
    process_stations()

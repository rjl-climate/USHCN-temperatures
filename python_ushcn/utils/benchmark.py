""" Benchmarks to test loading times of the USHCN data. """

import timeit
from pathlib import Path

import pandas as pd

parquet_file_path = Path(
    "/Users/richardlyon/SynologyDrive/[01] Areas/[07] Hobbies/[04] Climate/ushcn-daily-2024-07-17.parquet"
)


def with_columns():
    df = pd.read_parquet(
        parquet_file_path,
        columns=["tmax", "date", "id"],
        filters=[("tmax", "<=", 60.0)],
    )


def dropping_columns():
    df = pd.read_parquet(parquet_file_path, filters=[("tmax", "<=", 60.0)])
    df = df.drop(columns=["tmin", "prcp"])


execution_time = timeit.timeit(
    "with_columns()", setup="from __main__ import with_columns", number=10
)
print(f"With columns: {execution_time} seconds")

execution_time = timeit.timeit(
    "dropping_columns()", setup="from __main__ import dropping_columns", number=10
)
print(f"Dropping columns: {execution_time} seconds")


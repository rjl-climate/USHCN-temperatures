"""Inspects the contents of the USHCN data files."""

import pandas as pd

from python_ushcn.utils.data import daily, monthly, stations

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)


df_daily = daily()
print(
    "\n== Daily data: ============================================================================================\n"
)
print(df_daily.info())
print()
print(df_daily.describe())
print()
print(df_daily.tail())

df_monthly = monthly()
print(
    "\n\n== Monthly data: ==========================================================================================\n"
)
print(df_monthly.info())
print()
print(df_monthly.describe())
print()
print(df_monthly.tail())


df_stations = stations()
print(
    "\n== Stations data: ==========================================================================================\n"
)
print(df_stations.info())
print()
print(df_stations.describe())
print()
print(df_stations.tail())

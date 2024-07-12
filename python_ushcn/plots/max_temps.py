"""
Plots the maximum temperature in each month for each year.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from python_ushcn import patch
from python_ushcn.utils.process_data import get_data


def get_dataframe() -> pd.DataFrame:
    """Return the data for the specified station."""
    WINDOW_SIZE = 10

    df = get_data("max", "fls52")
    df = df[df.index >= pd.to_datetime('1880-01-01')]

    df["max_temp"] = df.max(axis=1, skipna=True)
    df["max_avg"] = df["max_temp"].rolling(window=WINDOW_SIZE).mean().shift(-(WINDOW_SIZE - 1))

    return df


def plot(df: pd.DataFrame, outfile: Path):
    fig, ax = plt.subplots(figsize=(10, 10 * 9 / 16))

    ax.plot(df.index, df["max_temp"], label="Max Temp", color="tab:red", alpha=0.1)
    ax.plot(df.index, df["max_avg"], label="Max Temp", color="tab:red")
    ax.fill_between(df.index, df["max_temp"], df["max_avg"], color="tab:red", alpha=0.2)

    ax.set_title("US Historical Climate Network - Maximum Annual Temperature", loc="left", pad=20)
    ax.set_ylabel("Maximum Temperature (°C)")
    ax.set_ylim(0, 50)

    rect = patch(1880, 1915, "red")
    ax.add_patch(rect)

    rect = patch(1915, 1975, "green")
    ax.add_patch(rect)

    rect = patch(1975, 2000, "red")
    ax.add_patch(rect)

    rect = patch(2000, 2024, "green")
    ax.add_patch(rect)

    ax.annotate(
        "© Lyon Energy Futures Ltd. (2024)",
        (0, 0),
        (724, 535),
        xycoords="figure points",
        textcoords="offset pixels",
        va="top",
        color="grey",
    )

    ax.annotate(
        "Source: NOAA USHCN (2024) https://www.ncei.noaa.gov/products/land-based-station/us-historical-climatology-network",
        (0, 0),
        (90, 30),
        xycoords="figure points",
        textcoords="offset pixels",
        va="top",
        color="grey",
    )

    plt.savefig(outfile)

    plt.show()


if __name__ == "__main__":
    print("Running max_temps.py")

    plot_dir = Path("/Users/richardlyon/Desktop")
    file_name = "USHCN-max-temperatures-1880-2024.png"
    outfile = plot_dir / file_name

    df = get_dataframe()
    plot(df, outfile)
    print(f"Plot saved to '{outfile}'")

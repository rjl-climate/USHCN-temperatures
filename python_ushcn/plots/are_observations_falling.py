"""
Are the number of daily observations falling?

This script plots the number of daily observations recorded in the
USHCN to assess whether and how quickly they are falling.
"""

import os

from python_ushcn.utils.paths import image_path
from python_ushcn.utils.data import daily_tmax
import matplotlib.pyplot as plt

from python_ushcn.utils.plots import configure_plot


def do_plot():

    file_name = os.path.basename(__file__)

    df = daily_tmax()

    # Group by 'date' and count the number of reports for each day
    report_counts = df.groupby("date").size()

    # Drop the last rows, which are incomplete
    report_counts = report_counts.iloc[:-60]

    # Compute the rolling average
    df = report_counts.to_frame(name="counts")
    window_size = 360
    df["max_avg"] = (
        df["counts"].rolling(window=window_size).mean().shift(-(window_size - 1))
    )

    # Plotting

    title = "Daily observations\nare falling"
    subtitle = "Number of daily observations"

    fig, ax = configure_plot(title, subtitle)

    plt.plot(df.index, df["max_avg"], color="tab:red")
    plt.plot(df.index, df["counts"], color="grey", alpha=0.3)

    # Save
    image_path = image_path(file_name)
    plt.savefig(image_path)


if __name__ == "__main__":
    do_plot()

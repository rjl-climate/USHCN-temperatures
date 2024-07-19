"""
Is the number of very hot days increasing?

This script plots the number of days that maximum temperatures exceeds a
threshold in each year. We select stations that have data for the entire
period from 1900 to 2024 to exclude the effect of station closures on the
count.
"""

import os

from python_ushcn.utils.paths import image_path
from python_ushcn.utils.data import daily_tmax
import matplotlib.pyplot as plt

from python_ushcn.utils.plots import configure_plot

file_name = os.path.basename(__file__)

df = daily_tmax()

# Remove stations that do not have 100 years of data
# NOTE: Equates to about 32% of stations
report_counts = df.groupby("id").size()
report_counts_filtered = report_counts[report_counts >= 365 * 100]

# Filter the original DataFrame to only include stations with data for the required period
df = df[df["id"].isin(report_counts_filtered.index)]

max_temp_95 = 35
max_temp_100 = 37.8
max_temp_105 = 40.6

# Count the number of days that the maximum temperature exceeds the threshold for each year
df["count_95"] = df["tmax"] > max_temp_95
df["count_100"] = df["tmax"] > max_temp_100
df["count_105"] = df["tmax"] > max_temp_105

# Group by 'year' and sum the number of days that the maximum temperature exceeds the threshold
df["year"] = df["date"].dt.year
year_count = df.groupby("year").size()
counts_95 = 100 * df.groupby("year")["count_95"].sum() / year_count
counts_100 = 100 * df.groupby("year")["count_100"].sum() / year_count
counts_105 = 100 * df.groupby("year")["count_105"].sum() / year_count

# Convert to DataFrame and reset index for plotting
counts_95_df = counts_95.reset_index(name="count")
counts_100_df = counts_100.reset_index(name="count")
counts_105_df = counts_105.reset_index(name="count")

# Plotting

title = "The number of very hot days \nis not increasing"
subtitle = "U.S. observed number of very hot days"
axis_label = "Percent"
source = "Source: US Historical Climatology Network, https://www.ncei.noaa.gov/pub/data/ushcn/v2.5/"

fig, ax = configure_plot(title, subtitle, axis_label, source)

plt.plot(
    counts_95_df["year"],
    counts_95_df["count"],
    color="tab:blue",
    alpha=0.5,
    label="> 95F",
)
plt.fill_between(
    counts_95_df["year"],
    counts_95_df["count"],
    counts_100_df["count"],
    color="tab:blue",
    alpha=0.2,
)
plt.plot(
    counts_100_df["year"],
    counts_100_df["count"],
    color="tab:blue",
    alpha=0.7,
    label="> 100F",
)
plt.fill_between(
    counts_100_df["year"],
    counts_100_df["count"],
    counts_105_df["count"],
    color="tab:blue",
    alpha=0.5,
)
plt.plot(
    counts_105_df["year"],
    counts_105_df["count"],
    color="tab:blue",
    alpha=0.9,
    label="> 105F",
)
plt.fill_between(
    counts_105_df["year"],
    counts_105_df["count"],
    0,
    color="tab:blue",
    alpha=0.9,
)


plt.legend()

# Save
image_path = image_path(file_name)
plt.savefig(image_path)

"""Functions for formatting plots."""

import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Rectangle

default_source = "Source: US Historical Climatology Network, https://www.ncei.noaa.gov/pub/data/ushcn/v2.5/"


def configure_plot(
    title: str, subtitle: str, axis_label: str = "", source: str = default_source
):
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.subplots_adjust(top=0.65, left=0.075, right=0.99)

    fig_top = 0.95
    title_margin = 0.04
    subtitle_margin = 0.22
    y_axis_label_margin = 0.26

    # fancy red line
    fig_line_1 = Line2D(
        [0.03, fig_top],
        [fig_top, fig_top],
        transform=fig.transFigure,
        color="tab:red",
        linewidth=1,
    )
    rect = Rectangle(
        (0.03, fig_top),
        0.1,
        0.02,
        fill=True,
        color="tab:red",
        linewidth=1,
        transform=fig.transFigure,
        figure=fig,
    )
    fig.add_artist(fig_line_1)
    fig.add_artist(rect)

    # title
    fig.suptitle(
        title,
        fontsize=24,
        color="tab:red",
        fontweight="bold",
        x=0.03,
        y=(fig_top - title_margin),
        ha="left",
    )

    # subtitle
    fig.text(
        0.03,
        (fig_top - subtitle_margin),
        subtitle,
        fontsize=14,
        fontweight="bold",
        ha="left",
    )

    # units
    fig.text(0.03, (fig_top - y_axis_label_margin), axis_label, fontsize=14, ha="left")

    fig.text(0.03, 0.035, source, fontsize=10, color="grey", ha="left")
    fig.text(
        0.97,
        0.035,
        "Chart: Lyon Energy Futures Ltd.",
        fontsize=10,
        color="grey",
        ha="right",
    )

    for spine in ax.spines.values():
        spine.set_visible(False)

    return fig, ax

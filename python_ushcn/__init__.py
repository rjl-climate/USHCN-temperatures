from datetime import datetime
from pathlib import Path

import matplotlib
import matplotlib.dates as mdates


def data_dir() -> Path:
    """Return the path to the data directory."""
    project_root = Path(__file__).resolve().parent.parent

    return project_root / "data"


def get_dir(folder_name: str, do_create: bool = False):
    dir = data_dir() / folder_name
    if do_create:
        dir.mkdir(parents=True, exist_ok=True)

    return dir


def patch(start_year, end_year, colour):
    """Creates a plot patch for the specified years."""
    x_position = mdates.date2num(datetime(start_year, 6, 1))
    width = mdates.date2num(datetime(end_year, 7, 1)) - x_position
    face_colour = f"tab:{colour}"

    rect = matplotlib.patches.Rectangle(
        (x_position, 0),
        width,
        50,
        linewidth=1,
        edgecolor=colour,
        facecolor=face_colour,
        alpha=0.1,
    )

    return rect


def database_path() -> Path:
    """Return the path to the SQLite database."""
    data_dir_path = get_dir("daily", do_create=True)
    database_filename = data_dir_path / "ghcnd.sqlite"

    return database_filename

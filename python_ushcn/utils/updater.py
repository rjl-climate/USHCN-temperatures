"""
updater.py

This module updates the USHCN data files from the NOAA FTP server.
"""
import os
import tarfile

import requests

from python_ushcn import data_dir


def url_from_parts(element: str, dataset: str) -> str:
    """Return the file name from the element and dataset."""

    element_map = {
        "max": "tmax",
        "min": "tmin",
        "avg": "tavg",
    }
    dataset_map = {
        "fls52": "FLs.52j",
        "raw": "raw",
        "tob": "tob",
    }
    element = element_map[element]
    dataset = dataset_map[dataset]

    root = "https://www.ncei.noaa.gov/pub/data/ushcn/v2.5"
    file_name = f"ushcn.{element}.latest.{dataset}.tar.gz"

    return f"{root}/{file_name}"


def download_file(element: str, dataset: str):
    """Download the file from the given URL to the destination."""

    # Source url
    url = url_from_parts(element, dataset)

    # Destination path
    dir_path = data_dir() / element / dataset
    dir_path.mkdir(parents=True, exist_ok=True)
    file_name = url.split("/")[-1]
    file_path = dir_path / file_name

    # Download the file
    response = requests.get(url)

    # Save the file
    with open(file_path, "wb") as file:
        file.write(response.content)

    # Extract the file
    with tarfile.open(file_path, 'r:gz') as tar:
        for member in tar.getmembers():
            member.name = os.path.basename(member.name)  # Modify the member's name to only its basename
            if member.name:  # Check if the member's name is not empty
                tar.extract(member, path=dir_path)

    os.remove(file_path)


def update_data():
    """Update the USHCN data files from the NOAA FTP server."""

    for element in ["max", "min", "avg"]:
        for dataset in ["fls52", "raw", "tob"]:
            print(f"Downloading {element} {dataset}...")
            download_file(element, dataset)


if __name__ == "__main__":
    update_data()

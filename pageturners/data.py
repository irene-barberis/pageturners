# DATA LOADING AND DOWNLOAD
# Download missing datasets and load CSV files from the raw data folder
# The filename is provided as an argument to make the function reusable

import os

import pandas as pd
import requests

BASE_URL = "https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/"
RAW_DATA_DIR = "data/raw (dati_grezzi)"


def download_file(url, path):
    """Download a file from the web unless it already exists locally."""

    if os.path.exists(path):
        return

    response = requests.get(url, timeout=30)
    response.raise_for_status()

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "wb") as f:
        f.write(response.content)


def load_dataset(filename):
    """
    Load a Goodbooks-10k CSV file, downloading it if it is not
    already available in the raw data folder.

    Parameters
    ----------
    filename : str
        Name of the CSV file to load.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the data loaded from the CSV file.
    """

    url = BASE_URL + filename
    path = os.path.join(RAW_DATA_DIR, filename)

    download_file(url, path)

    return pd.read_csv(path)

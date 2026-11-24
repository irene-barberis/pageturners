# DATA LOADING
# Load a CSV dataset from the raw data folder
# The filename is provided as an argument to make the function reusable

import pandas as pd


def load_dataset(filename):
    """
    Load a CSV file from the Goodbooks-10k raw data folder.

    Parameters
    ----------
    filename : str
        Name of the CSV file to load.

    Returns
    -------
    pandas.DataFrame
        DataFrame containing the data loaded from the CSV file.
    """

    return pd.read_csv("data/raw (dati_grezzi)/" + filename)

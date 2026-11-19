"""Functions for loading the Goodbooks-10k datasets."""

import pandas as pd

def load_dataset(filename):
    """Load a CSV file from the raw data folder."""
    return pd.read_csv("data/raw (dati_grezzi)/" + filename)


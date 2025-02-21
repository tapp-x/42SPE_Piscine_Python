import pandas as pd
import os


def load(path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.
    Parameters:
    path (str): The path to the CSV file.
    """
    try:
        assert path.lower().endswith("csv"), "Only CSV files are supported."
        if not os.path.exists(path):
            raise AssertionError("File not found:", path)
        if os.path.getsize(path) == 0:
            raise AssertionError("File is empty:", path)
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions \
({dataset.shape[0]}, {dataset.shape[1]})")
        return dataset

    except AssertionError as error:
        print(f"AssertionError: {error}")
        return ""

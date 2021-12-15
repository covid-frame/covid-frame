import pandas as pd


def load_database(filename):

    return pd.read_csv(filename)


def load_database_from_hdf(filename):

    return pd.read_hdf(filename)

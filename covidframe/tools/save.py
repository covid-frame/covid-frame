import pickle
from pathlib import Path
from covidframe.tools.pickle_prot import pickle_protocol


def save_databases_info(info, filename):

    filename = Path(filename)
    filename.parent.mkdir(parents=True, exist_ok=True)

    with open(filename, 'ab') as f:
        pickle.dump(info, f)


def save_database(df, filename, sep=',', header=True):

    filename = Path(filename)
    filename.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(filename, index=False, sep=sep, header=header)


def save_database_to_hdf(df, filename):

    filename = Path(filename)
    filename.parent.mkdir(parents=True, exist_ok=True)
    with pickle_protocol(4):
        df.to_hdf(filename, "df", mode='w')


def save_database_to_feather(df, filename):

    filename = Path(filename)
    filename.parent.mkdir(parents=True, exist_ok=True)
    df.to_feather(filename)

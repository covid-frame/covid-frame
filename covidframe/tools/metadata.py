import pandas as pd
from pathlib import Path


def get_db_from_file(file, encoding=None):

    file = Path(file)

    if file.suffix in [".xls", ".xlsx"]:
        return pd.read_excel(file)

    if encoding is not None:
        return pd.read_csv(file, encoding=encoding)
    return pd.read_csv(file)


def get_list_columns(df):
    return df.columns


def get_categories(df, category_column):

    return df[category_column].unique()


def select_values_list(df, column, lst):

    return df[df[column].isin(lst)]


if __name__ == "__main__":

    from covidframe.database.load import load_paths
    from covidframe import config

    base_path = "/mnt/Archivos/dataset-xray"
    databases = [database for database in config.databases
                 if database["type"] == "metadata"]

    for database in databases:
        print(database)
        paths = load_paths(database, base_path)
        metadata_file = database["type_own"]["metadata_file"]
        metadata_path = paths["db_path"] / metadata_file

        if "file_encoding" in database["type_own"]:
            file_encoding = database["type_own"]["file_encoding"]
        else:
            file_encoding = "utf-8"
        df = get_db_from_file(metadata_path, file_encoding)
        columns = get_list_columns(df)
        print(columns)

    databases = [database for database in config.databases
                 if database["type"] == "folders-metadata"]

    for database in databases:
        print(database)
        paths = load_paths(database, base_path)

        for _, metadata_file in database["type_own"]["metadata_files"].items():

            metadata_path = paths["db_path"] / metadata_file
            if "file_encoding" in database["type_own"]:
                file_encoding = database["type_own"]["file_encoding"]
            else:
                file_encoding = "utf-8"
            df = get_db_from_file(metadata_path, file_encoding)

            columns = get_list_columns(df)
            print(columns)

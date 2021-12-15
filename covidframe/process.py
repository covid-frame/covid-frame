from covidframe.integrate import load_databases, generate_hashes, \
    generate_clean_database
from covidframe.tools.save import save_database, save_databases_info
from covidframe.tools.path import build_file_name
from covidframe.database.build import copy_files
from pathlib import Path
from covidframe.database.resample import resample_database_to_min
from covidframe.database.split import split_database


DEFAULT_DATABASE_INFO_FILE = "info_databases"
DEFAULT_DATABASE_CLEAN_FILE = "database_clean.csv"
DEFAULT_DATABASE_NAME_CLEAN = "database_clean"
DEFAULT_DATABASE_NAME_BALANCED = "database_clean_balanced"
DEFAULT_SUFFIX = "metadata"
DEFAULT_METADATA_EXT = ".metadata.csv"
DEFAULT_EXT = ".csv"


def consolidate_databases(list_database_info, base_path=None,
                          output_folder=None,
                          filename=None,
                          parallel=False,
                          n_jobs=-1):

    info_databases = load_databases(list_database_info, base_path=base_path)

    info_databases = generate_hashes(info_databases, parallel=parallel,
                                     n_jobs=n_jobs)

    if filename is None:
        filename = DEFAULT_DATABASE_INFO_FILE

    filename_path = Path(output_folder).resolve() / filename
    save_databases_info(info_databases, filename_path)

    return info_databases


def generate_database(info_databases=None,
                      output_folder=None,
                      output_file=None):

    df = generate_clean_database(info_databases)

    if output_file is None:
        output_file = DEFAULT_DATABASE_CLEAN_FILE

    output_path = Path(output_folder).resolve() / output_file
    save_database(df, output_path)

    return df


def generate_database_files(df, output_folder=None, output_name=None,
                            suffix=None):

    if output_name is None:
        output_name = DEFAULT_DATABASE_NAME_CLEAN

    output_folder = Path(output_folder)
    dir_images = output_folder / output_name
    dir_images.mkdir(parents=True, exist_ok=True)
    n_df = copy_files(
        df,
        "image_path",
        "image_name",
        "folder_name",
        dir_images)

    if suffix is None:
        suffix = DEFAULT_SUFFIX

    output_file_name = build_file_name(output_name, DEFAULT_METADATA_EXT)

    output_file_path = output_folder / output_file_name
    save_database(n_df, output_file_path)

    return n_df


def balance_database(df, output_folder, output_file_name=None):

    n_df = resample_database_to_min(df, "category")

    if output_file_name is None:
        output_file_name = build_file_name(DEFAULT_DATABASE_NAME_BALANCED,
                                           DEFAULT_METADATA_EXT)

    output_file_path = Path(output_folder).resolve() / output_file_name
    save_database(n_df, output_file_path)

    return n_df


def get_train_test_database(
        df,
        output_folder,
        test_size=0.2,
        base_file_name=None):

    df_train, df_test = split_database(df, "category", test_size=test_size)

    if base_file_name is None:
        base_file_name = DEFAULT_DATABASE_NAME_BALANCED

    output_folder = Path(output_folder).resolve()
    train_file_path = output_folder / \
        build_file_name(base_file_name, DEFAULT_METADATA_EXT, suffix="train")

    test_file_path = output_folder / \
        build_file_name(base_file_name, DEFAULT_METADATA_EXT, suffix="test")

    save_database(df_train, train_file_path)
    save_database(df_test, test_file_path)

    return df_train, df_test

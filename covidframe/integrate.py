
from covidframe.database.load import load_files_list
from covidframe.database.hash import drop_duplicated_hashes, add_hash_to_df

from covidframe.tools.image import load_image, resize_image, \
    to_equal_aspect_ratio

import pandas as pd


def load_databases(list_database_info, base_path=None):

    info_databases = []

    for database_info in list_database_info:
        info = load_files_list(database_info, base_path)

        info_databases.append(info)

    return info_databases


def generate_hashes(info_databases, parallel=False, n_jobs=-1):

    for info_database in info_databases:
        info_database["info"] = add_hash_to_df(info_database["info"],
                                               parallel=parallel,
                                               n_jobs=n_jobs)

    return info_databases


def drop_duplicates_from_databases(info_databases):

    for info_database in info_databases:
        info_database["info"] = drop_duplicated_hashes(info_database["info"])

    return info_databases


def group_databases(info_databases):

    df_info = [info_database["info"] for info_database in info_databases]
    df = pd.concat(df_info, ignore_index=True)

    return df


def generate_clean_database(info_databases):

    info_databases = drop_duplicates_from_databases(info_databases)

    df = group_databases(info_databases)
    df = drop_duplicated_hashes(df)

    return df


def load_images_in_df(df, column_image_path="image_path",
                      column_vector="vector"):

    n_df = df.copy()
    n_df[column_vector] = df[column_image_path].apply(load_image)

    return n_df


def describe_images_in_df(df, column_vector="vector"):

    n_df = df.copy()
    n_df["size"] = n_df[column_vector].apply(lambda x: x.shape)
    n_df["is_squared"] = n_df["size"].apply(lambda x: x[0] == x[1])
    n_df['aspect_ratio'] = n_df["size"].apply(lambda x: x[1] / x[0])

    return n_df


def resize_images_in_df(df, new_size, column_vector="vector",
                        column_resized="resized",
                        describe=True):

    n_df = df.copy()
    n_df[column_resized] = n_df[column_vector].apply(
        lambda x: resize_image(to_equal_aspect_ratio(x), new_size))

    if describe:
        n_df["new_size"] = n_df[column_resized].apply(lambda x: x.shape)

    return n_df


def process_images_in_df(df, new_size, describe=True):

    print("Loading images into dataframe")
    n_df = load_images_in_df(df)

    if describe:
        print("Describing images")
        n_df = describe_images_in_df(n_df)

    print("Resizing images in dataframe")
    n_df = resize_images_in_df(n_df, new_size)

    return n_df

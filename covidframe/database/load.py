from covidframe import config
from covidframe.tools import metadata

from pathlib import Path
import numpy as np
import pandas as pd


def load_files_list(database_info, base_path=None):

    database_type = database_info["type"]

    if database_type not in config.database_types:
        raise Exception("Database type not in the config file")

    paths = load_paths(database_info, base_path)
    print(paths)

    all_files = paths["image_path"].rglob("*")
    files = [f for f in all_files if
             f.name.endswith(tuple(config.image_extensions))]

    files = np.array(files, dtype=object)
    df = None
    if database_info["type"] == "metadata":
        df = clean_metadata_files(database_info, base_path=base_path)
        print(len(df))

        filenames_df = df[database_info["type_own"]["column_file_names"]]

        include_suffix = True
        if "include_suffix" in database_info["type_own"]:
            include_suffix = database_info["type_own"]["include_suffix"]

        if include_suffix:
            filenames = np.array([f.name for f in files], dtype=object)
        else:
            filenames = np.array([f.stem for f in files], dtype=object)

        files = files[np.isin(filenames, list(filenames_df))]

    n_df = generate_metadata(database_info, files, df)
    return {
        "original": df,
        "info": n_df
    }


def load_paths(database_info, base_path=None):

    if base_path is None:
        base_path = config.paths["datasets_base_path"]
    base_path = Path(base_path).resolve()
    db_path = base_path / database_info["folder_name"]
    image_path = db_path / database_info["image_relative_path"]

    return {
        "base_path": base_path,
        "db_path": db_path,
        "image_path": image_path
    }


def clean_metadata_files(database_info, base_path=None):

    paths = load_paths(database_info, base_path=base_path)
    metadata_file = paths["db_path"] / \
        database_info["type_own"]["metadata_file"]

    if "file_encoding" in database_info["type_own"]:
        file_encoding = database_info["type_own"]["file_encoding"]
    else:
        file_encoding = "utf-8"

    df = metadata.get_db_from_file(metadata_file, file_encoding)

    print(f"Metadata original size: {len(df)}")

    if "selection" in database_info["type_own"].keys():
        criteria_list = database_info["type_own"]["selection"]

        print("Selection key present")
        if len(criteria_list) > 0:
            for criteria in criteria_list:
                column = criteria["column"]
                values = criteria["values"]
                print(f"Select {column} with values: {values}")
                df = metadata.select_values_list(df,
                                                 column,
                                                 values)

    category_column = database_info["type_own"]["column_category"]
    allowed_categories = list(database_info["type_own"]["mappings"].keys())

    print(f"Selecting in {category_column}, the allowed categories"
          f"{allowed_categories}")

    df = metadata.select_values_list(
        df,
        category_column,
        allowed_categories)

    return df


def generate_metadata(database_info, files, original_metadata=None):

    file_names = [f.name for f in files]
    d = {"image_path": files, "image_name": file_names}
    df = pd.DataFrame(data=d)

    if original_metadata is not None:
        column_file_names = database_info["type_own"]["column_file_names"]
        column_category = database_info["type_own"]["column_category"]
        column_id = database_info["type_own"]["column_id"]

        n_df = df.join(original_metadata
                       .set_index(column_file_names)[[column_category,
                                                      column_id]],
                       on="image_name", how="left")

        mappings = database_info["type_own"]["mappings"]
        n_df["category"] = n_df[column_category].map(mappings)
        n_df.rename(columns={column_id: "id", column_category:
                             "original_category"}, inplace=True)

    else:
        parent_names = [f.parents[0].parts[-1] for f in files]
        image_no_suffix = [f.stem for f in files]
        n_df = df.copy()
        n_df["original_category"] = parent_names
        n_df["id"] = image_no_suffix

        mappings = database_info["type_own"]["mappings"]
        n_df["category"] = n_df["original_category"].map(mappings)

    n_df["type"] = database_info["type"]
    n_df["source"] = database_info["source"]
    n_df["folder_name"] = database_info["folder_name"]
    return n_df


if __name__ == "__main__":

    metadata_db = config.databases[4]

    base_path = "/mnt/Archivos/dataset-xray"
    info = load_files_list(metadata_db, base_path)
    print(len(info["info"]))

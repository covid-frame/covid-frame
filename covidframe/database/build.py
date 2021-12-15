from pathlib import Path

from covidframe.tools.path import append_prefix_to_path

from shutil import copy2


def copy_files(df, column_image_path,
               column_image_name,
               column_folder_name,
               output_folder):

    image_paths = df[column_image_path]
    folder_name = df[column_folder_name]

    new_image_paths = []
    for path, prefix in zip(image_paths, folder_name):
        new_path = append_prefix_to_path(path, prefix,
                                         parent_path=output_folder)
        new_image_paths.append(new_path)

    for source, dest in zip(image_paths, new_image_paths):
        copy2(source, dest)

    n_df = df.copy()
    n_df["original_image_path"] = df[column_image_path]
    n_df["original_image_name"] = df[column_image_name]

    n_df[column_image_path] = new_image_paths
    n_df[column_image_name] = [path.name for path in new_image_paths]

    return n_df

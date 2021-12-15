from pathlib import Path

import numpy as np


def get_relative_path(original_path, parent_path):

    if isinstance(original_path, list):

        return [get_relative_path(path, parent_path)
                for path in original_path]
    elif isinstance(original_path, np.ndarray):

        return np.array([get_relative_path(path, parent_path)
                         for path in original_path],
                        dtype=object)
    original_path = Path(original_path).resolve()
    relative_path = original_path.relative_to(parent_path)
    return relative_path


def df_to_relative_path(df, column_image_path, parent_path):

    n_df = df.copy()
    original_path = list(df[column_image_path])
    relative_path = get_relative_path(original_path, parent_path=parent_path)

    n_df[column_image_path] = relative_path

    return n_df


def get_absolute_path(relative_path, parent_path):

    if isinstance(relative_path, list):

        return [get_absolute_path(path, parent_path)
                for path in relative_path]
    elif isinstance(relative_path, np.ndarray):

        return np.array([get_absolute_path(path, parent_path)
                         for path in relative_path],
                        dtype=object)

    if Path(relative_path).is_absolute():
        return relative_path

    absolute_path = Path(parent_path) / relative_path
    return absolute_path.resolve()


def df_to_absolute_path(df, column_image_path, parent_path):

    n_df = df.copy()
    original_path = list(df[column_image_path])
    absolute_path = get_absolute_path(
        original_path, parent_path=parent_path)

    n_df[column_image_path] = absolute_path

    return n_df


def append_prefix_to_path(absolute_path, prefix, join_character="_",
                          parent_path=None):

    absolute_path = Path(absolute_path).resolve()
    if parent_path is None:
        parent_path = absolute_path.parent
    else:
        parent_path = Path(parent_path).resolve()
    original_name = absolute_path.name
    return parent_path / join_character.join([prefix, original_name])


def build_file_name(
        name,
        extension,
        prefix=None,
        suffix=None,
        join_character="_"):

    items = [prefix, name, suffix]
    items = [element for element in items if element is not None]
    full_name = join_character.join(items)

    return "".join([full_name, extension])

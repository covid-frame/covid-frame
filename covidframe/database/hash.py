from covidframe.tools.hash import dhash, imhash

from joblib import Parallel, delayed
from covidframe.multi.callback import BatchCompletionCallBack

import joblib.parallel
joblib.parallel.BatchCompletionCallBack = BatchCompletionCallBack


def add_hash_to_df(
        df,
        column_image_path="image_path",
        parallel=False,
        n_jobs=-1):

    # df["cv_hash"] = df.apply(lambda
    #                         row: dhash(str(row[column_image_path])),
    #                         axis=1)
    # df["img_hash"] = df.apply(lambda
    #                          row: imhash(str(row[column_image_path])),
    #                          axis=1)
    file_paths = df[column_image_path]

    cv_hashes = []
    im_hashes = []

    if parallel:
        cv_hashes = Parallel(n_jobs=n_jobs)(
            delayed(dhash)(str(file_path)) for file_path in
            file_paths)
        im_hashes = Parallel(n_jobs=n_jobs)(
            delayed(imhash)(str(file_path)) for file_path in
            file_paths)
    else:
        for idx, file_path in enumerate(file_paths):
            print(f"Generating hash {idx+1}/{len(file_paths)}")
            file_path = str(file_path)
            cv_hashes.append(dhash(file_path))
            im_hashes.append(imhash(file_path))

    df["cv_hash"] = cv_hashes
    df["im_hash"] = im_hashes
    return df


def get_duplicated(df, column_name=None):

    hash_columns = ["cv_hash", "im_hash"]

    duplicates = dict.fromkeys(hash_columns, [])
    for hash_column in hash_columns:
        hashes_duplicated = df[df[hash_column]
                               .duplicated()][hash_column].unique()

        items = []
        for hash_duplicated in hashes_duplicated:
            result = df.loc[df[hash_column] == hash_duplicated]

            if column_name is not None:
                result = list(result[column_name])
            items.append(result)

        duplicates[hash_column] = items

    return duplicates


def drop_duplicated_hashes(df):
    df = df.drop_duplicates(subset=["cv_hash"])
    df = df.drop_duplicates(subset=["im_hash"])

    return df


if __name__ == "__main__":

    from covidframe.database.load import load_files_list
    from covidframe import config

    metadata_db = config.databases[0]

    base_path = "/mnt/Archivos/dataset-xray"
    info = load_files_list(metadata_db, base_path)
    print(len(info["info"]))

    info["info"] = add_hash_to_df(info["info"])

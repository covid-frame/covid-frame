import pandas as pd
from sklearn.utils import resample


def resample_database(df, column_category, n_samples):

    category_list = df.groupby([column_category]).size()
    list_idx = []
    for category in category_list.keys():
        index = df[df[column_category] == category]
        list_idx.append(index)

    resampled_list = []
    for idx in list_idx:
        resampled = resample(
            idx,
            n_samples=n_samples,
            replace=False,
            stratify=idx,
            random_state=0)
        resampled_list.append(resampled)

    n_df = pd.concat(resampled_list, ignore_index=True)

    return n_df


def resample_database_to_min(df, column_category):
    category_list = df.groupby([column_category]).size()
    reference_size = min(category_list.values)
    return resample_database(df, column_category, reference_size)

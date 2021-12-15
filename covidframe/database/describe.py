

def get_columns_max_unique(df, limit=10):

    return df.columns[df.nunique() <= limit]


def get_representative_columns(df, limit=10):

    return df[get_columns_max_unique(df, limit=limit)]

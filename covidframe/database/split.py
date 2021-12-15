from sklearn.model_selection import train_test_split


def split_database(df, output_column, test_size=0.2):

    X, y = separate_output(df, output_column)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=0, stratify=y)

    df_train = join_output(X_train, y_train, output_column)
    df_test = join_output(X_test, y_test, output_column)

    return df_train, df_test


def separate_output(df, output_column):

    y = df[output_column]
    X = df.drop(columns=[output_column])

    return X, y


def join_output(X, y, output_column):

    df = X.copy()
    df[output_column] = y

    return df

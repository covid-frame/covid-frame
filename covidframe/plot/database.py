import matplotlib.pylab as plt
import seaborn as sns

from covidframe.database.describe import get_representative_columns


def histplot_representative_columns(df, limit_unique=10,
                                    category_column="category"):

    df = get_representative_columns(df, limit_unique)
    columns = df.columns

    for column in columns:
        histplot_column(df, column, category_column)


def histplot_column(df, column, category_column, ax=None):

    if ax is None:
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

    sns.histplot(data=df, ax=ax, y=column,
                 hue=category_column,
                 multiple="stack")

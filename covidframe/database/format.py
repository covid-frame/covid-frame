from covidframe.tools.save import save_database
from covidframe import config
from covidframe.tools.filterinfo import get_element_from_dicts


def to_covidnet_format(df, output_file,
                       column_id="id",
                       column_image_name="image_name",
                       column_category="category"
                       ):

    covidnet_info = get_element_from_dicts(config.cnn, "name", "COVID-Net")

    n_df = df.copy()
    n_df[column_category] = df[column_category].map(covidnet_info["mappings"])
    save_database(
        n_df[[column_id, column_image_name, column_category]],
        output_file,
        sep=" ",
        header=False)

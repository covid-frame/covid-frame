
from covidframe.database.load import load_files_list
from covidframe.database.hash import drop_duplicates


def load_databases(list_database_info):

    info_databases = []

    for database_info in list_database_info:
        info = load_files_list(database_info)

        info_databases.append(info)

    return info_databases


def drop_duplicates_list(info_databases):

    for info_database in info_databases:
        info_database["info"] = drop_duplicates(info_database["info"])

    return info_databases

from pathlib import Path


def get_extensions(path):

    path = Path(path).resolve()
    ext = [f.suffix for f in path.rglob("*") if f.is_file()]
    ext = list(dict.fromkeys(ext))

    return ext


if __name__ == "__main__":

    from covidframe.database.load import load_paths
    from covidframe import config

    base_path = "/mnt/Archivos/dataset-xray"
    for database_info in config.databases:
        paths = load_paths(database_info, base_path)
        extensions = get_extensions(paths["image_path"])
        print(extensions)

import os
from dotenv import load_dotenv

load_dotenv()

paths = {
    "datasets_base_path": os.getenv("DATASETS_BASE_PATH", "."),
    "output_folder": os.getenv("OUTPUT_FOLDER", ".")
}

categories = [
    "pneumonia",
    "normal",
    "covid-19"
]

databases = [
    {
        "type": "metadata",
        "source": "github",
        "folder_name": "covid-chestxray-dataset",
        "image_relative_path": "images",
        "type_own": {
            "metadata_file": "metadata.csv",
            "selection": [{
                "column": "view",
                "values": ["PA",
                           "AP",
                           "AP Supine",
                           "AP semi erect",
                           "AP erect"]
            }],
            "column_category": "finding",
            "column_file_names": "filename",
            "column_id": "patientid",
            "mappings": {
                'Pneumonia/Viral/COVID-19': "covid-19",
                'Pneumonia': "pneumonia",
                'Pneumonia/Viral/SARS': "pneumonia",
                'Pneumonia/Bacterial/Streptococcus': "pneumonia",
                'No Finding': "normal",
                'Pneumonia/Bacterial/Chlamydophila': "pneumonia",
                'Pneumonia/Bacterial/E.Coli': "pneumonia",
                'Pneumonia/Bacterial/Klebsiella': "pneumonia",
                'Pneumonia/Bacterial/Legionella': "pneumonia",
                'Pneumonia/Viral/Varicella': "pneumonia",
                'Pneumonia/Bacterial': "pneumonia",
                'Pneumonia/Bacterial/Mycoplasma': "pneumonia",
                'Pneumonia/Viral/Influenza': "pneumonia",
                'Tuberculosis': "pneumonia",
                'Pneumonia/Viral/Influenza/H1N1': "pneumonia",
                'Pneumonia/Aspiration': "pneumonia",
                'Pneumonia/Bacterial/Nocardia': "pneumonia",
                'Pneumonia/Viral/MERS-CoV': "pneumonia",
                'Pneumonia/Bacterial/Staphylococcus/MRSA': "pneumonia",
            }},
    },
    {
        "type": "metadata",
        "source": "github",
        "folder_name": "Actualmed-COVID-chestxray-dataset",
        "image_relative_path": "images",
        "type_own": {
            "metadata_file": "metadata.csv",
            "column_category": "finding",
            "column_file_names": "imagename",
            "column_id": "patientid",
            "mappings": {
                "No finding": "normal",
                "COVID-19": "covid-19",
                "Pneumonia": "pneumonia"
            }
        }},
    {
        "type": "metadata",
        "source": "github",
        "folder_name": "Figure1-COVID-chestxray-dataset",
        "image_relative_path": "images",
        "type_own": {
            "metadata_file": "metadata.csv",
            "file_encoding": "ISO-8859-1",
            "column_category": "finding",
            "column_file_names": "patientid",
            "column_id": "patientid",
            "include_suffix": False,
            "mappings": {
                "No finding": "normal",
                "COVID-19": "covid-19",
                "Pneumonia": "pneumonia"
            }
        }
    },
    {
        "type": "folders",
        "source": "kaggle",
        "folder_name": "Covid19-dataset",
        "image_relative_path": "",
        "type_own": {
            "sub_dirs": ["test",
                         "train"],
            "mappings": {
                "Covid": "covid-19",
                "Normal": "normal",
                "Viral Pneumonia": "pneumonia"
            },
        },
    },
    {
        "type": "folders-metadata",
        "source": "kaggle",
        "folder_name": "COVID-19_Radiography_Dataset",
        "image_relative_path": "",
        "type_own": {
            "sub_dirs": [],
            "mappings": {
                "COVID": "covid-19",
                "Normal": "normal",
                "Viral Pneumonia": "pneumonia",
                "Lung_Opacity": "pneumonia"
            },
            "metadata_files": {
                "COVID": "COVID.metadata.xlsx",
                "Normal": "Normal.metadata.xlsx",
                "Viral Pneumonia": "Viral Pneumonia.metadata.xlsx",
                "Lung_Opacity": "Lung_Opacity.metadata.xlsx"
            },
        }
    },
]


database_types = [
    "metadata",
    "folders",
    "folders-metadata"
]

image_extensions = [
    ".png", ".jpg", ".jpeg", ".tiff", ".bmp", '.PNG', '.JPG', '.JPEG'
]

#!/bin/bash

# This script downloads the databases from the corresponding sources
# it requires have installed kaggle and git
# for kaggle your kaggle.json file should be placed at the config folder:
# $HOME/.kaggle/

if [[ -z $DB_FOLDER ]]; then
  echo "Not DB_FOLDER defined, using current directory"
  DB_FOLDER=$(pwd)
fi

cd $DB_FOLDER

KAGGLE_DB_1_ZIP="covid19-image-dataset.zip"
KAGGLE_DB_1_FOLDER="Covid19-dataset"
KAGGLE_DB_1_PROJECT="pranavraikokte/covid19-image-dataset"
KAGGLE_DB_2_ZIP="covid19-radiography-database.zip"
KAGGLE_DB_2_FOLDER="COVID-19_Radiography_Dataset"
KAGGLE_DB_2_PROJECT="tawsifurrahman/covid19-radiography-database"

function check_kaggle() {
  if [[ ! -d $2 ]]; then
    if [[ ! -f $1 ]]; then
      echo "Database $1 is not downloaded"
      kaggle datasets download -d $3
    else
      echo "Database $1 is downloaded but not uncompressed"
      unzip -o $1 
    fi
  else
    echo "Database $2 exists in folder."
  fi
}

check_kaggle $KAGGLE_DB_1_ZIP $KAGGLE_DB_1_FOLDER $KAGGLE_DB_1_PROJECT
check_kaggle $KAGGLE_DB_2_ZIP $KAGGLE_DB_2_FOLDER $KAGGLE_DB_2_PROJECT

# cheking repositories from github
GITHUB_DB_1_FOLDER="Figure1-COVID-chestxray-dataset"
GITHUB_DB_1_URL="https://github.com/agchung/Figure1-COVID-chestxray-dataset"
GITHUB_DB_2_FOLDER="Actualmed-COVID-chestxray-dataset"
GITHUB_DB_2_URL="https://github.com/agchung/Actualmed-COVID-chestxray-dataset"
GITHUB_DB_3_FOLDER="covid-chestxray-dataset"
GITHUB_DB_3_URL="https://github.com/ieee8023/covid-chestxray-dataset"

function check_github() {
  if [[ ! -d $1 ]]; then
    echo "Database $1 is not downloaded"
    git clone $2
  else
    echo "Database $1 exists in folder."
    cd $1
    git pull --all
    cd $DB_FOLDER
  fi
}


check_github $GITHUB_DB_1_FOLDER $GITHUB_DB_1_URL
check_github $GITHUB_DB_2_FOLDER $GITHUB_DB_2_URL
check_github $GITHUB_DB_3_FOLDER $GITHUB_DB_3_URL

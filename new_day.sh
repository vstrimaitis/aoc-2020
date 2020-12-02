#!/bin/bash
if [[ $# -eq 0 ]] ; then
    echo "Usage: ./new_day.sh <day_number>"
    exit 1
fi

DAY_FOLDER=$(printf "%02d" $1)
TEMPLATES_FOLDER="templates"

if [[ -d $DAY_FOLDER ]] ; then
    read -p "Directory $DAY_FOLDER already exists. Overwrite? (y/n) " yn
    case $yn in
        [Yy]* ) rm -rf $DAY_FOLDER;;
        * ) echo "Exiting"; exit 0;;
    esac
fi

cp -r $TEMPLATES_FOLDER $DAY_FOLDER

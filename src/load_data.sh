#!/bin/bash
DIR=/mnt/c/wsl_shared/ETL
echo "DIR: ${DIR}"

DATA_DIR=$DIR/data
echo "DATA_DIR: ${DATA_DIR}"

cd $DIR
find $DATA_DIR/ -maxdepth 1 -type f -iname "*.csv" -print0 | while IFS= read -r -d '' f; do
  # process file
  echo "processing $f ..."
  python3 main.py $f
done
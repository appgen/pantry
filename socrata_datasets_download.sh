#!/bin/sh
set -e

download_page() {
  [ -z "$1" ] && echo 'You must specify a page number' && return 1
  file="socrata/datasets/$1"
  test -f "$file" || wget -O "$file" "https://data.cityofnewyork.us/browse?limitTo=datasets|maps&page=$1&sortBy=oldest&view_type=table"
}

mkdir -p socrata/datasets
for page in $(seq 1 210); do
  download_page $page
done

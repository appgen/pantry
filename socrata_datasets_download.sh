#!/bin/sh
set -e

download_page() {
  [ -z "$1" ] && echo 'You must specify a page number' && return 1
  file="socrata/datasets/$1-$2"
  test -f "$file" || wget -O "$file" "https://data.cityofnewyork.us/browse?limitTo=$1&page=$2&sortBy=oldest&view_type=table"
}

mkdir -p socrata/datasets
for page in $(seq 1 80); do
  download_page datasets $page
done
for page in $(seq 1 50); do
  download_page maps $page
done

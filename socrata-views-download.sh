#!/bin/sh
set -e

mkdir -p socrata/views
for viewid in $(./socrata-datasets-viewids.py); do
  test -e "socrata/views/${viewid}" || wget -O "socrata/views/${viewid}" "https://data.cityofnewyork.us/views/${viewid}.json"
done

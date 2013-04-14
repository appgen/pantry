#!/bin/sh
set -e

mkdir -p socrata/rows
for viewid in $(./datasets-parse.py); do
  # Skip big stuff.
  grep 311\ Service\ Requests "socrata/views/${viewid}" > /dev/null && continue
  [ 'ym2h-u9dt' = "${viewid}" ] && continue
  [ 's22f-jsd4' = "${viewid}" ] && continue

  # Download what we don't have.
  test -e "socrata/rows/${viewid}" || curl "https://data.cityofnewyork.us/api/views/${viewid}/rows.csv?accessType=DOWNLOAD" > "socrata/rows/${viewid}"
done

#!/bin/sh
set -e

mkdir -p socrata/rows
for viewid in $(./socrata_datasets_viewids.py); do
  # Skip big stuff.
  grep 311\ Service\ Requests "socrata/views/${viewid}" > /dev/null && continue
  [ 'ym2h-u9dt' = "${viewid}" ] && continue
  [ 's22f-jsd4' = "${viewid}" ] && continue

  # Download what we don't have.
  test -e "socrata/rows/${viewid}" || curl "https://data.cityofnewyork.us/api/views/${viewid}/rows.csv?accessType=DOWNLOAD" > "socrata/rows/${viewid}"
  grep '"message" : "You have exceeded the number of unregistered requests during the last hour. Please specify an app_token in your request"' "socrata/rows/${viewid}" && rm "socrata/rows/${viewid}" && sleep 1h
done

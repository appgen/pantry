#!/bin/sh
set -e
# Upload NYC big apps rows from S3.

for viewid in $(s3cmd ls s3://rows.appgen.me|cut -d/ -f4|sort > /tmp/uploaded); do
  echo Retrieving $viewid
  if test -f "socrata/rows/${viewid}"; then
    # Do nothing if we have it.
    sleep 0s
  elif test -f "socrata/rows/${viewid}.gz"; then
    # Gunzip if we have it gzipped.
    gunzip "socrata/rows/${viewid}.gz"
  else
    s3cmd get "s3://rows.appgen.me/${viewid}" "socrata/rows/${viewid}"
  fi
done

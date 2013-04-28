#!/bin/sh
set -e
# Upload NYC big apps rows to S3.

s3cmd ls s3://rows.appgen.me|cut -d/ -f4|sort > /tmp/uploaded
ls socrata/rows/*-*|sed -e 's/.*\///' -e 's/\.gz//' |sort > /tmp/downloaded

for viewid in $(diff /tmp/{downloaded,uploaded}|sed 1d|cut -d\  -f2); do
  echo Uploading $viewid
  gzip "socrata/rows/${viewid}"
  s3cmd put --add-header=Content-Encoding:gzip --add-header=Content-Type:text/csv "socrata/rows/${viewid}.gz" s3://rows.appgen.me
done

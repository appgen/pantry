#!/bin/sh
# Convert the csv files to pdf, take the first page, concatenate them.
set -e

mkdir -p /tmp/socrata-concat/
rm -f /tmp/socrata-concat/*.pdf

# http://ask.libreoffice.org/en/question/13207/filter-options-for-convert-to-using-command-line/
unoconv -f pdf -o /tmp/socrata-concat -eSelectPdfVersion=1 socrata/rows/*

(
  set -e
  cd /tmp/socrata-concat

  # First page
  for file in $(ls *.pdf); do
    pdftk "$file" cat 1 output "$file-firstpage.pdf"
  done
  
  # Combine
  pdftk *-firstpage.pdf output first-pages.pdf
)

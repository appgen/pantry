#!/bin/sh
# Convert the csv files to pdf, take the first page, concatenate them.

# http://ask.libreoffice.org/en/question/13207/filter-options-for-convert-to-using-command-line/
mkdir -p /tmp/socrata-concat/
rm -f /tmp/socrata-concat/*.pdf

unoconv -f pdf -o /tmp/socrata-concat -eSelectPdfVersion=1 socrata/rows/*

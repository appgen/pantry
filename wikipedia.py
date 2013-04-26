#!/usr/bin/env python2
'Download Wikipedia articles.'
from urllib import urlencode

import helpers

def article(title):
    'Download the English Wikipedia article of a given title.'
    urlbase = 'http://en.wikipedia.org/w/api.php?format=json&action=query&prop=revisions&rvprop=content&'
    params = urlencode({'titles': title.encode('utf-8')})
    return helpers.get(urlbase + params, cachedir = 'wikipedia')

# d['query']['pages']['9252']['revisions'][0]['*']
if __name__ == '__main__':
    import sys
    article(sys.argv[1])

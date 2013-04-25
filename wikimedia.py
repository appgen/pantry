#!/usr/bin/env python2
'''
Download images from Wikimedia Commons Documentation:
* https://www.mediawiki.org/wiki/API
* http://wikimedia.7.x6.nabble.com/can-I-use-the-API-to-search-for-images-in-commons-wikimedia-org-td2549464.html
* http://stackoverflow.com/questions/1467336/downloading-images-from-wikimedia-commons
'''
import re
from urllib import urlencode

import json
import lxml.etree

import helpers

def download(search_term):
    '''
    Save files to disk. Don't call this to search the files
    '''
    filenames = _filenames(search_term)
    for filename in filenames:
        print u'Looking up %s' % filename
        image_url = _image_url(filename)
        helpers.get(image_url, cachedir = 'wikimedia')

def _filenames(search_term):
    'Search for a search term.'
    urlbase = u'https://commons.wikimedia.org/w/api.php?action=query&list=search&srnamespace=6&format=json&'
    searchparam = urlencode({'srsearch': search_term.encode('utf-8')})
    r = helpers.get(urlbase + searchparam, cachedir = 'wikimedia')

    results = json.load(r)['query']['search']
    if len(results) == 0:
        raise ValueError('No results')

    return [re.sub(r'^File:', '', result['title']) for result in results]

def _image_url(filename):
    url = u'http://toolserver.org/~magnus/commonsapi.php?' + urlencode({u'image': filename.encode('utf-8')})
    r = helpers.get(url, cachedir = 'wikimedia')
    response = lxml.etree.parse(r)
    urls = response.xpath('//urls/file/text()')
    if len(urls) == 1:
        return urls[0]
    else:
        raise ValueError('No file urls')


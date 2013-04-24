#!/usr/bin/env python2
'''
Download images from Wikimedia Commons Documentation:
* https://www.mediawiki.org/wiki/API
* http://wikimedia.7.x6.nabble.com/can-I-use-the-API-to-search-for-images-in-commons-wikimedia-org-td2549464.html
'''
import re

import json
import lxml.etree

import requests

import helpers

def download(search_term):
    '''
    Save files to disk. Don't call this to search the files
    '''
    filenames = _filenames(search_term)
    for filename in filenames:
        image_url = _image_url(filename)
        helpers.get(image_url, cachedir = 'wikimedia')

def _filenames(search_term):
    'Search for a search term.'
    url = 'https://commons.wikimedia.org/w/api.php'
    params = {
        'action': 'query',
        'list': 'search',
        'srnamespace': '6',
        'format': 'json',
        'srsearch': search_term,
    }
    headers = {
        'User-Agent': 'AppGen (http://www.appgen.me), by Thomas Levine (http://thomaslevine.com) and Ashley Williams',
    }
    r = requests.get(url, params = params, headers = headers)
    if r.status_code != 200:
        return None

    results = json.loads(r.text)['query']['search']
    if len(results) == 0:
        return None

    return [re.sub(r'^File:', '', result['title']) for result in results]

def _image_url(filename):
    url = 'http://toolserver.org/~magnus/commonsapi.php'
    params = {'image': filename}
    r = requests.get(url, params = params)
    response = lxml.etree.fromstring(r.text.encode('utf-8'))
    urls = response.xpath('//urls/file/text()')
    if len(urls) == 1:
        return urls[0]

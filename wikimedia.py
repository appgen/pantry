#!/usr/bin/env python2
import requests

'''
Download images from Wikimedia Commons Documentation:
* https://www.mediawiki.org/wiki/API
* http://wikimedia.7.x6.nabble.com/can-I-use-the-API-to-search-for-images-in-commons-wikimedia-org-td2549464.html
'''

def search(search_term):
    'Search for a search term.'
    url = 'https://commons.wikimedia.org/w/api.php'
    params = {
        'action': 'query',
        'list': 'search',
        'srnamespace': '6',
        'srsearch': search_term,
    }
    headers = {
        'User-Agent': 'AppGen (http://www.appgen.me), by Thomas Levine (http://thomaslevine.com) and Ashley Williams',
    }
    return requests.get(url, params = params, headers = headers)

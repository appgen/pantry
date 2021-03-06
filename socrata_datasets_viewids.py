#!/usr/bin/env python2
import os
import lxml.html

DIR = os.path.join('socrata', 'datasets')

def get_viewids():
    pages = filter(lambda page: set(page.split('-')[-1]).issubset(set('0123456789')), os.listdir(DIR))
    viewids = set()
    for page in pages:
        html = lxml.html.parse(os.path.join(DIR, page))
        viewids = viewids.union(parse(html))
    return viewids

def parse(html):
    'Get the viewids out.'
    return set(map(unicode, html.xpath('//tr[@itemtype="http://schema.org/Dataset"]/@data-viewid')))

if __name__ == '__main__':
    print ' '.join(get_viewids())

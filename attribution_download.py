#!/usr/bin/env python2
import os, json

import helpers
from socrata_datasets_viewids import get_viewids

def get_attribution_bodies():
    'Get the bodies of the attribution links.'
    for attribution in get_attribution_links():
        yield (attribution, helpers.get(attribution, cachedir = 'attribution'))

def get_attribution_links():
    'Get the urls.'
    for viewid in get_viewids():
        f = open(os.path.join('socrata', 'views', viewid))
        attribution = json.load(f).get('attributionLink')
        if attribution:
            yield attribution

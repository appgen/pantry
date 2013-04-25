#!/usr/bin/env python2
'Download content about dataset topics.'
import os, json

from wikimedia import download as wm
from wikipedia import article  as wp

def view_words(viewid):
    'Pick the topic words for a particular view.'
    view = json.load(open(os.path.join(VIEWS, viewid)))
    words_list = view['tags'] + view['name'].split(' ') + \
        view['description'].split(' ') + [view['category']] + \
        [c['name'] for c in view['columns']]
    return set([w.lower() for w in words_list])

if __name__ == '__main__':
    VIEWS = os.path.join('socrata', 'views')
    todos = set()
    for viewid in os.listdir(VIEWS):
        todos = todos.union(view_words(viewid))
    for todo in todos:
        wm(todo)
        wp(todo)

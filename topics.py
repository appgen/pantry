#!/usr/bin/env python2
'Download content about dataset topics.'
import os, json
import re
from unidecode import unidecode

from wikimedia import download as wm
from wikipedia import article  as wp

_ONLY_LETTERS = re.compile(r'^[a-z]+$', flags = re.IGNORECASE)
def only_letters(word):
    return re.match(_ONLY_LETTERS, word)

def keywords(viewid):
    'Pick the topic words for a particular view.'
    view = json.load(open(os.path.join(VIEWS, viewid)))

    column_words = []
    for c in view['columns']:
        column_words.extend(c['name'].split(' '))

    words_list = column_words + view.get('tags', []) + view['name'].split(' ') + \
        view.get('description', '').split(' ') + [view.get('category', '')]

    return set(filter(only_letters, set([unidecode(w.lower()) for w in words_list])))

if __name__ == '__main__':
    VIEWS = os.path.join('socrata', 'views')
    todos = set()
    for viewid in os.listdir(VIEWS):
        todos = todos.union(keywords(viewid))
    for todo in todos:
        print todo
      # wm(todo)
      # wp(todo)

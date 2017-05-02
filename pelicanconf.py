#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'AbrahamV'
SITENAME = 'Abraham Varricatt'
SITESUBTITLE = 'Note To Self'
DEFAULT_DATE_FORMAT = '%Y/%m&#8209;%b/%d'
SITEURL = 'http://localhost:8000'

THEME = 'the-notes'

PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = [
  'articles',
  'static',
]
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [
  'summary',
  'neighbors',
  'headerid',
]

# Articles in respective folders
PATH_METADATA = r'(?P<path>.*)/(?P<slug>.*)\..*'
ARTICLE_SAVE_AS = '{path}/{slug}.html'
ARTICLE_URL = '{path}/{slug}.html'

TIMEZONE = 'America/Toronto'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 5

USE_FOLDER_AS_CATEGORY = False
DISPLAY_CATEGORIES_ON_MENU = False
TYPOGRIFY = True
HEADERID_LINK_CHAR = ' #'

# For pygments highlighting
PYGMENTS_RST_OPTIONS = {
  'linenos': 'table',
}

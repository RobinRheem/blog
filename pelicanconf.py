#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Robin Rheem'
SITENAME = 'Robin Rheem'
SITESUBTITLE = 'Software Engineer'

THEME = 'pelican-clean-blog'

PATH = 'content'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'en'

MENUITEMS = (
    ('Essays', '/category/essay.html'),
    ('Analyses', '/category/analysis.html'),
)

STATIC_PATHS = [
    'images',
    'extra',
]

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
}

PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = ['pelican-ipynb.markup']

MARKUP = ('md', 'ipynb')

IGNORE_FILES = [".ipynb_checkpoints"]

IPYNB_USE_METACELL = True

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/RobinRheem/'),
    ('Twitter', 'https://twitter.com/RobinRheem/'),
    ('LinkedIn', 'https://www.linkedin.com/in/robinrheem/'),
)

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# clean-blog
HEADER_COLOR = 'black'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


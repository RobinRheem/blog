#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Robin Rheem'
SITENAME = 'Robin Rheem'
SITEURL = ''
SITESUBTITLE = 'Software Engineer'

THEME = 'pelican-clean-blog'

PATH = 'content'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('GitHub', 'https://github.com/RobinRheem/'),
    ('Twitter', 'https://twitter.com/RobinRheem/'),
    ('LinkedIn', 'https://www.linkedin.com/in/robinrheem/'),
)

DEFAULT_PAGINATION = 10

# clean-blog
HEADER_COVER = 'images/cover.jpg'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


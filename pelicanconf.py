#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = './theme'
AUTHOR = u'Ryan Sturmer'
SITENAME = u'Ryan Sturmer'
SITEURL = 'http://ryansturmer.com'

PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False
DISPLAY_PAGES_ON_MENU = True

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

PROFILE_IMG_URL = 'http://www.gravatar.com/avatar/c96b5cb714feed171a880b093e05b5a1.png?s=200'
COVER_IMG_URL = '/theme/images/bronto.jpg'
SOCIAL = (
        ('github', 'https://github.com/ryansturmer'),
        ('twitter-square', 'https://twitter.com/ryansturmer'),
        ('facebook', 'https://facebook.com/ryan.sturmer'),
        ('soundcloud', 'https://soundcloud.com/ryansturmer'),
        ('flickr', 'https://flickr.com/photos/thepr0fess0r'),
        ('youtube', 'https://youtube.com/ryansturmer'),
)

MENUITEMS = (('Archives', '/archives.html'),)

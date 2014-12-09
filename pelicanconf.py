#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = './theme'
AUTHOR = u'Ryan Sturmer'
SITENAME = u'Ryan Sturmer'
SITEURL = 'http://ryansturmer.com'

PLUGINS = ['pelican_flickrtag']
PATH = 'content'

STATIC_PATHS = ['images']

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

DISQUS_SITENAME = 'ryansturmer'
GOOGLE_ANALYTICS = 'UA-55169068-1'

FLICKR_API_KEY = '19292690b768d54b8ad527e374ed63eb'
FLICKR_API_SECRET = '18db0034688ac024'

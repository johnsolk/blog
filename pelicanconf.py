#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import markdown

AUTHOR = u'Lisa Johnson'
SITENAME = u'monsteRbashSeq'
SITEURL = 'https://ljcohen.github.io/blog'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

PATH = 'content'

OUTPUT_PATH = 'output'

CUSTOM_CSS = 'static/css/custom.css'

THEME = './theme'
# https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3

LINKS = [('name','url')]

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')
SEARCH_URL = '/blog/search.html'
DISPLAY_CATEGORIES_ON_MENU = True

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'tipue_search','i18n_subsites']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

DISPLAY_PAGES_ON_MENU = True

BOOTSTRAP_THEME = 'simplex'

BOOTSTRAP_NAVBAR_INVERSE = True

STATIC_PATHS = ['img']

READERS = {'html': None}

CC_LICENSE = `CC0`

SOCIAL = (('twitter', 'https://twitter.com/monsterbashseq'),
          ('github', 'https://github.com/ljcohen'),
          ('flickr','https://www.flickr.com/155690017@N06/'),
          ('linkedin','https://www.linkedin.com/in/johnsolk/'),
          ('envelope','mailto:ljcohen@ucdavis.edu'))

DISQUS_SITENAME = "johnson_lk"

#GOOGLE_ANALYTICS = ""


### Theme specific settings
BANNER = '/img/sanomacoast.png'
BANNER_SUBTITLE = 'Lisa K. Johnson'
BANNER_ALL_PAGES = True
DISPLAY_TAGS_ON_SIDEBAR = True
TAGS_URL = 'tags.html'
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_ARCHIVE_ON_SIDEBAR = True

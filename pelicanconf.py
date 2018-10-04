#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import markdown

AUTHOR = 'Lisa Johnson'
SITENAME = 'monsteRbashSeq'
SITEURL = 'https://ljcohen.github.io/blog/'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'
#DEFAULT_DATE = 'fs'
#DEFAULT_DATE_FORMAT = '%d %b %Y'

PATH = 'content'
OUTPUT_PATH = 'output'


THEME = './theme'
# https://github.com/arulrajnet/attila
LINKS = [('name','url')]

HEADER_COVER = './img/sanomacoast.jpg'
#GITHUB_URL = 'https://github.com/ljcohen'
#TWITTER_USERNAME = 'monsterbashseq'
DISQUS_SITENAME = 'https-ljcohen-github-io-blog'


#SOCIAL = [('twitter','https://twitter.com/monsterbashseq')]

SOCIAL = (('twitter', 'https://twitter.com/monsterbashseq'),
          ('github', 'https://github.com/ljcohen'),
          ('flickr','https://www.flickr.com/155690017@N06/'),
          ('envelope','mailto:ljcohen@ucdavis.edu'))

# Post and Pages path
#ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}.html'
#ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
#PAGE_URL = 'pages/{slug}/'
#PAGE_SAVE_AS = 'pages/{slug}/index.html'
#YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
#MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Tags and Category path
#CATEGORY_URL = 'category/{slug}'
#CATEGORY_SAVE_AS = 'category/{slug}/index.html'
#CATEGORIES_SAVE_AS = 'catgegories.html'
#TAG_URL = 'tag/{slug}'
#TAG_SAVE_AS = 'tag/{slug}/index.html'
#TAGS_SAVE_AS = 'tags.html'

# Author
#AUTHOR_URL = 'author/{slug}'
#AUTHOR_SAVE_AS = 'author/{slug}/index.html'
#AUTHORS_SAVE_AS = 'authors.html'

### Plugins

#PLUGIN_PATHS = [
#  'pelican-plugins'
#]

#PLUGINS = [
#  'sitemap',
#  'neighbors',
#  'assets'
#]

# Sitemap
#SITEMAP = {
#    'format': 'xml',
#    'priorities': {
#        'articles': 0.5,
#        'indexes': 0.5,
#        'pages': 0.5
#    },
#    'changefreqs': {
#        'articles': 'monthly',
#        'indexes': 'daily',
#        'pages': 'monthly'
#    }
#}

# Comments
DISQUS_SITENAME = "attilademo"

# Analytics
GOOGLE_ANALYTICS = "UA-3546274-12"


### Theme specific settings

HEADER_COVER = 'img/sanomacoast.jpg'

COLOR_SCHEME_CSS = 'github.css'

CSS_OVERRIDE = ['css/myblog.css']

AUTHORS_BIO = {
  "zutrinken": {
    "name": "Zutrinken",
    "cover": "https://casper.ghost.org/v1.0.0/images/team.jpg",
    "image": "assets/images/avatar.png",
    "website": "http://blog.arulraj.net",
    "linkedin": "unavailable",
    "github": "arulrajnet",
    "location": "Chennai",
    "bio": "This is the place for a small biography with max 200 characters. Well, now 100 are left. Cool, hugh?"
  }
}

# Custom Header

#HEADER_COVERS_BY_TAG = {'cupcake': 'assets/images/rainbow_cupcake_cover.png', 'general':'https://casper.ghost.org/v1.0.0/images/writing.jpg'}

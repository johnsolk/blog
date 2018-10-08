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

#CUSTOM_CSS = 'static/css/custom.css'

THEME = './theme'
# https://github.com/getpelican/pelican-themes/tree/master/pelican-bootstrap3


LINKS = [("Titus Brown's DIB Lab","http://ivory.idyll.org/lab/"),
         ("Andrew Whitehead's Lab, Environmental Genomics",'https://whiteheadresearch.wordpress.com/'),
         ('UCD DIB Training','https://dib-training.readthedocs.io/en/pub/'),
         ('NSF-XSEDE Jetstream login','https://use.jetstream-cloud.org/application/dashboard'),
         ('Python conda environment docs','https://conda.io/docs/user-guide/tasks/manage-environments.html'),
         ('hackmd.io','https://hackmd.io/'),
         ('osf','https://osf.io/'),
         ('EvidentialGene, killifish genome project','http://arthropods.eugenes.org/EvidentialGene/killifish/')]

DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')
SEARCH_URL = '/blog/search.html'

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = (
    ('Main','https://ljcohen.github.io/'),
    ('About','https://ljcohen.github.io/about.html'),
    ('Publications','https://ljcohen.github.io/publications.html'),
    ('Teaching','https://ljcohen.github.io/teaching.html'),
    ('Blog', '/category/blog.html'),
    ('Old Blog','https://monsterbashseq.wordpress.com/')
    )


PLUGIN_PATHS = ['./plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code',
           'tipue_search','i18n_subsites']

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

DISPLAY_PAGES_ON_MENU = True

BOOTSTRAP_THEME = 'simplex'

BOOTSTRAP_NAVBAR_INVERSE = True

STATIC_PATHS = ['img']

READERS = {'html': None}

#CC_LICENSE = 'zero'

SOCIAL = (('twitter', 'https://twitter.com/monsterbashseq'),
          ('github', 'https://github.com/ljcohen'),
          ('flickr','https://www.flickr.com/155690017@N06/'),
          ('linkedin','https://www.linkedin.com/in/johnsolk/'),
          ('envelope','mailto:ljcohen@ucdavis.edu'))

DISQUS_SITENAME = "https-ljcohen-github-io-blog"

#GOOGLE_ANALYTICS = ""


### Theme specific settings
BANNER = '/img/sanomacoast.png'
BANNER_SUBTITLE = 'Lisa K. Johnson'
BANNER_ALL_PAGES = True
DISPLAY_TAGS_ON_SIDEBAR = True
TAGS_URL = 'tags.html'
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_ARCHIVE_ON_SIDEBAR = True

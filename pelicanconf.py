#!/usr/bin/env python
# -*- coding: utf-8 -*- #

PATH = 'content'
TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'ja'
DEFAULT_PAGINATION = 10

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
THEME = 'theme/Flex'

# Flex
AUTHOR = "liqsuq"
SITEURL = ""
SITENAME = "rkgknet"
SITETITLE = "rkgknet"
SITESUBTITLE = "ネット出張らくがき帳"
SITEDESCRIPTION = "ネット出張らくがき帳"
# SITELOGO = SITEURL + "/images/profile.png"
# FAVICON = SITEURL + "/images/favicon.ico"

# BROWSER_COLOR = "#333"
# ROBOTS = "index, follow"

# CC_LICENSE = {
#     "name": "Creative Commons Attribution-ShareAlike",
#     "version": "4.0",
#     "slug": "by-sa"
# }

COPYRIGHT_YEAR = 2021

# EXTRA_PATH_METADATA = {
#     "extra/custom.css": {"path": "static/custom.css"},
# }

# CUSTOM_CSS = "static/custom.css"

MAIN_MENU = True

# ADD_THIS_ID = "ra-77hh6723hhjd"
# DISQUS_SITENAME = "yoursite"
# GOOGLE_ANALYTICS = "UA-1234-5678"
# GOOGLE_TAG_MANAGER = "GTM-ABCDEF"

# Enable i18n plugin.
# PLUGINS = ["i18n_subsites"]
# Enable Jinja2 i18n extension used to parse translations.
# JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

# Translate to German.
DEFAULT_LANG = "ja"
# OG_LOCALE = "de_DE"
# LOCALE = "de_DE"

# Default theme language.
# I18N_TEMPLATES_LANG = "en"


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
        'markdown.extensions.admonition': {},
    },
    'output_format': 'html5',
}

FILENAME_META = r"(?P<date>\d{4}\d{2}\d{2})_(?P<slug>.*)"
ARTICLE_PATHS = ["articles"]

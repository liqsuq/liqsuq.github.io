#!/usr/bin/env python
# -*- coding: utf-8 -*- #

TIMEZONE = "Asia/Tokyo"
DEFAULT_LANG = "ja"
DEFAULT_PAGINATION = 10

AUTHOR = "liqsuq"
SITEURL = ""
SITENAME = "rkgknet"

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



PATH = "content"
ARTICLE_PATHS = ["articles"]
ARTICLE_URL = "articles/{slug}.html"
ARTICLE_SAVE_AS = "articles/{slug}.html"
ARTICLE_LANG_URL = "articles/{slug}.html"
ARTICLE_LANG_SAVE_AS = "articles/{slug}.html"
FILENAME_METADATA = r"(?P<date>\d{4}\d{2}\d{2})_(?P<slug>.*)"
USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = "misc"
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.codehilite": {"css_class": "highlight"},
        "markdown.extensions.extra": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {},
        "markdown.extensions.admonition": {},
        "markdown.extensions.nl2br": {},
        "mdx_linkify.mdx_linkify": {},
        "markdown_del_ins": {},
    },
    "output_format": "html5",
}

# Flex
THEME = 'themes/Flex'
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
MENUITEMS = (
    ("Categories", "/categories.html"),
    ("Archives", "/archives.html"),
)

PLUGIN_PATHS = ["plugins"]
PLUGINS = [
    "related_posts",
    "tipue_search",
    "neighbors",
    "sitemap",
]

SITEMAP = {"format": "xml"}

# ADD_THIS_ID = "ra-77hh6723hhjd"
# DISQUS_SITENAME = "yoursite"
# GOOGLE_ANALYTICS = "UA-1234-5678"
# GOOGLE_TAG_MANAGER = "GTM-ABCDEF"

# Enable i18n plugin.
# PLUGINS = ["i18n_subsites"]
# Enable Jinja2 i18n extension used to parse translations.
# JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}

# Default theme language.
# I18N_TEMPLATES_LANG = "en"
PYGMENTS_STYLE = "monokai"



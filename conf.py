# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time

# Data about this site
BLOG_AUTHOR = "chronodekar"
BLOG_TITLE = "Note To Self"
SITE_URL = "https://note2self.abraham-v.com/"
BLOG_EMAIL = "no@email.here"
BLOG_DESCRIPTION = "Snippets of information"

# Multi-lingual settings (Not used - keeping them blank)
DEFAULT_LANG = "en"
TRANSLATIONS = {
    DEFAULT_LANG: "",
}

# Sidebar/Navigation
NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/archive.html", "Archives"),
        ("/categories/index.html", "Tags"),
        ("/rss.xml", "RSS feed"),
    ),
}

# Theme settings
THEME = "bootstrap3"
THEME_COLOR = '#5670d4'

# POST/PAGE tuples
POSTS = (
    ("posts/*.rst", "posts", "post.tmpl"),
    ("posts/*.html", "posts", "post.tmpl"),
)
PAGES = (
    ("stories/*.rst", "stories", "story.tmpl"),
    ("stories/*.html", "stories", "story.tmpl"),
)

TIMEZONE = "UTC+5:30"

# Mapping language with file extension
COMPILERS = {
    "rest": ('.rst', '.txt'),
    "html": ('.html', '.htm'),
}

WRITE_TAG_CLOUD = True
POSTS_SECTIONS = True
CATEGORY_ALLOW_HIERARCHIES = False
CATEGORY_OUTPUT_FLAT_HIERARCHY = False
FRONT_INDEX_HEADER = {
    DEFAULT_LANG: '',
}
REDIRECTIONS = []
GITHUB_COMMIT_SOURCE = True
OUTPUT_FOLDER = 'output'
IMAGE_FOLDERS = {'images': 'images'}
GLOBAL_CONTEXT = {}
GLOBAL_CONTEXT_FILLER = []

COMMENT_SYSTEM = ""
COMMENT_SYSTEM_ID = ""

LICENSE = ""

CONTENT_FOOTER = 'Contents &copy; {date}         <a href="mailto:{email}">{author}</a> - Powered by<a href="https://getnikola.com" rel="nofollow">Nikola</a>         {license}'
CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE,
        }
    )
}



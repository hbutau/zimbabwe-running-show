AUTHOR = 'Zimbabwe Running Show'
SITENAME = 'Zimbabwe Running Show'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Africa/Harare'

DEFAULT_LANG = 'en'

# Theme settings
THEME = 'themes/evently'
THEME_STATIC_DIR = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# Path configuration
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
PAGE_URL = 'pages/{slug}.html'

# Use static page as home page
INDEX_SAVE_AS = 'news.html'

# Static paths
STATIC_PATHS = ['images', 'extra']

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

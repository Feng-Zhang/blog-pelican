AUTHOR = 'Feng'
SITENAME = '生信小屋'
SITEURL = "http://localhost:8000"

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'
LOCALE = ['C.utf8']
# LANGUAGES = { 
#     'en': 'English',
#     'zh': '中文',
# }

ARTICLE_URL = '{slug}.html'
ARTICLE_SAVE_AS = '{slug}.html'

PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

ARCHIVES_URL = 'archives.html'
ARCHIVES_SAVE_AS = 'archives.html'
LANDING_PAGE_TITLE = '关于我'

TAGS_URL = 'tags.html'
TAGS_SAVE_AS = 'tags.html'
MENUITEMS = []

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
THEME = 'pelican-themes/elegant'
# THEME_STATIC_DIR = 'pelican-themes'
THEME_TEMPLATES_OVERRIDES = ['custom_template']

# plugin
PLUGIN_PATHS = ['pelican-plugins', 'pelican-plugins/tipue_search/pelican/plugins']
PLUGINS = ['tipue_search'] #, 'extract_toc'
# PLUGINS = [ ]
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.codehilite": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {
            "permalink": True,
        },
    },
    "output_format": "html5",
}



AUTHOR = 'Feng'
SITENAME = 'test_site'
SITEURL = "http://localhost:8000"

PATH = "content"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'
LOCALE = ['C.utf8']
# LANGUAGES = { 
#     'en': 'English',
#     'zh': '中文',
# }

ARTICLE_URL = '{lang}/{slug}.html'
ARTICLE_SAVE_AS = '{lang}/{slug}.html'

PAGE_URL = '{lang}/{slug}.html'
PAGE_SAVE_AS = '{lang}/{slug}.html'

ARCHIVES_URL = '{lang}/archives.html'
ARCHIVES_SAVE_AS = '{lang}/archives.html'


TAGS_URL = '{lang}/tags.html'
TAGS_SAVE_AS = '{lang}/tags.html'
MENUITEMS = [
    ('English', '/en/'),
    ('中文', '/zh/'),
]

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
# THEME_TEMPLATES_OVERRIDES = ['custom_template']

# plugin
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [ 'i18n_subsites'] #'extract_toc',
# PLUGINS = [ ]
I18N_SUBSITES = {
    'en': {},
    'zh': {},
}
MARKDOWN = {
    "extension_configs": {
        "markdown.extensions.extra": {},
        "markdown.extensions.codehilite": {},
        "markdown.extensions.toc": {
            "permalink": True,
        },
    },
    "output_format": "html5",
}



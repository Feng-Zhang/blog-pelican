AUTHOR = 'Feng'
SITENAME = 'test_site'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'zh'
LOCALE = ('en_US', 'zh_CN')
LANGUAGES = {
    'en': 'English',
    'zh': '中文',
}

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
THEME = 'elegant'
THEME_STATIC_DIR = 'pelican-themes'
I18N_SUBSITES = {
    'zh': {
        'SITENAME': '我的博客',
        'LOCALE': 'zh_CN',
    },
}
THEME_TEMPLATES_OVERRIDES = ['custom_template']

# plugin
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['extract_toc', 'i18n_subsites']
TOC = {
    'TOC_HEADERS': '^h[1-6]',  # Include headers from h1 to h6
    'TOC_RUN': 'true',         # Automatically generate the TOC
    'TOC_INCLUDE_TITLE': 'false',  # Exclude the article title from the TOC
}




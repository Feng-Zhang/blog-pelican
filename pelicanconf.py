AUTHOR = 'Feng'
SITENAME = '生信小屋'
SITEURL = ""

PATH = "content"

# 允许文章图片与 index.md 放在同一目录：
# 1) 将 zh/post 下的非 Markdown 文件作为静态资源复制到 output
# 2) 通过 {static}/zh/post/... 在文章中稳定引用
# 3) 首页轮播图放在 pages/home 目录
STATIC_PATHS = ['zh/post', 'pages/home']
STATIC_EXCLUDES = ['**/*.md']

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'
LOCALE = ['zh_CN.UTF-8', 'zh_CN.utf8', 'zh_CN', 'C.utf8']
DATE_FORMATS = {
    'zh': '%Y年%m月%d日',
}
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

# 首页排版配置
HOMEPAGE_TOP_IMAGES = [
    '/pages/home/slide1.png',
    '/pages/home/slide2.png',
    '/pages/home/slide3.jpg',
]
HOMEPAGE_CAROUSEL_INTERVAL = 4200
CONTACT_EMAIL = 'fengzhang0709@hotmail.com'
CONTACT_WECHAT = ''
CONTACT_GITHUB = 'https://github.com/Feng-Zhang'

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
RELATIVE_URLS = True
THEME = 'pelican-themes/elegant'
# THEME_STATIC_DIR = 'pelican-themes'
THEME_TEMPLATES_OVERRIDES = ['custom_template']

# plugin
PLUGIN_PATHS = ['pelican-plugins', 'pelican-plugins/tipue_search/pelican/plugins']
PLUGINS = ['tipue_search', 'extract_toc'] #
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



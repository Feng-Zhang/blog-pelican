AUTHOR = '章峰'
SITENAME = '章峰的网站'
SITEURL = ""

# Default social-share image fallback (used when an article/page has no featured_image)
FEATURED_IMAGE = '/pages/home/bio-banner1.jpg'

PATH = "content"

# 允许文章图片与 index.md 放在同一目录：
# 1) 将 zh/post 下的非 Markdown 文件作为静态资源复制到 output
# 2) 通过 {static}/zh/post/... 在文章中稳定引用
# 3) 首页轮播图放在 pages/home 目录
STATIC_PATHS = ['zh/post', 'pages/home']
STATIC_EXCLUDES = ['**/*.md']

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh_cn'
LOCALE = ['zh_CN.UTF-8', 'zh_CN.utf8', 'zh_CN', 'C.utf8']
DATE_FORMATS = {
    'zh_cn': '%Y年%m月%d日',
    'zh': '%Y年%m月%d日',
}
# Docutils does not provide a plain "zh" locale; use simplified Chinese locale explicitly.
DOCUTILS_SETTINGS = {
    'language_code': 'zh_cn',
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

# 首页排版配置（图片自动从 content/pages/home/ 下发现）
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
PLUGINS = ['tipue_search', 'extract_toc', 'relative_images', 'home_images']
# PLUGINS = [ ]
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']
MARKDOWN = {
    "extension_configs": {
        "fix_toc_marker": {},
        "markdown.extensions.extra": {},
        "markdown.extensions.codehilite": {},
        "markdown.extensions.meta": {},
        "markdown.extensions.toc": {
            "permalink": True,
        },
        "markdown.extensions.sane_lists": {},
        "pymdownx.arithmatex": {
            "generic": True,
        },
    },
    "output_format": "html5",
}

# Keep standalone .html files as static assets (do not parse them as Pelican content).
READERS = {
    'html': None,
}

# Comments (Utterances → GitHub Issues: Feng-Zhang/blog-pelican-comment)
OUTPUT_RETENTION = ['.git', 'CNAME']

UTTERANCES_REPO = "Feng-Zhang/blog-pelican-comment"
UTTERANCES_THEME = "github-light"
COMMENTS_INTRO = "欢迎留言，使用 GitHub 账号登录即可评论。"


#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Cokernut'
AUTHOR_EMAIL = u'Cokernut@foxmail.com'
SITENAME = 'Cokernut'
TAGLINE = u'逆水行舟，不进则退!'
SITEURL = ''
DEFAULT_DATE_FORMAT = ('%Y-%m-%d')
#OUTPUT_PATH = '.'#需要把输出路径从默认的'output'改成根目录(your_id.github.com目录), 因为githubpage需要把index.html上传到repo的master分支的根目录才可以!
#这个是指定放置.md/.rst文件的目录
PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'
DEFAULT_METADATA = (
)
# 删除输出文件夹目录
DELETE_OUTPUT_DIRECTORY = False

DEFAULT_DATE_FORMAT = ('%Y-%m-%d')
THEME = 'themes/new-bootstrap2'  #http://www.pelicanthemes.com/
#COVER_BG_COLOR = '#375152'
DEFAULT_PAGINATION = 10

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
FEED_DOMAIN = SITEURL
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
USE_FOLDER_AS_CATEGORY = True

# Disqus
#DISQUS_SITENAME = u"mcsrainbow"

# Plugin
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = [ 'sitemap', 'gravatar' ]

## 配置sitemap 插件
SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.5,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}

#相关文章
RELATED_POSTS_MAX = 10

STATIC_PATHS = [u'images', u'files']

FILENAME_METADATA = '(?P<slug>.*)'
# 友情链接
LINKS = (('主页', 'http://cokernut.top'),)
#GITHUB_URL = 'https://github.com/cokernut'#github链接
# 社交网站链接
SOCIAL = (('Github', 'https://github.com/cokernut'),
          ('Documents', 'https://github.com/cokernut/Documents'),
          ('CSDN', 'http://blog.csdn.net/u011965040?viewmode=contents'),)


MENUITEMS = (
)

# 讨论名称
#DISQUS_SITENAME = u"Cokernut"
"""
# Content path
PATH = 'content'
PAGE_PATHS = ['pages']
ARTICLE_PATHS = ['articles']
STATIC_PATHS = ['images', 'files']
EXTRA_PATH_METADATA = {
  'files/robots.txt': {'path': 'robots.txt'},
  'images/favicon.ico': {'path': 'favicon.ico'},
}

# URL settings
PAGINATION_PATTERNS = (
  (1, '{base_name}/', '{base_name}/index.html'),
  (2, '{base_name}/page/', '{base_name}/page/{number}.html'),
)
ARTICLE_URL = ('articles/{slug}.html')
ARTICLE_SAVE_AS = ('articles/{slug}.html')
PAGE_LANG_SAVE_AS = False
"""
#默认每一页有多少篇文章
DEFAULT_PAGINATION = 10

#可用于开发,但当你准备发布设置为False
#RELATIVE_URLS = False   # 禁用相对路径引用



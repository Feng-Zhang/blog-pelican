Title: pelican 创建静态网站
Date: 2026-07-01 15:48
Modified: 2026-07-01 19:30
Category: 网站
Tags: pelican
Slug: pelican
Authors: 章峰
Lang: zh
--------

## 介绍

之前用过hexo和hugo搭建静态网站，确实可以快速生一个网页，但是由于不懂JavaScript和GO语言，没有办法对网页样式进行细致地调整。此外，由于它们所使用主题的不断更新，可很难pull到自己的网站，导致网站出问题。实践中发现，主题什么的简单一点好，更主要是把精力放到内容创作上，因此我对网站生成器的要求变为：

- 主要使用python语法
- 配置要简单，不用花精力在配置上。

Perlican是用Python实现的一个静态网站生成器，支持reStructuredText或Markdown。它支持以下功能：

- 博客文章和静态网页
- 支持评论。评论是通过第三方服务Disqus支持的。即评论数据保存在第三方服务器上
- 主题支持
- 把博客文章生成PDF格式文档
- 多语言博客支持，如可以用英文和中文写同一篇博客。不同语言访问者访问相应语言的博文
- 支持Atom/RSS订阅
- 博文中代码高亮支持
- 博客搬家支持(WordPress, Dotclear, 或RSS feeds)
- 支持插件，如Twiter, Google Analytics等

## 快速开始

```
# 1 安装
conda create -n pelican python=3.11
conda activate pelican
pip install "pelican[markdown]" # 安装pelican
pip install pelican-i18n-subsites # 双语翻译，不需要不用安装
pip install beautifulsoup4 # 安装toc插件依赖
pip install pymdown-extensions # latex 渲染

# 2 创建目录
mkdir -p ~/projects/myblog
cd ~/projects/myblog

# 3 初始设置
pelican-quickstart

# 4. 输出静态网页
pelican content

# 5 本地展示
pelican --listen
# 或者在开发过程中，希望内容有变化本地网页同时变化，而不需要重新运行 --listen
pelican -r -l # 

# 6 发布到github page展示
pelican content -s publishconf.py
cd output
git init
git remote add origin XX # 如git@github.com:Feng-Zhang/blog-content.git
git push
# https://Feng-Zhang.github.io/blog-content/ 可以在网站上看到内容
```

这些代码可以快速生成一个网站，但是想让网站变成你心目中的样子还需要进行更多地配置。下面进行详细解释。

## 内容

最简单的方法是使用markdown进行编写。和一般的markdown有点区别的是，需要在开头写明metadata信息，方便网站进行引用。
常用的metadata有以下几种：

```
Title: 标题
Date: 创建时间
Modified: 修改时间
Category: 分类，一般只有一个
Tags: 标签，可以有多个
Slug: 文章的URL别名，只有一个
Authors: Feng Zhang
Lang: zh
```

## 发布

写的网站如何进行发布呢？一般得买域名并进行渲染，这个有点麻烦。有个最简单的方法是使用Github Pages，即把生成好的静态文件（HTML/CSS/JS）上传到 GitHub 仓库的指定仓库，然后 GitHub 自动帮你部署成网站。访问网址为`https://username.github.io/仓库名`，比如我把静态文件上传blog-content仓库，访问网站即为 `https://feng-zhang.github.io/blog-content/`。

把output下文件push到github后，打开网站后是404，原因是github page没有配置。
GitHub Pages 不会自动帮你把仓库“变成网站”，需要进行配置：
1.去 GitHub 仓库：Settings → Pages
2.然后设置：

```
Source: Deploy from a branch
Branch: master
Folder: / (root)
```

## 设置

比较麻烦的还是配置这块，详细配置示例可以到https://github.com/Feng-Zhang/blog-pelican/blob/master/pelicanconf.py 查看。

### 时间和日期

LOCALE：控制博客“时间/日期/语言显示风格”，让文章看起来符合中文或英文习惯。

## 插件

pelican从3.0版本开始支持插件。通过插件，不必直接修改Pelican的核心代码就可以给Pelican添加新功能。

### 1 如何使用插件

Pelican从4.5版本开始使用了一种全新的插件结构，利用了命名空间包，并且可以轻松地通过 Pip 进行安装。支持此结构地插件都会被安装在命名空间包 pelican.plugins 下，因此Pelican可以自动发现他们。下面的命令可以用于查看环境中用Pip安装的所有插件：`pelican-plugins`

若将 PLUGINS 配置项设为默认的 None ，Pelican会自动发现命名空间中的插件并且将他们全部加载；若你在 PLUGINS 设置项中指定了一系列的插件，Pelican就不会去自动发现插件，也就是说，你需要显式地指定所有要使用的插件。
在配置 PLUGINS 时，有两种方式。一是用字符串列表指定插件的名称，可以是包含命名空间的完整名称（例如 pelican.plugins.myplugin ），也可以是简短名称（ myplugin）：

```
PLUGINS = ['package.myplugin',
           'namespace_plugin1',
           'pelican.plugins.namespace_plugin2']
```

二是在设置文件中先import进来，再将import进的模块放在 PLUGINS 设置项中：

```
from package import myplugin
from pelican.plugins import namespace_plugin1, namespace_plugin2
PLUGINS = [myplugin, namespace_plugin1, namespace_plugin2]
```

在尝试不同的插件时（尤其是那些处理元数据和内容的插件），缓存可能会相互干扰，一些更改不会生效。发生这种情况时，就需要通过设置 LOAD_CONTENT_CACHE = False 或使用 --ignore-cache 命令行选项禁用缓存。
如果插件处于无法直接进行import的路径，可以在 PLUGIN_PATHS 配置项中指定这些路径。如下例所示， PLUGIN_PATHS 中的路径可以是绝对的，也可以是相对于设置文件的：

```
PLUGIN_PATHS = ["plugins", "/srv/pelican/plugins"]
PLUGINS = ["assets", "liquid_tags", "sitemap"]
```

### 2 在哪儿下载插件

新的命名空间插件可以在GitHub的 [pelican-plugins 组织](https://github.com/pelican-plugins) 中找到，每个插件都是一个独立的仓库。而老的插件则可以在GitHub的 [pelican-plugins 仓库](https://github.com/getpelican/pelican-plugins) 中找到。这些老的插件会逐步淘汰并转移到新的命名空间版本。

### pelican-extract-toc

pelican显示markdown时，将toc展示出来

```
# 在老系统中，需要手动clone
git clone  https://github.com/getpelican/pelican-plugins
pip install beautifulsoup4 # 安装依赖
```

### 双语插件

在新仓库中，直接使用pip安装

```
pip install pelican-i18n-subsites
```

## 主题

### 1.下载主题

```
git clone https://github.com/getpelican/pelican-themes

# 只下载 Elegant 这个主题。
git submodule update --init elegant

# 如果想下载所有主题，速度有点慢：
git submodule update --init --recursive
# 或者一开始就：
git clone --recursive https://github.com/getpelican/pelican-themes
```

### 2.配置主题

在pelicanconf.py中配置THEME = "pelican-themes/elegant"

## 评论

1. elegant主题有内置评论系统Utterances。只要在在 pelicanconf.py 中加入 Utterances 配置，文章页会加载评论组件。

```
# Comments (Utterances → GitHub Issues: Feng-Zhang/blog-pelican-comment)
UTTERANCES_REPO = "Feng-Zhang/blog-pelican-comment"
UTTERANCES_THEME = "github-light"
COMMENTS_INTRO = "欢迎留言，使用 GitHub 账号登录即可评论。"
```

publishconf.py 会继承这些设置，发布时无需再改。
你还需要在 GitHub 上完成这几步（否则评论区会空白或报错）：
2. 确认 Feng-Zhang/blog-pelican-comment 是 公开仓库
3. 在仓库 Settings → General → Features 里开启 Issues
4. 打开 https://utteranc.es/，安装 Utterances GitHub App，并授权该仓库
完成后重新部署网站，打开任意文章页，点击 Comments 折叠区即可看到评论框。

可选设置：
某篇文章不想开评论，在 front matter 里加 comments: false
深色主题可改 UTTERANCES_THEME = "github-dark"
关闭某篇评论：utterances_filter: on（需同时设 UTTERANCES_FILTER = True）

## 参考资料

- Pelican document： https://docs.getpelican.com/en/latest/
- pelican github: https://github.com/getpelican/pelican
- pelican主题：https://github.com/getpelican/pelican-themes

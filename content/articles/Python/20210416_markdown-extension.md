Title: pelicanで使っているmarkdownモジュール拡張

[TOC]

# 概要

Pythonのmarkdownモジュールには公式/非公式な拡張があり、本来の(今から見ると少々機能に乏しい)markdown仕様に機能を追加することができます。pelicanでは下記の通りデフォルトで幾つかの公式拡張を有効にしています。

~~~
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}
~~~

本記事ではpelicanデフォルトの拡張の他に導入した方が便利そうな拡張を提示しておきます。

# toc

本記事冒頭の様な目次を以下の記述で追加できる拡張です。

~~~ text
[TOC]
~~~

導入するにはpelicanconf.pyに以下を記述する。...としたのは他の拡張に追記することを意図して。

~~~
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        ...
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}
~~~

# mdx_linkify

角括弧で囲まずともURLを記述するだけでリンク化してくれる拡張です。個人的にはこれと脚注の組み合わせがmdとhtmlどちらもいい感じになって好き。導入するにはpipでmdx-linkifyをインストールして...

~~~
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        ...
        'mdx_linkify.mdx_linkify': {},
    },
    'output_format': 'html5',
}
~~~

# nl2br

デフォルトではブロック中の改行はmdの視覚的整理に優先されて改行と扱われませんが、この拡張を使用すると改行が反映される様になります。当然ながら2回以上改行して空の行を挟むと段落として扱われるので注意。導入するには...

~~~
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        ...
        'markdown.extensions.nl2br': {},
    },
    'output_format': 'html5',
}
~~~

# markdown_del_ins

以前の記事で取り消し線と下線をHTMLタグを使って表現する方法を紹介しましたが、mdの記述をより自然にするならこちらがベターです。

~~~
<ins>こう</ins>やったり<del>こう</del>してたのを

+++こう+++したり~~~こう~~~できる
~~~

<ins>こう</ins>やったり<del>こう</del>してたのを

++こう++したり~~こう~~できる

導入するにはpipでmarkdown-del-insをインストールして...

~~~
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        ...
        'markdown_del_ins': {},
    },
    'output_format': 'html5',
}
~~~

# adomonition

Tipsやコメント等、コラム調の表現が出来ます。デフォルトで幾つかのタイトルに対応しているはずですが、テーマが使用しているCSSにもよると思われます。

~~~
!!! test
    テスト

!!! tip
    Tips

!!! hint
    ヒント

!!! note
    ノート

!!! important
    重要

!!! attention
    注意

!!! warning
    警告

!!! danger
    危険

!!! error
    エラー
~~~

!!! test
    テスト

!!! tip
    Tips

!!! hint
    ヒント

!!! note
    ノート

!!! important
    重要

!!! attention
    注意

!!! warning
    警告

!!! danger
    危険

!!! error
    エラー

導入するには...

~~~
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        ...
        'markdown.extensions.admonition': {},
    },
    'output_format': 'html5',
}
~~~


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import fibo

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "fibo"
copyright = "2023, yamaimo"
author = "yamaimo"
release = fibo.__version__

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.githubpages",
    "myst_parser",
    "autodoc2",
]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

templates_path = ["_templates"]
exclude_patterns: list[str] = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]


# Settings for MyST

myst_enable_extensions = [
    "replacements",  # (c)などを©などに置き換える
    "smartquotes",  # '...', "..."を開き/閉じのグリフに変更する
    "strikethrough",  # ~~...~~による打ち消し線
    "dollarmath",  # $...$, $$...$$による数式サポート
    "amsmath",  # amsmathのサポート（\begin{align}...\end{align}などを直接書ける）
    "linkify",  # URLにリンクがつく
    "substitution",  # 置換の設定をし、{{<key>}}で設定した文字列に置換する
    "colon_fence",  # :::でコードブロックを書ける（directiveに使うといい）
    "deflist",  # 定義リスト
    "tasklist",  # タスクリスト
    "fieldlist",  # API記述のパラメータなどで使う
    "attrs_block",  # ブロック要素の前に{...}で属性指定
    "attrs_inline",  # インライン要素の後ろに{...}で属性指定
    "html_image",  # img要素をsphinxの内部表現に変換する
    "html_admonition",  # admonitionクラスのdiv要素をsphinxの内部表現に変換する
]


# Settings for autodoc2

autodoc2_packages = [
    "../fibo",
]

autodoc2_render_plugin = "myst"

autodoc2_hidden_objects = ["private", "inherited"]

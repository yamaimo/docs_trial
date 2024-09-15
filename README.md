# docs_trial

Sphinxを利用してドキュメントを用意し、GitHub Pagesで公開してみる。

## はじめる

`pyproject.toml`でパッケージを追加しインストール：

```toml
[project.optional-dependencies]
develop = [
    # ...
    "sphinx",
]
```

クイックスタートで始める：

```console
sphinx-quickstart
```

ソースディレクトリとビルドディレクトリは分けるようにした。

公開用にビルドの出力先は`docs/`へ。
`.nojekyll`を追加。

"Settings" > "Pages" > "Branch"で、"main"ブランチの`/docs`を指定して"Save"を押す。
https://yamaimo.github.io/docs_trial/ で公開された。

## Markdownの導入

`pyproject.toml`で`myst-parser`パッケージを追加しインストール
（機能拡張で`linkify`を使う場合、`myst-parser[linkify]`でインストール）：

```toml
[project.optional-dependencies]
develop = [
    # ...
    "myst-parser[linkify]",
]
```

`conf.py`でMarkdown用の設定を追加：

```python
# 拡張を追加
extensions = [
    # ...
    "myst_parser",
]

# 拡張子の設定
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
```

MyST用の設定も`conf.py`に追加する。

```python
myst_enable_extensions = [
    # 詳細はconf.pyを見ること
    ...
]
```

ディレクティブは以下の形で書く：

<pre>
```{directivename} arguments
:key1: val1
:key2: val2

This is
directive content
```
</pre>

ロールは以下の形で書く：

```
{role-name}`role content`
```

## APIリファレンスの自動生成

`pyproject.toml`で`sphinx-autodoc2`パッケージを追加しインストール：


```toml
[project.optional-dependencies]
develop = [
    # ...
    "sphinx-autodoc2",
]
```

`conf.py`でautodoc2の拡張を追加：

```python
# 拡張を追加
extensions = [
    # ...
    "autodoc2",
]
```

autodoc2用の設定も`conf.py`に追加する。

```python
# 自動生成の対象のパッケージを指定
autodoc2_packages = [
    "../fibo",
]

# docstringでMarkdownを使えるようにし、
# 生成される文書もMarkdownにする
autodoc2_render_plugin = "myst"

# 自動生成しない対象を指定
autodoc2_hidden_objects = ["private", "inherited"]
```

自動生成された文書は`sphinx/apidocs/`以下に出ていた。
（このパスを変えたい場合、`autodoc2_output_dir`の設定を変える）

あとは生成された文書を目次に追加する必要がある：

<pre>
```{toctree}
...

apidocs/index  # これを追加
```
</pre>

## テーマの変更

ここではテーマをFuroにしてみる。

`pyproject.toml`で`furo`パッケージを追加しインストール：

```toml
[project.optional-dependencies]
develop = [
    # ...
    "furo",
]
```

`conf.py`でテーマを変更：

```python
# テーマを変更
html_theme = "furo"
```

## （補足）autodoc+napoleonの試し

autodoc2ではNumPyスタイルのdocstringをいい感じに扱えなかった。
そこでautodoc+napoleonの組み合わせを試してみた。

この場合、単にビルドするだけだとAPIドキュメントが生成されないので、
事前に`sphinx-apidoc`で生成する必要がある
（プレースホルダーの文書が出来て、その内容がビルド時に埋められるイメージ）。

ただ、これで生成される文書が微妙。
なので、自前でAPIドキュメントを用意して、その中でディレクティブを指定する感じっぽい。
ちょっと面倒。

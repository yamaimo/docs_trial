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

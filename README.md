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

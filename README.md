# liqsuq.github.io

```
$ sudo apt-get install ruby-full build-essential zlib1g-dev
$ echo '# Install Ruby Gems to ~/gems' >> ~/.bashrc
$ echo 'export GEM_HOME="$HOME/gems"' >> ~/.bashrc
$ echo 'export PATH="$HOME/gems/bin:$PATH"' >> ~/.bashrc
$ source ~/.bashrc
$ gem install jekyll bundler no-style-please
```

プロジェクト内：

```
$ jekyll new --skip-bundle .
```

Gemfileの`gem "jekyll"...`をコメントアウト・`gem "github-pages"...`をコメント解除・`gem "no-style-please"`を追加

```
$ bundle install
```


\_config.ymlを`theme: no-style-please`に変更・`plugins:`に`- jekyll-remote-theme`を追加

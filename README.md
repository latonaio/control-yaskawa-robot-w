# 概要

安川電機製ロボットコントローラYRC1000に対してイーサネット経由でデータを書き込むマイクロサービスです。

このマイクロサービスをご利用いただくには、別途安川電機製ロボットコントローラYRC1000が必要となります。

## このマイクロサービスの振る舞い


### YRC1000との入出力について

YRC1000の高速Ethernetサーバ機能に準ずる
（YRC1000の取扱説明書をご確認ください）

## セットアップ手順

### aion-coreをセットアップする

事前に下記リポジトリからaion-coreのセットアップを行ってください。

https://github.com/latonaio/aion-core

### リポジトリをクローンする

このリポジトリをgit cloneしてください

git clone https://github.com/latonaio/control-yaskawa-robot-w.git

### Dockerイメージをビルドする

付属のスクリプトを使用して、control-yaskawa-robot-wのDockerイメージをビルドしてください。
```
bash docker-build.sh
```


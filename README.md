# atcoder-clar2slack

## これは何

* AtCoderのクラーが来たらSlackに通知します。
* これは、owner権限持ってる前提のコンテスト管理者用のツールです
  * コンテスタントだと使えないです。

* ※AtCoder Betaには対応していません。

## 使い方

```
cp config_sample config
# edit config
./login.sh
nohup ./run.sh > ~/clar2slack.log &
```

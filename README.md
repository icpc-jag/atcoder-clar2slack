# atcoder-clar2slack

## これは何

![サンプル画像](https://imgur.com/9T2Tg7W.png)

* ↑のような感じで、AtCoderの質問(Clarification)が来たらSlackに通知します。
* Manager権限を持っている前提のコンテスト管理者用のツールのため、Contestantだと使えません。
* 旧サイト(`https://xxx.contest.atcoder.jp`)の廃止に伴い、新サイト(`https://atcoder.jp/contests/xxx`)に対応しました。

## 使い方

1. 設定のサンプルファイルを config というファイル名としてコピー。

```
cp config_sample config
```

2. configファイルを以下の例に従って編集。

```
CONTEST_URL=https://atcoder.jp/contests/jag2017autumn/         # クラー通知したいコンテストのURL
ATCODER_ID=username                                            # コンテストの管理権限を所持しているユーザのID
ATCODER_PASS=password                                          # ユーザのパスワード
SLACK_HOOK_URL=https://hooks.slack.com/services/XXXX/XXXX/XXXX # slackのincoming webhook url ※1
SLEEP_TIME=10                                                  # 最新クラーを取得するポーリングの間隔(秒)
```

※1 以下のURLから、incoming webhook urlを生成できます。  
  https://slack.com/apps/A0F7XDUAZ-incoming-webhooks

3. AtCoderへログインするためのスクリプトを実行。

```
./login.sh
```

4. クラーチェックスクリプトを起動。

```
nohup ./run.sh > ~/clar2slack.log &
```

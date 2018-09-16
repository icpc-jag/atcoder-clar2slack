import json
import subprocess
import sys

SLACK_SH = sys.argv[3]

def question_json(clar_no, info):
    return json.dumps({"attachments":[{
        "pretext": "<!here>",
        "title": "[Clar No.{clar_no}]".format(clar_no=clar_no),
        "color": "good",
        "fields": [
            {"title": "問題名", "value": info["title"], "short": "true"},
            {"title": "ユーザ名", "value": info["user_name"], "short": "true"},
            {"title": "質問", "value": info["question"]}
        ],
        "actions": [
            {"type": "button", "text": "回答する", "url": info["update_url"]}
        ]
    }]})

def response_json(clar_no, info):
    return json.dumps({"attachments":[{
        "title": "[Clar No.{clar_no} に回答しました]".format(clar_no=clar_no),
        "color": "#439FE0",
        "fields": [
            {"title": "問題名", "value": info["title"], "short": "true"},
            {"title": "ユーザ名", "value": info["user_name"], "short": "true"},
            {"title": "質問", "value": info["question"]},
            {"title": "回答", "value": info["response"]},
            {"title": "全体公開", "value": info["public"], "short": "true"}
        ],
        "actions": [
            {"type": "button", "text": "回答を修正する", "url": info["update_url"]}
        ]
    }]})

with open(sys.argv[1], encoding="utf8") as f:
    a = json.loads(f.read())
    data_before = {x["update_url"]: x for x in a}

with open(sys.argv[2], encoding="utf8") as f:
    data_after = json.loads(f.read())

for x in data_after:
    update_url = x["update_url"]
    clar_no = update_url.split("/")[-1]
    if update_url in data_before:
        y = data_before[update_url]
        if x["response"] != y["response"] or x["public"] != y["public"]:
            subprocess.call(["/bin/bash", SLACK_SH, response_json(clar_no, x)])
    else:
        subprocess.call(["/bin/bash", SLACK_SH, question_json(clar_no, x)])

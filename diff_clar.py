import json
import subprocess
import sys

SLACK_SH = sys.argv[3]

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
            s = "[Clar No.{clar_no} に回答しました]\n問題名：{title}\nユーザ名：{user_name}\n質問：{question}\n回答：{response}\n全体公開：{public}\n<{update_url}|質問に回答する>".format(
                clar_no=clar_no,
                title=x["title"],
                user_name=x["user_name"],
                question=x["question"],
                response=x["response"],
                public=x["public"],
                update_url=x["update_url"],
            )
            subprocess.call(["/bin/bash", SLACK_SH, json.dumps({"text": s})])
    else:
        s = "[Clar No.{clar_no}]\n問題名：{title}\nユーザ名：{user_name}\n質問：{question}\n<{update_url}|質問に回答する>".format(
            clar_no=clar_no,
            title=x["title"],
            user_name=x["user_name"],
            question=x["question"],
            update_url=x["update_url"],
        )
        subprocess.call(["/bin/bash", SLACK_SH, json.dumps({"text": s})])

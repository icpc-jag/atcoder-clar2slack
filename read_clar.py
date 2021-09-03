import json
import re
import sys

SAVE_PATH = sys.argv[2]


data = []
with open(sys.argv[1], encoding="utf-8") as f:
    tbody = re.findall(r"<tbody>.*?</tbody>", f.read(), re.S)
    if not tbody:
        print("<tbody> not found")
    else:
        assert len(tbody) == 1
        rows = re.findall(r"<tr.*?</tr>", tbody[0], re.S)
        for row in rows:
            columns = re.findall(r"<td.*?</td>", row, re.S)

            title = re.sub(r"\s+", " ", columns[0])[4:-5].strip()
            if title == "":
                title = "（指定なし）"
            else:
                m = re.search(r"<a href=\"(.*)\">(.*)</a>", title)
                title = "<%s|%s>" % ("https://atcoder.jp" + m.group(1), m.group(2).strip())

            m = re.search(r"<a href=\"(.*)\" .*\"><span.*>(.*)</span></a>.*<a.*", re.sub(r"\s+", " ", columns[1]))
            user_name = "<%s|%s>" % ("https://atcoder.jp" + m.group(1), m.group(2))

            assert re.fullmatch(r"<td>.*</td>", columns[2], re.S)
            assert re.fullmatch(r"<td>.*</td>", columns[3], re.S)
            question = re.sub(r"<.*?>", "", columns[2][55:-11]).replace("&#039;", "'")
            response = re.sub(r"<.*?>", "", columns[3][55:-11]).replace("&#039;", "'")
            public = re.sub(r"<.*?>", "", columns[4][4:-5])
            update_url = "https://atcoder.jp" + re.search(r"<a href=\"(.*?)\">", columns[7]).group(1)

            data.append({
                "title": title,
                "user_name": user_name,
                "question": question,
                "response": response,
                "public": public,
                "update_url": update_url,
            })

with open(SAVE_PATH, "w", encoding="utf8") as f:
    f.write(json.dumps(data, ensure_ascii=False))

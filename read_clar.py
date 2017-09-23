import json
import re
import sys

CONTEST_URL = sys.argv[2]
SAVE_PATH = sys.argv[3]

def func(s):
    m = re.search(r"<a href=\"(.*)\">(.*)</a>", s)
    return "<%s%s|%s>" % (CONTEST_URL, m.group(1), m.group(2))


data = []
with open(sys.argv[1], encoding="utf-8") as f:
    a = re.findall(r"<tbody>.*?</tbody>", f.read(), re.S)
    assert len(a) == 1
    a = re.findall(r"<tr>.*?</tr>", a[0], re.S)
    for x in a:
        b = re.findall(r"<td.*?</td>", x, re.S)
        title = func(b[0])
        user_name = func(b[1])
        assert re.fullmatch(r"<td>.*</td>", b[2], re.S)
        assert re.fullmatch(r"<td>.*</td>", b[3], re.S)
        question = re.sub(r"<.*?>", "", b[2][4:-5])
        response = re.sub(r"<.*?>", "", b[3][4:-5])
        public = re.sub(r"<.*?>", "", b[4])
        update_url = CONTEST_URL + re.search(r"<a href=\"(.*?)\">", b[7]).group(1)

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

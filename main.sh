set -e
source ./config
curl -s -b ./cookiejar "${CONTEST_URL}/clarifications" > ./clar.html
python3 ./read_clar.py ./clar.html ${CONTEST_URL} ./clar1.json
if [[ -e ./clar0.json ]]; then
  python3 ./diff_clar.py ./clar0.json ./clar1.json ./slack.sh
fi
mv ./clar1.json ./clar0.json

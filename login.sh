set -e
source ./config
LOGIN_URL='https://atcoder.jp/login'
CSRF_TOKEN=$(curl -c ./cookiejar -s ${LOGIN_URL} | grep 'csrfToken' | cut -f 2 -d '"')
curl -b ./cookiejar -c ./cookiejar -X POST -F "csrf_token=${CSRF_TOKEN}" -F "username=${ATCODER_ID}" -F "password=${ATCODER_PASS}" "${LOGIN_URL}"

set -e
source ./config
curl -c ./cookiejar -F "name=${ATCODER_ID}" -F "password=${ATCODER_PASS}" "${CONTEST_URL}/login"

source ./config
curl -s -X POST -H 'Content-type: application/json' --data "$1" ${SLACK_HOOK_URL}

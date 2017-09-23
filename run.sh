source ./config
while :; do
  date
  ./main.sh
  sleep ${SLEEP_TIME}
done

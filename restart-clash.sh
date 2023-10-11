cd "$(dirname "$0")"
sudo lsof -i:7890 | grep LISTEN | awk -F " " '{print $2}' | xargs kill || echo failed to stop
nohup clash -d . 1>clash-log.log 2>&1 &
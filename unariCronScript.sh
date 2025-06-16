#!/bin/bash

# this script is intended for a cronjob
# therefore all paths must be absolute

# checks for internet connection, if one is not found, it will retry N times and then exit

TIME_TO_SLEEP=60 # seconds
RETRY_TIMES=10 # number of retries

#SCRIPT_DIR="/home/ohinfotaulu/INFOTAULU/unari_grep/"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

while true; do
    wget -q --spider http://google.com
    if [ $? -eq 0 ]; then
        python3 $SCRIPT_DIR/getMap.py 
        python3 $SCRIPT_DIR/kanttiinitgrep.py > $SCRIPT_DIR/data.txt
        break
    else
        sleep $TIME_TO_SLEEP
        RETRY_TIMES=$((RETRY_TIMES - 1))
        if [ $RETRY_TIMES -le 0 ]; then
            echo "No internet connection after multiple attempts. Exiting." > $SCRIPT_DIR/data.txt
            exit 1
        fi
    fi
done 
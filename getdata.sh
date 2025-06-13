#!/bin/bash

# this script is used to write the output of the menu getter to a file.
# It checks for an internet connection and then runs the menu getter script.
# If no internet connection is found, it will sleep and retry after a time.

TIME_TO_SLEEP=60 # seconds
RETRY_TIMES=10 # number of retries


SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

#!/bin/bash
while true; do
    wget -q --spider http://google.com
    if [ $? -eq 0 ]; then
        python3 $SCRIPT_DIR/getMap.py 
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

while true; do
    python3 $SCRIPT_DIR/kanttiinitgrep.py > $SCRIPT_DIR/data.txt
    sleep 3600
    #Sleep for 1 hour before running the script again, checking only the restaurants which are listed in .env
done
#!/bin/bash

# this script is used to write the output of the menu getter to a file.
# It checks for an internet connection and then runs the menu getter script.
# If no internet connection is found, it will sleep and retry after a time.

TIME_TO_SLEEP=60 # seconds
RETRY_TIMES=10 # number of retries

CURRENT_DIR=$(pwd)

#!/bin/bash

while true; do
    wget -q --spider http://google.com
    if [ $? -eq 0 ]; then
        #internet connection is available
        python3 $CURRENT_DIR/kanttiinitgrep.py > $CURRENT_DIR/data.txt
        exit 0
    else
        sleep $TIME_TO_SLEEP
        RETRY_TIMES=$((RETRY_TIMES - 1))
        if [ $RETRY_TIMES -le 0 ]; then
            echo "No internet connection after multiple attempts. Exiting." > $CURRENT_DIR/data.txt
            exit 1
        fi
        #echo "No internet connection. Retrying in $TIME_TO_SLEEP seconds..."
    fi
done
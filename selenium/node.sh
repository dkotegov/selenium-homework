#!/usr/bin/env bash

CWD=$(dirname $0)

java -Dwebdriver.chrome.driver="$CWD/chromedriver" \
    -Dwebdriver.gecko.driver="$CWD/geckodriver" \
    -jar ${CWD}/selenium-server-standalone-3.0.1.jar \
    -role node \
    -hub http://localhost:4444/grid/register \
    -browser browserName=chrome,maxInstances=2 \
    -browser browserName=firefox,maxInstances=2

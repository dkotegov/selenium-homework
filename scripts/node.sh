#!/usr/bin/env bash

if [ $# -eq 0 ]
  then
    echo "Argument expected: -w <path/to/web/drivers/dir> -s <path/to/selenium/server>"
    exit 1
fi

if [ -z "$2" ] || [ -z "$4"]
  then
    echo "Argument expected: -w <path/to/web/drivers/dir> -s <path/to/selenium/server>"
    exit 1
fi


while getopts s:w: option
do
    case "${option}"
    in
        s) PATH_TO_JAR=${OPTARG};;
        w) PATH_TO_WD=${OPTARG};;
    esac
done

java -Dwebdriver.chrome.driver="./$PATH_TO_WD/chromedriver" \
    -Dwebdriver.gecko.driver="./$PATH_TO_WD/geckodriver" \
    -jar $PATH_TO_JAR/selenium-server-standalone-3.0.1.jar \
    -role node \
    -hub http://localhost:4444/grid/register \
    -browser browserName=chrome,maxInstances=2 \
    -browser browserName=firefox,maxInstances=2

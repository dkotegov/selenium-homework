#!/usr/bin/env bash

if [ $# -eq 0 ]
  then
    echo "Argument expected: -s <path/to/dir> (where selenium jar file)"
    exit 1
fi

if [ -z "$2" ]
  then
    echo "Argument expected: -s <path/to/dir> (where selenium jar file)"
    exit 1
fi

while getopts s: option
do
    case "${option}"
    in
        s) PATH_TO_JAR=${OPTARG};;
    esac
done

java -jar $PATH_TO_JAR/selenium-server-standalone-3.0.1.jar \
    -role hub

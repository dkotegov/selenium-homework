#!/usr/bin/env bash

CWD=$(dirname $0)

java -jar $CWD/selenium-server-standalone-3.0.1.jar \
    -role hub

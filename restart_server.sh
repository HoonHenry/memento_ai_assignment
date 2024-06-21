#!/bin/bash

set -e

docker rm memento_ai-server-1 memento_ai-db-1
if [ "$1" == "d" ]; then
    docker compose up --build -d
else
    docker compose up --build
    docker ps
fi

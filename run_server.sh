#!/bin/bash

set -e

if [ "$1" == "d" ]; then
    docker compose up --build -d
    docker ps
else
    docker compose up --build
fi

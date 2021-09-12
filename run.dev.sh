#!/bin/bash

IMAGE=${1:-papermerge/documentation-dev}
PORT=${2:-9012}

docker run --rm \
    -p ${PORT}:80 \
    -v "$(pwd)/src:/docs/src" \
    ${IMAGE}
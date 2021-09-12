#!/bin/bash


# Starts a docker container of given documentation image.
#
# Usage:
#
# ./run.dev.sh <HOST-PORT> <DOCKER-IMAGE>
#
# Example:
#   # run papermerge/documentation:dev image on port 8888
#   $ ./run.dev.sh 8888
#
#   # run docs:dev image on port 9988
#   $ ./run.dev.sh 9988 docs:dev
#
#   # run papermerge/documentation:dev image on port 9012
#   # ./run.dev.sh

IMAGE=${2:-papermerge/documentation:dev}
PORT=${1:-9012}

docker run --rm \
    -p ${PORT}:80 \
    -v "$(pwd)/src:/docs/src" \
    ${IMAGE}
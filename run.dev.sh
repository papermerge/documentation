#!/bin/bash

docker run --name docs-dev \
    -p 9012:80 \
    -v "$(pwd)/src:/docs/src" \
    papermerge/documentation-dev
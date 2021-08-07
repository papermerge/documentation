#!/bin/bash

docker run --name docs-dev  -p 8042:80 -v "$(pwd)/src:/docs/src" docs-dev:1.0.0
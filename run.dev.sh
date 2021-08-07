#!/bin/bash

docker run --name docs-dev  -p 8042:80 -v "$(pwd)/source:/docs/source" docs-dev
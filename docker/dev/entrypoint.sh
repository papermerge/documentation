#!/bin/sh

sphinx-autobuild \
    --host 0.0.0.0 \
    --port 80 \
    /docs/src/ \
    /docs/_build/html
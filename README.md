# Papermerge - Documentation

Papermerge documentation is based on [sphinx-doc](https://www.sphinx-doc.org)
which uses [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) as
markup language.

## Online Version

Papermerge documentation is available online at [https://docs.papermerge.io/](https://docs.papermerge.io/).

## How to Use

Make sure you have installed [python](https://www.python.org/)
and [poetry](https://python-poetry.org/docs/), then in root repository
folder run following commands::

    $ poetry install
    $ poetry run sphinx-autobuild --port 9600 src/ _build/html/

Above commands will install all dependencies, switch into environment variable
and run documentation in auto build mode. Any change in documentation
repository will be automatically rebuild.

Also, instead of `poetry run ...` command you can  use provided bash script as shortcut::

    $ ./run.dev.sh

## Docker

In order to browse documentation **locally**, get its latest docker image from docker hub:

    docker pull papermerge/documentation

``papermerge/documentation`` docker image exposes web service on port 80 i.e.
it serves static html using nginx on port 80:

    docker run -d --name docs -p 9010:80 papermerge/documentation

## Contributors

Before making changes to documentations, please make sure that:

1. Your English level is decent
2. You understand the basics of [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
format

## Repository Branches / Multi-versions

For each papermerge major version there is separate repository branch in this
repository.

Papermerge 2.0.x documentation can be found in branch 2.0.x of this
repository.
Papermerge 2.1.x documentation is found in branch 2.1.x.
Master branch in this repository corresponds to latest (in development) version
of papermerge.

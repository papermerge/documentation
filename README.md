# Papermerge - Documentation

Papermerge documentation is based on [sphinx-doc](https://www.sphinx-doc.org)
which uses [reStructuredText](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html) as
markup language.

Documentation is divided into four major sections:

1. Installation
2. Help
3. User's Manual
4. REST API

## Online Version

Papermerge documentation is available online at [https://docs.papermerge.io/](https://docs.papermerge.io/).

## How to Use

Make sure you have installed [python](https://www.python.org/)
and [poetry](https://python-poetry.org/docs/), then in root repository
folder run following commands::

    $ poetry install
    $ poetry shell
    $ sphinx-autobuild --host 0.0.0.0 --port 80 9600 src/ _build/html

Above commands will install all dependencies, switch into environment variable
and run documentation in auto build mode. Any change in documentation
repository will be automatically rebuild.

## Docker

In order to ease distribution and development two docker images are provided:

1. production
2. development


### Production Image

In order to browse documentation **locally**, get its latest docker production
image from docker hub:

    docker pull papermerge/documentation

``papermerge/documentation`` docker image exposes web service on port 80 i.e.
it serves static html using nginx on port 80:

    docker run -d --name docs -p 9010:80 papermerge/documentation



### Development Mode

In development mode docker image ``papermerge/documentation-dev`` mounts
local sources and:

1. serves it via port 80
2. automatically rebuilds (regenerates html files) when you change source code

First clone this repository:

    git clone https://github.com/papermerge/documentation


Then pull ``papermerge/documentation-dev`` image from docker hub:

    docker pull papermerge/documentation-dev

Change your current working directory to the folder where code
was cloned into and from there run:

    docker run --name docs-dev  -p 9012:80 -v "$(pwd)/src:/docs/src" papermerge/documenation-dev

In development mode only one documentation version (which corresponds to mounted sources) is rendered.

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

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
    $ poetry run task autobuild

Above commands will install all dependencies, switch into environment variable
and run documentation in auto build mode. Any change in documentation
repository will be automatically rebuild. You can access
documentation on ``http://localhost:9600``.


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

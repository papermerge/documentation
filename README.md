# Papermerge DMS Documentation

Papermerge DMS documentation is based on [mkdocs material](https://squidfunk.github.io/mkdocs-material/).

## Online Version

Papermerge DMS documentation is available online at [https://docs.papermerge.io/](https://docs.papermerge.io/)


## How to Use

Make sure you have installed [python](https://www.python.org/)
and [poetry](https://python-poetry.org/docs/), then in root repository
folder run following commands:

    $ poetry install
    $ poetry run mkdocs serve

Above commands will install all dependencies, switch into environment variable
and run documentation in auto build mode. Any change in documentation
repository will be automatically rebuild.

## Multi-versions

For each Papermerge major version there is separate repository branch in this
repository.

- Papermerge version 2.0.x docs are in git branch v2.0
- Papermerge version 2.1.x docs are in git branch v2.1
- Papermerge version 3.0.x docs are in git branch v3.0
- etc

As of writing this readme, 3.0.x is under development.

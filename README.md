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

- Papermerge version 3.3.x docs are in git branch v3.3
- Papermerge version 3.4.x docs are in git branch v3.4
- Papermerge version 3.5.x docs are in git branch v3.5

## How It Works

Documentation is deployed from `gh-pages` branch. There you will find one
fodler per each version i.e. 3.3, 3.4, 3.5.
In `gh-pages` branch there is a file `versions.json` which is used by
mike to figure out what it where. You can manually update that file.


## How to Add New Version

Say current stable is 3.4 and you want to add 3.5 as development version.
Run following commands:

```
$ git switch v3.4
$ git checkout -b v3.5
$ mike deploy -p 3.5 -t dev
```

It is very important that`v3.5` was branched from `v3.4` and not from `master`!

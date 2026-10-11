# 📢 About Papermerge OSS

This documentation covers **Papermerge OSS** (the open-source, self-hosted version).

**Status:** Actively maintained by the community maintainer team.
It was originally created by Eugen Ciur, who now focuses on Papermerge Cloud (SaaS).

- **Using Papermerge OSS?** You're in the right place — the docs below are for you.
- **Interested in the managed, GoBD-compliant version?**
  Try [Papermerge Cloud](https://papermerge.com) and see the [Cloud documentation](https://docs.papermerge.com).

For the latest source code, issues, and pull requests, see
[papermerge/papermerge-core](https://github.com/papermerge/papermerge-core).

---

# Papermerge DMS Documentation

Papermerge DMS documentation is built with [mkdocs material](https://squidfunk.github.io/mkdocs-material/).

## Online Version

The documentation is available online at [https://docs.papermerge.dev/](https://docs.papermerge.dev/).

## How to Use

Install [python](https://www.python.org/) and [poetry](https://python-poetry.org/docs/), then run the following commands in the repository's root folder:

    $ poetry install
    $ poetry run mkdocs serve

This installs all dependencies and starts the documentation server in auto-build mode, so any change is rebuilt automatically.

## Multi-Version Support

Each Papermerge major version has its own branch in this repository:

| Papermerge version | Git branch |
|---|---|
| 3.3.x | `v3.3` |
| 3.4.x | `v3.4` |
| 3.5.x | `v3.5` |

## How It Works

Documentation is deployed from the `gh-pages` branch, which contains one folder per version (e.g. 3.3, 3.4, 3.5). The `versions.json` file in that branch tells [mike](https://github.com/jimporter/mike) which version is where; you can update it manually if needed.

## How to Add a New Version

Say the current stable version is 3.4 and you want to add 3.5 as a development version:

```
$ git switch v3.4
$ git checkout -b v3.5
$ mike deploy -p 3.5 -t dev
```

It is very important that `v3.5` is branched from `v3.4` and **not** from `master`!

# Papermerge CLI

Command line utility which uses REST API to interact with your {{ extra.project }}
instance. It can be used to upload documents from local filesystem to yout {{ extra.project }}
instance.

![](../img/cli//upload-documents-from-local-folder.gif)


## Requirements


In order to use `papermerge-cli` you need to have python installed.
You need python version >= 3.10.

## Install

Install `papermerge-cli` with following command:

    pip install papermerge-cli

pip is package installer for python - it usually comes with python
interpreter. In order to install pip on Ubuntu use following command:

    sudo apt install python3-pip


## Configuration

Papermerge Cli is configured via environment variables:

* `PAPERMERGE_CLI__HOST`
* `PAPERMERGE_CLI__TOKEN`

as the name suggests, the first one is the host of the REST API server
and second value is the REST API token.

REST API server should be specified with `http://` or `https://`
prefix, but without the `/api` suffix. Valid values examples: http://papermege.local,
https://my-dms.papermerge.de.

!!! note

     The host may or may not contain the `/`. E.g. http://papermege.local and
    http://papermerge.local/ are both valid values and point to the same host


REST API token can be obtained from {{ extra.project }} `user menu -> API Tokens <rest_api_token>`.


## ls

List the content of you home folder:

      papermerge-cli ls

In order to list content of specific folder (including inbox folder)::

      papermerge-cli ls --parent-uuid=UUID-of-the-folder

## me

In order to see current user details use `me` command:

      papermerge-cli me


## import

Recursively imports documents and folders from local filesystem. For example, in order
to import recursively all documents from local folder:

    papermerge-cli import /path/to/local/folder/

You can also import one single document:

    papermerge-cli import /path/to/some/document.pdf

By default all documents are imported to your user's `.inbox` folder. If you
want to import to another folder, use `--target-uuid`:

    papermerge-cli import /path/to/some/document.pdf --target-uuid <uuid>

In order to learn UUID of the folder you want to import to use `papermerge-cli
ls` command. To get UUIDs of `.home` and `.inbox` folders, use
`papermerge-cli me` command.


If you want the local copy the uploaded documents to be deleted after
successful import - use `--delete` flag:

    papermerge-cli import --delete /path/to/folder/


!!! danger

     Be careful with `--delete` flag! When present,
   `papermerge-cli` will irreversible delete the local copy of all
   documents and folders in the `/path/to/folder/`!

!!! danger

    Always, before using this flag make safe backup of the documents to be uploaded!

!!! note: `--delete` flag deletes the local copy of the documents/path to import
    after successful upload - this means that even if though you local copy
    of the documents vanished - the originals are still available in {{ extra.project }}!


## help

In order to get general help about the command use:

      papermerge-cli --help

In order to get help for individual commands, place `--help` flag after the command:

      papermerge-cli import --help
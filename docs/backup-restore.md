# Backup/Restore


{{ extra.project }} is shipped with two Django managements commands for performing backup/restore operations.


## Backup

Invoke backup command using Django's manage.py:

    ./manage.py backup <optional-location>


where `<optional-location>` is the path to where to save backup file. If location
is not provided, backup file will be saved in current folder.


Backup command can be invoked via docker container as follows:

    docker run papermerge/papermerge backup /place/backup/file/here/

The result of backup operation is a (zipped) tar archive which
contains following:

1. `backup.json` file
2. `sidecars/` folder
3. `docs/`  folder
4. `username1`/, `username2`, ... i.e. one folder per user with folder title being user's username

`backup.json` file contains all necessary info to restore the database.
(all users, their nodes, tags etc).
`sidecars/` contains the exact content of <media_root>/sidecars/ folder
`docs/` contains the exact content of <media_root>/docs/ folder

`backup.json` is used to backup/restore database content.
`sidecars/` and `docs/` are used to backup/restore associated files.

Folder mentioned in point 4. contain same folder structure as users see in web
frontend, grouped by username. Instead of documents, in folder structure
symbolic links are used. Symbolic links point to the last version
(i.e. associated file) of the document. Whatever is in these folders
(in <username1>, <username2>, ...) is NOT used to restore the data (i.e. it
is redundant) instead they are human-readable i.e. make backup archive easier
to use by human to quickly assert the content of the archive.


## Restore

Invoke restore command using Django's manage.py:

    ./manage.py restore <path/to/backup-archive>


Restore command can be invoked via docker container as follows::

    docker run papermerge/papermerge restore backup-archive.tar.gz


Note that before restoring the backup archive, the DB schema should exist i.e.
all required tables with correct schema should be already in database.
You create schema by running `migrate` command (this is Django native management command):

    ./manage.py migrate


## Backup


For peace of mind you always need to backup data. There three aspects of full backup:

* media directory
* database
* application version

If all you want is to just to ensure safe copy of you documents then all you need to
do is to backup media directory.
If you want to create full snapshot (i.e you want to be able to restore full application state from specific moment in past) then you need media directory backup + database backup + Papermerge version
of that specific moment in time.


## Media Directory

Media directory is place where Papermerge application saves all your original
documents and their derivatives (extracted text, images etc). By backing
up your media directory - you ensure your documents are safe.

Media directory is configured with :ref:`media_dir` setting. By default it is a folder
named "media" in of same directory where papermerge project was cloned.

!!! note

    `media_dir` has two subfolders *docs* and *results*. `media_dir`/docs is place where
    original documents are uploaded - it is the location you want to ensure is regularly backed up.
    Media directory configuration is pure Django web framework thing; in Django it is called <a href="https://docs.djangoproject.com/en/3.1/ref/settings/#media-root" class="external-link" target="_blank">MEDIA_ROOT </a>

!!! note

    **Papermerge never overwrites or renames original uploads!**, in that sense, Papermerge is non-destructive :ref:`dms`. Every time you perform changes on document, like :ref:`moving pages around <page_management>` a new document version is created, thus keeping original document version intact.


### Database

Another important part of whole backup picture - is backing up your Papermerge database. In database, Papermerge stores information like user related information, documents' metadata, documents' tags etc.

!!! note

    Uploaded documents are NOT stored in database! Uploaded files are stored (by default) on local filesystem.
    In general, binary files are never stored in databases.

Basically with database backup you can restore "the state" of Papermerge application.


### Application Version

If you want to restore Papermerge backups you need to know for what
application version that backup is. This is why it is a good idea to append
Papermerge application version to your backup archives.


### Backup Utility

Papermerge is shipped with backup command line utility. You can run it from project current directory:

```console
./manage.py backup
```

That command will backup all your documents with preserved directory structure (it will backup documents of all users).

!!! note

    provided backup utility does not backup tags and metadata information.


In order to restore backup:

```console
./manage.py restore <path-to-tar-file>
```
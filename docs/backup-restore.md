# Backup/Restore


{{ extra.project }} docker image is shipped with backup and restore utilities.
Shipped utility will backup all your folders, documents with their associated versions
and OCR data, tags and users. Search engine index is not included in backup though.

!!! Note

    User passwords are included in backup file as well. Passwords are stored
    as digests.

## Backup

Backup your documents with following command:

    $ docker exec <papermerge-server-container> backup.sh <optional-location>


where `<optional-location>` is the path to file or folder **inside container** where to save backup
file. If location is not provided, backup file will be saved in /core_app/ folder
- the papermerge core application's current folder.

Example:

```
    $ docker ps --format '{\{.ID\}} {\{.Command\}} {\{.Names\}}'

    914dda21dd3d "/run.bash server" 091223_30-web-1
    42095cee91f0 "docker-entrypoint.s…" 091223_30-solr-1
    d65b3205d9ec "/run.bash worker" 091223_30-worker-1
    ac5cfd76993a "docker-entrypoint.s…" 091223_30-redis-1
    8ad6d0a7eb6c "/opt/bitnami/script…" 091223_30-db-1
```

In above example the {{ extra.project }} has 5 containers: app server (the core
or web or http or REST API server, pick the name you like :P), solr search
engine, redis, database and finally one paper worker.

To create a backup in root folder of the app container just run:

    $ docker exec 914dda21dd3d backup.sh /

When above command is ready, check that backup file was created:

    $ docker exec 914dda21dd3d ls /

    auth_server_app
    backup_10_12_2023-11_30_37.tar.gz
    bin
    boot
    ...
    core_app
    core_ui
    db
    ...
    usr
    var

Backup file is backup_10_12_2023-06_30_37.tar.gz.
Now you can copy backup file to your local filesystem:

    $ docker cp 914dda21dd3d:/backup_10_12_2023-06_30_37.tar.gz .


You may choose to name file differently:

    $ docker exec 914dda21dd3d backup.sh /my-daily-backup.tar.gz

Then copy it to your local filesystem:

    $ docker cp 914dda21dd3d:/my-daily-backup.tar.gz .


!!! Note

    Backup files are gzipped tar archives, thus you probably want to
    append ".tar.gz" to their name.


## Restore

When you plan to restore previous backup, we suggest to start with new {{ extra.project }} instance,
with only one superuser (which is created by
default anyway). Make sure there are no documents in the new instance.

For sake of example, let's say the superuser's username is "admin".
For restoring use `restore.sh` command:

    $ docker exec <papermerge-server-container> restore.sh <backup-file>

For that to work, you need first to copy backup archive file
to core (server) container. Sticking with example from previous section:

    $ docker cp my-backup.tar.gz 914dda21dd3d:/my-backup.tar.gz
    $ docker exec 914dda21dd3d restore.sh /my-backup.tar.gz


If "admin" user already existed in backup file, then admin's password will
be set to the one from the backup file.


## Backup File Structure

The backup file is a gzipped tar archive with following content:

1. `backup.json` file
2. `ocr/` folder
3. `docvers/`  folder
4. `username1`/, `username2`, ... i.e. one folder per user with folder title being user's username

`backup.json` file contains all necessary info to restore the database i.e.
all users, their nodes, tags etc.

`docvers/` contains actually document versions files. Your documents are here.

`ocr/` contains OCR data of each individual page in the document.

User folders mentioned in point 4. are provided for convenience, so that you
may quickly get an understanding of the folder structure and their content.
Each file in user folder is actually a symbolic link pointing to the last
version of the document (from `docvers`).


!!! Warning

    Each user has two special folders: `.home` and `.inbox`; special folder's title
    start with dot. If you open backup archive in file browsers which hides dot files
    (file starting with dot character) - the content of user folder may appear
    empty! When opening backup archive **make sure you set 'show hidden files flag' on**.


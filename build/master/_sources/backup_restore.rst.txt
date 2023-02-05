Backup/Restore
==============

|project| is shipped with two Django managements commands for performing backup/restore operations.


Backup
-------

Invoke backup command using Django's manage.py::

    $ ./manage.py backup <optinal-location>


where ``<optional-location>`` is the path to where to save backup file. If location
is not provided, backup file will be saved in current folder.


Backup command can be invoked via docker container as follows::

    $ docker run papermerge/papermerge backup /place/backup/file/here/

The result of backup operation is a (zipped) tar archive which
contains following:

1. ``backup.json`` file
2. ``sidecars/`` folder
3. ``docs/``  folder
4. <username1>/, <username2>, ... i.e. one folder per user with folder title being user's username

``backup.json`` file contains all necessary info to restore the database.
(all users, their nodes, tags etc).
``sidecars/`` contains the exact content of <media_root>/sidecars/ folder
``docs/`` contains the exact content of <media_root>/docs/ folder

``backup.json`` is used to backup/restore database content.
``sidecars/`` and ``docs/`` are used to backup/restore associated files.

Folder mentioned in point 4. contain same folder structure as users see in web
frontend, grouped by username. Instead of documents, in folder structure
symbolic links are used. Symbolic links point to the last version
(i.e. associated file) of the document. Whatever is in these folders
(in <username1>, <username2>, ...) is NOT used to restore the data (i.e. it
is redundant) instead they are human-readable i.e. make backup archive easier
to use by human to quickly assert the content of the archive.


Restore
-------

Invoke restore command using Django's manage.py::

    $ ./manage.py restore <path/to/backup-archive>


Restore command can be invoked via docker container as follows::

    $ docker run papermerge/papermerge restore backup-archive.tar.gz


Note that before restoring the backup archive, the DB schema should exist i.e.
all required tables with correct schema should be already in database.
You create schema by running ``migrate`` command (this is Django native management command)::

    $ ./manage.py migrate

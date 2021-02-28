Backup
=======

For peace of mind you always need to backup data. There three aspects of full backup:

* media directory
* database
* application version

If all you want is to just to ensure safe copy of you documents then all you need to
do is to backup media directory.
If you want to create full snapshot (i.e you want to be able to restore full application state from specific moment in past) then you need media directory backup + database backup + Papermerge version
of that specific moment in time.

Media Directory
~~~~~~~~~~~~~~~~

Media directory is place where Papermerge application saves all your original
documents and their derivatives (extracted text, images etc). By backing
up your media directory - you ensure your documents are safe.  

Media directory is configured with :ref:`media_dir` setting. By default it is a folder
named "media" in of same directory where papermerge project was cloned.

.. note::
    
    :ref:`media_dir` has two subfolders *docs* and *results*. :ref:`media_dir`/docs is place where
    original documents are uploaded - it is the location you want to ensure is regularely backed up.
    Media directory configuration is pure Django webframework thing; in Django it is called `MEDIA_ROOT <https://docs.djangoproject.com/en/3.1/ref/settings/#media-root>`_

.. note::

    **Papermerge never overwrites or renames original uploads!**, in that sense, Papermerge is non-destructive :ref:`dms`. Every time you perform changes on document, like :ref:`moving pages around <page_management>` a new document version is created, thus keeping original document version intact.


Database 
~~~~~~~~~

Another important part of whole backup picture - is backing up your Papermerge database. In database, Papermerge stores information like user related informations, documents' metadata, documents' tags etc.

.. note::

    Uploaded documents are NOT stored in database! Uploaded files are stored (by default) on local filesystem.
    In general, binary files are never stored in databases.

Basically with database backup you can restore "the state" of Papermerge application.


Application Version
~~~~~~~~~~~~~~~~~~~~

If you want to restore Papermerge backups you need to know for what
application version that backup is. This is why it is a good idea to append
Papermerge application version to your backup archives.


Backup Utility
~~~~~~~~~~~~~~~

Papermerge is shipped with backup command line utility. You can run it from project current directory:

.. code-block:: bash

    $ ./manage.py backup

That command will backup all your documents with preserved directory structure (it will backup documents of all users).

.. note::

    provided backup utility does not backup tags and metadata information.

In order to restore backup:

.. code-block:: bash

    $ ./manage.py restore <path-to-tar-file>
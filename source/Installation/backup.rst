Backup
=======

For peace of mind you always need to backup data. There two parts:

* media directory backup
* database backup

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

    **Papermerge never overwrites or renames originally uploaded files!**, in that sense, Papermerge is non-destructive :ref:`dms`. Every time you perform changes on document, like :ref:`moving pages around <page_management>` a new document version is created, thus keeping original document version intact.


Database Backup
~~~~~~~~~~~~~~~~
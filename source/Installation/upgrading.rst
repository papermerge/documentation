Upgrading
==========

Always :ref:`backup <backup>` your database, media directory and configuration files before
upgrading. We try very hard to make sure that all database changes are
non-destructive, but you should always backup beforehand anyway. You will
never regret backing up your database and media directory. You may regret not doing so, so it’s
just better to get into the habit.

General Instructions
~~~~~~~~~~~~~~~~~~~~~

In general, an upgrade involves two parts:

* upgrade application code and dependencies
* apply new database changes (called database migrations)

Upgrading application code is usually something like:

.. code-block:: bash

    $ git pull  # pull latest changes
    $ export DJANGO_SETTINGS_MODULE=config.settings.prod
    $ pip install -r requirements/base.txt

Applying new database changes is performed with ``migrate`` command:

.. code-block:: bash

    $ export DJANGO_SETTINGS_MODULE=config.settings.prod
    $ ./manage.py migrate

Note however that above instructions are very generic and may very depending on the release and deployment environment.


Docker
~~~~~~~~

In case you run Papermerge via docker container, then all you need to do is to
change docker image to the newer version of papermerge docker image. New
docker image means actually new application code (with correct dependencies
already built-in) and, the most important part **docker (startup script) will run database migrations
for you**!
 
.. _settings__database:

Database
========

This sections is for database configurations.
|project| supports following databases SQLite3, PostgreSQL, MySQL/MariaDB.


.. _settings__database__type:

``DATABASE__TYPE``
~~~~~~~~~~~~~~~~~~~

Database type.
For PostgreSQL database use one of following values:

* pg
* postgre
* postgres
* postgresql

For MySQL/MariaDB database use one of
following values:

* my
* mysql
* maria
* mariadb

Example as environment variable::

    PAPERMERGE__DATABASE__TYPE=mysql

.. _settings__database__user:

``DATABASE__USER``
~~~~~~~~~~~~~~~~~~

Database user.

Example as environment variable::

  PAPERMERGE__DATABASE__USER=john

Example as toml config::

  [database]
  user="john"

.. _settings__database__name:

``DATABASE__NAME``
~~~~~~~~~~~~~~~~~~

Database name.
Default value is papermerge.

.. _settings__database__host:

``DATABASE__HOST``
~~~~~~~~~~~~~~~~~~
 
Database host.
Default value is localhost.

.. _settings__database__port:

``DATABASE__PORT``
~~~~~~~~~~~~~~~~~~
   
Database port. Port must be specified as integer number. No string quotes.

Example::

  DBPORT = 5432

Default value is 5432 for PostgreSQL and 3306 for MySQL/MariaDB.

.. _settings__database__password:

``DATABASE__PASSWORD``
~~~~~~~~~~~~~~~~~~~~~~
 
Password for connecting to database
Default value is empty string.

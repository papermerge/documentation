# Database

This sections is for database configurations.
{{ extra.project }} supports following databases SQLite3, PostgreSQL, MySQL/MariaDB.


## TYPE

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



## USER

Database user.

Example as environment variable::

    PAPERMERGE__DATABASE__USER=john

Example as toml config:

    [database]
    user="john"


## NAME

Database name.
Default value is papermerge.

Example as environment variable:

    PAPERMERGE__DATABASE__NAME=db

Example as toml config:

    [database]
    name="db"


## HOST

Database host.
Default value is localhost.

Example as environment variable:

    PAPERMERGE__DATABASE__HOST=mydbhost

Example as toml config:

    [database]
    host="mydbhost"


## PORT

Database port. Port must be specified as integer number. No string quotes.

Example as environment variable::

    PAPERMERGE__DATABASE__PORT=5432

Example as toml config:

    [database]
    port=5432

Default value is 5432 for PostgreSQL and 3306 for MySQL/MariaDB.


## PASSWORD

Password for connecting to database

Example as environment variable:

    PAPERMERGE__DATABASE__PASSWORD=somesecurepassword

Example as toml config:

    [database]
    password=somesecurepassword

Default value is empty string.

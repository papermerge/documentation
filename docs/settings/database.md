# Database

This sections is for database configurations.
{{ extra.project }} supports following databases SQLite3, PostgreSQL, MySQL/MariaDB.


## DATABASE__URL

For PostgreSQL the database URL is given in following format:

```
postgres://USER:PASSWORD@HOST:PORT/NAME
```
or

```
postgresql://USER:PASSWORD@HOST:PORT/NAME
```

Example:

```
postgresql://scott:tiger@db:5432/mydatabase
```

For SQLite the format is: ``sqlite:///PATH``.

Example:

```
sqlite:////db/db.sqlite3
```

Default value is ``sqlite:////db/db.sqlite3``, in other words,
if ```DATABASE__URL``` is missing, {{extra.project}}
will use SQLite with ``/db/db.sqlite3`` as db file.





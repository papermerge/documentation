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


For MariaDB and MySQL the URL scheme is `mysql`.

Example:

```
mysql://myuser:mypass@db:3306/paperdb
```



For SQLite the format is: ``sqlite:///PATH``.

Example:

```
sqlite:////db/db.sqlite3
```

Default value is ``sqlite:////db/db.sqlite3``, in other words,
if ```DATABASE__URL``` is missing, {{extra.project}}
will use SQLite with ``/db/db.sqlite3`` as db file.

!!! Note

    Both web_app and worker must have same ``PAPERMERGE__DATABASE__URL``.

# Database

This sections is for database configurations.
{{ extra.project }} supports following databases SQLite3, PostgreSQL, MySQL/MariaDB.


## DATABASE__URL

For PostgreSQL the database URL is given in following format:

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


## DATABASE__POOL_SIZE

Applies only for Tivoli. Set database connections pool size. Defaults to 5.

!!! Note

    This configuration option applies only to [Tivoli](https://github.com/papermerge/tivoli), which is internal JWT token validator component.
    Tivoli uses SQLAlchemy as ORM. SQLAlchemy has built-in database connections
    pooling. The core app though, uses Django ORM - which does not have
    built-in pooling capabilities.

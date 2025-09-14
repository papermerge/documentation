# DB Migration

This document describes the migration of databases, that are used by {{extra.project}}.

## Migrate from SQLite to PostgreSQL

This scenario assumes, that you have a working installation, which is using a [SQLite database](/3.5/settings/database/?h=db.sqlite3#database__url) setup. For migration, you'll need a PostgreSQL database.

!!! Note

    The automatically generated table setup needs to be retained, as SQLite uses different types (e.g. string for IDs, instead of uuid).

### Prepare PostgreSQL

1. Start PostgreSQL 16.1
2. Configure {{extra.project}} to use PostgreSQL instead of SQLite. Change the [`DATABASE__URL` environment variable](/3.5/settings/database/#database__url).
3. (Re)start Papermerge. The startup process will create initiate the database, create all tables with the correct data types for the columns (e.g. uuid instead of text for IDs) and add a default user (which we'll remove again in the following steps).
4. Stop the PostgreSQL database and {{extra.project}}.
5. The automatically generated admin users needs to be delete again, as it has a random ID and would break the previously used user id. All users will be imported again with the correct IDs.
    - `DELETE FROM users`

### Import data

!!! Note

    Backup your Papermerge instance, incl. the database first!

Migrating data from SQLite to PostgreSQL fortunately is an easy task using e.g. [pgloader](https://pgloader.readthedocs.io/en/latest/index.html). The migration is pretty much straigh forward. We need to point out, that the data types differ for some columns in the two databases. They are compatible, but different (text vs. uuid). By default, pgloader would delete tables and recreate them with the data types that it finds in SQLite. We want to prevent that.

Start by creating a configuration file `db.load` for pgloader, which defines source and destination databases, as well as migration options.

```
LOAD database
FROM sqlite:///<sourcefolder>/db.sqlite3
INTO postgresql://papermerge@localhost:5432/pmgdb

WITH include no drop, create no tables, create no indexes, reset sequences, data only

SET work_mem to '16MB', maintenance_work_mem to '512 MB';
```

1. Install pgloader
    - `sudo apt update`
    - `sudo apt install pgloader`
2. Import the data
    - `pgloader db.load`
3. Start PostgreSQL
4. Start {{extra.project}}

Your {{extra.project}} instance is now using another database, nothing else changed.
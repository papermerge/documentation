# PMDump

Tool for migrating Papermerge DMS data between different versions. PMDump can
be used for backups as well. PMDump is not installed automatically with
{{ extra.project }}, it is an independent tool and must be installed,
as binary file, separately from {{ extra.project }}.

PMDump has two main commands:

  * `export`
  * `import`

`export` command will create a tar.gz archive with all your documents files as well as data
from the database.

`import` command takes tar.gz created by the `export` command and imports all files and data.

`export` and `import` works across different Papermerge DMS versions.

For PMDump version 0.4 `export` command works for following Papermerge DMS versions/databases

|  db/pmg version  |  2.0 | 2.1   | 3.2         | 3.3 | 3.4  |
|------------------|------|-------|-------------|-----|------|
|       SQLite     |  ✅  | ✅    | ✅          | ✅  | ✅   |
|       PostgreSQL |  ❌  | ✅    | ✅          | ✅  | ✅   |

Currently `import` command works to import only into 3.4 either SQLite or PostgreSQL database.

 - ✅ - means: it works
 - ❌ - means: no plans to implement this part yet. If you need this to be implemented, please
     [open a ticket](https://github.com/ciur/papermerge/issues) and provide docker compose with your setup.


## Get It

Download suitable binary file directly from [release page](https://github.com/papermerge/pmdump/releases)

```
wget -O pmdump <URL to the binary of the latest version for your platform>
```

OR

```
curl -o pmdump  <URL to the binary of the latest version for your platform>
```

And then:

```
chmod +x pmdump
sudo mv pmdump /usr/local/bin/
```

You can add the current directory to your PATH temporarily:

```
export PATH=$PWD:$PATH
```

## Usage

There are two commands:

  * export
  * import

for both you need to specify also configuration file. For `export` command,
configuration file indicates "the source". For `import` command
configuration file indicates "the destination".

For help use `-h` flag:

```bash
pmdump -h
```

### Export Config

create `source.yaml` file in which you need specify
version of the Papermerge DMS from where to export, media
root folder, and database.

For example, to export from Papermerge DMS 2.0 (i.e. app version 2.0),
which stores its data in SQLite database:

```yaml
app_version: 2.0
media_root: /path/to/media/folder/
database_url: sqlite:///path/to/data/papermerge.db
```

In case of exporting data from app version 3.3 which
store data in postgres database, configuration yaml file
would look like:

```yaml
media_root: /home/eugen/DockerCompose/pm3.3.1-pg/media
database_url: postgresql://coco:jumbo@127.0.0.1:5432/pmgdb?sslmode=disable
app_version: 3.3
```

`app_version` - it the version of Papermerge DMS from which you intend to export data. Version must be specified in `<major>.<minor>` format. Here are some examples of valid values: `2.0`, `2.1`, `3.0`, `3.2`, `3.4`.

`media_root` is folder where Papermerge DMS stores actual files. `pmdump` should have access to this folder.
Papermerge DMS uses `PAPERMERGE__MAIN__MEDIA_ROOT` environment variable to configure its media root folder. If not configured, it defaults to `/core_app/media/`.

`database_url` - is the database URL. For SQLite it is the path to sqlite3 file, prefixed with `sqlite://`. Some examples: `sqlite:///home/eugen/DockerCompose/pm3.4-sqlite/data/db.sqlite3`, `sqlite:///var/data/db.sqlite3`. Notice in examples
there are three `///`: two stand for the sqlite scheme, and one stands for root folder.

For PostgreSQL scheme must either `postgres://` or `postgresql://`. Here are some valid examples: `postgresql://coco:jumbo@127.0.0.1:5432/pmgdb?sslmode=disable`, `postgresql://coco:jumbo@127.0.0.1:5432/pmgdb`

### Export

Export command will save all data into zipped tar archive. You specify name of the exported file via `-f` flag and configuration file via `-c` flag:

```bash
pmdump -c source.yaml -f pm3.3.tar.gz export
```

Note `export` command **must be at the end of parameters list**.
Placing `export` command BEFORE parameters list won't work:

```
// wrong! "export" command must be at the end!
$ pmdump export -c source.yaml -f pm3.3.tar.gz
```

If you place `export` before parameters flag, you will get "missing configuration" error.

The general form for export command is:

```bash
pmdump <flag parameters> export
```

Here are couple of valid examples for `export` command:

```bash
pmdump -c examples/source_3_3_pg.yaml -f pm3.3_pg.tar.gz export
```


### Import


Create `dest_pg.yaml` file

```yaml
media_root: /home/eugen/DockerCompose/pm3.4-pg/media/
database_url: postgresql://coco:kesha@127.0.0.1:5432/pmg34?sslmode=disable
app_version: 3.4
```

Run import command (notice that `import` is at the end of parameters)

```bash
pmdump -c dest_pg.yaml -f /path/to/archive.tar.gz import
```

If you are importing into SQLite database, configuration file, dest_sqlite.yaml, will look like:

```yaml
media_root: /home/eugen/DockerCompose/pm3.4-sqlite/media/
database_url: sqlite:///home/eugen/DockerCompose/pm3.4-sqlite/data/db.sqlite3
app_version: 3.4
```

And command is same:

```bash
pmdump -c dest_sqlite.yaml -f /path/to/archive.tar.gz import
```

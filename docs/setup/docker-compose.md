# Docker Compose

This section describes how to setup {{ extra.project }} using docker compose.
As mentioned in overview section, {{ extra.project }} philosophy revolves around
progressive setup concept. As such, you are adviced to start with simple setups
and progress, in small steps, towards more complicated scenarios. The idea is
that on the way you will learn and understand better internals, which in
turn will enable you to be build very creative deployments.

We assign a complexity level, to each of following docker compose setups.

Complexity level ranges from 1 to 10.
Level 1 is simplest.
Level 10 is the most advanced.

Level 1, 2, ..., 10 here are meant to rate only docker compose setups.
Even the complexity level 10 of docker compose setups are innocent babies 👶 when compared to he very basic
k8s 🤓 deployments!

So, my heros, let's start!


## Level 1 - Database/PostgreSQL

By default, web app uses SQLite database. SQLite is great for quick demos, not for
production environments.

Following docker compose file starts {{extra.project}} with PostgreSQL 16.1 database:

```yaml
services:
  webapp:
    image: papermerge/papermerge:{{ extra.docker_image_version }}
    environment:
      PAPERMERGE__SECURITY__SECRET_KEY: 12345
      PAPERMERGE__AUTH__USERNAME: admin
      PAPERMERGE__AUTH__PASSWORD: admin
      PAPERMERGE__DATABASE__URL: postgresql://coco:jumbo@db:5432/pmgdb
    ports:
     - "12000:80"
    depends_on:
      - db
  db:
    image: postgres:16.1
    volumes:
      - pgdata:/var/lib/postgresql/data/
    environment:
      POSTGRES_PASSWORD: jumbo
      POSTGRES_DB: pmgdb
      POSTGRES_USER: coco
    healthcheck:
      test: pg_isready -U $$POSTGRES_USER -d $$POSTGRES_DB
      interval: 5s
      timeout: 10s
      retries: 5
      start_period: 10s
volumes:
  pgdata:
```

Start it with:

```
  $ docker compose up
```


You can access {{ extra.project }} user interface using any modern web browser (e.g. Firefox, Chrome).
Open your web browser and point it to http://localhost:12000.

🥳 Congratulations! 🥳 You have two microservices running: web app and
PostgreSQL 16.1 database. The web app will wait until db service is up and
running - and only then it will start.

The format `PAPERMERGE__DATABASE__URL` is documented in [database settings](../settings/database.md#database__url).

However, in this setup has a problem 🙁. To understand it - upload couple of documents.
Now if you remove docker containers with:

```
  $ docker compose down
```

And then bring them back with:

```
  $ docker compose up
```
You will notice that all documents "sort of disappeared". You can see document's titles, but when opening them there are errors.

Why so?

The problem is that the storage where uploaded documents are stored is not persistent i.e. it uploaded pdf files
lives inside docker container and when docker container is removed - so are our documents! Only documents "titles"
are still there, because that part is stored in database, which at this time is persistent.

!!! note

    Uploaded **files are NOT stored in database**! They are stored in file system directory called **media root**


## Level 2 - Persistent Media Storage

Uploaded files are not stored in database. They are stored in file system directory called *media root*.
In order to persist uploaded files, you need to:

1. Mount persistent volume
2. Point {{ extra.project }} to upload files to the persistem directory

In our example we will create docker compose volume `media_root` and mount it to internal (to container) directory `/var/media/pmg`. Finally, we use `PAPERMERGE__MAIN__MEDIA_ROOT` environment variable to tell
{{ extra.project }} where to upload documents.
Here is docker compose file:

```yaml
services:
  webapp:
    image: papermerge/papermerge:{{ extra.docker_image_version }}
    environment:
      PAPERMERGE__SECURITY__SECRET_KEY: 12345
      PAPERMERGE__AUTH__USERNAME: admin
      PAPERMERGE__AUTH__PASSWORD: admin
      PAPERMERGE__DATABASE__URL: postgresql://coco:jumbo@db:5432/pmgdb
      PAPERMERGE__MAIN__MEDIA_ROOT: /var/media/pmg
    volumes:
      - media_root:/var/media/pmg
    ports:
     - "12000:80"
    depends_on:
      - db
  db:
    image: postgres:16.1
    volumes:
      - pgdata:/var/lib/postgresql/data/
    environment:
      POSTGRES_PASSWORD: jumbo
      POSTGRES_DB: pmgdb
      POSTGRES_USER: coco
    healthcheck:
      test: pg_isready -U $$POSTGRES_USER -d $$POSTGRES_DB
      interval: 5s
      timeout: 10s
      retries: 5
      start_period: 10s
volumes:
  pgdata:
  media_root:
```

Now you can:

```
$ docker compose up
```
and
```
$ docker compose down
```
How many times you want! Your documents will still be there for you 🥳! We call that - persistent 😎.

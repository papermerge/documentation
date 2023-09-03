# Docker

!!! Danger

      Papermerge 3.0 is currently in active development. There is no stable version yet.
      At this stage all docker images are tagged either 3.0devX or 3.0aX.

## TL;DR

The only two required environment variables are `PAPERMERGE__SECURITY__SECRET_KEY` and `PAPERMERGE__AUTH__PASSWORD`:

```console
docker run -p 9400:80 \
    -e PAPERMERGE__SECURITY__SECRET_KEY=abc \
    -e PAPERMERGE__AUTH__PASSWORD=123 \
    papermerge/papermerge:{{ extra.docker_image_version }}
```

Point your web browser to http://localhost:9400 and you will see login screen:


![login screen](../img/setup/login.png)


Credentials are:

- username `admin`
- password `123`


## Official Docker Images

Official {{ extra.project  }} docker images are stored in <a href="https://hub.docker.com/u/papermerge" class="external-link" target="_blank">docker hub</a>.


## Get Docker Image

The recommended way to get the {{ extra.project }} Docker Image is to pull the prebuilt image from the <a href=" https://github.com/papermerge/papermerge-core/pkgs/container/papermerge" class="external-link" target="_blank">github repository packages</a>:

```console
docker pull papermerge/papermerge:{{ extra.docker_image_version }}
```

To use a specific version, you can pull a versioned tag. You can view the list
of available versions in the github repository packages:

```console
docker pull papermerge/papermerge:{{ extra.docker_image_version }}
```


## Use PostgreSQL as Database

By default {{ extra.project }} uses sqlite3 database. In order to use
PostgreSQL use following docker compose file:

```yaml
    version: '3.7'

    services:
      app:
        image: papermerge/papermerge:{{ extra.docker_image_version }}
        environment:
          - PAPERMERGE__SECURITY__SECRET_KEY=abc
          - PAPERMERGE__AUTH__PASSWORD=12345
          - PAPERMERGE__DATABASE__URL=postgresql://scott:tiger@db:5432/mydatabase
        ports:
          - 9400:80
        depends_on:
          - db
      db:
        image: bitnami/postgresql:14.4.0
        volumes:
          - postgres_data:/var/lib/postgresql/data/
        environment:
          - POSTGRES_PASSWORD=123
    volumes:
        postgres_data:
```

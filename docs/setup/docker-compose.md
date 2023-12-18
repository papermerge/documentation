# Docker Compose

This section describes how to setup {{ extra.project }} using docker compose.


## Web App + Worker

The simpliest docker compose setup for {{ extra.project }} is following:

```yaml
  version: "3.9"

  x-backend: &common
    image: papermerge/papermerge:{{ extra.docker_image_version }}
    environment:
        PAPERMERGE__SECURITY__SECRET_KEY: 12345
        PAPERMERGE__AUTH__USERNAME: john
        PAPERMERGE__AUTH__PASSWORD: hohoho
        PAPERMERGE__REDIS__URL: redis://redis:6379/0
    volumes:
        - data:/db
        - index_db:/core_app/index_db
        - media:/core_app/media
  services:
    web:
      <<: *common
      ports:
       - "12000:80"
      depends_on:
        - redis
    worker:
      <<: *common
      command: worker
    redis:
      image: redis:6
  volumes:
    data:
    index_db:
    media:
```

You can access {{ extra.project }} user interface using any modern web browser (e.g. Firefox, Chrome).
Open your web browser and point it to http://localhost:12000.


## PostgreSQL

By default {{ extra.project }} uses sqlite3 database. Here is setup to which
uses PostgreSQL:

```yaml
  version: "3.9"

  x-backend: &common
    image: papermerge/papermerge:{{ extra.docker_image_version }}
    environment:
        PAPERMERGE__SECURITY__SECRET_KEY: 12345
        PAPERMERGE__AUTH__USERNAME: john
        PAPERMERGE__AUTH__PASSWORD: hohoho
        PAPERMERGE__DATABASE__URL: postgresql://scott:tiger@db:5432/mydatabase
        PAPERMERGE__REDIS__URL: redis://redis:6379/0
    volumes:
      - index_db:/core_app/index_db
      - media:/core_app/media
  services:
    web:
      <<: *common
      ports:
       - "12000:80"
      depends_on:
        - redis
        - db
    worker:
      <<: *common
      command: worker
    redis:
      image: redis:6
    db:
      image: bitnami/postgresql:14.4.0
      volumes:
        - postgres_data:/var/lib/postgresql/data/
      environment:
        POSTGRES_USER: scott
        POSTGRES_PASSWORD: tiger
        POSTGRES_DB: mydatabase
  volumes:
    postgres_data:
    index_db:
    media:
```


## Solr

By default {{ extra.project }} uses Xapian search engine. However, for
production environments, full fledged search engine like Solr is recommanded.

```yaml
version: "3.9"

x-backend: &common
  image: papermerge/papermerge:{{ extra.docker_image_version }}
  environment:
    PAPERMERGE__SECURITY__SECRET_KEY: 12345
    PAPERMERGE__AUTH__USERNAME: john
    PAPERMERGE__AUTH__PASSWORD: hohoho
    PAPERMERGE__DATABASE__URL: postgresql://scott:tiger@db:5432/mydatabase
    PAPERMERGE__REDIS__URL: redis://redis:6379/0
    PAPERMERGE__SEARCH__URL: solr://solr:8983/pmg-index
  volumes:
    - media:/core_app/media

services:
  web:
    <<: *common
    ports:
     - "12000:80"
    depends_on:
      - redis
      - db
      - solr
  worker:
    <<: *common
    command: worker
  redis:
    image: redis:6
  db:
    image: bitnami/postgresql:14.4.0
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      POSTGRES_USER: scott
      POSTGRES_PASSWORD: tiger
      POSTGRES_DB: mydatabase
  solr:
    image: solr:9.3
    ports:
     - "8983:8983"
    volumes:
      - solr_data:/var/solr
    command:
      - solr-precreate
      - pmg-index

volumes:
  postgres_data:
  solr_data:
  media:
```

## MySQL / MariaDB

Here is an example of docker compose setup with MariaDB:

```yaml
version: "3.9"

x-backend: &common
  image: papermerge/papermerge:{{ extra.docker_image_version }}
  environment:
      PAPERMERGE__SECURITY__SECRET_KEY: 1234  # top secret
      PAPERMERGE__AUTH__USERNAME: eugen
      PAPERMERGE__AUTH__PASSWORD: 1234
      PAPERMERGE__DATABASE__URL: mysql://myuser:mypass@db:3306/paperdb
      PAPERMERGE__REDIS__URL: redis://redis:6379/0
      PAPERMERGE__SEARCH__URL: solr://solr:8983/pmg-index
  volumes:
    - media_root:/core_app/media
  depends_on:
    - redis
    - solr
    - db

services:
  web:
    <<: *common
    ports:
     - "11000:80"
  worker:
    <<: *common
    command: worker
  redis:
    image: redis:6
  solr:
    image: solr:9.3
    ports:
     - "8983:8983"
    volumes:
      - solr_data:/var/solr
    command:
      - solr-precreate
      - pmg-index
  db:
    image: mariadb:11.2
    volumes:
      - maria:/var/lib/mysql
    environment:
      MYSQL_ROOT_PASSWORD: mypass
      MYSQL_DATABASE: paperdb
      MYSQL_USER: myuser
      MYSQL_PASSWORD: mypass
volumes:
  maria:
  solr_data:
  media_root:
```

## OAuth 2.0

...

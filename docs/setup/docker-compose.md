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
      PAPERMERGE__AUTH__USERNAME: admin
      PAPERMERGE__AUTH__PASSWORD: admin
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
    PAPERMERGE__AUTH__USERNAME: admin
    PAPERMERGE__AUTH__PASSWORD: admin
    PAPERMERGE__DATABASE__URL: postgresql://coco:kesha@db:5432/cocodb
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
      db:
        condition: service_healthy
      redis:
        condition: service_healthy
  worker:
    <<: *common
    command: worker
  redis:
    image: redis:6
    healthcheck:
      test: redis-cli --raw incr ping
      interval: 5s
      timeout: 10s
      retries: 5
      start_period: 10s
  db:
    image: postgres:16.1
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      POSTGRES_PASSWORD: kesha
      POSTGRES_DB: cocodb
      POSTGRES_USER: coco
    healthcheck:
      test: pg_isready -U $$POSTGRES_USER -d $$POSTGRES_DB
      interval: 5s
      timeout: 10s
      retries: 5
      start_period: 10s
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
    PAPERMERGE__SECURITY__SECRET_KEY: 1234  # top secret
    PAPERMERGE__AUTH__USERNAME: admin
    PAPERMERGE__AUTH__PASSWORD: admin
    PAPERMERGE__DATABASE__URL: postgresql://coco:kesha@db:5432/cocodb
    PAPERMERGE__REDIS__URL: redis://redis:6379/0
    PAPERMERGE__SEARCH__URL: solr://solr:8983/pmg-index
  volumes:
    - media_root:/core_app/media
  depends_on:
    db:
      condition: service_healthy
    redis:
      condition: service_healthy

services:
  web:
    <<: *common
    ports:
     - "12000:80"
  worker:
    <<: *common
    command: worker
  redis:
    image: redis:6
    healthcheck:
      test: redis-cli --raw incr ping
      interval: 5s
      timeout: 10s
      retries: 5
      start_period: 10s
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
    image: postgres:16.1
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      POSTGRES_PASSWORD: kesha
      POSTGRES_DB: cocodb
      POSTGRES_USER: coco

    healthcheck:
      test: pg_isready -U $$POSTGRES_USER -d $$POSTGRES_DB
      interval: 5s
      timeout: 10s
      retries: 5
      start_period: 10s

volumes:
  postgres_data:
  solr_data:
  media_root:
```

## MySQL / MariaDB

Here is an example of docker compose setup with MariaDB:

```yaml
version: "3.9"

x-backend: &common
  image: papermerge/papermerge:{{ extra.docker_image_version }}
  environment:
    PAPERMERGE__SECURITY__SECRET_KEY: 1234  # top secret
    PAPERMERGE__AUTH__USERNAME: admin
    PAPERMERGE__AUTH__PASSWORD: admin
    PAPERMERGE__DATABASE__URL: mysql://coco:kesha@db:3306/cocodb
    PAPERMERGE__REDIS__URL: redis://redis:6379/0
    PAPERMERGE__SEARCH__URL: solr://solr:8983/pmg-index
  volumes:
    - media_root:/core_app/media
  depends_on:
    db:
      condition: service_healthy
    redis:
      condition: service_healthy

services:
  web:
    <<: *common
    ports:
     - "12000:80"
  worker:
    <<: *common
    command: worker
  redis:
    image: redis:6
    healthcheck:
      test: redis-cli --raw incr ping
      interval: 5s
      timeout: 10s
      retries: 5
      start_period: 10s
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
      MYSQL_ROOT_PASSWORD: kesha
      MYSQL_DATABASE: cocodb
      MYSQL_USER: coco
      MYSQL_PASSWORD: kesha
    ports:
      - "3306:3306"
    healthcheck:
      test: mariadb-admin ping -h 127.0.0.1 -u $$MYSQL_USER --password=$$MYSQL_PASSWORD
      interval: 5s
      timeout: 10s
      retries: 5
      start_period: 10s

volumes:
  maria:
  solr_data:
  media_root:
```

## OAuth 2.0

...

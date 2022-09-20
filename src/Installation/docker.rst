.. _docker:


Docker
======


TL;DR
-----

The only two required environment variables are :ref:`settings__main__secret_key` and :ref:`settings__superuser__password`::

    docker run -p 8000:8000 \
        -e PAPERMERGE__MAIN__SECRET_KEY=abc \
        -e DJANGO_SUPERUSER_PASSWORD=123 \
        ghcr.io/papermerge/papermerge:latest

Use ``POST http://localhost:8000/api/auth/login/`` endpoint to authenticate.

Credentials are:

- username ``admin``
- password ``123``


Official Docker Images
----------------------

Offical |project| docker images are stored on `docker hub`_ and `github packages`_.


Get Docker Image
-----------------

The recommended way to get the |project| Docker Image is to pull the prebuilt image from the `github repository packages`_::

    docker pull ghcr.io/papermerge/papermerge:latest

To use a specific version, you can pull a versioned tag. You can view the list of available versions in the `github repository packages`_::

    docker pull ghcr.io/papermerge/papermerge:2.1.0b4


.. _docker_adding_ocr_languages:

Adding OCR Languages to the Docker Image
----------------------------------------

By default the Docker image includes English and German OCR languages only.

You may want to add other OCR languages. You add extra OCR languages in three steps:

1. Install extra langs in docker image (by extending it)
2. Update ``papermerge.toml`` file with extra languages
3. Use/Mount ``papermerge.toml`` in docker, docker compose, kubernetes


You install extra languages in docker image by creating a new Dockerfile
from ``ghcr.io/papermerge/papermerge`` docker image.
Create new docker file with following content::

  FROM ghcr.io/papermerge/papermerge

  # add Italian, Spanish and French
  RUN apt install tesseract-ocr-ita tesseract-ocr-spa tesseract-ocr-fra


.. note::
  ``FROM ghcr.io/papermerge/papermerge`` pull docker image from GitHub container
  registry. If you write ``FROM papermerge/papermerge`` it pulls docker image
  from Dockerhub.

All languages are specified in three letters code as per `ISO 639-2T`_ standard -
second column in the table.

Then run following command::

  docker build -t mypapermerge:multi-lang -f Dockerfile .

Notice the "." character at the end. After running above command, you can use
newly build docker image for lunching |project| with Italian, Spanish and
French OCR languages.

Besides installing extra OCR languages in docker image, you also need to mount
papermerge.toml file with following OCR languages configuration::

  [ocr]
  languages = { ita = "Italian", fra = "French", spa = "Spanish", eng = "English", deu = "German" }
  default_language = "ita"

.. important::
  ``languages`` must be written as one line! It uses so called `inline table`_ of toml format.

Here is an example of docker compose file which mounts ``papermerge.toml`` file::

  version: '3.7'
  x-backend: &common
    image: mypapermerge:multi-lang  # <--- use docker image with extra OCR langs
    volumes:
      - media_root:/app/media
      - xapian_index: /app/xapian_index
      - ./papermerge.toml:/etc/papermerge.toml  # <--- Mounted papermerge.toml (!)
    environment:
      - PAPERMERGE__MAIN__SECRET_KEY=12345SKK
      - DJANGO_SUPERUSER_PASSWORD=1234
      - PAPERMERGE__REDIS__HOST=redis
      - PAPERMERGE__REDIS__PORT=6379
      - PAPERMERGE__DATABASE__TYPE=postgres
      - PAPERMERGE__DATABASE__USER=postgres
      - PAPERMERGE__DATABASE__NAME=postgres
      - PAPERMERGE__DATABASE__PASSWORD=postgres
      - PAPERMERGE__DATABASE__HOST=db
      - PAPERMERGE__DATABASE__PORT=5432
      - PAPERMERGE__SEARCH__ENGINE=xapian
      - PAPERMERGE__SEARCH__PATH=/app/xapian_index
  services:
    backend:
      <<: *common
      labels:
        - "traefik.enable=true"
        - "traefik.http.routers.backend.rule=Host(`mydms.local`) && PathPrefix(`/api/`)"
    ws_server:
      <<: *common
      command: ws_server
      labels:
        - "traefik.enable=true"
        - "traefik.http.routers.ws_server.rule=Host(`mydms.local`) && PathPrefix(`/ws/`)"
    worker:
      <<: *common
      command: worker
    traefik:
      image: "traefik:v2.6"
      command:
        - "--api.insecure=true"
        - "--providers.docker=true"
        - "--providers.docker.exposedbydefault=false"
        - "--entrypoints.web.address=:80"
      ports:
        - "6080:80"
      volumes:
        - "/var/run/docker.sock:/var/run/docker.sock:ro"
    frontend:
      image: ghcr.io/papermerge/papermerge.js:latest
      labels:
        - "traefik.enable=true"
        - "traefik.http.routers.traefik.rule=Host(`mydms.local`) && PathPrefix(`/`)"
    redis:
      image: redis:6
      ports:
        - '6379:6379'
    db:
      image: postgres:14.4
      volumes:
        - postgres_data:/var/lib/postgresql/data/
      environment:
        - POSTGRES_USER=postgres
        - POSTGRES_DB=postgres
        - POSTGRES_PASSWORD=postgres
  volumes:
    media_root:
    postgres_data:
    xapian_index:


.. note:: For detailed explanation of docker compose file, see :ref:`Docker Compose Detailed Explanation <docker_compose_detailed_explanation>`


Use PostgreSQL as Database
--------------------------

By default |project| uses sqlite3 database. In order to use PostgreSQL use following docker compose file::

    version: '3.7'

    services:
      app:
        image: ghcr.io/papermerge/papermerge
        environment:
          - PAPERMERGE__MAIN__SECRET_KEY=abc
          - DJANGO_SUPERUSER_PASSWORD=12345
          - PAPERMERGE__DATABASE__TYPE=postgres
          - PAPERMERGE__DATABASE__USER=postgres
          - PAPERMERGE__DATABASE__PASSWORD=123
          - PAPERMERGE__DATABASE__NAME=postgres
          - PAPERMERGE__DATABASE__HOST=db
        ports:
          - 8000:8000
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


Above mentioned docker compose file can be used to start |project| REST
API backend server which will use PostgreSQL database to store data.


.. _docker hub: https://hub.docker.com/u/papermerge
.. _github packages: https://github.com/orgs/papermerge/packages
.. _github repository packages: https://github.com/papermerge/papermerge-core/pkgs/container/papermerge
.. _inline table: https://toml.io/en/v1.0.0#inline-table
.. _ISO 639-2T: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes

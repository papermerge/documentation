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

    docker pull ghcr.io/papermerge/papermerge:2.1.0a32


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
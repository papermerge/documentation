# Backend

This guide is intended for those who want play with backend code for Papermerge.
It order to follow it you need to be comfortable with linux command line and python
programming language.

In this guide Ubuntu 20.04 LTS is used as Linux distribution.

If you follow this document and still have troubles, please open an
<a href="https://github.com/ciur/papermerge/issues" class="external-link" target="_blank">issue on GitHub</a>.


Install required Ubuntu 20.04 LTS deb packages:

    $ sudo apt install build-essential \
        python3-dev \
        libpq-dev \
        imagemagick \
        tesseract-ocr \
        tesseract-ocr-eng \
        tesseract-ocr-deu \
        tesseract-ocr-fra \
        tesseract-ocr-spa


Clone <a href="https://github.com/papermerge/papermerge-core" class="external-link" target="_blank">papermerge-core</a> repository:

    $ git clone git@github.com:papermerge/papermerge-core.git


Install python <a href="https://python-poetry.org/" class="external-link" target="_blank">poetry</a> - it is used for python dependencies management.


Using poetry, install python dependencies:

      $ cd ~/papermerge-core
      $ poetry install

Activate python virtual environment:

      poetry shell


Set following shell environment variables:

      $ export DJANGO_SETTINGS_MODULE=config.settings
      $ export PAPERMERGE_SECRET_KEY=somesecretkey
      $ export PYTHONPATH=<project-root>


!!! note

    `<project-root>` is folder where your project was cloned. Example: `/home/vagrant/papermerge-core/`.


Change current working directory to `<project-root>/docker/dev`:

    $ cd docker/dev

Run database migrations:

    $ ./manage.py migrate

!!! note:

    By default Papermerge uses sqlite3 database.

Create superuser for Papermerge instance:

    $ ./manage.py createsuperuser


Papermerge backend can start either as REST API server or as worker.
There can be as many workers as you want, but only one REST API server.
REST API server is http web server for serving REST API requests.
Worker(s) perform background jobs like OCR processing, indexing.


## REST API Server


Switch to `docker/dev` folder in `<project-root>` and activate python virtual environment:

    $ cd <project-root>/docker/dev
    $ poetry shell

Set shell environment variables:

    $ export DJANGO_SETTINGS_MODULE=config.settings
    $ export PAPERMERGE__MAIN__SECRET_KEY=somesecretkey
    $ export PYTHONPATH=<project-root>


Start REST API webserver with:

    $ poetry run task server

Last command will start backend REST API server on localhost port 8000.

If you want to bind REST API server to `0.0.0.0` IP use::

    $ ./manage.py runserver 0.0.0.0:8000

You can access REST API backend via `http://localhost:8000/api/` url.


## Worker

Worker(s) perform background jobs like OCR processing. Worker communicate with
REST API server via `Redis`_. By default Worker(s) and REST API server will assume
that Redis is up and available on 127.0.0.1:6379.

!!! note:

      Without any further configuration boths REST API server and worker(s) will
      communicate via `Redis`_ which is expected to be available on
      127.0.0.1:6379


Switch to `docker/dev` folder in `<project-root>` and activate python virtual environment:

    $ cd <project-root>/docker/dev
    $ poetry shell

Set shell environment variables:

    $ export DJANGO_SETTINGS_MODULE=config.settings
    $ export PAPERMERGE_SECRET_KEY=somesecretkey
    $ export PYTHONPATH=<project-root>

Start worker with following command:

    $ poetry run task worker


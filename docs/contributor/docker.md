# Docker

There is docker image for development mode. Docker image is tagged with `3.0devX`.
With dev image, you can get feedback of your source code changes without needing to install
any dependency or any deveopment environment configurations.

All examples described below assume that you got {{ extra.project }} <a href="https://github.com/papermerge/papermerge-core" class="external-link" target="_blank">source code</a>
and you are in root repository of source code folder:


    $ git clone git@github.com:papermerge/papermerge-core.git PapermergeSourceCode
    $ cd PapermergeSourceCode


## Web App

This is the simplest local dev scenario, you start docker compose file only with
web app i.e. REST API server + ui.

The go to the folder where source was cloned and create following docker compose file:

    version: "3.9"

    services:
      backend:
        image: papermerge/papermege:3.0dev  # check the latest dev image number in dockerhub!
        volumes:
            - ./papermerge:/core_app/papermerge/
            - ./ui:/core_ui/
        environment:
          PAPERMERGE__SECURITY__SECRET_KEY: 1234  # top secret
          PAPERMERGE__AUTH__USERNAME: admin
          PAPERMERGE__AUTH__PASSWORD: 1234
        ports:
          - "11000:80"


Assuming you are in root folder of the source code, above docker compose will
mount the source code to the correct location in docker image. The appliction will
be accessible to on local port 11000.

Here is docker compose file for the case when you want to build dev docker image yourself:

    version: "3.9"

    services:
      backend:
        build:
          context: .
          dockerfile: docker/dev/Dockerfile
        volumes:
            - ./papermerge:/core_app/papermerge/
            - ./ui:/core_ui/
        environment:
          PAPERMERGE__SECURITY__SECRET_KEY: 1234  # top secret
          PAPERMERGE__AUTH__USERNAME: admin
          PAPERMERGE__AUTH__PASSWORD: 1234
        ports:
          - "11000:80"


## Web App + Worker

Following docker compose adds worker service. Worker and Web App
communicate via redis (message broker), thus we need to add redis service as
well:

    version: "3.9"

    x-backend: &common  # yaml anchor definition
      build:
        context: .
        dockerfile: docker/dev/Dockerfile
      environment:
          PAPERMERGE__SECURITY__SECRET_KEY: 1234  # top secret
          PAPERMERGE__AUTH__USERNAME: admin
          PAPERMERGE__AUTH__PASSWORD: 1234
          PAPERMERGE__REDIS__URL: redis://redis:6379/0
      volumes:
          - ./papermerge:/core_app/papermerge/
          - ./ui:/core_ui/
          - data:/db
          - index_db:/core_app/index_db
          - media_root:/core_app/media

    services:
      web:
        <<: *common
        ports:
         - "11000:80"
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
        media_root:



## Logging Config

Both worker and web app read their logging configurations from file pointed by
`PAPERMERGE__MAIN__LOGGING_CFG` environment variable. An example of custom
logging config would be:

    version: 1
    disable_existing_loggers: true

    formatters:
      verbose:
        format: '%(asctime)s %(levelname)s %(name)s.%(funcName)s %(message)s'

    handlers:
      console:
        level: DEBUG
        class: logging.StreamHandler
        formatter: verbose

    loggers:
      auth_server:
        level: DEBUG
        handlers: [console]
      papermerge.search.tasks:
        level: DEBUG
        handlers: [console]
        propagate: no
        format: verbose

You may recognize it. It should be YAML version of <a href="https://docs.python.org/3/library/logging.config.html#configuration-file-format" class="external-link" target="_blank">python logging config</a>.

Here is an example of docker compose with web wepp + worker + custom logging configuration:

    version: "3.9"

    x-backend: &common
      build:
        context: .
        dockerfile: docker/dev/Dockerfile
      environment:
          PAPERMERGE__SECURITY__SECRET_KEY: 1234  # top secret
          PAPERMERGE__AUTH__USERNAME: admin
          PAPERMERGE__AUTH__PASSWORD: 1234
          PAPERMERGE__REDIS__URL: redis://redis:6379/0
          PAPERMERGE__MAIN__LOGGING_CFG: /logging.yml  # <-- absolute path to custom config file
      volumes:
          - ./papermerge:/core_app/papermerge/
          - ./ui:/core_ui/
          - data:/db
          - index_db:/core_app/index_db
          - media_root:/core_app/media
          - ./custom_logging.yml:/logging.yml  # mount local logging config file

    services:
      web:
        <<: *common
        ports:
         - "11000:80"
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
        media_root:


## Solr

{{ extra.project }} is shipped with a default search library - Xapian.

However, you may opt-in to use full fledged search engine like Solr. In order to
change search backend, use `PAPERMERGE__SEARCH__URL` env variable:

    version: "3.9"

    x-backend: &common
      build:
        context: .
        dockerfile: docker/dev/Dockerfile
      environment:
          PAPERMERGE__SECURITY__SECRET_KEY: 1234
          PAPERMERGE__AUTH__USERNAME: admin
          PAPERMERGE__AUTH__PASSWORD: 1234
          PAPERMERGE__REDIS__URL: redis://redis:6379/0
          PAPERMERGE__SEARCH__URL: solr://solr:8983/pmg-index  # <- use Solr's "pmg-index" index
      volumes:
          - ./papermerge:/core_app/papermerge/
          - ./ui:/core_ui/
          - data:/db
          - index_db:/core_app/index_db
          - media_root:/core_app/media

    services:
      web:
        <<: *common
        ports:
         - "11000:80"
        depends_on:
          - redis
          - solr
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
          - pmg-index  # <- creates index at startup of the Solr service

    volumes:
      data:
      solr_data:
      index_db:
      media_root:

Notice that Solr is started with `solr-precreate pmg-index` command, which means that Solr service will be started with
pre-created index named `pmg-index`.

## PostgreSQL

Here is an example of docker compose which uses PostgreSQL as database:

    version: "3.9"

    x-backend: &common
      build:
        context: .
        dockerfile: docker/dev/Dockerfile
      environment:
          PAPERMERGE__SECURITY__SECRET_KEY: 1234  # top secret
          PAPERMERGE__AUTH__USERNAME: admin
          PAPERMERGE__AUTH__PASSWORD: 1234
          PAPERMERGE__DATABASE__URL: postgresql://postgres:123@db:5432/postgres
          PAPERMERGE__REDIS__URL: redis://redis:6379/0
          PAPERMERGE__SEARCH__URL: solr://solr:8983/pmg-index
      volumes:
        - ./papermerge:/core_app/papermerge/
        - ./ui:/core_ui/
        - index_db:/core_app/index_db
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
        image: bitnami/postgresql:14.4.0
        volumes:
          - postgres_data:/var/lib/postgresql/data/
        environment:
          - POSTGRES_PASSWORD=123

    volumes:
      postgres_data:
      solr_data:
      index_db:
      media_root:



## OAuth 2.0
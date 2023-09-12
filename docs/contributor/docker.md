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


Optionally you can add custom logging configuration:

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
          PAPERMERGE__MAIN__LOGGING_CFG: /logging.yml  # <-- custom config
      volumes:
          - ./papermerge:/core_app/papermerge/
          - ./ui:/core_ui/
          - data:/db
          - index_db:/core_app/index_db
          - media_root:/core_app/media
          - ./custom_logging.yml:/logging.yml  # mount config file

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

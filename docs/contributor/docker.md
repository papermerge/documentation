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

...

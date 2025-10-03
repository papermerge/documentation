# S3 Backend

{{ extra.project }} supports S3 backend. This means that it can store
document files in S3 storage.

There are two parts to consider here:

1. Documents upload to S3 storage
2. Content delivery i.e. serving of document files

The second part, content delivery, is about offloading document files delivery
from {{ extra.project }} to CDN. Once files are served via CDN, `webapp`
becomes stateless, which means you can have multiple instances of `webapp`
and thus scale it as much as you have want.

## Documents Upload to S3 Storage

This scenario is straightforward - {{ extra.project }} will upload every
document version to S3 storage. However, in this scenario
{{ extra.project }} **serves documents from its local disk**. This works if
and only if you have exactly one instance of webapp.

If you change document version, {{ extra.project }} will upload changed version as well.
If you delete a document, {{ extra.project }} will remove deleted document
from S3 bucket as well.

This setup is useful for small deployments accessible only to couple of users on
local network.

!!! Remember

	1. This setup works only for one instance of `webapp`
	2. In this scenario `webapp` is serving document files

To make this work, you need to provide to S3 worker following settings:

```
* PAPERMERGE__S3__BUCKET_NAME
* AWS_REGION_NAME
* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* S3_WORKER_ARGS should be set to "-Q s3 -c 2"
```

Note that both `webapp` and `s3worker` need to have access same `PAPERMERGE__REDIS__URL`
and `PAPERMERGE__DATABASE__URL`.

In following is an example of docker compose file which features S3 backend:

```yaml
services:
  webapp:
    image: papermerge/papermerge:{{ extra.docker_image_version }}
    environment:
      PAPERMERGE__SECURITY__SECRET_KEY: "random-sequence-of-characters"
      PAPERMERGE__AUTH__USERNAME: admin
      PAPERMERGE__AUTH__PASSWORD: 1234
      PAPERMERGE__DATABASE__URL: postgresql://coco:jumbo@db:5432/pmgdb
      PAPERMERGE__MAIN__MEDIA_ROOT: /var/media/pmg
      PAPERMERGE__REDIS__URL: redis://redis:6379/0
    ports:
     - "12000:80"
    depends_on:
      - db
      - redis
    volumes:
      - media_root:/var/media/pmg
  path_template_worker:
    image: papermerge/path-tmpl-worker:0.4
    command: worker
    environment:
      PAPERMERGE__DATABASE__URL: postgresql://coco:jumbo@db:5432/pmgdb
      PAPERMERGE__REDIS__URL: redis://redis:6379/0
      PATH_TMPL_WORKER_ARGS: "-Q path_tmpl -c 2"
    depends_on:
      - db
      - redis
  s3worker:
    image: papermerge/s3worker:{{ extra.s3_worker_version }}
    command: worker
    environment:
      PAPERMERGE__DATABASE__URL: postgresql://coco:jumbo@db:5432/pmgdb
      PAPERMERGE__REDIS__URL: redis://redis:6379/0
      PAPERMERGE__MAIN__MEDIA_ROOT: /var/media/pmg
      PAPERMERGE__S3__BUCKET_NAME: p<your bucket name>l
      S3_WORKER_ARGS: "-Q s3 -c 2"
      AWS_REGION_NAME: eu-central-1
      AWS_ACCESS_KEY_ID: A<your value here>L
      AWS_SECRET_ACCESS_KEY: s<your value here>j
    depends_on:
      - db
      - redis
    volumes:
      - media_root:/var/media/pmg
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
  redis:
    image: redis:7.2
    ports:
      - "6379:6379"
    environment:
      ALLOW_EMPTY_PASSWORD: "yes"
volumes:
  pgdata:
  media_root:
```

You can use [pmcompose](https://github.com/papermerge/pmcompose) to generate docker compose
for {{extra.project}}. To generate above configuration, use following command:

```
$ pmcompose -u admin -p 1234 -lc -s3
```

!!! Note

    You can also run [pmcompose](https://github.com/papermerge/pmcompose) in iterative mode,
    in which you will be asked configuration questions one by one:

    ```
    $ pmcompose -i
    ```

## Content Delivery

To enable files delivery via CDN, you need to set, in `webapp`, `PAPERMERGE__MAIN__FILE_SERVER` to `s3`:

`PAPERMERGE__MAIN__FILE_SERVER=s3`

At this point the only CDN provider which can be used with {{extra.project}} is AWS Cloud Front.
Besides `PAPERMERGE__MAIN__FILE_SERVER=s3`, you need to set, on `webapp`, following, cloud front specific,
environment variables (CF=AWS Cloud Front):

* `PAPERMERGE__MAIN__CF_SIGN_URL_PRIVATE_KEY`
* `PAPERMERGE__MAIN__CF_SIGN_URL_KEY_ID`
* `PAPERMERGE__MAIN__CF_DOMAIN`

With above these settings all URLs to the document files will be 1. signed 2.
pointing to cloud front domain. Each signed URL will be valid for 10 minutes.
The key take away here is that document files will be retrieved from
(signed URLS of) aws cloud front distribution.

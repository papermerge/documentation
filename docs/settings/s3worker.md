# S3 Worker

S3 Worker is configured via environment variables.
Note that database, media root and redis url must be **same** as for webapp.


!!! Note

	Source code for S3 worker is <a href="https://github.com/papermerge/s3-worker/" class="external-link" target="_blank">on github</a>.
	Its docker image is <a href="https://hub.docker.com/r/papermerge/s3worker" class="external-link" target="_blank">on dockerhub</a>.

## PAPERMERGE__DATABASE__URL

Database URL. For PostgreSQL the database URL is given in following format:

```
postgresql://USER:PASSWORD@HOST:PORT/NAME
```

Example:

```
postgresql://scott:tiger@db:5432/mydatabase
```


For MariaDB and MySQL the URL scheme is `mysql`.

Example:

```
mysql://myuser:mypass@db:3306/paperdb
```

!!! Note

    Both web_app and s3worker must have same ``PAPERMERGE__DATABASE__URL``



## PAPERMERGE__MAIN__MEDIA_ROOT

Absolute filesystem path to the directory where to store the document files.

Example:

    PAPERMERGE__MAIN__MEDIA_ROOT=/var/www/example.com/media/


!!! Note

    Both web_app and s3worker must have same ``PAPERMERGE__MAIN__MEDIA_ROOT``


## PAPERMERGE__REDIS__URL

For Redis the URL is given in following format:

```
redis://HOST:PORT/NUMBER
```

For example:

```
redis://redis:6379/0
```

!!! Note

    Both web_app and s3worker must have same ``PAPERMERGE__REDIS__URL``


## PAPERMERGE__S3__BUCKET_NAME

Self explanatory

## S3_WORKER_ARGS

Pass celery worker parameters via this environment variable.
In case `PAPERMERGE__MAIN__PREFIX` value is empty, use S3_WORKER_ARGS="-Q s3" to
instruct worker to use name "s3" for the input queue.
For non-empty prefixes, use S3_WORKER_ARG="-Q prefix_s3".

For example, if `PAPERMERGE__MAIN__PREFIX=demo`, then S3_WORKER_ARG should have -Q as S3_WORKER_ARG="-Q demo_s3".

Long story short, if you don't know what celery is and how to work with it, use either:

`S3_WORKER_ARGS="-Q s3"`

or

`S3_WORKER_ARGS="-Q s3 -c 2"`

!!! Note

	Celery? Not the plant :smile:! But Python's Celery <a href="https://docs.celeryq.dev/en/stable/getting-started/introduction.html" class="external-link" target="_blank">this one</a>. The task distribution thingy :stuck_out_tongue:!


## AWS_REGION_NAME

Self explanatory


## AWS_ACCESS_KEY_ID

Self explanatory

## AWS_SECRET_ACCESS_KEY

Self explanatory


## PAPERMERGE__MAIN__LOGGING_CFG

Absolute filesystem path to the yaml file with configuration.
Content of logging configuration file is expected to be in
yaml format and it is very python specific.

Example:

    PAPERMERGE__MAIN__LOGGING_CFG=/etc/papermerge/logging.yaml

## PAPERMERGE__MAIN__PREFIX

This parameter is used in case of multi-tenant deployments. Each tenant has
it's own prefix. E.g. "demo", "prod1".
In case `PAPERMERGE__MAIN__PREFIX` is not empty, its value will
be used to prefix object documents path in S3 bucket.

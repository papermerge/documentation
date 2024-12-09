# OCR Worker

OCR Worker is configured via environment variables.
Note that database and redis url must be **same** as for webapp.


!!! Note

	Source code for OCR worker is <a href="https://github.com/papermerge/ocr-worker/" class="external-link" target="_blank">on github</a>.
	Its docker image is <a href="https://hub.docker.com/r/papermerge/ocrworker" class="external-link" target="_blank">on dockerhub</a>.

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

    Both web_app and ocrworker must have same ``PAPERMERGE__DATABASE__URL``


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

    Both web_app and ocrworker must have same ``PAPERMERGE__REDIS__URL``

## OCR_WORKER_ARGS

Pass celery worker parameters via this environment variable.
In case `PAPERMERGE__MAIN__PREFIX` value is empty, use OCR_WORKER_ARGS="-Q ocr" to
instruct worker to use name "ocr" for the input queue.
For non-empty prefixes, use OCR_WORKER_ARG="-Q prefix_ocr".

For example, if `PAPERMERGE__MAIN__PREFIX=demo`, then OCR_WORKER_ARG should have -Q as OCR_WORKER_ARG="-Q demo_ocr".

Long story short, if you don't know what celery is and how to work with it, use either:

`OCR_WORKER_ARGS="-Q ocr"`

or

`OCR_WORKER_ARGS="-Q ocr -c 2"`

!!! Note

	Celery? Not the plant :smile:! But Python's Celery <a href="https://docs.celeryq.dev/en/stable/getting-started/introduction.html" class="external-link" target="_blank">this one</a>. The task distribution thingy :stuck_out_tongue:!


## Storage

OCR Worker supports two storage backends: local file system and S3.

### Media Root


### S3


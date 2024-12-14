# I3 Worker

I3 Worker is configured via environment variables.
Note that database and redis url must be **same** as for webapp.


!!! Note

	Source code for I3 worker is <a href="https://github.com/papermerge/i3-worker/" class="external-link" target="_blank">on github</a>.
	Its docker image is <a href="https://hub.docker.com/r/papermerge/i3worker" class="external-link" target="_blank">on dockerhub</a>.

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

## I3_WORKER_ARGS

Pass celery worker parameters via this environment variable.
In case `PAPERMERGE__MAIN__PREFIX` value is empty, use I3_WORKER_ARGS="-Q i3" to
instruct worker to use name "i3" for the input queue.
For non-empty prefixes, use I3_WORKER_ARG="-Q prefix_i3".

For example, if `PAPERMERGE__MAIN__PREFIX=demo`, then I3_WORKER_ARG should have -Q as I3_WORKER_ARG="-Q demo_i3".

Long story short, if you don't know what celery is and how to work with it, use either:

`I3_WORKER_ARGS="-Q i3"`

or

`I3_WORKER_ARGS="-Q i3 -c 2"`

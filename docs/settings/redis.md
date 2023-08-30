# Redis


{{ extra.project }} uses redis.


## HOST

Redis host.

Example as environment variable::

    PAPERMERGE__REDIS__HOST=redis

Example as toml config:

    [redis]
    host="redis"


## PORT

Redis port.

Example as environment variable:

    PAPERMERGE__REDIS__PORT=6379

Example as toml config:

    [redis]
    host=6379

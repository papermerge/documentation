# Redis


{{ extra.project }} uses redis.


## REDIS__URL

For Redis the URL is given in following format:

```
redis://HOST:PORT/NUMBER
```

For example:

```
redis://redis:6379/0
```

!!! Note

    Both web_app and worker must have same ``PAPERMERGE__REDIS__URL``

.. _settings__redis:

Redis
=====

|project| uses `redis <https://redis.io/>`_.


.. _settings__redis__host:

``REDIS__HOST``
~~~~~~~~~~~~~~~~

Redis host.

Example as environment variable::

    PAPERMERGE__REDIS__HOST=redis

Example as toml config::

    [redis]
    host="redis"


.. _settings__redis__port:

``REDIS__PORT``
~~~~~~~~~~~~~~~~

Redis port.

Example as environment variable::

    PAPERMERGE__REDIS__PORT=6379

Example as toml config::

    [redis]
    host=6379

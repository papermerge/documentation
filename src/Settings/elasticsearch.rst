.. _settings__elasticsearch:

Elastic Search
==============

|project| uses `elastic search <https://www.elastic.co/>`_ for
indexing and searching.


.. _settings__elasticsearch__hosts:

``ELASTICSEARCH__HOSTS``
~~~~~~~~~~~~~~~~~~~~~~~~~

Elastic search hosts (notice plural).

Example as environment variable::

    PAPERMERGE__ELASTICSEARCH__HOST=es

Example as toml config::

    [elasticsearch]
    hosts="es"


.. _settings__elasticsearch__port:

``ELASTICSEARCH__PORT``
~~~~~~~~~~~~~~~~~~~~~~~~

Elastic search port.

Example as environment variable::

    PAPERMERGE__ELASTICSEARCH__PORT=9200

Example as toml config::

    [elasticsearch]
    port=9200

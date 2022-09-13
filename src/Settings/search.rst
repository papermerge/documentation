.. _settings__elasticsearch:

Search Engine
=============

|project| supports multiple search engine backends:

* `xapian`_
* `elasticsearch`_
* `solr`_
* `whoosh`_


.. _settings__search__engine:

``PAPERMERGE__SEARCH__ENGINE``
------------------------------

Search engine backend to use. Following
values are possible:

* ``xapian`` (for Xapian search engine)
* ``es``, ``elastic``, ``elasticsearch``, ``es7``, ``elastic7``, ``elasticsearch7`` for elastic search backend
* ``solr`` - for solr search engine backend
* ``whoosh`` - for whoosh backend

Example as environment variable::

    PAPERMERGE__SEARCH__ENGINE=xapian

Example as toml config::

    [search]
    engine=whoosh

Default value is ``xapian``.

.. _settings__search__url:

``PAPERMERGE__SEARCH__URL``
---------------------------

URL of search engine.
This setting is **applicable only in case of Elastic and Solr** backends.

Example as environment variable::

    PAPERMERGE__SEARCH__ENGINE=elastic7
    PAPERMERGE__SEARCH__URL=http://my-elastic7-host:9200

Example as toml config::

    [search]
    engine=elastic7
    url=http://my-elastic7-host:9200


.. _settings__search__path:

``PAPERMERGE__SEARCH__PATH``
----------------------------

PATH on the filesystem where of search index is stored.
This setting is **applicable only in case of Xapian and Whoosh** backends.

Example as environment variable::

    PAPERMERGE__SEARCH__ENGINE=xapian
    PAPERMERGE__SEARCH__PATH=/app/xapian_index

Example as toml config::

    [search]
    engine=xapian
    path=/app/xapian_index


.. _elasticsearch: https://www.elastic.co/
.. _solr: https://solr.apache.org/
.. _xapian: https://xapian.org/
.. _whoosh: https://whoosh.readthedocs.io/en/latest/
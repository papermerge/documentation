# Search Engine

{{ extra.project }} supports multiple search engine backends:

* <a href="https://xapian.org/" class="external-link" target="_blank">xapian</a>
* <a href="https://www.elastic.co/" class="external-link" target="_blank">elasticsearch</a>
* <a href="https://solr.apache.org/" class="external-link" target="_blank">solr</a>
* <a href="https://whoosh.readthedocs.io/en/latest/" class="external-link" target="_blank">whoosh</a>


## ENGINE

Search engine backend to use. Following
values are possible:

* `xapian` (for Xapian search engine)
* `es`, `elastic`, `elasticsearch`, `es7`, `elastic7`, `elasticsearch7` for elastic search backend
* `solr` - for solr search engine backend
* `whoosh` - for whoosh backend

Example as environment variable::

    PAPERMERGE__SEARCH__ENGINE=xapian

Example as toml config:

    [search]
    engine=whoosh

Default value is `xapian`.

## URL

URL of search engine.
This setting is {== applicable only in case of Elastic and Solr ==} backends.

Example as environment variable:

    PAPERMERGE__SEARCH__ENGINE=elastic7
    PAPERMERGE__SEARCH__URL=http://my-elastic7-host:9200

Example as toml config:

    [search]
    engine=elastic7
    url=http://my-elastic7-host:9200


## INDEX_NAME

Index name.
This setting is {== applicable only for Elastic ==} backends.

Example as environment variable::

    PAPERMERGE__SEARCH__ENGINE=elastic7
    PAPERMERGE__SEARCH__INDEX_NAME=my_index

Example as toml config:

    [search]
    engine=elastic7
    index_name=my_index


Default value is `papermerge`.



## PATH

PATH on the filesystem where of search index is stored.
This setting is {== applicable only in case of Xapian and Whoosh ==} backends.

Example as environment variable::

    PAPERMERGE__SEARCH__ENGINE=xapian
    PAPERMERGE__SEARCH__PATH=/app/xapian_index

Example as toml config::

    [search]
    engine=xapian
    path=/app/xapian_index

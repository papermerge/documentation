# Search Engine

{{ extra.project }} supports multiple search engine backends. Currently two backends are available:

* <a href="https://xapian.org/" class="external-link" target="_blank">xapian</a>
* <a href="https://solr.apache.org/" class="external-link" target="_blank">solr</a>

## SEARCH__URL

Search engine backend to use. For Solr
format is:

```
solr://HOST:PORT/INDEX
```

Example: ``solr://solr:8983/pmg-index``

For Xapian URL format is `xapian:///PATH`. Example: `xapian:////index_db` - in other words, xapian will store all index
data in `/index_db` folder.

Default value for `PAPERMERGE__SEARCH__URL` is `xapian:////index_db`


!!! Note

    Both web_app and worker must have same ``PAPERMERGE__SEARCH__URL``

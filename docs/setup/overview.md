# Overview

## Web App and Worker

{{ extra.project }} consists of one web app and multiple workers (at least one).
The web app is the one which you see in your browsers or interact via REST API.
The worker (one or multiple) is the part which performs background tasks like
OCR, updating search engine index etc.

## Database

In order to function {{ extra.project }} needs a database, which can be one of following:

* SQLite
* PostgreSQL
* MySQL (MariaDB)

By default {{ extra.project }} uses SQLite.

## Search Engine

{{ extra.project }} supports multiple search engine backends:

* <a href='https://getting-started-with-xapian.readthedocs.io/en/latest' class='external-link' target="_blank">Xapian</a>
* Apache Solr

Xapian is used by default.


## OCR

{{ extra.project }} uses <a class="external-link" target="_blank" href="https://github.com/tesseract-ocr/tesseract">Tesseract</a> to perform Optical Character Recognition.

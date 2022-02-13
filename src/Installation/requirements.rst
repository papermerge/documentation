Requirements
============

Papermerge is web based application. As with any web based application it can be
accessed and used from any modern web browser, like Mozilla Firefox, Chrome,
Edge, or Safari.

.. note::

    To **use** Papermerge all you need is just a modern web browser. Papermerge can be
    accessed and used **from any operating system** (provided a web browser). It can be
    accessed via web browsers from Desktop computers, tablets or mobile phones.

Like a typical web application it runs on server-side Linux or Unix-like
computer. Thus, if you want to deploy and run Papermerge on your own, you
need a Linux/Unix compatible operating system.


If you are interested in how to install Papermerge using docker -
read :ref:`installation_with_docker` section.

In order to successfully deploy Papermerge you need following software:

* `Python`_ >= 3.7
* `Tesseract`_ - because of :ref:`OCR <ocr>`
* Database (`PostgreSQL`_/MySQL/MariaDB/SQLite)
* `Redis`_
* `Elasticsearch`_

Python
#######

Papermerge (server side) is written in Python programming language. The
minimum Python version required is 3.7.

Papermerge uses `Django`_ Web Framework as backend technology.

Tesseract
#########

If you never heard of `Tesseract software`_ - it is google's open source
`Optical Character Recognition`_ software.  It extracts text from images. It
works fantastically well for wide range of human languages.


.. _Python: https://www.python.org/
.. _Tesseract: https://github.com/tesseract-ocr/tesseract
.. _Tesseract software: https://en.wikipedia.org/wiki/Tesseract_(software)
.. _Elasticsearch: https://www.elastic.co/downloads/elasticsearch
.. _Redis: https://redis.io/documentation
.. _PostgreSQL: https://www.postgresql.org/
.. _Optical Character Recognition: https://en.wikipedia.org/wiki/Optical_character_recognition
.. _Django: https://www.djangoproject.com/
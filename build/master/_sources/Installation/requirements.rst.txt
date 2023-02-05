Requirements
============

|project| is web based application. As with any web based application it can be
accessed and used from any modern web browser, like Mozilla Firefox, Chrome,
Edge, or Safari.

.. note::

    To **use** |project| all you need is just a modern web browser. |project| can be
    accessed and used **from any operating system** (provided a web browser). It can be
    accessed via web browsers from Desktop computers, tablets or mobile phones.

Like a typical web application it runs on server-side Linux or Unix-like
computer. Thus, if you want to deploy and run |project| on your own, you
need a Linux/Unix compatible operating system.


If you are interested in how to install |project| using docker -
read :ref:`installation_with_docker` section.

In order to successfully deploy |project| you need following software:

* `Python`_ >= 3.9
* `Tesseract`_ - because of :ref:`OCR <ocr>`
* Database (`PostgreSQL`_/MySQL/MariaDB/SQLite)
* `Redis`_


Python
------

Papermerge (server side) is written in Python programming language. The
minimum Python version required is 3.7.

Papermerge uses `Django`_ Web Framework as backend technology.

Tesseract
---------

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
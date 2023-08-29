# Requirements


{{ extra.project }} is web based application. As with any web based application it can be
accessed and used from any modern web browser, like Mozilla Firefox, Chrome,
Edge, or Safari.

!!! note

    To **use** {{ extra.project }} all you need is just a modern web browser. {{ extra.project }} can be
    accessed and used **from any operating system** (provided a web browser). It can be
    accessed via web browsers from Desktop computers, tablets or mobile phones.

Like a typical web application it runs on server-side Linux or Unix-like
computer. Thus, if you want to deploy and run {{ extra.project }} on your own, you
need a Linux/Unix compatible operating system.


If you are interested in how to install {{ extra.project }} using docker -
read [installation with docker](docker.md) section.

In order to successfully deploy {{ extra.project }} you need following software:

* <a class="external-link" target="_blank" href="https://www.python.org/">Python</a> >= 3.9
* <a class="external-link" target="_blank" href="https://github.com/tesseract-ocr/tesseract">Tesseract</a> - because of OCR
* Database (PostgreSQL/MySQL/MariaDB/SQLite)
* Redis


## Python

Papermerge (server side) is written in Python programming language. The
minimum Python version required is 3.7.

Papermerge uses <a class="external-link" target="_blank" href="https://www.djangoproject.com/">Django Web Framework</a> as backend technology.


## Tesseract

If you never heard of <a class="external-link" target="_blank" href="https://github.com/tesseract-ocr/tesseract">Tesseract</a>  - it is google's open source Optical Character Recognition software.  It extracts text from images. It
works fantastically well for wide range of human languages.


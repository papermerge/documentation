Requirements
============

Papermerge is web based application. As with any web based application it can be
accessed and used from any modern web browser, like Mozilla Firefox, Chrome,
Edge, or Safari.

.. note::

    To **use** Papermerge all you need is just a modern web browser. Papermerge can be 
    accessed and used **from any operating system** (provided a web browser). It can be
    accessed via web browsers from Desktop computers, tablets or mobile phones. 

Like a typical web application it runs on server-side Linux or Unix-like computer. Thus, if you want
to deploy and run Papermerge on your own, you need a Linux/Unix compatible operating system.

.. note::

    To **deploy** Papermerge you need a Linux or Unix-like operating system. 

Following installation guide explains how to install and configure Papermerge
on Ubuntu or Debian based Linux computer. With minor adjustments you must be
able to successfully install and run Papermerge on any flavor of modern Linux
(or Unix) computer.


Software Requirements
~~~~~~~~~~~~~~~~~~~~~~~

In order to successfully deploy Papermerge you need following software:

* `Python <https://www.python.org/>`_ >= 3.7
* `Django <https://www.djangoproject.com/>`_ >= 3.0
* `Tesseract <https://github.com/tesseract-ocr/tesseract>`_ - because of :ref:`OCR <ocr>`
* `Imagemagick <https://imagemagick.org/script/index.php>`_ - Image operations
* `Poppler <https://poppler.freedesktop.org/>`_ - PDF operations

Python
#######

Papermerge is a Python 3 application.

Imagemagick
###########

Papermerge uses Imagemagick to convert between images format

Poppler
#########

More exactly poppler utils are used. For exampple pdfinfo command line
utility is used to find out number of page in PDF document.

Tesseract
#########

If you never heard of `Tesseract software
<https://en.wikipedia.org/wiki/Tesseract_(software)>`_ - it is google's open
source `Optical Character Recognition
<https://en.wikipedia.org/wiki/Optical_character_recognition>`_ software.  It
extracts text from images. It works fantastically well for wide range of
languages.


In addition to the above, there are a number of Python requirements, all of which are listed in a file called ``requirements/base.txt`` in the project root directory.


Hardware Requirements
~~~~~~~~~~~~~~~~~~~~~~~
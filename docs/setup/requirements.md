# Requirements

Papermerge is web based application. As with any web based application it can be
accessed and used from any modern web browser, like Mozilla Firefox, Chrome,
Edge, or Safari.

!!! note

    To use Papermerge all you need is just a modern web browser. Papermerge can be
    accessed and used from any operating system (provided a web browser). It can be
    accessed via web browsers from Desktop computers, tablets or mobile phones.


Like a typical web application it runs on server-side Linux or Unix-like
computer. Thus, if you want to deploy and run Papermerge on your own, you need a
Linux/Unix compatible operating system.

!!! note

    To deploy Papermerge you need a Linux or Unix-like operating system.

Following installation guide explains how to install and configure Papermerge
on Ubuntu or Debian based Linux computer. With minor adjustments you must be
able to successfully install and run Papermerge on any flavor of modern Linux
(or Unix) computer.


## Software Requirements


In order to successfully deploy Papermerge you need following software:

* [Python](https://www.python.org/>) >= 3.7
* [Django](https://www.djangoproject.com/) >= 3.1
* [Tesseract](https://github.com/tesseract-ocr/tesseract)
* [Imagemagick](https://imagemagick.org/script/index.php)
* [Poppler](https://poppler.freedesktop.org/) - PDF operations


## Python

Papermerge (server side) is written in Python programming language. The
minimum Python version required is 3.7.


## Django

Papermerge uses Django Web Framework for its web facing components. The
minimum required version for Django is 3.1. Generally speaking the fact that
Papermerge is written in Django is not important for setup. You won't need to
worry about exact version of Django (or other internal python libraries on
which Papermerge depends) required as this details are conveniently covered by
package management tools like ``pip``.


## Imagemagick


Papermerge uses Imagemagick to convert between images format. You will need to make sure
you have image magic installed.


## Poppler

More exactly poppler utils are used. For exampple pdfinfo command line
utility is used to find out number of page in PDF document.


## Tesseract

If you never heard of [Tesseract software]
(https://en.wikipedia.org/wiki/Tesseract_(software)) - it is google's open
source [Optical Character Recognition](https://en.wikipedia.org/wiki/Optical_character_recognition) software.  It
extracts text from images. It works fantastically well for wide range of
human languages.


In addition to the above, there are a number of Python requirements, all of
which are listed in a file called ``requirements/base.txt`` in the project
root directory.


## Hardware Requirements


Papermerge can run a single or multiple hosts (computers). OCR operations are
performed by a component called worker. There can be one or more workers. For
more efficient setups worker(s) should run on separate computer(s). The exact
number of papermerge workers depends on your documents volume.


### Single Host

On single host, both web component and worker components run on same computer.

The minimum hardware requirements in this case are:

* 1 GHz CPU
* 1 GB RAM
* 25 GB disk space

!!! note

    Please keep in mind that Papermerge uses Tesseract for optical character
    recognition (OCR) operations. **OCR is very CPU intense task.** The rule here
    is simple - more powerful CPU and more RAM - better! A more powerful CPU (+
    more RAM) will be able to complete OCR operations faster.


### Multiple Hosts

In multiple hosts scenarios, the web component (i.e. the web application)
requires less resources:

* 900 MHz CPU
* 512 MB RAM
* 15 GB disk space

Minimum requirements for 1 worker are:

* 1 GHz CPU
* 1 GB RAM
* 25 GB disk space

# Requirements

## Software

{{ extra.project }} is designed to run on Linux/Unix compatible system.

You need to have docker installed, as {{ extra.project }} is shipped as docker image.
All docker images are stored on <a href="https://hub.docker.com/u/papermerge" class="external-link" target="_blank">docker hub</a>.

Make sure that you have docker available:

        $ docker --version
        Docker version 24.0.3, build 3713ee1

## Hardware

Hardware specification for {{ extra.project }} depends on number of documents and users.

For one user with 1000-2000 pages a system spec with:

* 2 CPU at 2.8GHz clock
* 2 GB RAM
* 25 GB Storage

will do just fine.

For OCR, {{ extra.project }} uses [Tesseract](https://github.com/tesseract-ocr/tesseract).
OCR is very CPU intensive operation, thus more CPUs and RAM memory your system has - better.
More CPU cores and more powerful the CPUs means OCR will be performed faster.


!!! Note

        **GPU is not needed** as Tesseract runs OCR entirely on your CPU.

Testing system for {{ extra.project }} has following specs:

* Ubuntu 22.04
* 8 Core i7 2.8GHz CPU
* 16 GB RAM
* 50 GB storage

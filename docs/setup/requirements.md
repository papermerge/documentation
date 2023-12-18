# Requirements


All you need is to have docker, as {{ extra.project }} is shipped as docker image.
All docker images are stored on <a href="https://hub.docker.com/u/papermerge" class="external-link" target="_blank">docker hub</a>.

Make sure that you have docker available:

        $ docker --version
        Docker version 24.0.3, build 3713ee1


In order to extract textual data from document {{ extra.project }} uses OCR (Optical Character Recognition).
For OCR {{ extra.project }} uses [Tesseract](https://github.com/tesseract-ocr/tesseract).
OCR is very CPU intensive operation, thus more CPUs and RAM memory your system has - better.

Note that GPU is not needed as Tesseract runs OCR entirely on your CPU.

Testing system for {{ extra.project }} has following specs:

* Ubuntu 22.04
* 8 Core i7 2.8GHz CPU
* 16 GB RAM
* 50 GB storage

The minimum system specification are:

* 1 CPU at 1.8GHz clock
* 1 GB RAM
* 10 GB Storage

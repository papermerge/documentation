# Papermerge - Documentation


Documentation is divided into 4 sections:

1. Installation
2. Help
3. User's Manual
4. Contributing


## Getting Started

In order to see documentation locally get latest docker image from docker hub::

    $ docker pull papermerge/documentation

``papermerge/documentation`` docker images exposes web service on port 80 i.e. it serves
documentation as html using nginx on port 80::

    $ docker run -d --name docs -p 9042:80 papermerge/documentation
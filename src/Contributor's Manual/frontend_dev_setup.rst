.. _frontend_dev_setup:

Frontend Development Setup
==========================

This guide is intended for those who want play with **frontend** code for Papermerge.
It order to follow it you need to be comfortoble with linux command line and JavaScript
programming language.

In this guide Ubuntu 20.04 LTS is used as Linux distribution.

If you follow this document and still have troubles, please open an
`issue on GitHub <https://github.com/ciur/papermerge/issues>`_.

First install `NodeJs`_ version 16.x and make sure it is available on your system::

    $ node -v

    v16.15.0

Also, make sure you have `npm`_  (node package manager) as well::

    $ npm --version

    8.5.5


Install `EmberJs`_::

    $ sudo npm install -g ember-cli


Clone `PapermergeJs`_ repository::

    $ git clone git@github.com:papermerge/papermerge.js.git


Install javascript dependencies::

    $ cd papermerge.js
    $ npm install

Run local development server::

    $ ember serve

If you wish to bind local server to different IP::

    $ ember serve --host 0.0.0.0 --port 4200


.. note::

    By default ember application assumes that REST API backend server
    is available on ``http://localhost:8000/api/``


.. _NodeJs: https://nodejs.org/en/
.. _npm: https://www.npmjs.com/
.. _EmberJs: https://emberjs.com/
.. _PapermergeJs: https://github.com/papermerge/papermerge.js
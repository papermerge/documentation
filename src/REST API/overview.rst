.. _rest_api:

Overview
=========


In order to use REST API interface you need an http client. Probably the most
wide-spread (and free) http client is `cUrl <https://en.wikipedia.org/wiki/CURL>`_.

Another convenient, free to use and with graphical user interface http client is
`Postman <https://www.postman.com/>`_.

In following sections cUrl will be used to illustrate examples of usages.

Server URL + Prefix
--------------------

Throughout this REST API documentation you will notice reference to
``<server-url>`` - this is base http (or https) url of your Papermerge instance. Base url depends on where your instance was deployed.

Please note that ``<server-url>`` always includes the ``/api/`` prefix.
In subsequent parts this reference the ``/api/`` prefix is omitted, however
you always need to keep a mental note to include it.

Examples of
``<server-url>`` with prefix:

* http://localhost:8000/api/
* https://example.com/api/
* https://my-papermerge-instance.secure.com/api/

Let's take an example for specific API, say :ref:`api_auth`. If your ``<server-url>``
is https://example.com/api/ then, in order to authenticate and get a token you'll need to run
following curl command::

  curl -XPOST https://example.com/api/auth/login/ \
  -H 'Content-Type: application/json' \
  -d '{"username":"john","password":"password"}'

Another example, this time using :ref:`api_users`::

   curl https://example.com/api/users/ \
    -H 'Content-Type: application/vnd.api+json'
    -H 'Authorization: Token ababfa840abb6b8aa3a185e631c19095c70de932'

.. note:: When quering **for json data types always pay attention to
   Content-Type header**. For json data it sometimes may be either
   ``application/json`` or ``application/vnd.api+json``. Each REST API call
   reference documents correct value of ``Content-Type`` header.

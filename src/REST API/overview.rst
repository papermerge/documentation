.. _rest_api:

Overview
=========

In order to use REST API interface you need an http client. The most
wide-spread http client is `curl`_.

In following sections `curl`_ will be used to illustrate examples of usages.

Server URL
~~~~~~~~~~

Throughout this REST API documentation you will notice reference to
``<server-url>`` - this is base http address of your |project|
instance. Base url/address is where your instance was deployed.
Depending where your |project| instance was deployed you may use
``https`` instead of ``http`` and use correct port number.

Examples of ``<server-url>``:

* http://localhost:8000/
* https://example.com/
* https://my-app.papermerge.io/

Let's take an example for authentication REST API. If your ``<server-url>``
is https://example-app.papermerge.io/ then, in order to authenticate and get a token you'll need to run
following curl command::

  curl -XPOST https://example-app.papermerge.io/api/auth/login/ \
  -H 'Content-Type: application/json' \
  -d '{"username":"john","password":"password"}'

Another example, this time with users endpoint::

   curl https://example-app.papermerge.io/api/users/ \
    -H 'Content-Type: application/vnd.api+json'
    -H 'Authorization: Token ababfa840abb6b8aa3a185e631c19095c70de932'

.. note:: When quering **for json data types always pay attention to
   Content-Type header**. For json data it sometimes may be either
   ``application/json`` or ``application/vnd.api+json``. Each REST API call
   reference documents correct value of ``Content-Type`` header.

.. _rest_api_overview_authentication:


Authentication
~~~~~~~~~~~~~~

Papermerge REST API backend uses **token based** authentication, this means
that you will need to send your credentials to the backend API server and if
credentials are correct, then server's response will contain a valid token in
response's body. For all subsequent requests, which require authorization,
you will need to append ``Authorization`` header with ``Token <token>``
value.

.. tip::

  After you've retrieved token for your account, **all subsequent requests** need to
  include ``Authorization: Token <token>`` header.


For authentication use authentication endpoint.
Example:

.. code-block:: bash

  curl -X POST \
    <server-url>/api/auth/login/ \
    -H 'Content-Type: application/json' \
    -d '{"username":"john","password":"<password here>"}'

When credentials are correct, response will have status 200 OK,
``content-type`` will be ``application/json`` and response will have
following body:

.. code-block:: bash

  {
    "token": <your token here>,
    "expiry": null
  }

With authentication token at hand, you can perform any REST API, for
example:

.. code-block:: bash

  curl https://example.com/api/users/me/ \
    -H 'Content-Type: application/vnd.api+json'
    -H 'Authorization: Token ababfa840abb6b8aa3a185e631c19095c70de932'

.. note:: When quering for json data types always pay attention to
   ``Content-Type``. For json data it sometimes may be either
   ``application/json`` or ``application/vnd.api+json``. Each REST API call
   reference documents correct value of ``Content-Type`` header.


Nodes, Folders and Documents
~~~~~~~~~~~~~~~~~~~~~~~~~~~~




.. _curl: https://en.wikipedia.org/wiki/CURL

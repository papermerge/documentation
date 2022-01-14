Authentication
================


Papermerge REST API backend uses **token based** authentication, this means that you will need to send your
credentials to the backend API server and if credentials are correct server's response
will contain a valid token in response's body. For all subsequent requests, which require authorization, you will need to append ``Authorization``
header with ``Token <token>`` value.

.. tip::

  After you retrieved token for your user, **all subsequent requests** need to
  include ``Authorization: Token <token>`` header.


For authentication use :ref:`api_auth_token` endpoint.
Example:

.. code-block:: bash

  curl -X POST \
    <server-url>/auth-token/ \
    -H 'Content-Type: application/json' \
    -d '{"username":"john","password":"<password here>"}'

When credentials are correct, response will have status 200 OK,
``content-type`` will be ``application/json`` and response will have
following body:

.. code-block:: bash

  {
    "token": <your token here>
  }

With authentication token at hand, you can perform any REST API, for
example:

   curl https://example.com/api/users/me/ \
    -H 'Content-Type: application/vnd.api+json'
    -H 'Authorization: Token ababfa840abb6b8aa3a185e631c19095c70de932'

.. note:: When quering for json data types always pay attention to
   ``Content-Type``. For json data it sometimes may be either
   ``application/json`` or ``application/vnd.api+json``. Each REST API call
   reference documents correct value of ``Content-Type`` header.
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
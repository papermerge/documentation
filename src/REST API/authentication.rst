Authentication
================

.. warning::

  REST API described here is work in progress. It changes
  along with the development of `Papermerge Core <https://github.com/papermerge/papermerge-core>`_ in master branch.

Papermerge REST API backend uses **token based** authentication, this means that you will need to send your
credentials to the server and it will respond (in case credentials are correct)
with a token. For all subsequent requests, you will need to append ``Authorization``
header with ``Token <token>`` value.

.. note::

  After you retrieved token for your user, **all subsequent requests** need to
  have ``Authorization: Token <token>`` header.


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
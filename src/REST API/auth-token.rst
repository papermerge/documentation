auth-token
===========


POST /auth-token/
******************

Authenticates user with given username and password. Response will contain token to be used
for subsequent requests.

Request
--------

content-type: application/json

.. code-block:: bash

  {
    username*: string
    password*: string
  }


Response
---------


.. code-block:: bash

  {
    token: string
  }


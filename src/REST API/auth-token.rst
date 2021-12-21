.. _auth_token:

auth-token
===========


POST /auth-token/
******************

Authenticates user with given username and password. Response will contain token to be used
for subsequent requests. Notice the slash ``/`` at the end of endpoint.

Request
--------

content-type: **application/json**

.. code-block:: bash

  {
    username*: string
    password*: string
  }


Response (success) / 200
--------------------------

If provided credentials are correct, the response will have following format:

.. code-block:: bash

  {
    token: string
  }

Response (error) / 400 Bad Request
------------------------------------

If provided credentials are wrong, the response will have following:

.. code-block:: bash

  {
    non_field_errors: [
      "Unable to log in with provided credentials."
    ]
  }

In case request missed (or misspelled) username field, the reponse will be (with status 400 Bad Request):

.. code-block:: bash

  {
    username: [
      "This field is required."
    ]
  }


Examples
--------

.. code-block:: bash

  curl -X POST \
    <server-url>/auth-token/ \
    -H 'Content-Type: application/json' \
    -d '{"username":"john","password":"<password here>"}'

When credentials are correct, response will have status 200 OK, ``content-type`` will be``application/json`` and response will have following body:

.. code-block:: bash

  {
    "token": <your token here>
  }

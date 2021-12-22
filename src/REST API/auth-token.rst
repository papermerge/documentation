.. _api_auth_token:

Auth-token
===========


.. http:POST:: /auth-token/
  :noindex:

  Authenticates user with given username and password. Response will contain token to be used as part of Authorization header in subsequent requests whenever authorization is required.

  :reqheader Content-Type: application/json
  :status 200: on successfull authentication
  :status 400: when credentials are wrong OR when mandatory json fields (username, password) are missing

  **Request Body Schema**

  .. code-block:: bash

    {
      username*: string
      password*: string
    }

  **200 - Response Body Schema**

  .. code-block:: bash

    {
      token: string
    }

  **400 - Response Body Schema**

  If provided credentials are wrong, the response's body will have following structure:

  .. code-block:: bash

    {
      non_field_errors: [
        "Unable to log in with provided credentials."
      ]
    }

  In case request missed (or misspelled) username field, the reponse's body will be:

  .. code-block:: bash

    {
      username: [
        "This field is required."
      ]
    }


  **Example Request**

  .. sourcecode:: http

    POST /http-auth/ HTTP/1.1
    Host: example.com
    Accept: application/json
    Content-Type: application/json

    {
      "username": "john",
      "password": "password"
    }


  **Example Response**

  .. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
      "token": "12caf9840aeb6bafa3a218e321c19095c70de298"
    }

  **Example with cURL**

  .. code-block:: bash

    curl -X POST <server-url>/auth-token/ \
      -H 'Content-Type: application/json' \
      -d '{"username":"john","password":"password"}'

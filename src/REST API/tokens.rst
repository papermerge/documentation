.. _api_tokens:

Tokens
=======

.. warning::

  REST API described here is work in progress. It changes
  along with the development of `Papermerge Core`_ in master branch.


Each user can have multiple authentication tokens. The reason to have multiple
tokens per user is that he (or she) may consume Papermerge REST API from
multiple clients (or devices) using one single user account. User may then use a separate authentication token per each device or client.

For token usage see :ref:`api_authentication`.

.. _Papermerge Core: https://github.com/papermerge/papermerge-core


.. _api_get_tokens:

GET /tokens/
------------------

.. http:GET:: /tokens/

  Retrieves user's (user is identified based on token in ``Authorization`` header) all tokens.

  :reqheader Content-Type: application/vnd.api+json
  :reqheader Authorization: Token <token>
  :status 200: on success

  **200 - Response Body Schema**

  .. code-block:: bash

    {
      links: {
        first: string,
        last: string,
        next: string,
        prev: string
      },
      data: [  # an array of tokens
        {
          type: "auth_tokens",
          id: string,
          attributes: {
            token: null,
            digest: string,
            created: datetime,
            expiry: datimetime | null
          },
        },
        {
          ... token instance
        },
        ...
      ],
      meta: {
        pagination: {
            page: integer,
            pages: integer,
            count: integer
        }
      }
    }

.. note::

  Because tokens are stored encrypted in database, user can retrieve only
  token's digest. Also, this is the reason why, in ``GET /tokens/`` response,
  field ``token`` will be always set to ``null``.


.. _api_post_tokens:

POST /tokens/
------------------

.. http:POST:: /tokens/

  Creates a token for user (user is identified based on token in ``Authorization`` header). Created token is set to expire in ``expiry_hours`` hours.

  :reqheader Content-Type: application/vnd.api+json
  :reqheader Authorization: Token <token>
  :status 200: on success

**Request Body Schema**

  .. code-block:: bash

    {
      data: {
        type: "auth_tokens",
        attributes: {
          expiry_hours: integer,
        }
      }
    }

.. note::

  Request's body can be empty. If request's body is empty, newly created token
  will be set to expire in 31 days.


**200 - Response Body Schema**

  .. code-block:: bash

    {
      data: {
        type: "auth_tokens",
        id: string,
        attributes: {
          digest: string,
          token: string,
          created: datetime,
          expiry: datetime,
        },
      }
    }

.. note::

  ``POST /tokens/`` respose's body contains **non empty** ``token`` field. This
  field (i.e. ``token`` field) contains **unencrypted** token which must be
  saved further usage. Token creation's response body is the only place where token is visible unencrypted.


DELETE /tokens/<token-digest>/
-------------------------------

.. http:DELETE:: /tokens/<token-digest>/

  Deletes user token.

  :reqheader Content-Type: application/vnd.api+json
  :reqheader Authorization: Token <token>
  :status 200: on success

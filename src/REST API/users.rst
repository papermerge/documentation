.. _api_users:

Users
======

.. warning::

  REST API described here is work in progress. It changes
  along with the development of `Papermerge Core <https://github.com/papermerge/papermerge-core>`_ in master branch.


.. _api_get_users:

GET /users/
-------------

.. http:GET:: /users/

  Retrieves information about all users

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
      data: [  # an array of users
        { # user instance BEGIN
          type: "users",
          id: string,
          attributes: {
            username: string,
            first_name: string,
            last_name: string,
            email: string,
            is_active: boolean,
            is_staff: boolean,
            is_superuser: boolean,
            date_joined: datetime
          },
          relationships: {
            inbox_folder: {
              data: {
                  type: "folders",
                  id: string
              }
            },
            home_folder: {
              data: {
                  type: "folders",
                  id: string
              }
            }
          }
        }  # user instance END
      ],
      meta: {
        pagination: {
            page: integer,
            pages: integer,
            count: integer
        }
      }
    }

.. _api_post_users:

POST /users/
-------------

.. http:POST:: /users/

  Creates a user. Note that password field is not part of this request. The only
  mandatory field is ``username``.

  :reqheader Content-Type: application/vnd.api+json
  :reqheader Authorization: Token <token>
  :status 200: on success
  :status 400: when request does not contain valid schema

  **Request Body Schema**

  .. code-block:: bash

    {
      data: {
        type: "users",
        attributes: {
          username*: string,
          first_name: string,
          last_name: string,
          email: string,
          is_active: boolean,
          is_staff: boolean,
          is_superuser: boolean,
          date_joined: datetime
        }
      }
    }

  **200 - Response Body Schema**

  .. code-block:: bash

    {
      data: {
        type: "users",
        id: string,
        attributes: {
          username: string,
          first_name: string,
          last_name: string,
          email: string,
          is_active: boolean,
          is_staff: boolean,
          is_superuser: boolean,
          date_joined: datetime
        },
        relationships: {
          inbox_folder: {
            data: {
              type: "folders",
              id: string
            }
          },
          home_folder: {
            data: {
              type: "folders",
              id: string
            }
          }
        }
      }
    }

.. note::

  Upon creation, newly created user is assigned
  two special folders *inbox* and *home*. The IDs of these special folders is included in http the reponse (``relationships`` field). Use can use IDs of those folders to query their content.


.. _api_get_users_id:

GET /users/{id}/
-----------------

.. http:GET:: /users/{id}/

  Retrieve information about user

  :reqheader Content-Type: application/vnd.api+json
  :reqheader Authorization: Token <token>
  :status 200: on success
  :status 404: when user with given ID does not exists

  **200 - Response Body Schema**

  .. code-block:: bash

    {
      type: "users",
      id: string,
      attributes: {
        username: string,
        first_name: string,
        last_name: string,
        email: string,
        is_active: boolean,
        is_staff: boolean,
        is_superuser: boolean,
        date_joined: datetime
      },
      relationships: {
        inbox_folder: {
          data: {
              type: "folders",
              id: string
          }
        },
        home_folder: {
          data: {
              type: "folders",
              id: string
          }
        }
      }
    }


  **404 - Response**

  .. sourcecode:: http

    HTTP/1.1 404 Not Found
    Content-Type: application/vnd.api+json

    {
      "errors": [
        {
          "detail": "Not found.",
          "status": "404",
          "code": "not_found"
        }
      ]
    }


  **Example Response**

  .. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/vnd.api+json

    {
      "data": {
        "type": "users",
        "id": "2",
        "attributes": {
          "username": "john",
          "first_name": "",
          "last_name": "",
          "email": "john@example.com",
          "is_active": true,
          "is_staff": false,
          "is_superuser": false,
          "date_joined": "2021-12-21T10:55:18.976430Z"
        },
        "relationships": {
          "inbox_folder": {
            "data": {
                "type": "folders",
                "id": "4"
            }
          },
          "home_folder": {
            "data": {
              "type": "folders",
              "id": "5"
            }
          }
        }
      }
    }

.. _api_delete_users_id:

DELETE /users/{id}/
--------------------

.. http:DELETE:: /users/{id}/

  Deletes user

  :reqheader Authorization: Token <token>
  :status 204: on successful user deletion
  :status 404: when user with given ID does not exists

.. _api_patch_users_id:

PATCH /users/{id}/
-------------------

.. http:PATCH:: /users/{id}/

  Updates user

  :reqheader Content-Type: application/vnd.api+json
  :reqheader Authorization: Token <token>
  :status 200: on successful user update
  :status 404: when user with given ID does not exists

  **Request Body Schema**

  .. code-block:: bash

    {
      type: "users",
      id: string,
      attributes: {
        username: string,
        first_name: string,
        last_name: string,
        email: string,
        is_active: boolean,
        is_staff: boolean,
        is_superuser: boolean,
        date_joined: datetime
      },
      relationships: {
        inbox_folder: {
          data: {
              type: "folders",
              id: string
          }
        },
        home_folder: {
          data: {
              type: "folders",
              id: string
          }
        }
      }
    }

.. _api_post_users_id_change_password:

POST /users/{id}/change-password/
----------------------------------

.. note::

  For this endpoint Content-Type header must be **application/json**

.. http:POST:: /users/{id}/change-password/

  Change user password

  :reqheader Content-Type: application/json
  :reqheader Authorization: Token <token>
  :status 200: on successful password update
  :status 404: when user with given ID does not exists


  **Request Body Schema**

  .. code-block:: bash

    {
      password: string
    }

  **Request Example**

  .. sourcecode:: http

    POST /users/2/change-password/ HTTP/1.1
    Content-Type: application/json
    Host: example.com

    {
      "password": "newpassword"
    }


.. _api_get_users_me:

GET /users/me/
----------------

.. http:GET:: /users/me/

  Notice the slash ``/`` at the end.
  Retrieves information about currently authenticated user.

  reqheader Content-Type: application/json


  **200 - Response Body Schema**

  .. code-block:: bash

    {
      data: {
        type: "users",
        id: string,
        attributes: {
          username: string,
          first_name: string,
          last_name: string,
          email: string,
          is_active: boolean,
          is_staff: boolean,
          is_superuser: boolean,
          date_joined: datetime
        },
        relationships: {
          inbox_folder: {
            data: {
                type: "folders",
                id: string
            }
          },
          home_folder: {
            data: {
                type: "folders",
                id: string
            }
          }
        }
      }
    }

.. note::

  Pay special attention to *relationships* part.
  It provides IDs of user's home and inbox folders.
  With those IDs you can query content of
  user's home and inbox folders via :ref:`api_nodes` endpoint.

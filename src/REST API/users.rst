.. _api_users:

Users
======


GET /users/
*************

Retrieves information about all users


Request
--------

content-type: **application/vnd.api+json**


Response (success) / 200 OK
---------------------------

.. code-block:: bash

  {
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
    ]
  }


POST /users/
***************

Creates a user. Note that password field is not part of this request. The only
mandatory field is ``username``.

Request
---------

content-type: **application/vnd.api+json**

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

Response (success) / 200 OK
-----------------------------

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


GET /users/{id}/
******************

Retrieve information about user

DELETE /users/{id}/
********************

Deletes user


PATCH /users/{id}/
*******************

Updates user

POST /users/{id}/change-password/
***********************************

Change user password


GET /users/me/
******************

Notice the slash ``/`` at the end.
Retrieves information about currently authenticated user.


Request
--------

content-type: **application/vnd.api+json**


Response (success) / 200 OK
---------------------------

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

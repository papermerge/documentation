.. _api_users:

Users
======

.. warning::

  REST API described here is work in progress. It changes
  along with the development of `Papermerge Core <https://github.com/papermerge/papermerge-core>`_ in master branch.


.. http:GET:: /users/

  Retrieves information about all users

  :reqheader Content-Type: application/vnd.api+json
  :reqheader Authorization: Token <token>
  :status 200: on success
  :status 400: when request does not contain valid schema


  **200 - Response Body Schema**

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


.. http:GET:: /users/{id}/

  Retrieve information about user

.. http:DELETE:: /users/{id}/

  Deletes user


.. http:PATCH:: /users/{id}/

  Updates user


.. http:POST:: /users/{id}/change-password/

  Change user password


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

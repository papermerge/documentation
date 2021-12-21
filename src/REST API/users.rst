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
  With home and inbox folder's ID you can query then via :ref:`api_nodes` and point

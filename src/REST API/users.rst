.. _api_users:

users
======


GET /users/me/
******************

Notice the slash ``/`` at the end.
Retrieves information about currently authenticated user.

Request
--------

content-type: **application/json**


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


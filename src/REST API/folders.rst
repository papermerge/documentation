.. _api_folders:

Folders
=========

.. warning::

  REST API described here is work in progress. It changes
  along with the development of `Papermerge Core <https://github.com/papermerge/papermerge-core>`_ in master branch.

.. _api_get_folders:

GET /folders/
-------------

.. http:GET:: /folders/

  Retrieves a flat list of all folders of current user. If your intention is to get a list of directly descendent *folders and documents* of specific folder - use :ref:`api_get_nodes_id` endpoint.

  .. note:: This endpoint deals only with folders

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
      data: [
        {
          type: "folders",
          id: string,
          attributes: {
            title: string,
            created_at: datetime,
            updated_at: datetime
          },
          relationships: {
            parent: {
              data: {
                type: "folders",
                id: string
              }
            }
          }
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

.. _api_post_users:

POST /folders/
-------------

.. http:POST:: /folders/

  Creates a folder. Similarely you can create
  a folder using :ref:`api_post_nodes`.

  :reqheader Content-Type: application/vnd.api+json
  :reqheader Authorization: Token <token>
  :status 200: on success
  :status 400: when request does not contain valid schema

  **Request Body Schema**

  .. code-block:: bash

    {
      data: {
        type: "folders",
        attributes: {
            title: string
        },
        relationships: {
           parent: {
              data: {
                 id: string,
                 "type": "folders"
              }
           }
        }
      }
    }

.. _api_get_folders_id:

GET /folders/{id}/
----------------------

.. http:GET:: /folders/{id}/

  Retrieves information about document

  :reqheader Content-Type: application/vnd.api+json
  :reqheader Authorization: Token <token>
  :status 200: on success
  :status 404: when folder with given ID does not exists


  **200 - Response Body Schema**

  .. code-block:: bash

    {
      data: {
        type: "folders",
        id: string,
        attributes: {
          title: string,
          created_at: datetime,
          updated_at: datetime
        },
        relationships: {
          parent: {
            data: {
              type: "folders",
              id: string
            }
          }
        }
      }
    }


.. _api_delete_folders_id:

DELETE /folders/{id}/
--------------------

.. http:DELETE:: /folders/{id}/

  Deletes the folder with specified ID

  :reqheader Authorization: Token <token>
  :status 204: on successful folder deletion
  :status 404: when folder with given ID does not exists


.. _api_patch_folders_id:

PATCH /folders/{id}/
-------------------

.. http:PATCH:: /folders/{id}/

  Updates folder title

  :reqheader Content-Type: application/vnd.api+json
  :reqheader Authorization: Token <token>
  :status 200: on successful folder update
  :status 404: when folder with given ID does not exists

  **Request Body Schema**

  .. code-block:: bash

    {
      data: {
        id: string,
        type: "folders",
        attributes: {
          title: string
        },
      }
    }

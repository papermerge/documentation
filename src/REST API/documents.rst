.. _api_documents:

Documents
==========

.. warning::

  REST API described here is work in progress. It changes
  along with the development of `Papermerge Core <https://github.com/papermerge/papermerge-core>`_ in master branch.


Notice that document creation/upload is two steps process:

1. Use :ref:`api_post_nodes` with ``type: "documents"`` to create document model
2. Use :ref:`api_put_documents_upload` to upload the actual file

as of result of above mentioned two step process, there is no "POST method for /documents/ endpoint".

.. note::
  It is actually three steps process, if you consider the fact that for creating/uploading you also need to know the parent node ID where to place that document:
    a. Learn ID of the parent node (eventually using :ref:`api_get_users_me`)
    b. Create document under specific node using  :ref:`api_post_nodes`
    c. Upload file for already created document using :ref:`api_put_documents_upload`

.. _api_get_documents:

GET /documents/
-----------------

.. http:GET:: /documents/

  Retrieves a flat list of all documents of current user. If your intention is to get a list of directly descendent *folders and documents* of specific folder - use :ref:`api_get_nodes_id` endpoint.

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
          type: "documents",
          id: string,
          attributes: {
            title: string,
            lang: "deu" | "eng" | "ron" | ... any other supported language,
            file_name: string,
            ocr: boolean,
            ocr_status: succeeded | pending | unknown | failed,
            versions: [ GetVersionAttr, GetVersionAttr, ... ],
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

.. _api_get_documents_id:

GET /documents/{id}/
----------------------

.. http:GET:: /documents/{id}/

  Retrieves information about document

  :reqheader Content-Type: application/vnd.api+json
  :reqheader Authorization: Token <token>
  :status 200: on success
  :status 404: when document with given ID does not exists


  **200 - Response Body Schema**

  .. code-block:: bash

    {
      data: {
        type: "documents",
        id: string,
        attributes: {
          title: string,
          lang: "deu" | "eng" | "ron" | ... any other supported language,
          file_name: string,
          ocr: boolean,
          ocr_status: succeeded | pending | unknown | failed,
          versions: [ GetVersionAttr, GetVersionAttr, ... ],
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

.. _api_delete_documents:

DELETE /documents/{id}/
------------------------

.. http:DELETE:: /documents/{id}/

  Deletes the document with specified ID

  :reqheader Authorization: Token <token>
  :status 204: on successful folder deletion
  :status 404: when document with given ID does not exists

.. _api_patch_documents_id:

PATCH /documents/{id}/
-----------------------

.. http:PATCH:: /documents/{id}/

  Updates document's attributes

  :reqheader Content-Type: application/vnd.api+json
  :reqheader Authorization: Token <token>
  :status 200: on successful document update
  :status 404: when document with given ID does not exists

  **Request Body Schema**

  .. code-block:: bash

    {
      data: {
        id: string,
        type: "documents",
        attributes: {
          title: string,
          lang: "deu" | "eng" | other supported lang
          file_name: string,
          ocr: boolean,
          ocr_status: succeeded | pending | unknown | failed,
        },
      }
    }



.. _api_put_documents_upload:


PUT /documents/{id}/upload/{file_name}/
-----------------------------------------

.. http:PUT:: /documents/{id}/upload/{file_name}/

  Uploads a file for given document node. If last version of the document does
  not have any file associated yet, this REST API call will associated given
  file with document's last version. If, on the other hand, last version of
  the document already has a file associated with it - a new document version
  will be created and associated it with respective file.

  :reqheader Content-Disposition: Content-Disposition attachment; filename={file_name}
  :reqheader Authorization: Token <token>
  :status 200: on success


GetVersionAttrs
--------------------

.. code-block:: bash

  {
    id: string:
    number: integer,
    lang: "deu" | "eng" | "ron" | any other supported language code,
    file_name: string,
    size: integer,
    page_count: integer,
    short_description: string,
    pages: [
      {
        type: "Page",
        id: string
      },
      ...
    ],
    document: {
      type: "Document",
      id: string  # ID of the parent document
    }
  }

.. _api_nodes:

Nodes
======

.. warning::

  REST API described here is work in progress. It changes
  along with the development of `Papermerge Core <https://github.com/papermerge/papermerge-core>`_ in master branch.

Documents can be organized in folders. One folder can contain documents as
well as other folders. A *node* is an abstraction of two concepts - folder
and document. Each node has a ``type`` field with value either "folders"
or "documents" depending on what kind of node it is.


.. _api_get_nodes_id:

GET  /nodes/{id}/
-------------------

.. note::

  Difference between this endpoint and /folders/{id}/ endpoint is that **/folders/{id}/ will retrieve only folder instances**.

.. http:GET:: /nodes/{id}/

  Retrieves the list of child nodes (i.e. documents and folders) of the given
  node. In this context node identified with {id} should be of type "folders"
  (it does not make sense to "retrieve the list of documents and folders of a
  document").

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
          id: string,
          type: "folders" | "documents",
          attributes: GetNodeFolderAttrs | GetNodeDocumentAttrs,
          relationships: [
            parent: {
              data: {
                type: "folders",
                id: string
              }
            }
          ]
        },
        {
          ...
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


POST /nodes/
--------------

.. http:POST:: /nodes/

  :reqheader Content-Type: application/vnd.api+json
  :reqheader Authorization: Token <token>
  :status 200: on success

  Creates a node (i.e. a document or a folder).

  **Request Body Schema**

  .. code-block:: bash

    {
      data: {
        type: "documents" | "folders"
        attributes: PostNodeFolderAttrs | PostNodeDocumentAttrs,
        parent: {
          data: {
            id: string,
            type: "folders"
          }
        }
      }
    }


POST /nodes/move/
-------------------

.. http:POST:: /nodes/move/

  Moves one or multiple nodes from one location to another.


GetNodeFolderAttrs
--------------------

.. code-block:: bash

  {
    title: string,
    created_at: datetime,
    updated_at: datetime
  }


GetNodeDocumentAttrs
----------------------

.. code-block:: bash

  {
    title: string,
    lang: string,
    ocr: boolean,
    ocr_status: "succeeded" | "failed" | "received" | "started",
    file_name: string,
    size: integer,
    page_count: integer,
    created_at: "2022-01-11T07:40:23.278375Z",
    updated_at: "2022-01-11T07:40:28.979284Z"
  }


PostNodeFolderAttrs
--------------------

.. code-block:: bash

  {
    title: string,
  }


PostNodeDocumentAttrs
----------------------

.. code-block:: bash

  {
    title: string,
    lang: string
  }
.. _api_nodes:

Nodes
======

.. warning::

  REST API described here is work in progress. It changes
  along with the development of `Papermerge Core <https://github.com/papermerge/papermerge-core>`_ in master branch.

Documents can be organized in folders. One folder can contain documents as
well as other folders. A *node* is a convinient abstraction of two concepts - folder
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

.. _api_post_nodes:

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

  In order to create a **new folder you need to know
  its parent's ID** (i.e where to place newly created
  folder). Each user has two special, top level folders - ".inbox" and ".home". Special folder'
  IDs are retrieved using :ref:`api_get_users_me` endpoint.
  Once you know user's ".home" folder ID, creating a folder under user's ".home" is straightforward:

  .. sourcecode:: http

    POST /nodes/ HTTP/1.1
    Host: example.com
    Content-Type: application/vnd.api+json

    {
      "data": {
        "type":"folders",
        "attributes": {
            "title": "My Folder"
        },
        "relationships": {
          "parent": {
            "data": {
              "type": "folders",
              "id":"2"
            }
          }
        }
      }
    }


  Uploading documents is two steps process:

  1. Create an empty document (similar to creating a folder)
  2. Upload actual file.

  First step does not differ much from creating a folder:

  .. sourcecode:: http

    POST /nodes/ HTTP/1.1
    Host: example.com
    Content-Type: application/vnd.api+json

    {
      "data": {
        "type":"documents",
        "attributes": {
            "title": "invoice.pdf",
            "lang": "deu"
        },
        "relationships": {
          "parent": {
            "data": {
              "type": "folders",
              "id":"2"
            }
          }
        }
      }
    }

  With example above, an empty document structure will be created. At this step you need to specify only document's ``lang`` attribute (i.e. in what language is the document) and its ``title`` attribute.
  Similarly to creating a folder, you need to specify its parent folder ID. Use  :ref:`api_get_users_me` endpoint to learn ID of user's ".home" folder.

  .. note::

    Each document in Papermerge can have multiple versions associated.
    When creating document model as described above (step 1), besides
    document model, also the first version of the document will be created. No associated files so far though.

  At this point, only document's structure (a node) was created. The actual file was not uploaded yet.
  In order to upload a file, use :ref:`api_put_documents_upload`

.. _api_get_nodes_download:

GET  /nodes/download/
-----------------------


.. http:GET:: /nodes/download/

  Downloads one or multiple nodes i.e. single or multiple folders
  and/or documents. If only one node ID is provided and that
  node is a document, then specified document won't be downloaded as part of
  archive (in such case request's `Content-Type` header will be ignored).


  :query node_ids*: one or multiple nodes to download
  :query file_name: name for the downloaded file
  :query include_version: ``only_last`` | ``only_original``
  :query archive_type: ``zip`` | ``targz``
  :reqheader Authorization: Token <token>
  :reqheader Content-Type: not applicable
  :status 200: on success

  ``node_ids`` is the only mandatory parameter. When omitted will result
  in "400 Bad Request" response.

  ``include_version`` defaults to ``only_last`` which means that  downloaded
  file (or archive) will contain only last version of the document. With
  ``only_original`` value - downloaded file (or archive) will contain only
  original version of the document

  ``archive_type`` default value is ``zip``. This parameters determines type
  of archive requested. When ``zip`` - downloaded content will be bundled
  into a zip archive. When ``targz`` - downloaded content will be bundled
  into a gzipped tarball. Note that ``archive_type`` parameter is **not
  applicable** when user requests download of a single document i.e. there is
  a single node requested and that node is actually a document.


  **Example Reqest**

  .. sourcecode:: http

    GET /nodes/download/?node_ids=115&node_ids=210&file_name=archive.zip HTTP/1.1

  Use curl to download two nodes (a folder and a document):

  .. code-block:: bash

    curl \
      -H 'Authorization: Token 63cbf9840' \
      'http://example.io/api/nodes/download/?node_ids=210&node_ids=115' \
      --output archive.zip

  Use curl to download single document node's last version:

  .. code-block:: bash

    curl \
      -H 'Authorization: Token 63cbf9840' \
      'http://example.io/api/nodes/download/?node_ids=115' \
      --output invoice_115_latest.pdf

  Use curl to download single document node's original version:

  .. code-block:: bash

      curl \
      -H 'Authorization: Token 63cbf9840' \
      'http://example.io/api/nodes/download/?node_ids=115&include_version=only_original' \
      --output invoice_115_original.pdf


.. _api_get_nodes_inboxcount:

GET  /nodes/inboxcount/
-----------------------


.. http:GET:: /nodes/inboxcount/

  Returns number of items in user's inbox folder

  :reqheader Authorization: Token <token>
  :reqheader Content-Type: ``application/vnd.api+json``
  :status 200: on success


  **200 - Response Body Schema**

  .. code-block:: bash

    {
      data: {
        count: number
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
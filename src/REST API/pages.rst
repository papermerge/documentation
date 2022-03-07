.. _api_pages:

Pages
======

.. warning::

  REST API described here is work in progress. It changes
  along with the development of `Papermerge Core <https://github.com/papermerge/papermerge-core>`_ in master branch.

.. _api_get_pages_id:

GET  /pages/{id}/
-------------------

.. http:GET:: /nodes/{id}/

  Retrieves page resource.

  :reqheader Content-Type: ``image/svg+xml`` | ``image/jpeg`` | ``text/plain`` | ``application/vnd.api+json``
  :reqheader Authorization: Token <token>
  :status 200: on success

  Depending on ``Accept`` of the request header - response's body can be:

    1. an image in svg format (for ``image/svg+xml``)
    2. an image in jpeg format (for ``image/jpeg``)
    3. plain text i.e extracted (with OCR) page's text (for ``text/plain``)
    4. json formated page details (for ``application/vnd.api+json``)

  .. note:: Returned SVG image embedds extracted JPEG image and the layer of OCRed text mapped over (so called text overlay)

  .. note:: When ``text/plain`` response has empty body, it means that page was not OCRed yet

  **200 - Response Body Schema**

  When client supplied ``Accept`` header with ``application/vnd.api+json`` value, server's response body
  will contain following schema:

  .. code-block:: bash

    {
      data: {
        type: "pages",
        id: string,
        attributes: {
          number: number,
          text: string,
          lang: string
        },
        relationships: {
          document_version: {
            data: {
              type: "DocumentVersion",
              id: string
            }
          }
        }
      }
    }

.. _api_delete_pages_id:

DELETE  /pages/{id}/
---------------------

.. http:DELETE:: /pages/{id}/

  Deletes the page with specified ID

  :reqheader Authorization: Token <token>
  :status 204: on successful folder deletion
  :status 404: when page with given ID does not exists


.. _api_delete_pages:

DELETE  /pages/
---------------------

.. http:DELETE:: /pages/

  Deletes one or multiple pages. Pages are specified by their IDs.

  :reqheader Content-Type: ``application/json``
  :reqheader Authorization: Token <token>
  :status 204: on successful folder deletion
  :status 404: when page with given ID does not exists


  **200 - Request Body Schema**

  .. code-block:: bash

    {
      pages: [ page_id1, page_id2, ... ]
    }


  .. note:: All specified pages must belong to same document version.

  Example:

  .. code-block:: bash

    curl -H "Authorization: Token <token>"  \
      -H 'Content-Type: application/json' \
      -XDELETE \
      -d '{"pages": [350, 348]}' \
      <server-url>/pages/


.. _api_delete_pages:

POST  /pages/reorder/
---------------------

.. http:POST:: /pages/reorder/

  Reorders pages.

  :reqheader Content-Type: ``application/json``
  :reqheader Authorization: Token <token>
  :status 204: on successful page reorder
  :status 404: when page with given ID does not exists


  **204 - Request Body Schema**

  .. code-block:: bash

    {
      pages: [
        {id: page_id1, old_number: integer, new_number: integer},
        {id: page_id2, old_number: integer, new_number: integer},
        {id: page_id3, old_number: integer, new_number: integer},
        ...
      ]
    }


  .. note:: All specified pages must belong to same document version.

  Each object in the list has following fields::

    - id: ID of the page whose order will change
    - old_number: previous page number i.e. page order within document version
    - new_number: new page number i.e. page order within document version

  In example below first page is swapped with fourth page. Notice that both
  pages should below to the same document version. Document version is not
  specified though, because document version will be inferred from page
  model.

  .. code-block:: bash

    curl -H "Authorization: Token <token>"  \
        -H 'Content-Type: application/json' \
        -XPOST \
        -d '{"pages": [{"id": 389, "old_number": 1, "new_number": 4}, {"id": 392, "old_number": 4, "new_number": 1}]}' \
        <server-url>/pages/reorder/


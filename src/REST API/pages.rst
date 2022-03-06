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

  :reqheader Accept: ``image/svg+xml`` | ``image/jpeg`` | ``text/plain`` | ``application/vnd.api+json``
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

  When ``Accept`` header is ``application/vnd.api+json``, response body
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

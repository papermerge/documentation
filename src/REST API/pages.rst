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

  :reqheader Content-Type: image/svg+xml | image/jpeg | text/plain | application/vnd.api+json
  :reqheader Authorization: Token <token>
  :status 200: on success

  .. note:: Depending on ``Content-Type`` of the request header  - response's body can be:

     1. an image in svg format (image/svg+xml)
     2. an image in jpeg format (image/jpeg)
     3. plain text i.e extracted (with OCR) page's text (text/plain)
     4. json formated page details (application/vnd.api+json)


.. _api_delete_pages_id:

DELETE  /pages/{id}/
---------------------

.. http:DELETE:: /pages/{id}/

  Deletes the page with specified ID

  :reqheader Authorization: Token <token>
  :status 204: on successful folder deletion
  :status 404: when page with given ID does not exists

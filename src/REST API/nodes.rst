.. _api_nodes:

Nodes
======

.. warning::

  REST API described here is work in progress. It changes
  along with the development of `Papermerge Core <https://github.com/papermerge/papermerge-core>`_ in master branch.

Documents can be organized in folders. One folder can contain documents as
well as other folders. A *node* is an abstraction of two concepts - folder
and document, which means that a node is either a document or a folder.

Just keep in mind that node may refer to either of two - folder or document.

.. _api_get_nodes:

GET /nodes/
------------

.. http:GET:: /nodes/

  Retrieves all top level nodes which user has access to


.. _api_get_nodes_id:


POST /nodes/
--------------

.. http:POST:: /nodes/

  Creates a node (in this case only folders).

GET  /nodes/{id}/
-------------------

.. note::

  Difference between this endpoint and /folders/{id}/ endpoint is that **/folders/{id}/ will retrieve only folder instances**.

.. http:GET:: /users/{id}/

  Retrieves the list of **documents and folders** of the given node. In this context node should be a folder as
  it does not make sense to "retrieve the list of documents and folders of a document".


POST /nodes/move/
-------------------

.. http:POST:: /nodes/move/

  Moves one or multiple nodes from one location to another.
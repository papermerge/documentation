Upload Documents
================

There are different ways to upload documents to |project|: via web
user interface, like upload button, drag'n drop, or via command line
utilities like papermerge-cli. All methods have one thing in common: they use
REST API to perfrom the actual upload. In this sense all applications which
upload documents, even web user interface's described in this manual,
act as REST API clients:


.. figure:: ./upload_documents/rest-api-clients.svg


.. note:: REST API Server is web application. As any web application it is
   accessible with an url prefixed with http or https scheme e.g.
   https://my-example-dms.com, https://my-papermerge.local, http://localhost:8000/


.. note:: A fancy English word for "uploading" is *ingesting* i.e. "ingest
   documents to |project|" is same as "upload documents to |project|".


All documents are organized in folders. Each user has two special folders -
`Inbox` and `Home`. `Inbox` and `Home` folders are special in sense that they
are always there they cannot be renamed or deleted. Actually, whenever a new
user is added into the |project| the two special folders `Inbox` and `Home`
are automatically created for him/her.

.. note:: Internally the two special folders are named ``.home`` and ``.inbox`` -
    title starts with a dot and has only lowercase characters.



Upload Button
--------------

Uploading documents via user interface is the most straightforward method, just click
"upload" button:

.. figure:: ./user_interface/upload-documents.svg

Note that documents will be uploaded into your current folder. Current folder is
considered the one which you currently see as opened in web UI - that may be
Inbox folder, Home folder or any arbitrarily deeply nested folder inside Home
or Inbox.

.. figure:: ./upload_documents/deeply-nested-inside-home.svg

    Uploading documents into deeply nested folder inside Home


Drag'n Drop
-----------


Command Line
------------



REST API
--------

|project| exposes a well defined HTTP interface with HTTP body (payload) being in
json format. This means that you can use any http client (e.g. `curl`_) to interact with
|project| e.g. upload documents, create folders, assign tags, move documents to specific
folder, trigger OCR.

For detailed REST API overview see :ref:`REST API <rest_api>`.
For detailed reference see :ref:`REST API Reference <rest_api_reference>`.  

In particular :ref:`rest_api_overview_nodes_folders_documents`
section explains how to use REST API to upload documents (also it goes into details of all necessary concepts like nodes, special folders etc).

.. _papermerge.js: https://github.com/papermerge/papermerge.js
.. _curl: https://en.wikipedia.org/wiki/CURL

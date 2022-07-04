.. _rest_api:

Overview
=========

In order to use REST API interface you need an http client. The most
wide-spread http client is `curl`_.

In following sections `curl`_ will be used if all examples.

Server URL
----------

Throughout this REST API documentation you will notice reference to
``<server-url>`` - this is base http address of your |project|
instance. Base url/address is where your instance was deployed.
Depending where your |project| instance was deployed you may use
``https`` instead of ``http`` and use correct port number.

Examples of ``<server-url>``:

* http://localhost:8000/
* https://example.com/
* https://my-app.papermerge.io/

Let's take an example for authentication REST API. If your ``<server-url>``
is https://example-app.papermerge.io/ then, in order to authenticate and get a token you'll need to run
following curl command::

  curl -XPOST https://example-app.papermerge.io/api/auth/login/ \
  -H 'Content-Type: application/json' \
  -d '{"username":"john","password":"password"}'

Another example, this time with users endpoint::

   curl https://example-app.papermerge.io/api/users/ \
    -H 'Content-Type: application/vnd.api+json'
    -H 'Authorization: Token ababfa840abb6b8aa3a185e631c19095c70de932'

.. note:: When quering **for json data types always pay attention to
   Content-Type header**. For json data it sometimes may be either
   ``application/json`` or ``application/vnd.api+json``. Each REST API call
   reference documents correct value of ``Content-Type`` header.

.. _rest_api_overview_authentication:


Authentication
--------------

Papermerge REST API backend uses **token based** authentication, this means
that you will need to send your credentials to the backend API server and if
credentials are correct, then server's response will contain a valid token in
response's body. For all subsequent requests, which require authorization,
you will need to append ``Authorization`` header with ``Token <token>``
value.

.. tip::

  After you've retrieved token for your account, **all subsequent requests** need to
  include ``Authorization: Token <token>`` header.


For authentication use authentication endpoint.
Example:

.. code-block:: bash

  curl -X POST \
    <server-url>/api/auth/login/ \
    -H 'Content-Type: application/json' \
    -d '{"username":"john","password":"<password here>"}'

When credentials are correct, response will have status 200 OK,
``content-type`` will be ``application/json`` and response will have
following body:

.. code-block:: bash

  {
    "token": <your token here>,
    "expiry": null
  }

With authentication token at hand, you can perform any REST API, for
example:

.. code-block:: bash

  curl https://example.com/api/users/me/ \
    -H 'Content-Type: application/vnd.api+json'
    -H 'Authorization: Token ababfa840abb6b8aa3a185e631c19095c70de932'

.. note:: When quering for json data types always pay attention to
   ``Content-Type``. For json data it sometimes may be either
   ``application/json`` or ``application/vnd.api+json``. Each REST API call
   reference documents correct value of ``Content-Type`` header.


Nodes, Folders and Documents
----------------------------

This section explains by example how to use nodes, folders and documents
endpoints because they feature some peculiarities.

In |project| one folder can contain other folders and documents. It is de
factor standard nowadays for a typical `file manager`_ to organize files and
folders in hierarchical structure (i.e folder can contains other folders and
files). In this regard |project| behaves like a common `file manager`_.


Our goal of this short tutorial like section is to create, with help of REST API,
following structure of folders and documents:

.. figure:: img/example.svg 


In illustration above folder *My Documents* contains two folders and two
documents:

* Fruits (folder)
* Vegetables (folder)
* mydoc_1.pdf
* mydoc_2.pdf

Folder Fruits contains two documents: apples.pdf and lemons.pdf.
Folder Vegetables contains just one document titled broccoli.pdf.


Let's first create folder "My Documents".

Each folder belongs to a specific user and has one parent folder - which means
that in order to create folder "My Documents" we need to know parent folder
id (user id is deduced from the token). Notice that folder "My Documents",
which we are about to create, looks like it will be top level folder - which
may lead you to wrong conclusion that "My Documents" folder does not need
parent id.

.. important:: Each and every folder and document you create in
   |project| **requires** non empty folder parent id field.


Special Folders
~~~~~~~~~~~~~~~

Every user in |project| has two special folders:

- ``.home``
- ``.inbox``

These folders are special because they are created during user's account
creation and are always there as long user's account exists. You cannot
delete ``.home``, ``.inbox`` folders and you cannot alter their title
(which starts with dot character). Folder "My Documents" must be direct
child of either ``.home`` or ``.inbox`` folder.


.. note:: You can create "My Documents" folder directly in user's ``.inbox``. However
  ``.inbox`` folder is intended for received document (e.g. via email attachments)


In order to get user's ``.home`` folder id use ``api/users/me/`` endpoint::


  curl <server-url>/api/users/me/ \
    -H 'Authorization: Token beb...'

Example of response::

  {
    "data": {
      "type": "users",
      "id": "169d8",
      "attributes": {
        "username": "admin",
        ...
      },
      "relationships": {
        "inbox_folder": {
          "data": {
            "type": "folders",
            "id": "8d6ee1"
          }
        },
        "home_folder": {
          "data": {
            "type": "folders",
            "id": "18381e"  // <-- .home folder id
          }
        },
      }
    }
  }

In response above home folder id is "18381e".
folder id is actually an `uuid`_ number, however for sake of simplicity,
we abbreviate it and remove all irrelevant fields.

.. important:: For creating folder and documents you always need parent folder
   id. User has two special folders: ``.inbox`` and ``.home`` and all other
   documents and folders are under one of these two folders. In order to
   get special folder's ids use ``api/users/me/`` REST API endpoint


Create Folder
~~~~~~~~~~~~~

Now, once we have folder's parent id, we can create "My Documents" folder::


  curl -XPOST <server-url>/api/folders/ \
    -H 'Authorization: Token beb...' \
    -H 'Content-Type: application/vnd.api+json' \
    -d '{
      "data": {
        "type": "folders",
        "attributes": {
          "title": "My Documents"
        },
        "relationships": {
          "parent": {
            "data": {
                "type": "folders",
                "id": "18381e"  // <- .home folder id
            }
          }
        }
      }
    }'

Similarly you can create folder with help of ``POST /api/nodes/`` endpoint::


  curl -XPOST <server-url>/api/nodes/ \
    -H 'Authorization: Token beb...' \
    -H 'Content-Type: application/vnd.api+json' \
    -d '{
      "data": {
        "type": "folders",
        "attributes": {
          "title": "My Documents"
        },
        "relationships": {
          "parent": {
            "data": {
                "type": "folders",
                "id": "18381e"  // <- .home folder id
            }
          }
        }
      }
    }'


We can create as many folders with same title as we want.
|project| does not impose folder title uniqueness.

Also it is important to note that when creating folder,
``Content-Type: application/vnd.api+json``
header must be used. If you forget to include ``application/vnd.api+json``
value for content-type you will get "400 Bad Request" response from REST API
server.

.. important:: When content-type  is ``application/vnd.api+json``, always
  wrap all fields inside "data" field::

    {
      "data": {...}
    }

.. note:: Even though you can use both endpoints i.e. ``POST /api/nodes/``
  and ``POST /api/folders/`` for creating folders, we recommend
  to use ``POST /api/nodes``. The point is, as you will see later,
  it make creating of folder and document consistent.


View Folder's Content
~~~~~~~~~~~~~~~~~~~~~

Once we've created folder "My Documents" under user's ``.home``, we want to
see what's inside ``.home`` folder, this way we can confirm that indeed
folder "My Documents" was created and it is direct descendant of ``.home``
folder.

Correct endpoint for listing the content of specific folder is ``GET /api/nodes/{folder-id}/``.
For our case, we want to list user's ``.home``::

   curl <server-url>/api/nodes/18381e/ \
    -H 'Authorization: Token beb...'

And response json body will look something like::

  {
    "links": {
      ...
    },
    "data": [
      {
        "type": "folders",
        "id": "949baf",
        "attributes": {
          "title": "My Documents",
          ...
        },
        "relationships": {
          "parent": {
            "data": {
              "type": "folders",
              "id": "18381e"
            }
          }
        }
      },
      ...
    ],
    "meta": {
      "pagination": {
        ...
      }
    }
  }

Node - is an abstraction of both folder and document, thus
when we use ``GET /api/nodes/{node-id}/`` REST API endpoint we
basically request to list all **documents and folders** under specific node-id.

To be exact the correct signature of the endpoint is ``GET /api/nodes/
{folder-id}/``, because it does not make any sense to list "folders and
documents under a document".

There two other endpoints which you may think of as a way to list all
folder's content:

- ``GET /api/folders/``
- ``GET /api/folders/{folder-id}/``


First one, ``GET /api/folders/``, indeed will return all folders of specific
user. However, it will return **only folders** and all folders will be listed
as flat structure. In our case this means that folder "My Documents", ``.home``,
``.inbox`` will be in the same flat list.

Second one, ``GET /api/folders/{folder-id}/``, will return folder's properties
details i.e. id, title, tags, created_at etc

.. important:: Correct endpoint for listing the content of specific folder is
   ``GET /api/nodes/{folder-id}/``


Create Document
~~~~~~~~~~~~~~~

At this point, creating "Fruits" and "Vegetables" folders should be
straightforward and we leave it as exercise.

Creating documents, on the other hand, needs clarification.
First of all, from user point of view - documents are "uploaded", not "created".
But from REST API point of view, uploading a document is performed in two steps:

1. create document entry
2. upload associated file

In first step we create document entry::

  curl -XPOST <server-url>/api/nodes/ \
    -H 'Authorization: Token beb...' \
    -H 'Content-Type: application/vnd.api+json' \
    -d '{
      "data": {
        "type": "documents",
        "attributes": {
          "title": "mydoc_1.pdf"
        },
        "relationships": {
          "parent": {
            "data": {
                "type": "folders",
                "id": "18381e1"
            }
          }
        }
      }
    }'

Creating document entry in this way is very similar to creating a
folder. The difference is that for documents you specify type "documents".

At this point, if you list all documents and folders under "My Document", you will
see folders "Vegetables", "Fruits" and document "mydoc_1.pdf".
However, document "mydoc_1.pdf" does not have a file associated yet, in other words,
we still need to upload file and associated it with "mydoc_1.pdf" document.

This is second step. In order to perform second step we need to have a file and we need
to know the id of the document entry we've just created. Document id can be retrieved
either from response of ``POST /api/nodes/`` endpoint, or by listing all children nodes
of "My Documents" folder with ``GET /api/nodes/{my-documentsn-node-id}/``.

Here is curl command to upload pdf file and associate it with given document id::

  curl -H 'Authorization: Token beb...' \
       -H 'Content-Disposition: attachment; filename=mydoc_1.pdf' \
       -H 'Content-Type: application/pdf' \
       -T /path/to/my_doc_1.pdf \
       http://<server-url>/api/documents/{document-id}/upload/mydoc_1.pdf


``-T`` parameter in ``curl`` implies usage of ``PUT``.
Also, notice that ``Content-Disposition: attachment; filename=<file-name>`` is mandatory header.


Summary
~~~~~~~

* Retrieve special folder ids with ``GET /api/users/me/`` endpoint
* Creating a node (document or folder) requires non-empty parent id
* Create a folder with ``POST /api/nodes/`` endpoint (type "folders")
* List content of the folder with ``GET /api/nodes/`` endpoint
* Uploading document is two steps process:

  1. create document entry with ``POST /api/nodes/`` (type "documents")
  2. upload file to document node created in first step using ``PUT /api/documents/{document-id}/upload/file-name``


.. _curl: https://en.wikipedia.org/wiki/CURL
.. _file manager: https://en.wikipedia.org/wiki/File_manager
.. _uuid: https://en.wikipedia.org/wiki/Universally_unique_identifier
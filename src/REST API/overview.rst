.. _rest_api:

Overview
=========

In order to use REST API interface you need an http client. The most
wide-spread http client is `curl`_.

In following sections `curl`_ will be used to illustrate examples of usages.

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
endpoints as these endpoints feature some peculiarities.

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
that in order to create folder "My Documents" we need to know the user id and
parent folder id. Notice that folder "My Documents", which we are about to
create, looks like it will be top level folder - which may lead you
to wrong conclusion that "My Documents" folder does not need parent id.

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
(which starts with dot character). Folder "My Documents" can be direct
child of either ``.home`` or ``.inbox`` folder.


.. note:: yes, you can create "My Documents" folder directly in user's ``.inbox``. However
  ``.inbox`` folder is intended for received document (e.g. via email attachments)


In order to get user id and user's ``.home`` folder id use ``api/users/me/`` endpoint::


  curl <server-url>/api/users/me/ \
    -H 'Authorization: Token beb...'

Example of response::

  {
    "data": {
      "type": "users",
      "id": "169d8",  // <-- user id
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

In response above user id is "169d8" and home folder id is "18381e". Actually
both user and folder ids are `uuid`_ numbers. For sake of simplicity in
examples used here we abbreviate ids and remove all irrelevant fields.

.. important:: For creating folder and documents you always need user
   (the owner) id and parent folder id. User has two special folders: ``.inbox`` and
   ``.home``. In order to get user id and special folder's ids use
   ``api/users/me/`` REST API endpoint


.. _curl: https://en.wikipedia.org/wiki/CURL
.. _file manager: https://en.wikipedia.org/wiki/File_manager
.. _uuid: https://en.wikipedia.org/wiki/Universally_unique_identifier
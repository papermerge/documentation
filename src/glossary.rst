Glossary
========

Here is a list of terms, expressions and abbreviations used in this
documentation. Many of terms here are specific for document management problem
domain.

.. _dms:

DMS
~~~

DMS = Document Management System

.. _digital_archive:


Digital Archive
~~~~~~~~~~~~~~~

Digital archive is a fancy name for a document whose content won't change
anymore. Think of PDF documents - you can't modifgy content of PDF file
unless you have specialized software. PDF documents are a good example of
digital archives. Any scanned document is automatically a digital archive as
well.

.. note::

  Throughout Papermerge documentation terms **document**, **scanned document**, **pdf document**, **digital archive** are used interchangeble and mean the same thing.


.. _glossary_gui:

GUI
~~~

Abbreviation from graphical user interface.


.. _ocr:

OCR
~~~

Abbreviation from **optical character recognition**. OCR is the process of
extracting plain text (and associated information) from file, document or image.

Example: John takes a photo with his mobile phone of a paper based
bank statement. Let's say IBAN number appears on that document. From resulted
photo - filename *bank-statement.jpeg* - John won't be able to copy IBAN
number and paste it over whatsapp to his wife.

On the other hand, if the same bank statement photo is processed using optical
character recognition technology (OCR) - the text is extracted from the photo
(for example as bank-statement.txt file) and John can open bank-statement.txt
file, select IBAN number and copy/paste it in whatsapp chat to his wife.

OCR technology has widespread usage across many areas. It **enables computers
to understand pictures**. If computers understand what text is inside images,
then users can search for specific terms across photos.

Scanned document is a just photo of the document - usually of higher quality
than photos taken with mobile phones for example. Described with informal
terms scanners are specialized devices for taking photos of the documents.


.. _strayed_page:

Strayed Page
~~~~~~~~~~~~

A page that during the scan ended up in wrong document is called *strayed page*.

For example, let's say you scanned two contracts A and B and each contract is
four pages long. Scanned document-A.pdf ended up having five pages and scanned
document-B.pdf - three pages:

- document-A.pdf: A1, A2, B2, A3, A4
- document-B.pdf: B1, B3, B4

Page B2 (page from contract B) obviously does not belong to document A. Page B2 belongs to document B.
In such case we say that page B2 is strayed page.


.. _incoming_documents:

Incoming Documents
~~~~~~~~~~~~~~~~~~

Documents which are in user's ``Inbox`` folder are called *Incoming Documents*.

.. _ingesting_documents:

Ingesting Documents
~~~~~~~~~~~~~~~~~~~

Same as saying uploading documents i.e. take documents from any external
source (e.g. S3 objects, storage, email account, local file system) and
tranfer them into |project|. All successfully ingested documets appear in
``Inbox`` folder of the user - the user whom documents were assigned to.

.. _glossary_metacolumn:

Metacolumn
~~~~~~~~~~~

Metacolumns are the columns displayed for metadata defined on current folder.

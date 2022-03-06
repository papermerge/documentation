Documentation
==============

Papermerge is a open source document management system designed to work with **scanned
documents**. It extracts text from your scans (which might be
PDF, TIFF, JPEG or PNG), indexes it, and prepares it for full text search.
Papermerge provides the look and feel of modern desktop file browsers. It has
features like tags, hierarchical folders and automations so
that you can efficiently organize your documents.

.. figure:: img/document-management-system-screenshot.png

   Papermerge screenshot

What It Does
~~~~~~~~~~~~~

* It extract and indexes text from your documents
* Provides nice user interface to easly find your documents
* Augments your documents with tags and :doc:`User's Manual/metadata`
* Helps you instantly find your documents:
    * based on extracted text
    * based on :doc:`User's Manual/metadata`
    * based on :doc:`/User's Manual/tags_and_folders`
* Helps you fix scanned documents issues


What It Doesn't Do
~~~~~~~~~~~~~~~~~~~~

* It does **not** take control of your documents. Documents are **stored on filesystem** in a simple and intuitive manner so that you can take snapshot of your data at any time
* It does **not** stay in your way when you make decisions about your data
* It does **not** overwrite your original documents


Right Tool for You?
~~~~~~~~~~~~~~~~~~~~~~

To be efficient you always need to choose right tool for the problem. Because
Document Management is too generic - I think that a definition of what is a
Document in context of this software is needed.

.. _what_is_a_doc:

What is a Document?
~~~~~~~~~~~~~~~~~~~~

For Papermerge a document is anything which is a good candidate for archiving
- some piece of information which is not editable but you need to store it for
future reference. For example **receipts** are perfect examples - you don't
need to read receipts everyday, but eventually you will need them for your tax
declaration. In this sense - **scanned documents**, which are usually in PDF
or `TIFF <https://en.wikipedia.org/wiki/TIFF>`_ format, are perfect match.

**PDF (Portable Document Format)** is de facto standard for storing archived documents. In correct technical terms - it is `PDF/A
<https://en.wikipedia.org/wiki/PDF/A>`_ subset. PDF/A differs from PDF by prohibiting features unsuitable for long-term archiving, such as font linking and encryption.

Most of the modern office scanners will output scanned files in PDF/A format.
This is why, PDF is practically synonymous for document in context of
Papermerge.

A picture made with your phone of a A4 paper document is ragarded by papermege
as full fledged document, even though digitally it is stored as jpeg or png
format. You can think of a picture made with a phone (of a document) as a bad
quality scan.

What is Not a Document?
~~~~~~~~~~~~~~~~~~~~~~~~

Out of scope are Office documents (ODT, DOCX, spreadsheets, presentations
etc), text files (notes); these files are usually editable i.e. user can alter
the content of the document. Any format of alterable type of document is out of scope
for Papermerge project.


Papermerge is simply **not designed to store books**. Yes, you can scan a book
and import it in Papermege, but again - this is not what Papermerge was
designed for.


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Installation/index.rst
   User's Manual/index.rst
   REST API/index.rst
   roadmap.rst

Documentation
==============

Papermerge is a document management system designed to work with scanned
documents. As well as it extracts text from scanned documents (which can be PDF, TIFF, JPEG or PNG) indexes it and makes it ready for full text search. Papermerge provides the look and feel
of major modern file browsers, with tags and hierarchical structure for files
and folders, so that you can efficiently organize your documents.

What It Does
~~~~~~~~~~~~~

* It extract and indexes text from your documents
* Provides you nice user interface to easly browse your documents
* Augments your documents with :doc:`metadata <metadata>`
* Helps you instantly find your documents:
    * based on extracted text
    * based on :doc:`metadata <metadata>`
    * based on :doc:`tags <tags>`

* Helps you fix scanned documents issues


What It Doesn't Do
~~~~~~~~~~~~~~~~~~~~
 
* It does **not** take control of your documents. Documents are **stored on filesystem** in a simple and intuitive manner so that you can take snapshot of your data at any time.
* It does **not** stay in your way when you make decisions about your data. 


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

What is Not a Document?
~~~~~~~~~~~~~~~~~~~~~~~~

Out of scope (at least for near future) are Office documents (ODT, DOCX,
spreadsheets, presentations etc), text files (notes); these files are usually
editable. In the future, Papermerge **might support Office documents** (ODT
etc). In such case support for office documents will be provided as external
plugins/Addon.

Papermerge is simply **not designed to store books**. Yes, you can scan a book
and import it in Papermege, but again - this is not what Papermerge was
designed for.



.. toctree::
   :maxdepth: 2
   :caption: Contents:

   Installation/index.rst
   Help/index.rst
   User's Manual/index.rst
   Contributing/index.rst

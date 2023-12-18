
# Papermerge DMS

Papermerge DMS or simply Papermerge is a open source document management
system designed to work with scanned documents (also called digital
archives). It extracts text from your scans using OCR, indexes them, and
prepares them for full text search. Papermerge provides look and feel of
modern desktop file browsers. It has features like dual panel document
browser, drag and drop, tags, hierarchical folders and full text search so
that you can efficiently store and organize your documents.

It supports PDF, TIFF, JPEG and PNG document file formats. Papermerge is
perfect tool for long term storage of your documents.

![Papermerge screenshot](img/papermerge3.png)


## Features Highlights

* Works with PDF, TIFF, JPEG, PNG formats
* Desktop like user interface
* Dual panel mode
* OCR - used to extract text for documents indexing
* OCRed text overlay (you can download document with OCRed text overlay)
* Full text search (supports multiple search engines)
* Document Versioning
* Tags - assign colored tags to documents or folders
* Folders - users can organize documents in folders
* Multi-User
* Fully REST API
* Page Management - delete, reorder, rotate, merge, move, extract


## What It Does

* It extracts (using OCR) and indexes text from your documents
* Provides modern, desktop like user interface to easily find your documents
* Helps you instantly find your documents
* Helps you fix scanned documents issues like:
   * delete blank, semi-blank or just irrelevant pages
   * rotate pages
   * move strayed pages between documents
   * change page order within the document


## What It Doesn't Do

* It does **not** take control of your documents. Documents are **stored on
  filesystem** in a simple and intuitive manner so that you can take snapshot of
  your data at any time
* It does **not** overwrite your original documents


## What is a Document?

For Papermerge a document is anything which is a good candidate for archiving
- some piece of information which is not editable but you need to store it for
future reference. For example **receipts** are good examples - you don't
need to read receipts everyday, but eventually you will need them for your tax
declaration. In this sense - **scanned documents**, which are usually in PDF
or [TIFF](https://en.wikipedia.org/wiki/TIFF) format, are perfect match.

**PDF (Portable Document Format)** is de facto standard for storing archived
documents. In correct technical terms - it is [PDF/A](https://en.wikipedia.org/wiki/PDF/A) subset.
PDF/A differs from PDF by prohibiting features unsuitable for long-term archiving, such as font linking
and encryption.

Most of the modern office scanners will output scanned files in PDF/A format.
This is why, PDF is practically synonymous for document in context of
Papermerge.

A picture made with smart phone of A4 paper document is regarded by {{ extra.project }}
as document.

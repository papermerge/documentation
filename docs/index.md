# Papermerge DMS

Papermerge DMS or simply Papermerge is a open source document management system
designed to work with scanned documents, also called digital archives. It
extracts text from your scans (which might be PDF, TIFF, JPEG or PNG), indexes
it, and prepares it for full text search. Papermerge provides the look and feel
of modern desktop file browsers. It has features like dual panel document
browser, drag and drop, tags, hierarchical folders, so that you can efficiently
store and organize your documents.

{{ extra.project }} is perfect tool for long term storage of digital archives.

![Papermerge screenshot](img/document-management-system-screenshot.png)


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
* User permissions management
* Fully REST API (all features can be consumed via REST API)
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


## Right Tool for You?

To be efficient you always need to choose right tool for the problem. Because
Document Management is too generic - I think that a definition of what is a
Document in context of this software is needed.


## What is a Document?


For Papermerge a document is anything which is a good candidate for archiving
- some piece of information which is not editable but you need to store it for
future reference. For example **receipts** are perfect examples - you don't
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

A picture made with your phone of a A4 paper document is regarded by Papermege
as full fledged document, even though digitally it is stored as jpeg or png
format. You can think of a picture made with a phone (of a document) as a bad
quality scan.

## What is Not a Document?

Out of scope are Office documents (ODT, DOCX, spreadsheets, presentations
etc), text files (notes); these files are usually editable i.e. user can alter
the content of the document. Any format of alterable type of document is out of scope
for Papermerge project.


Papermerge is simply **not designed to store books**. Yes, you can scan a book
and import it in Papermerge, but again - this is not what Papermerge was
designed for.

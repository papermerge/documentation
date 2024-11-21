
# Papermerge DMS

Papermerge DMS is open source document management system for digital archives.

It is designed to be user friendly: it has easy to use desktop like web
interface with familiar features like folders or drag 'n drop. In same time,
it has very powerful DMS features: document versioning, custom fields, path
templates, OCR, full text search, users and permissions management.

It supports PDF, TIFF, JPEG and PNG document file formats. {{ extra.project }} is
perfect tool for long term storage of your documents.

![Papermerge screenshot](img/papermerge3.png)


## Features Highlights

* Supports PDF, TIFF, JPEG, PNG file formats
* Desktop like user interface
* Dual panel mode
* Document versioning
* Custom fields
* Document types
* OCR - used to extract text for documents indexing
* OCRed text overlay (you can download document with OCRed text overlay)
* Full text search (supports multiple search engines)
* Tags - assign colored tags to documents or folders
* Folders - users can organize documents in folders
* Multi-User (Users/Groups/Permissions)
* Authorization via granular permissions to limit users' scopes
* SSO - single sign on using standard protocols such as OIDC
* REST API
* Page Management - delete, reorder, rotate, merge, move, extract pages


## What is a Document?

In short: document = PDF.

For {{ extra.project }} a document is anything which is a good candidate for archiving
- some piece of information which is not editable but you need to store it for
future reference. For example **receipts** - you don't
need to read receipts everyday, you don't need to change them, but eventually you will need them for your tax
declaration. **scanned documents**, which are usually in PDF
or TIFF format, are documents in {{extra.project}} sense.

**PDF (Portable Document Format)** is de facto standard for storing archived
documents. In correct technical terms - it is PDF/A subset. PDF/A differs
from PDF by prohibiting features unsuitable for long-term archiving, such
as font linking and encryption.

Most of the modern office scanners will output scanned files in PDF/A format.
This is why, PDF is practically synonymous for document in context of
Papermerge.

A picture made with smartphone of A4 paper document is regarded by {{ extra.project }}
as document.

.. _ocr_operation:

OCR
===

OCR is the process which extracts text information from the scanned document
and makes them searchable.

By default, ocr process is triggered automatically on document file upload.
The OCR process status is indicated by little circle next to document's
title. When OCR process is completed new document version is created and
document becomes searchable.

Automatic OCR
~~~~~~~~~~~~~

By default OCR is triggered automatically when document is uploaded. However,
you can disable automatic OCR triggering, in such case you can start OCR only
when you consider necessary.

.. important:: Documents for which OCR was skipped - are not searchable!

In order to disable automatic OCR, go to preferences -> OCR -> disable
OCR.

Default OCR Language
~~~~~~~~~~~~~~~~~~~~

In order to perform OCR on the document you need to indicate be forehands the
language of respective document. Choosing ocr language for each and every
document uploaded is tedious - instead, in preferences a default OCR Language
is set - and that language is applied for each uploaded document.


Status Indicator
~~~~~~~~~~~~~~~~

|project| features real time OCR status indicator - this means that you can
see document's OCR status updates as they happen (i.e. in real time).
The OCR status is displayed by a small circle next to the document's title.
The status indicates has following meanings:

* gray circle - status is unknown
* orange still circle - document was scheduled for OCR
* orange rotating circle - document's OCR process is in progress
* green check - document's OCR process completed successfully and document is now searchable
* red cross - document's OCR process failed.

OCRed Text Layer
~~~~~~~~~~~~~~~~

Once OCR process completed successfully a new document version is created -
version with OCRed text layer. This version is available for download from
the "versions" dropdown in document view.

.. note:: Under the hood |project| uses awesome OCRmyPDF utility to create
   OCRed text layer. Thus, in respect of OCRed text layer, |project| acts
   like a graphical user interface for OCRmyPDF.

.. _ocr_languages:

OCR Languages Support
~~~~~~~~~~~~~~~~~~~~~

|project| uses `Tesseract <https://github.com/tesseract-ocr/tesseract>`_ to
extract text from scanned documents. Tesseract supports over 130 languages -
thus with |project| you can have documents in any of those languages.

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
-------------

By default OCR is triggered automatically when document is uploaded. However,
you can disable automatic OCR triggering, in such case you can start OCR only
when you consider necessary.

.. important:: Documents for which OCR was skipped - are not searchable!

In order to disable automatic OCR, go to User Menu -> Preferences -> OCR -> Trigger -> Manual


Default OCR Language
--------------------

In order to perform OCR on the document you need to indicate beforehand the
language of respective document. Choosing ocr language for each and every
document uploaded is tedious - instead, in preferences a default OCR Language
is set - and that language is applied for each uploaded document.

In order to set default OCR language, go to User Menu -> Preferences -> OCR -> Language


Status Indicator
----------------

|project| features real time OCR status indicator - this means that you can
see document's OCR status updates as they happen (i.e. in real time).
The OCR status is displayed by a small circle next to the document's title.
The status indicates has following meanings:

* gray circle - status is unknown (figure 1)
* orange still circle - document was scheduled for OCR (figure 2)
* orange rotating circle - document's OCR process is in progress (figure 3)
* green check - document's OCR process completed successfully and document is now searchable (figure 4)
* red cross - document's OCR process failed.

.. figure:: ./ocr/unknown.png

   Figure 1. OCR status - unknown

.. figure:: ./ocr/pending.png

   Figure 2. OCR status - pending - document was scheduled for OCR, but process did not start yet

.. figure:: ./ocr/in-progress.png

   Figure 3. OCR status - in progress

.. figure:: ./ocr/complete.png

   Figure 4. OCR status - complete

OCRed Text Layer
----------------

Once OCR process completed successfully a new document version is created -
version with OCRed text layer. This version is available for download from
the ``Download`` dropdown in document view.


.. figure:: ./ocr/download-dropdown.svg


.. note:: Under the hood |project| uses awesome `OCRmyPDF`_ utility to create
   OCRed text layer. Thus, in respect of OCRed text layer, |project| acts
   like a graphical user interface for `OCRmyPDF`_.


Document OCRed Text
-------------------

You can view OCRed text of the entire document either from :ref:`commander` or from :ref:`viewer`,
in both cases choose "OCRed Text" from context menu:

.. figure:: ./ocr/commander-ocred-text-entire-document.svg

   See OCRed text of the document from commander

If you want to see OCRed text of entire document (to be exact - all pages of the last document version) from
the :ref:`viewer` - just make sure that no pages are selected:

.. figure:: ./ocr/viewer-ocred-text-entire-document.svg

   See OCRed text of the document from viewer


Selected Pages OCRed Text
-------------------------

In case document has many pages and you are interested in OCRed text of one
(or multiple) very specific pages, then select pages first and then from
context menu choose "OCRed Text" item:


.. figure:: ./ocr/viewer-ocred-text-selected-page.svg

   See OCRed text ONLY of the selected pages

.. note:: In case there are selected pages, OCRed Text menu item will show you OCRed
   text ONLY of the selected pages.


.. figure:: ./ocr/viewer-ocred-text-one-page-modal.png

   OCRed text modal dialog. Modal dialog shows OCRed text ONLY of the selected page.


.. _ocr_languages:

OCR Languages Support
---------------------

|project| uses `Tesseract`_ to
extract text from scanned documents. Tesseract supports over 130 languages -
thus with |project| you can have documents in any of those languages.


.. _OCRmyPDF: https://ocrmypdf.readthedocs.io/en/latest/
.. _Tesseract: https://github.com/tesseract-ocr/tesseract
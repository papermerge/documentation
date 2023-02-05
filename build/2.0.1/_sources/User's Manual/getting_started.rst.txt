.. _getting_started:

================
Getting Started
================

.. getting_started_documents:

##########
Documents
##########

Let's start by clarifying the most important concept first: the document. For
Papermerge a document is anything which is a good candidate for archiving -
some piece of information which is not editable but you need to store it for
future reference. For example receipts - you don’t need to edit receipts or
read them everyday, but eventually you will need them for your tax
declaration. In this sense - scanned documents, which are usually in PDF or
TIFF format, are perfect match.

Another important thing - if you take a picture of a paper document with your
mobile phone - you'll have a file in jpeg format (or maybe png file format).
In context of Papermerge that picture of a document (though just a single jpeg
file) is a valid one page document. Generally speaking, pictures of the
documents produced by your camera - might be regarded as bad quality scans.

On the other hand, if you take a picture of a flower and upload that jpeg
image to Papermerge - the 'document' will be processed. However, that jpeg
format flower image is not a document in Papermerge sense.

.. figure:: ../img/getting-started/pdf-png-jpeg-documents.png
    :alt: documents created by ingest files of different formats


    Figure 1. Png and jpeg formats along with PDF are natively supported

Usually office formats with .docx (Microsoft Word), .odt (Libre Office), .txt
(plain text) are not good candidates for archiving - as by their nature they
are meant to be changed/edit regularly. However, once converted to PDF format
(for instance Contract_C2.docx to Contract_C2.pdf) they are full fledged
documents in Papermege sense.

By default, Papermerge works with documents in 4 (four) file formats: pdf,
tiff, jpeg and png. However, many other formats (even email messages) can be
imported as documents by converting incoming file *automatically* to PDF
format. This is possible due to :ref:`document_pipelines` feature.

.. getting_started_ocr:

####################################
Optical Character Recognition (OCR)
####################################

OCR is a technique to extract **text** information from **binary image formats**.
This technique enables users to:
    
* **copy/paste  text** from the document's content
* **search documents** by document's actual text content

OCR is essential tool (or technique if you will) which helps basically to
extract textual information and thus derive useful work-flows
(based on document's actual content) with the documents.
Papermerge relies on external open source specialized tools like 
`Google's Tesseract OCR <https://github.com/tesseract-ocr/tesseract>`_

An informal, more detailed, explanation of term OCR is provided in :ref:`glossary <ocr>`.

.. getting_started_tags_and_folder:

###################
Tags and Folders
###################

Organizing documents in folders is very common. Thus the idea of keeping your
documents in folders doesn't need further introduction. It may be worth
mentioning that Papermerge supports folders and that folders may be
hierarchical i.e. one folder can contain other folder(s) as well. This nesting
(folder in folder) ca be arbitrarily deep.

.. figure:: ../img/getting-started/folder-with-tags.png

    Figure 2. Folder with tags on it.

The idea of using tags to organize your documents
may be new for you though. Tags are kind of labels. You can associate
(add) tags to a document or to a folder. Tags have a color and a name. Once
tagged, documents can be searched by their tags. Conversely, is it also
possible to show all the documents tagged with a particular tag(s).

Both tags and folders complement each other and provide you with powerful
means to stay organized. Learn more details about tags :doc:`here
<tags_and_folders>`.

.. getting_started_page_management:

################
Page Management
################

Many times scanning documents in bulk yields documents with blank pages; some
pages my be out of order or maybe part of totally different document. Even if
you notices these flaws immediately it is time consuming and frustrating to
redo scanning process. Papermerge helps you with your scanned documents like
no other tool. With Papermerge you can delete blank or erroneous pages, you
can move pages from one document into another (with cut and paste) and most
importantly you can reorder document pages in case you need to do so.

.. figure:: ../img/getting-started/blank-pages.png
    :alt: blank pages in a document

    Figure 3. Blank pages in a document.

There is a separate chapter about :doc:`page_management` where you can learn
details about this feature.

.. getting_started_metadata:

##########
Metadata
##########

Metadata is a very powerful concept and it marks the clear differences between
an usual file browser and a system dedicated to manage your documents.
Metadata is additional information about your folders, documents and pages. In
other words - data about your data. Following picture is a (scanned document)
receipt with highlighted shop name, price and date on it.

.. figure:: ../img/getting-started/macgeiz-receipt-with-metadata.png

   Figure 4. Receipt document with highlighted metadata.

This additional information - shop name, price and date is so called
document's **metadata**. It has two parts a label (in picture above ``shop``,
``date`` and ``price`` are all labels) and a value (in example above values
are ``Mäc-Geiz``, ``08.06.2020``, ``1.49`` for shop label, date label and
price label respectively). Many times instead of term *label* term *key* is
used.

Metadata is extremely useful as search criteria when you need to locate
specific document among many other very similar documents: for example if you
need to find specific receipt issued by Mäc-Geiz company on May 27th, 2018
among other several thousands Mäc-Geiz receipts.

In Papermerge you can set metadata on folders, on documents and on each
individual page of the document. Document's metadata can be viewed and edited
on the right side in widgets panel. Additionally if you are inside folder with
metadata attributes set, metadata information about each document (of current
parent folder) is displayed in so called metacolumns as highlighted in Figure
5.

.. figure:: ../img/getting-started/metadata-metacolumn-and-widget-panel.png
    :alt: document browser with highlighted metacolumn and highlighted widgets panel

    Figure 5. Different ways to view metadata.

Read more on this topic in chapter dedicated to :doc:`metadata`.
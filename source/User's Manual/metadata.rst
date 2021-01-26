.. _matadata:

Metadata
==========

Main Concepts
~~~~~~~~~~~~~~~

Metadata is extra information about your folders, documents and pages. In
other words - data about your data. Following picture is a (scanned document)
receipt with highlighted shop name, price and date on it.

.. figure:: ../img/user-manual/metadata/01-macgeiz-receipt-with-metadata.png
   :alt: document with metadata

   Figure 1. Receipt with metadata.

This additional information - shop name, price and date is so called document's **metadata**. It has two parts a label (in picture above ``shop``, ``date`` and ``price`` are all labels) and a value (in example above values are ``Mäc-Geiz``, ``08.06.2020``, ``1.49`` for shop label, date label and price label respectively). Many times instead of term *label* term *key* is used.
Metadata is extremely useful when you need to locate specific document among many other very similar documents.

Imagine that you scanned 60 groceries receipts and *organized* them in a
folder named Groceries. If you would just store those receipts on an ordinary
file system, then only way to distinguish between files is by file names or
maybe by their text content (if your storage supports OCR) - finding, specific
file, say all receipts you got in June 2020, would be time consuming.

A more efficient and practical way to tackle this problem is by associating to
all scanned documents (receipts in this example) - metadata. Let's continue
with groceries receipts example. It would be very time consuming to go to each
document and add metadata to each file individually. A faster way to create
metadata and associated it to a group of files, is by a creating a folder -
add metadata to that folder - let's name it Groceries-2020 - and then just
copy all groceries related files into that folder.

.. figure:: ../img/user-manual/metadata/02-inherited-metadata.png
   :alt: document inherits metadata attributes from its parent folder.

   Figure 2. Documents inherit their metadata attributes from parent folder.


.. note::

    Folder is nothing more than a group of related documents. Thus, folders
    are convient way to perform group operations on documents. In particular,
    by assigning metadata attributes to a folder - you automatically create
    those metadata attributes on all documents in the folder.

Metadata and Nested Folders
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nested folder is a folder stored within another folder. Folders can be nested
arbitrarely deep. Metadata inheritance from parent folder to containing
document's makes perfect and it is easy to grasp. 
A trickier situation is with nested folders.

Add, Edit, Delete Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Metadata is added/editing via metadata widget located on the right bar.
Depending on the context - adding or edditing metadata differs slightly: 
while you are browsing files and documents you will be able to edit only
metadata keys. However, in document viewer, you will be able to add or edit
both keys and values for metadata.
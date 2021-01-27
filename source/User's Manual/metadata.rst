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
    are convenient way to perform group operations on documents. In particular,
    by assigning metadata attributes to a folder - you automatically create
    those metadata attributes on all documents in the folder.

Metadata Inheritance and Nested Folders
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nested folder is a folder stored within another folder. Folders can be nested
arbitrarely deep. Same way as documents inherit their metadata attributes from
thier parent folder - child folders inherit their metadata attributes from their
parent folder. Let's consider following example:

.. figure:: ../img/user-manual/metadata/nested-folders-and-metadata.png

    Figure 3. Nested folders and metadata

In Figure 3 folders Groceries, Rent and Insurances are sub-folders of Expenses.
On topmost folder - Expenses - only one metadata label is defined, namely
``amount``. On folder Groceries two extra metadata labels are defined:
``shop`` and ``date``. On folder Rent metadata label ``date`` is defined. On
Insurances: ``company``, ``start date`` and ``end date``.

As explained above, metadata labels are inherited from parent folder to
descendant folders and documents. Because of metadata label inheritance, in
scenario described above, folder Groceries has  in total three metadata label:

1. ``shop`` - its own
2. ``date`` - its own
3. ``amount`` - inherited from parent

Similarly folder Insurances has in total four metadata labels, three of its
own and one inherited (metadata label ``amount``) and folder Rent has in total
two metadata labels: one inherited (metadata label ``amount``) and one of its
own (metadata label ``date``).

All documents from folder Insurances will inherit metadata labels from their
parental folders. Thus, documents ins-1.pdf and ins-2.pdf from Figure 3 have
four metadata labels: ``amount`` inherited from topmost folder Expenses and
``company``, ``start date``, ``end date`` inherited from their direct parental
folder - Insurances.

Metadata inheritance concept is very convenient because you don't need to
define all metadata labels on each individual document, instead you define
metadata only once on the folder containing documents.

Following illustrations show you how folder structure and metadata definition
described in Figure 3 look in practice.

.. figure:: ../img/user-manual/metadata/metadata-defined-on-expenses-folder-v2.png

    Figure 4. Metadata label "amount" defined on "Expenses" folder.

If you open "Expenses" folder and change view to list mode, among Type, Title
and Created At columns you will see an extra column. That extra column is
called :ref:`metacolumn`. Metacolumns are there to display actual metadata values defined
on the documents. At this moment there still no metadata values to display, thus metacolun
is empty.

.. figure:: ../img/user-manual/metadata/metacolumn-amount-v2.png 

    Figure 5. Empty metacolumn corresponding to metadata label "amount" defined on "Expenses" folder.

Add, Edit, Delete Metadata
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Metadata is added/editing via metadata widget located on the right bar.
Depending on the context - adding or editing metadata differs slightly: 
while you are browsing files and documents you will be able to edit only
metadata keys. However, in document viewer, you will be able to add or edit
both keys and values for metadata.
Versions
========

|project| is a non-destructive :ref:`dms <dms>`, which means you always have
available original document regardless how many transformations
(page rotations, deletion, document merges) you apply on the document.

Retention of the original is ensured because of document versioning feature.
With each extra transformation you apply - a new document
version is created.


Version 0 (zero) of the uploaded document - **is the original file** i.e. document
without any changes applied. Original document version is always available,
regardless what operation(s) you apply to the document (except deletion of
the document itself).

Any :ref:`page management <page_management>` or :ref:`OCR operations
<ocr_operation>` on the document will increment (increase by one) its
version.

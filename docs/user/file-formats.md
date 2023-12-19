# File Formats


{{ extra.project }} supports PDF, TIFF, JPEG and PNG file formats.

PDF format is called *native* because {{ extra.project }} interals operate
as if all documents are PDF.

TIFF, JPEG or PNG on the other hand are *not native* (non-native) formats.

The import of native format yields one version document - the PDF itself i.e.
orignal version.

The import of any non-native formats yields two versions document:

- version 1 with non-native file i.e. original file
- version 2 with PDF file into which non-native format was converted


!!! Note

        At its core {{ extra.project }} code is written to work with PDF files only.
        All other files (non-natives) are converted, on import, into PDF format.

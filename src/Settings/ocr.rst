.. _settings__ocr:

OCR
===

This section groups all OCR specific configurations.

.. _settings__ocr__default_language:

``PAPERMERGE__OCR__DEFAULT_LANGUAGE``
-------------------------------------

By default |project| will use language specified with this option to
perform :ref:`OCR <ocr>`. Change this value for language used by majority of your documents. For detailed list of three letter
codes see 639-2/T column from `ISO 639 2`_.

Example as environment variable::

    PAPERMERGE__OCR__DEFAULT_LANGUAGE=spa

Example in toml configuration file::

    [ocr]
    default_language="spa"

Default value is "deu" (German language).

.. _settings__ocr__languages:

``PAPERMERGE__OCR__LANGUAGES``
------------------------------

.. note::
  
  This option may be defined only in toml configuration file

Defines all languages available for OCR. This option is defined as dictionary
(a.k.a. map) where key is `ISO 639 2`_ code and value is human text name for
language.

Example::

    [ocr]
    languages = {
        heb = "hebrew",
        jpn = "japanese"
    }

Note that both `hebrew` and `japanes` language data for tesseract must be
installed. You can check Tesseract's available languages with following
command:

.. code-block:: bash
    :caption: List available languages

    $ tesseract --list-langs

Default value ::

    [ocr]
    languages = {
        deu = "Deutsch",
        eng = "English",
      }


.. _ISO 639 2: https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes
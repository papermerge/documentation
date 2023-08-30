# OCR

This section groups all OCR specific configurations.


## DEFAULT_LANGUAGE


By default {{ extra.project }} will use language specified with this option to
perform OCR. Change this value for language used by majority of your documents. For detailed list of three letter
codes see 639-2/T column from <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes" class="external-link" target="_blank">ISO 639 2</a>.

Example as environment variable:

    PAPERMERGE__OCR__DEFAULT_LANGUAGE=spa

Example in toml configuration file:

    [ocr]
    default_language="spa"

Default value is "deu" (German language).


## LANGUAGES


!!! note

    This option may be defined only in toml configuration file

Defines all languages available for OCR. This option is defined as <a href="https://toml.io/en/v1.0.0#inline-table"  class="external-link" target="_blank">inline table</a>
where key is <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes" class="external-link" target="_blank">ISO 639 2</a> code and value is human text name for language.

Example:

    [ocr]
    languages = { heb = "hebrew", jpn = "japanese"}

Note that both `hebrew` and `japanes` language data for tesseract must be
installed. You can check Tesseract's available languages with following
command:

!!! important

    `languages` value must be written in one line! This is requirement
    of the toml `inline table`_ format.

List all available languages:

    $ tesseract --list-langs

Default value:

    [ocr]
    languages = { deu = "Deutsch", eng = "English" }


See [adding ocr language](../setup/docker.md#adding-ocr-languages-to-the-docker-image) for detailed example of using this option.

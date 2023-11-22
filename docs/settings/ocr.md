# OCR

This section groups all OCR specific configurations.


## OCR__DEFAULT_LANGUAGE


By default {{ extra.project }} will use language specified with this option to
perform OCR. Change this value for language used by majority of your documents. For detailed list of three letter
codes see 639-2/T column from <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes" class="external-link" target="_blank">ISO 639 2</a>.

Example as environment variable:

    PAPERMERGE__OCR__DEFAULT_LANGUAGE=spa

Default value is "deu" (German language).

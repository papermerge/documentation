# OCR

This section groups all OCR specific configurations.


## OCR__DEFAULT_LANG_CODE


By default {{ extra.project }} will use language specified with this option to
perform OCR. Change this value for language used by majority of your documents. For detailed list of three letter
codes see 639-2/T column from <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes" class="external-link" target="_blank">ISO 639 2</a>.

Example as environment variable:

    PAPERMERGE__OCR__DEFAULT_LANG_CODE=spa

Default value is "deu":

    PAPERMERGE__OCR__DEFAULT_LANG_CODE=deu

This options is used only when `PAPERMERGE__OCR__AUTOMATIC=false`.


## OCR__LANG_CODES

List of comma delimited <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes" class="external-link" target="_blank">language codes</a> to be displayed in UI. Note this is just UI configuration. Whatever codes you put here, it is your resposability to make sure that OCR worker does have those languages available.

Examples:

    PAPERMERGE__OCR__LANG_CODES="eng,deu,fra,spa"
    PAPERMERGE__OCR__LANG_CODES="eng, deu"
    PAPERMERGE__OCR__LANG_CODES="ita, fra, ron"


Default value:

    PAPERMERGE__OCR__LANG_CODES="deu,eng,ron"


This options is used only when `PAPERMERGE__OCR__AUTOMATIC=false`.


## OCR__AUTOMATIC

When automatic is set to `true` - it means that OCR processing will be started without end user
intervention (e.g. by means of some sort of OCR scheduling worker)

When automatic is set to `false` -  it means that OCR will be performed only
if requested by end user. In this case user can choose to start schedule OCR
on upload; also in this case use can choose to schedule OCR later on any
document as ofter as he/she wishes.

PAPERMERGE__OCR__AUTOMATIC=`false` is practical only in environments where end
user is same as the one maintening {{extra.project}} instance, thus he/she
owns computational resources and thus is not prone to abuse it.


Default value is:

    PAPERMERGE__OCR__AUTOMATIC=false

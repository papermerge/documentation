# Add OCR Languages

By default the {{extra.project}} docker image includes English, German, French, Italian, Spanish, Romanian and Portugues OCR languages.

You can install extra languages by creating a new docker image from base `papermerge/papermerge`.

Create new docker file with following content:

```
FROM papermerge/papermerge:{{ extra.docker_image_version }}

# add Danish and Polish OCR languages
RUN apt install tesseract-ocr-dan tesseract-ocr-pol
```

All languages are specified in three letters code as per <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
" class="external-link" target="_blank">ISO 639-2T</a> standard -
second column in the table.


In order to build your image run:

```
docker build -t mypaper:3.0 -f Dockerfile .
```

Check that OCR languages were installed:

```
docker run -it --rm  mypaper:3.0  tesseract --list-langs
```

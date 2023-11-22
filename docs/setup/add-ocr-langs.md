# Add OCR Languages

By default the {{extra.project}} Docker image includes English, German, French, Italian, Spanish, Romanian and Portugues OCR languages.

You install extra languages in docker image by creating a new Dockerfile from papermerge/papermerge docker image. Create new docker file with following content:

```
FROM papermerge/papermerge:{{ extra.docker_image_version }}

# add Danish and Polish OCR languages
RUN apt install tesseract-ocr-dan tesseract-ocr-pol
```

Run following command:

```
docker build -t mypaper:3.0 -f Dockerfile .
```

Check that OCR languages were installed:

```
docker run -it --rm  mypaper:3.0  tesseract --list-langs
```

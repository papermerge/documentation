# Add OCR Languages

By default the {{extra.project}} docker image includes English, German, French, Italian, Spanish, Dutch,
Romanian and Portugues OCR languages.

All languages are specified in three letters code as per <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
" class="external-link" target="_blank">ISO 639-2T</a> standard -
second column in the table.


You can install extra languages in couple of steps described in following guide.


## Step 1 - Create your custom OCR docker image

First, you need to create your own OCR worker image to include the necessary
languages. Create a Dockerfile based on the existing
`papermerge/ocrworker:{{ extra.ocr_worker_version }}` image and install the required OCR language
packages:

```
FROM papermerge/ocrworker:{{ extra.ocr_worker_version }}
# Add the required languages here
RUN apt update && apt install -y tesseract-ocr-kaz tesseract-ocr-rus
```

## Step 2 - Verify the languages in the OCR worker

Once the docker image is built and the ocr worker is running verify that the languages are installed:

```
docker exec -it <ocr_worker_docker_container_id> tesseract --list-langs
```


## Step 3 - Add the language support in the Papermerge codebase:

a. Update OCR task schema:
In the `papermerge/core/features/tasks/schema.py` file, add the new language codes to the LangCode type:

```
LangCode = Literal[
    "ces",
    "dan",
    "deu",
    "ell",
    "eng",
    "fas",
    "fin",
    "fra",
    "guj",
    "heb",
    "hin",
    "ita",
    "jpn",
    "kor",
    "lit",
    "nld",
    "nor",
    "pol",
    "por",
    "ron",
    "san",
    "spa",
    # add additional languages here
    "kaz",
    "rus",
]
```

b. Update UI Constants:

In the `ui2/src/cconstants.ts` file, add required language names:

```
export const OCR_LANG: OCRLangType = {
    ces: "Čeština",
    dan: "Dansk",
    deu: "Deutsch",
    ell: "Ελληνικά",
    eng: "English",
    fin: "Suomi",
    fra: "Français",
    guj: "ગુજરાતી",
    heb: "עברית",
    hin: "हिंदी",
    ita: "Italiano",
    jpn: "日本語",
    kor: "한국어",
    lit: "Lietuvių",
    nld: "Nederlands",
    nor: "Norsk",
    osd: "Osd",
    pol: "Polski",
    por: "Português",
    ron: "Română",
    san: "संस्कृत",
    spa: "Español",
    // Add additional languages here
    kaz: "Қазақша",
    rus: "Русский",
};
```

c. Update OCRCode Type:
In the `ui2/src/types.ts` and `ui2/src/types/ocr.ts` files, extend the OCRCode type:

```
export type OCRCode =
    | "ces" | "dan" | "deu" | "ell" | "eng" | "fin" | "fra" | "guj" | "heb"
    | "hin" | "ita" | "jpn" | "kor" | "lit" | "nld" | "nor" | "osd" | "pol"
    | "por" | "ron" | "san" | "spa"
    // Add additional languages here
    | "kaz" | "rus";
```

## Step 4 - Build custom Papermerge image

```
docker buildx build --platform linux/amd64 -t myimage:0.0.1 -f docker/standard/Dockerfile .
```

## Step 5 - Run Papermerge with the custom OCR worker
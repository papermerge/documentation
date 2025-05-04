# Main


## MAIN__MEDIA_ROOT

Absolute filesystem path to the directory that will hold user-uploaded documents.

Example:

    PAPERMERGE__MAIN__MEDIA_ROOT=/var/www/example.com/media/


## MAIN__LOGGING_CFG

Absolute filesystem path to the yaml file that will hold logging detailed
configuration. Content of logging configuration file is expected to be in
yaml format and it is very python specific.

Example:

      PAPERMERGE__MAIN__LOGGING_CFG=/etc/papermerge/logging.yaml


## MAIN__FILE_SERVER

Context: `webapp`.
Who is serving document files? Is it `webapp` ? or CDN?
This environment variable can have two values:

* `local` (default)
* `s3`

With `local` (which is set by default), `webapp` is the one serving document files.
With `s3` is CDN serving document files. At this point only AWS CloudFront is supported as CDN.
If `PAPERMERGE__MAIN__FILE_SERVER=s3` then you need to provide following environment variables:

* `PAPERMERGE__MAIN__CF_SIGN_URL_PRIVATE_KEY`
* `PAPERMERGE__MAIN__CF_SIGN_URL_KEY_ID`
* `PAPERMERGE__MAIN__CF_DOMAIN`


## MAIN__CF_SIGN_URL_PRIVATE_KEY

Used only in combination with `PAPERMERGE__MAIN__FILE_SERVER=s3`.
`PAPERMERGE__MAIN__CF_SIGN_URL_PRIVATE_KEY` is the Cloud Front private key (as string).

## MAIN__CF_SIGN_URL_KEY_ID

Used only in combination with `PAPERMERGE__MAIN__FILE_SERVER=s3`.
`MAIN__CF_SIGN_URL_KEY_ID` is the Cloud Front (CF) sign url key id.

## MAIN__CF_DOMAIN

Used only in combination with `PAPERMERGE__MAIN__FILE_SERVER=s3`.
`MAIN__CF_DOMAIN` is the Cloud Front (CF) domain.


## MAIN__TIMEZONE

Which timezone to use.

Example:

    PAPERMERGE__MAIN__TIMEZONE=Europe/Berlin

# Main


## MEDIA_ROOT

Absolute filesystem path to the directory that will hold user-uploaded documents.

Example:

    PAPERMERGE__MAIN__MEDIA_ROOT=/var/www/example.com/media/


## LOGGING_CFG

Absolute filesystem path to the yaml file that will hold logging detailed
configuration. Content of logging configuration file is expected to be in
yaml format and it is very python specific.

Example:

      PAPERMERGE__MAIN__LOGGING_CFG=/etc/papermerge/logging.yaml


## TIMEZONE

Which timezone to use.

Example:

    PAPERMERGE__MAIN__TIMEZONE=Europe/Berlin

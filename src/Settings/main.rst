.. _settings__main:

Main
====

.. _settings__main__secret_key:

``MAIN__SECRET_KEY``
~~~~~~~~~~~~~~~~~~~~

Unique secret key. The secret key must be a large random value and it must be
kept secret. This option does not have default value, you always need
to supply a value for it.

Example as environment variable::

  PAPERMERGE__MAIN__SECRET_KEY=asjrijfpHHJH00huge00secret00QMNB344GHOOooaq

Example as toml configuration file::

  [main]
  secret_key = "asjrijfpHHJH00huge00secret00QMNB344GHOOooaq"


``MAIN__MEDIA_ROOT``
~~~~~~~~~~~~~~~~~~~~~

Absolute filesystem path to the directory that will hold user-uploaded documents.

Example as environment variable::

  PAPERMERGE__MAIN__MEDIA_ROOT=/var/www/example.com/media/

Example as toml config::

  [main]
  media_root="/var/www/example.com/media/"


``MAIN__LOGGING_CFG``
~~~~~~~~~~~~~~~~~~~~~

Absolute filesystem path to the yaml file that will hold logging detailed
configuration. Content of logging configuration file is expected to be in
yaml format and it is very python specific.

Example as environment variable::

  PAPERMERGE__MAIN__LOGGING_CFG=/etc/papermerge/logging.yaml

Example as toml config::

  [main]
  logging_cfg="/etc/papermerge/logging.yaml"


``MAIN__TIMEZONE``
~~~~~~~~~~~~~~~~~~

Which timezone to use.

Example as environment variable::

  PAPERMERGE__MAIN__TIMEZONE=Europe/Berlin

Example as toml configuration file::

  [main]
  timezone = "Europe/Berlin"

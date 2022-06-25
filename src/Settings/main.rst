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


``MAIN__TZ``
~~~~~~~~~~~~

Which timezone to use.

Example as environment variable::

  PAPERMERGE__MAIN__TZ=Europe/Berlin

Example as toml configuration file::

  [main]
  tz = "Europe/Berlin"

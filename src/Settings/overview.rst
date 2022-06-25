.. _settings_overview:

Overview
=========

|project| loads its settings from a configurations file and environment
variables. Configuration file must be in `toml format <https://toml.io/en/>`_.

At first it tries to read following files:

- /etc/papermerge/papermerge.toml
- /etc/papermerge.toml
- papermerge.toml - from current project directory

If neither of above files exists it will check environment variable
``PAPERMERGE__CONFIG`` (notice two underscores). In case environment variable
``PAPERMERGE__CONFIG`` points to an existing (toml) file - it will try to read
its configurations from there.

Notice that configuration file is optional i.e. if configuration file is not
found |project| will not complain.

Environment variables can be used to configure |project|. **Environment
variables have priority** over configurations found in toml configuration file.

In other words, if same configuration is present toml configuration file
and as environment variable - the one from environment variable will apply.

For example, say there is a toml configuration file with following content::

  [main]
  tz = 'Europe/Berlin'

  [ocr]
  default_language = 'deu'

  [database]
  host = 'localhost'

and there are defined two environment variables as follows::

  PAPERMERGE__DATABASE__HOST='postgres.svc'
  PAPERMERGE__OCR__DEFAULT_LANGUAGE='fra'


In such case, |project| will use following values:

- "Europe/Berlin" for the time zone
- "fra" for default ocr language
- "postgres.svc" for database host

first value is used from toml configuration file while last two values
are used from environment variable, because **environment variables have
priority over toml configurations**.

Environment variables have following format::

  PAPERMERGE__<section>__<name>

double underscores (__) are used as delimiter and all letters are in upper case.

All configurations are groups by sections ocr, database, main etc.

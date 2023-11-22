# Overview

{{ extra.project }} loads its settings from environment
variables.

Environment variables have following format:

    PAPERMERGE__<section>__<name>

double underscores are used as delimiter; environment variables names must be all upper case.

Only required environment variables are:

* PAPERMERGE__SECURITY__SECRET_KEY
* PAPERMERGE__AUTH__PASSWORD

``PAPERMERGE__SECURITY__SECRET_KEY`` is the key to securing signed
data – it is vital you keep this secure, or attackers could use it to
generate their own signed values.

``PAPERMERGE__AUTH__PASSWORD`` is the password for super user
(administrative user or admin user). Super user is created automatically for
you when {{ extra.project }} starts for the first time.


!!! Note

    In the documentation, for brevity sake, ``PAPERMERGE__`` prefix may be omitted.
    For example docs may say: default value for ``DATABASE__URL`` is "sqlite:////db/db.sqlite3"; what is meant actually is: default value for ``PAPERMERGE__DATABASE_URL`` is "sqlite:////db/db.sqlite3".

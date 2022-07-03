.. _settings__superuser:

Superuser
=========

Superuser is the most privileged user in the system. Superuser
has all permissions and thus can perform any action in the system.
|project| is instanciated with one superuser.

Following settings provide superuser's username, email and password.


.. warning:: Superuser related configurtations can be passed
    **only as environment variables**. Also, superuser related configurations use
    ``DJANGO`` prefix and **one underscore** as separator


.. _settings__superuser__username:

``DJANGO_SUPERUSER_USENAME``
----------------------------

Superuser's username.

Example as environment variable::

    DJANGO_SUPERUSER_USERNAME=john

This configuration can be passed only as environment variable.
Default value is ``admin``.


.. _settings__superuser__email:

``DJANGO_SUPERUSER_EMAIL``
--------------------------

Superuser's email.

Example as environment variable::

    DJANGO_SUPERUSER_EMAIL=john@example.com

This configuration can be passed only as environment variable.
Default value is ``admin@example.com``.


.. _settings__superuser__password:

``DJANGO_SUPERUSER_PASSWORD*``
------------------------------

**Required**. Superuser's password. Always must be set to non-empty value.

This configuration can be passed only as environment variable. This
environment variable **is required**. If not passed, superuser won't be
created and no authentication will be possible.

Example as environment variable::

    DJANGO_SUPERUSER_PASSWORD=456

# Superuser

Superuser is the most privileged user in the system. Superuser
has all permissions and thus can perform any action in the system.
{{ extra.project }} is instantiated with one superuser.

Following settings provide superuser's username, email and password.


!!! warning

    {== Superuser configurations can be passed
    only as environment variables ==}. Also, superuser related configurations use
    `DJANGO` prefix and one underscore as separator


## DJANGO_SUPERUSER_USENAME

Superuser's username.

Example as environment variable::

    DJANGO_SUPERUSER_USERNAME=john

This configuration can be passed only as environment variable.
Default value is `admin`.


## DJANGO_SUPERUSER_EMAIL

Superuser's email.

Example as environment variable::

    DJANGO_SUPERUSER_EMAIL=john@example.com

This configuration can be passed only as environment variable.
Default value is `admin@example.com`.


## DJANGO_SUPERUSER_PASSWORD

{== Required ==}. Superuser's password. Always must be set to non-empty value.

This configuration can be passed only as environment variable. This
environment variable is required. If not passed, superuser won't be
created and no authentication will be possible.

Example as environment variable:

    DJANGO_SUPERUSER_PASSWORD=456

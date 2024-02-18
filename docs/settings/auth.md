# Auth


## AUTH__USERNAME

Username for the superuser. Default value is `admin`.

Example:

    PAPERMERGE__AUTH__USERNAME=john


## AUTH__PASSWORD

Password for the superuser. No default value.

Example:

    PAPERMERGE__AUTH__PASSWORD=topsecret


## AUTH__EMAIL

Email for the superuser. Default value is `admin@example.com`.

Example:

    PAPERMERGE__AUTH__EMAIL=john@mail.com


## AUTH__GOOGLE_CLIENT_SECRET

When using oauth2 authentication with Google provider this variables is oauth2 client secret.
You get oauth2 client secret from Google Console.

Example:

    PAPERMERGE__AUTH__GOOGLE_CLIENT_SECRET=GOCSPX-qlqlqlqlqlqlqlqlq-FuOOOOORf

## AUTH__GOOGLE_CLIENT_ID

When using oauth2 authentication with Google provider this variables is oauth2 client ID.
You get oauth2 client ID from Google Console.

Example:

    PAPERMERGE__AUTH__GOOGLE_CLIENT_ID=900000999991-1tmegfjqqqqqqqqqqqqqqqqqqqqv.apps.googleusercontent.com

## AUTH__GOOGLE_AUTHORIZE_URL

Must be set to fixed value `https://accounts.google.com/o/oauth2/auth`:

    PAPERMERGE__AUTH__GOOGLE_AUTHORIZE_URL=https://accounts.google.com/o/oauth2/auth

In case google changed their authorize URL, please [open a ticket](https://github.com/ciur/papermerge/issues) for Papermerge to update this documentation entry with correct value.

## AUTH__GOOGLE_REDIRECT_URI

This value always should be set to `<http|https>://<your-domain>/google/callback`.
Example:

    PAPERMERGE__AUTH__GOOGLE_REDIRECT_URI=https://demo.trusel.net/google/callback


## AUTH__GITHUB_CLIENT_SECRET

When using oauth2 authentication with GitHub provider this variables is oauth2 client secret.

Example:

    PAPERMERGE__AUTH__GITHUB_CLIENT_SECRET=hohoho-edited-FuOOOOORf

## AUTH__GITHUB_CLIENT_ID

When using oauth2 authentication with GitHub provider, this variables is oauth2 client ID.

Example:

    PAPERMERGE__AUTH__GITHUB_CLIENT_ID=1tmegfjq-edited-qqqqv

## AUTH__GITHUB_AUTHORIZE_URL

Must be set to fixed value `https://github.com/login/oauth/authorize`:

    PAPERMERGE__AUTH__GITHUB_AUTHORIZE_URL=https://github.com/login/oauth/authorize

In case GitHub changes their authorize URL, please [open a ticket](https://github.com/ciur/papermerge/issues) for Papermerge to update this documentation entry with correct value.

## AUTH__GITHUB_REDIRECT_URI

This value always should be set to `<http|https>://<your-domain>/github/callback`.
Example:

    PAPERMERGE__AUTH__GITHUB_REDIRECT_URI=https://demo.trusel.net/github/callback


## AUTH__LDAP_URL

If this environment variable is set to non-empty value, {{extra.project}} will assume that authentication will be performed using LDAP
backend. Value should be set to URL of the ldap server. URL is specified without scheme
(i.e. no ldap://, ldaps:// prefix). Example:

    PAPERMERGE__AUTH__LDAP_URL=ldap.trusel.net

## AUTH__LDAP_USER_DN_FORMAT

Format of distingueshed name to the user entry. The "{username}" literal is used
as placeholder; in other words you mark the part of the DN where actual username will be placed with "{username}" string. Example:

    PAPERMERGE__AUTH__LDAP_USER_DN_FORMAT="uid={username},ou=People,dc=ldap,dc=trusel,dc=net"

Another example:

    PAPERMERGE__AUTH__LDAP_USER_DN_FORMAT="uid={username},ou=Users,dc=example,dc=com"

Yet another, fictional example:

    PAPERMERGE__AUTH__LDAP_USER_DN_FORMAT="uid={username},ou=Accounts,dc=acme,dc=com"

You see? "{username}" part stay fixed. It is placeholder.

## AUTH__LDAP_USE_SSL

Boolean value (True/False). Instructs {{ extra.project }} if secure connection should be used (TLS/SSL) when connecting to LDAP server.
Default value is True. Example:

    PAPERMERGE__AUTH__LDAP_USE_SSL=False

## AUTH__LDAP_EMAIL_ATTR

Email attribute name in user LDAP entry. Default value is `mail`.

## AUTH__LDAP_USER_EMAIL_DOMAIN_FALLBACK

Fallback value of the email domain.
In case {{ extra.project }} fails to extract user's email, it will use this value as fallback for email domain.
The full email format that {{ extra.project }} will set as fallback is:

    <username>@<email-domain-fallback>

For example, if:

    PAPERMERGE__AUTH__LDAP_USER_EMAIL_DOMAIN_FALLBACK=starship.com

and username is `coco` and, say, LDAP user entry does not feature mail attribute, the
email assigned to user will be `coco@starship.com`

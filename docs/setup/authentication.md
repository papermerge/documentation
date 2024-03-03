# Authentication

{{ extra.project }} supports different authentication modes:

- Database (default)
- OAuth 2.0
- LDAP

The difference consist in who decides if user with given username and
password, are valid. In first mode i.e. database authentication - it is
 {{ extra.project }} who decides if credentials are valid, this is why this
database authentication is also called "internal authentication". For other
two authentication modes it is the other party, external one like LDAP, which
decides on validity of the given credentials.


## Database Authentication

In this case authentication is performed against credentials stored in
database configured with `PAPERMERGE__DATABASE__URL`. This is default
operation mode.


## OAuth 2.0/OIDC

{{ extra.project }} supports OAuth 2.0/OpenID Connect authentication protocol.

In order to enable OIDC authentication you need to provide following environment variables:

- PAPERMERGE__AUTH__OIDC_CLIENT_SECRET
- PAPERMERGE__AUTH__OIDC_CLIENT_ID
- PAPERMERGE__AUTH__OIDC_AUTHORIZE_URL
- PAPERMERGE__AUTH__OIDC_ACCESS_TOKEN_URL
- PAPERMERGE__AUTH__OIDC_USER_INFO_URL
- PAPERMERGE__AUTH__OIDC_LOGOUT_URL
- PAPERMERGE__AUTH__OIDC_REDIRECT_URL

Note that last one, redirect URL, is the only URL pointing to {{ extra.project }} instance domain.
It should have following format `<http|https>://<papermerge-instance-domain>/oidc/callback`.
Example:

    PAPERMERGE__AUTH__OIDC_REDIRECT_URL=https://papermerge.net/oidc/callback

All other URLs, authorize URL, access point URL, user info URL and logout URL, should point
to OIDC provider domain, examples:

    - PAPERMERGE__AUTH__OIDC_AUTHORIZE_URL=http://authk.trusel.net/application/o/authorize/
    - PAPERMERGE__AUTH__OIDC_ACCESS_TOKEN_URL=http://authk.trusel.net/application/o/token/
    - PAPERMERGE__AUTH__OIDC_USER_INFO_URL=http://authk.trusel.net/application/o/userinfo/
    - PAPERMERGE__AUTH__OIDC_LOGOUT_URL=http://authk.trusel.net/application/o/calypso/end-session/


## LDAP

{{ extra.project }} can perform authentication against users stored in LDAP system.
In order to enable LDAP authentication you need to provide at least
two environment variables:

- [PAPERMERGE__AUTH__LDAP_URL](../settings/auth.md#auth__ldap_url)
- [PAPERMERGE__AUTH__LDAP_USER_DN_FORMAT](../settings/auth.md#auth__ldap_user_dn_format)



First one is the URL to your ldap server, without scheme, example:

    PAPERMERGE__AUTH__LDAP_URL=ldap.trusel.net

By default, {{ extra.project }} will connect to LDAP server using secure TLS connection. If you want {{ extra.project }} to access LDAP server using plain text connection, set [PAPERMERGE__AUTH__LDAP_USE_SSL](../settings/auth.md#auth__ldap_use_ssl) to False:

    PAPERMERGE__AUTH__LDAP_USE_SSL=False

The second mandatory option is [PAPERMERGE__AUTH__LDAP_USER_DN_FORMAT](../settings/auth.md#auth__ldap_user_dn_format). It instructs {{ extra.project }} the DN (distinguished name) of the user
you want to authenticate against. Example:

    PAPERMERGE__AUTH__LDAP_USER_DN_FORMAT=uid={username},ou=People,dc=ldap,dc=trusel,dc=net

Notice "{username}" part - it must be literaly this value; the "{username}" will be replaced with actual
username of the user when performing LDAP bind.

!!! Info

    In case you are curious, {{ extra.project }} uses [ldap3](https://ldap3.readthedocs.io/en/latest/) python package to perform LDAP authentication. [Here is source code](https://github.com/papermerge/auth-server/blob/main/auth_server/backends/ldap.py) of ldap authentication part.

By default {{ extra.project }} will try to extract user's email from `mail` attribute of LDAP entry identified `PAPERMERGE__AUTH__LDAP_USER_DN_FORMAT` distinguished name.
You can instruct {{ extra.project }} about email attribute in LDAP entry with [PAPERMERGE__AUTH__LDAP_URL](../settings/auth.md#auth__ldap_email_attr).

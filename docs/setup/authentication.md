# Authentication

{{ extra.project }} comes with flexible authentication features.
It can handle user accounts, groups, permissions. {{ extra.project }}
supports following authentication modes:

- Built-in
- OpenID Connect (OIDC)
- Remote User
- LDAP


## Built-in

By default {{ extra.project }} will use built-in authentication mechanism.
You only need to provide `PAPERMERGE__AUTH__USERNAME`, `PAPERMERGE__AUTH__PASSWORD`
environment variables.
In this mode there is no other authentication party involved as all
authentication is performed by {{ extra.project }} internal components.

Built-in authentication mechanism is suitable for simple setups when
{{ extra.project }} is your only application of concern.

When you want to give users access to multiple applications using same accounts,
you may consider:


## OpenID Connect (OIDC)

{{ extra.project }} supports OpenID Connect (OIDC) authentication.

In order to enable OIDC authentication you need to provide following environment variables:

- PAPERMERGE__AUTH__OIDC_CLIENT_SECRET
- PAPERMERGE__AUTH__OIDC_CLIENT_ID
- PAPERMERGE__AUTH__OIDC_AUTHORIZE_URL
- PAPERMERGE__AUTH__OIDC_ACCESS_TOKEN_URL
- PAPERMERGE__AUTH__OIDC_USER_INFO_URL
- PAPERMERGE__AUTH__OIDC_LOGOUT_URL
- PAPERMERGE__AUTH__OIDC_INTROSPECT_URL
- PAPERMERGE__AUTH__OIDC_REDIRECT_URL

Note that last one, redirect URL, is the only URL pointing to {{ extra.project }} instance domain.
It should have following format `<http|https>://<papermerge-instance-domain>/oidc/callback`.
Example:

    PAPERMERGE__AUTH__OIDC_REDIRECT_URL=https://papermerge.net/oidc/callback

All other URLs, authorize URL, access point URL, user info URL, introspect URL and logout URL,
should point to OIDC provider domain. Examples:

    PAPERMERGE__AUTH__OIDC_CLIENT_SECRET=pT5Ff-your-token-eWOSvEPmtyY
    PAPERMERGE__AUTH__OIDC_CLIENT_ID=papermerge
    PAPERMERGE__AUTH__OIDC_AUTHORIZE_URL=http://keycloak.trusel.net:8080/realms/myrealm/protocol/openid-connect/auth
    PAPERMERGE__AUTH__OIDC_ACCESS_TOKEN_URL=http://keycloak.trusel.net:8080/realms/myrealm/protocol/openid-connect/token
    PAPERMERGE__AUTH__OIDC_USER_INFO_URL=http://keycloak.trusel.net:8080/realms/myrealm/protocol/openid-connect/userinfo
    PAPERMERGE__AUTH__OIDC_LOGOUT_URL=http://keycloak.trusel.net:8080/realms/myrealm/protocol/openid-connect/logout
    PAPERMERGE__AUTH__OIDC_INTROSPECT_URL=http://keycloak.trusel.net:8080/realms/myrealm/protocol/openid-connect/token/introspect


## Remote User


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

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


## AUTH__OIDC_CLIENT_SECRET

When using OAuth 2.0/OIDC authentication, this variables is client secret.

Example:

    PAPERMERGE__AUTH__OIDC_CLIENT_SECRET=GOCSPX-qlqlqlqlqlqlqlqlq-FuOOOOORf

## AUTH__OIDC_CLIENT_ID

When using OAuth 2.0/OIDC authentication, this variables is client ID.

Example:

    PAPERMERGE__AUTH__OIDC_CLIENT_ID=papermerge

## AUTH__OIDC_AUTHORIZE_URL

Must be set to value OIDC authorization endpoint.

    PAPERMERGE__AUTH__OIDC_AUTHORIZE_URL=http://keycloak.trusel.net:8080/realms/myrealm/protocol/openid-connect/auth
    PAPERMERGE__AUTH__OIDC_AUTHORIZE_URL=http://authk.trusel.net/application/o/authorize/


Value points to identity provider's domain.


## AUTH__OIDC_ACCESS_TOKEN_URL

When using oauth2/oidc authentication, this variable contains access token endpoint.

Example:

    PAPERMERGE__AUTH__OIDC_ACCESS_TOKEN_URL=http://authk.trusel.net/application/o/token/
    PAPERMERGE__AUTH__OIDC_ACCESS_TOKEN_URL=http://keycloak.trusel.net:8080/realms/myrealm/protocol/openid-connect/token

Value points to identity provider's domain.


## AUTH__OIDC_USER_INFO_URL

When using oauth2/oidc authentication, this variable contains user info endpoint.

Example:

    PAPERMERGE__AUTH__OIDC_USER_INFO_URL=http://authk.trusel.net/application/o/userinfo/
    PAPERMERGE__AUTH__OIDC_USER_INFO_URL=http://keycloak.trusel.net:8080/realms/myrealm/protocol/openid-connect/userinfo

Value points to identity provider's domain.


## AUTH__OIDC_LOGOUT_URL

When using oauth2/oidc authentication, this variable contains logout endpoint.

Example:

    PAPERMERGE__AUTH__OIDC_LOGOUT_URL=http://keycloak.trusel.net:8080/realms/myrealm/protocol/openid-connect/logout
    PAPERMERGE__AUTH__OIDC_LOGOUT_URL=http://authk.trusel.net/application/o/calypso/end-session/

Value points to identity provider's domain.


## AUTH__OIDC_INTROSPECT_URL

Introspect endpoint.

    PAPERMERGE__AUTH__OIDC_INTROSPECT_URL=http://keycloak.trusel.net:8080/realms/myrealm/protocol/openid-connect/token/introspect

Value points to identity provider domain.
Introspect endpoint is used to validate all incoming requests if they are authenticated or not.


## AUTH__OIDC_SCOPE

List of OIDC scopes delimited by space. Example:

    PAPERMERGE__AUTH_OIDC_SCOPE="openid email profile"


## AUTH__OIDC_REDIRECT_URL

This value always should be set to `<http|https>://<your-papermerge-domain>/oidc/callback`.
Example:

    PAPERMERGE__AUTH__OIDC_REDIRECT_URL=http://papermerge.instance.net/oidc/callback


Value points to {{ extra.project }} domain. This is basically domain where the identity
provider (e.g. keycloak) will send information, or redirect, after successfull authentication.





## AUTH__LDAP_URL

If this environment variable is set to non-empty value, {{extra.project}} will assume that authentication will be performed using LDAP
backend. Value should be set to URL of the ldap server. URL is specified without scheme
(i.e. no ldap://, ldaps:// prefix). Example:

    PAPERMERGE__AUTH__LDAP_URL=ldap.trusel.net

## AUTH__LDAP_USER_DN_FORMAT

Format of distinguished name to the user entry. The "{username}" literal is used
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



## AUTH__REMOTE

When set to non-empty value it enables remote user authentication support.
By default this environment variable is not set.

Following examples enable remote user authentication:

    PAPERMERGE__AUTH__REMOTE=1

or

    PAPERMERGE__AUTH__REMOTE=True

or

    PAPERMERGE__AUTH__REMOTE=Yes


When remote user authentication is enabled, {{ extra.project }} expects to receive
user details via following http headers AND cookies:

- `Remote-User` (header) - user's username e.g. `john`
- `Remote-Groups` (header) - comma delimited list of groups user belongs to e.g. `admin`, `accounting,research`
- `Remote-Email` (header) - user's email
- `Remote-Name` (header) - user's name
- `remote_user` (cookie) - user's username
- `remote_groups` (cookie) - comma delimited list of groups
- `remote_email` (cookie)
- `remote_name` (cookie)


!!! Note

    Currently `Remote-Groups` header and `remote_groups` cookie have no effect. User groups will
    be introduced soon.




## AUTH__REMOTE_LOGOUT_ENDPOINT

When remote user authentication is enabled, it points to the logout endpoint which ends user's session.
Endpoint must be specified with full URL including scheme, domain and path.

Example:

    PAPERMERGE__AUTH__REMOTE_LOGOUT_ENDPOINT=https://auth.trusel.net/logout

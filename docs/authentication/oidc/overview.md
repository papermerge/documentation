# Overview

OpenID Connect (OIDC) is an interoperable authentication protocol based on the OAuth
2.0 framework of specifications.

It is usual for organizations to use multiple software applications. Even a
small home lab features dozens of different apps.

Imagine a small home lab with 7 apps and each of those app uses separate
authentication system. This means that the user of the home lab will need to
keep 7 separate accounts: 7 separate users and 7 different passwords!

Of course users will use various tricks to make their life easier, like register
in all 7 accounts with same username and password. But still, they will need
to sign in daily - 7 times :).

Sticking with same home lab example, wouldn't it be great to have one
single account with which user can sign in once and it will
take effect across all 7 apps? In other words, wouldn't it be great
to use single account for all application within home lab/organization/company ?

Enter OIDC.

OIDC solves above mentioned problem of multiple accounts hell.

With OIDC, the accounts registration, authentication, accounts management
(e.g. password management), is offloaded from the shoulders of the app to
separate entity - **identity provider**.

![One Identity Provider](../../img/auth/oidc/one-ip-many-apps.svg)

!!! Note

    "Authenticate" means same as "sign in", "login".
    Verbs "authenticate", "sign in", "login" are used interchangeably


With OIDC, instead of authenticating in each individual app, user
authenticates with on identity provider (IP) side. To authenticate users,
identity provider can employ various schemes like 2FA (two factor
authentication). Once authentication is successful on the identity provider
side, IP sends {{ extra.project }} a digitally signed token. All the
subsequent requests to {{extra.project}} need to have that token, or otherwise
they will be denied as not authorized.

It may sounds abstract, because it is abstract.
I think couple of illustration will clear the waters.


First, in order to authenticate, OIDC enabled app ({{ extra.project }}) will
redirect user to OIDC provider sign in page. On successful authentication
{{ extra.project }} receives a token - so called jwt token.

![One Identity Provider](../../img/auth/oidc/auth-process.svg)

In above illustration, for step 1 -> 2 to work `PAPERMERGE__AUTH__OIDC_AUTHORIZE_URL` setting
is employed. For step 2 -> 3 to work `PAPERMERGE__AUTH__OIDC_REDIRECT_URL` is used.

The trophy, which {{ extra.project }} receives from identity provider for
successful sign in, is so call called [JWT token](https://jwt.io/). Users
have no idea (and rightfully so) about JWT tokens, as all token business
happens behind the scenes.


!!! Note

    All processes described from here on, are not visible to the users. It all
    happens behind the scenes for them. Information which follows is
    meant for devs, DevOps, SREs.

Your OIDC application needs JWT token as prove of
successful authentication. As you may guess, JWt token will be carried inside
each subsequent http requsts as http header.

All incoming http requests are proved for validity of JWT token. If http request
has valid JWT token - request is permitted to reach app. If http request does not
contain valid JWT token - it is denied access to the app.


!!! Note

    By "valid JWT token" is usually meant that it contain valid digital signature,
    it is not expired and maybe some other checks specific to identity provider.


Following illustrations depict what happens with incoming requests:


![HTTP Request Access Granted](../../img/auth/oidc/request-access-granted.svg)

![HTTP Request Access Denied](../../img/auth/oidc/request-access-denied.svg)

Inside {{ extra.project }} there is a "guard" which, for every incoming
request, asks identity provider if respective HTTP request is valid or not.
If identity provider says that JWT token is valid - request is permitted to pass,
otherwise access is denied.
This step is possible due to `PAPERMERGE__AUTH__OIDC_INTROSPECT_URL` setting.
OIDC introspect endpoint is go to endpoint to inquiry for validity
of the JWT token.

The last technical detail to clarify, with high risk of diving in too many details,
is: what is this "guard" thingy?
"Guard" is nginx's
[authorization based on sub-request result](https://nginx.org/en/docs/http/ngx_http_auth_request_module.html).
In other words, there is nginx's "auth_request" for every incoming HTTP request and
depending on it's response's status code the request is allowed to pass or not.


That's all with OIDC theory. Now it is time to jump into
specific examples. First example is [Papermerge + Keycloak](keycloak.md) as identity provider.

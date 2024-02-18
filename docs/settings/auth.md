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
## AUTH__LDAP_USER_DN_FORMAT
## AUTH__LDAP_USE_SSL
## AUTH__LDAP_EMAIL_ATTR
## AUTH__LDAP_USER_EMAIL_DOMAIN_FALLBACK
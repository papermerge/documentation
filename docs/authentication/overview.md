# Overview

It is usual for organizations to use multiple software applications. Even a
small home lab features dozens of different apps.

Imagine a small home lab with 7 apps and each of those app uses separate
authentication system. This means that the user of the home lab will need to
keep 7 separate accounts: 7 separate users and 7 different passwords!

Of course users will use various tricks to make their life easier, like register
in all 7 accounts with same username and password. But still, they will need
to sign in daily - 7 times!

Wouldn't it be great to have one single account with which user can sign in
once and it will take effect across all 7 apps? In other words, wouldn't it
be great to use single account for all application within home
lab or company?

The solution is to setup so called "centralized authentication system".
This "centralized authentication system" is usually referred
as *SSO* - *single sign on*.

This documentation part is all about SSO, it goes into details of various SSO
method setups.

{{ extra.project }} supports following SSO methods:

- OIDC
- Remote User
- LDAP

OIDC is a standardized protocol.
"Remote User" user method conventional.
LDAP is the most creative method part of the three - means there many ways
to configure LDAP authentication.
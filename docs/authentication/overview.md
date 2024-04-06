# Overview

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

There are many ways to solve above mentioned problem i.e. using a centralized
authentication system. {{ extra.project }} supports following:

- OIDC
- Remote User
- LDAP

This part of documentation details into each of the methods.

OIDC is a standardized protocol.
"Remote User" user method conventional.
LDAP is the most creative method part of the three - means there many ways
to configure LDAP authentication.
# Security


## SECURITY__SECRET_KEY


{== Required ==}. Unique secret key. The secret key must be a large random value and it must be
kept secret. This option does not have default value, you always need
to supply a value for it. Secret key is used to sign JWT tokens.

Example as environment variable:

    PAPERMERGE__SECRET__SECRET_KEY=asjrijfpHHJH00huge00secret00QMNB344GHOOooaq


## SECURITY__TOKEN_EXPIRE_MINUTES


[REST API token](../rest-api/token.md) expiration in minutes. Default value is 360 (i.e. 6 hours).

Example, set token to expire in 7 days (10080 = 60x24x7):

    PAPERMERGE__SECURITY__TOKEN_EXPIRE_MINUTES=10080


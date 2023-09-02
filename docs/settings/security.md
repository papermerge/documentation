# Security


## SECRET_KEY


{== Required ==}. Unique secret key. The secret key must be a large random value and it must be
kept secret. This option does not have default value, you always need
to supply a value for it. Secret key is used to sign JWT tokens.

Example as environment variable:

    PAPERMERGE__SECRET__SECRET_KEY=asjrijfpHHJH00huge00secret00QMNB344GHOOooaq


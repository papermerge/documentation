# REST API


<iframe width="560" height="315" src="https://www.youtube.com/embed/OePTvPcnoMw" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


REST API is a way to interact with Papermerge far beyond Web Browser realm.
It gives you power to extend Papermerge in many interesting ways.
For example it allows you to write a simple bash script to automate uploading
of files from your local (or remote) computer's specific location.

Another practical scenario where REST API can be used is to automatically
(well, you need some sort of 3rd party script for that)
import attached documents from a given email account.

## How It Works?

Instead of usual Sign In, with username and password, via Web Browser,
you will *sign in* with a token (a fancy name for sequence of numbers and letters)
from practically any software which supports http protocol.

Thus, working with REST API is two step process:

1. get a token
2. use the token from 3rd party REST API client

## Get a Token

1. Click User Menu (top right corner) -> API Tokens
2. Click New Token
3. You will to decide on number of hours the token will be valid. Default is 4464 hours, which is roughly equivalent of 6 months. Click *Save* button.
4. After you click *Save* button, two information messages will be displayed. **Write down** your token from *Remember the token: ...* info window.

![token api](../img/user-manual/rest-api/01_token_api_user_menu.png)



![new token button](../img/user-manual/rest-api/02_new_token_button.png)

!!! important

    Write down your token. For security reasons, it is will be displayed only once.
    In picture below, it is the one marked in red.

!!! important

    Tokens are saved in database **encrypted**. Token's encrypted version is called
    **digest**. In tokens tables (by the way, you can have as many token you like)
    first column displays first 16 characters of the digest. It is a way to identify
    the token. In picture below, token's digest is marked with green.

![displayed token](../img/user-manual/rest-api/03_displayed_token.png)


## Use the Token


Once you have your REST API token, you can use Papermerge with any HTTP client,
just remember to include REST API token as header using following format:

```console
Authorization: Token <you token here>
```

Let's see some examples with  <a href="https://curl.haxx.se" class="external-link" target="_blank">curl</a>.
The simplest REST API call is:

```console
curl -H "Authorization: Token 7502db85f8d40bc7f4f5ab0a4e4fee4a"  <HOST>/api/documents
```

If get 2XX response, it means your `Authorization` header and token are correct.

Upload local file to remote host specified with ``<HOST>``:

```console
curl -H "Authorization: Token 7502db85f8d40bc7f4f5ab0a4e4fee4a"  \
  -T /home/eugen/documents/demo/2019/berlin1.pdf  \
  <HOST>/api/document/upload/berlin_x1.pdf
```

Notice that local file name is berlin1.pdf while it features in url as
berlin_x1.pdf. This way I can rename local file.

You can upload files without specifying their remote name, in that case remote
file will have same name as local file:

```console
curl -H "Authorization: Token 7502db85f8d40bc7f4f5ab0a4e4fee4a"  \
  -T /home/eugen/documents/demo/2019/berlin1.pdf  \
  <HOST>/api/document/upload/
```

!!! note

    Notice the trailing `/` character. When uploading file with `curl` without specifying file name URL must end with `/`. This is a way to notify curl that we don't want to rename files.

Your (REST API) uploaded files will end up in Inbox.

![inbox](../img/user-manual/rest-api/04_inbox.png)

## REST API Reference

REST API authorization header:

* name: `Authorization`
* value format `Token <your-token-here>`

Example:

```console
curl ... -H "Authorization: Token <your-token-here>"
```

REST API URLs:


|URL|HTTP Method| Description|
|---|-----------|------------|
|/api/documents|GET|json list of all documents|
|/api/document/<id>|GET| json info about document with id=<id>|
|/api/document/upload/|PUT| Uploads unnamed file (random name will be assigned)|
|/api/document/upload/<filename>|PUT|Uploads named file|

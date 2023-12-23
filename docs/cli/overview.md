# Overview

This section describes a set of command line utilities which can interact
(e.g. import documents to, list nodes etc) with your {{ extra.project }} instance.

What is common to all command line utilities listed here is that they all use REST API interface.
In order to use REST API you need to know:

* host address of the REST API server
* the token used for authentication - REST API token


## Host Address

Host address should be provided with `http://` or `https://` prefix.


Examples:

- http://papermerge.local
- https://mydms.com/
- https://my-own-digital-archives.de


!!! note

     REST API server may or may not end with ``/`` character. Thus, both http://papermerge.local
	    and http://papermerge.local/ are valid.


## REST API Token

Currently there is no web UI for getting your user's token.
The only way to get REST API token is by running docker command.

Click [here for details](../rest-api/token.md).

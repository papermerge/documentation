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

You get REST API token from web UI of your {{ extra.project }} instance. In user menu (upper right corner)
go to REST API Token menu item.

Further details are [described in user manual](../user/rest-api-token.md).

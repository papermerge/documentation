# Overview

This section describes a set of command line utilities which can interact
(e.g. import documents to, list nodes etc) with your {{ extra.project }} instance.

What is common to all command line utilities listed here is the "protocol" they
use to interact with - they all use REST API interface {{ extra.project }}. To
state it differently - all following command line tools, in order to interact
with {{ extra.project }} need to know:

* host address of the REST API server
* the token used for authentication (i.e. REST API token)


## Host Address

Host address should be provided with `http://` or `https://` prefix (depending
on the REST API server) and {== does not ==} include /api suffix.

Examples:

      http://papermerge.local, https://mydms.com/, https://my-own-digital-archives.de

!!! note

     REST API server may or may not end with ``/`` character. Thus, both http://papermerge.local
	    and http://papermerge.local/ are valid.


## REST API Token

REST API token can be obtained directly from respective command line utility e.g.:

	  papermerge-cli auth

or the REST API token can be obtained from {{ extra.project }} user interface as [described in user manual](../user/rest-api-token.md)

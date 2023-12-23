# REST API Token

Currently there is no web UI for getting the REST API token.
Instead, you get the REST API token by running one docker command:

	docker exec <papermege-container> create_token.sh <username>

You can list users in {{ extra.project }} with following command:

	docker exec <papermege-container> list_users.sh

![](../../img/rest-api/create_token.gif)
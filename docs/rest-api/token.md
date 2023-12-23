# REST API Token

Currently there is no web UI for getting the REST API token.
Instead, you get the REST API token by running one docker command:

    docker exec <papermege-container> create_token.sh <username>

You can list users in {{ extra.project }} with following command:

    docker exec <papermege-container> list_users.sh

Example:

    $ docker ps --format '{\{.ID\}} {\{.Command\}} {\{.Names\}}'

    d8b965388fd9 "/run.bash server" fordoc-web-1
    8fb8f6f565a2 "/run.bash worker" fordoc-worker-1
    8a42db0bb7f9 "/opt/bitnami/script…" fordoc-db-1
    8a6146801936 "docker-entrypoint.s…" fordoc-redis-1

In above example the Papermerge has four containers: app server, redis,
database and one worker.
For our purpose we need app container (in example above - fordoc-web-1).
Let's list all users first:

    $ docker exec d8b965388fd9 list_users.sh

    username=john email=admin@example.com

There is only one user with username "john".
In order to get REST API token for user "john" run following command:

    $ docker exec d8b965388fd9 create_token.sh john

    eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huIiwidXNlcl9pZCI6IjJiODQwY2RhLThjMmYtNDExYy05NDYwLTY0ZDA3YWY3YTJiZSIsImV4cCI6MTcwMzM1MTUzNn0.KJAL9TjRiV63liwVO5bh9GQ_I_QFXMoviKV9Lww3cDs

The long list of characters from above is the token for user with username "john".

![](../../img/rest-api/create_token.gif)

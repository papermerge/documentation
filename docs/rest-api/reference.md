# Reference


Papermerge REST API is exposed via <a href="https://www.openapis.org/" class="external-link" target="_blank">Open API</a> standard. which means that there is one `openapi-schema.yml` file that can be rendered by various 3rd
party visualizers. `openapi-schema.yml` file is generated directly from
application code and thus (at the time of generation) it matches actual
implementation.

{{ extra.project }}ships with two "REST API visualizers" - redoc and swagger ui. Both
of these "visualizers" read from same openapi schema file and thus convey same
information - just formatted differently.


## Online vs Local Instance

As you will see, there are two ways of accessing REST API reference - one is
from your own instance and another from online documentation website.
Accessing REST API reference from your own {{ extra.project }}instance's **guarantees
that the reference will match implementation**, because in this case REST API
reference is generated on the fly!

On the other hand, online version of the REST API (i.e. `redoc ui` and
`swagger ui`) reference uses `openapi-schema.yml` file generated beforehand
which means that it may slightly differ from your own {{ extra.project }}instance.
Online REST API reference is there only for convenience.


## Redoc

Papermerge REST API online reference is available via `redoc ui`.

Same reference can be accessed from your own {{ extra.project }}instance using
following URL:

        <server-url>/api/schema/redoc/

In case when you run {{ extra.project }}locally using default REST API server port
use http://localhost:8000/api/schema/redoc/.

Also, when you run your own instance of {{ extra.project }}you can access
redoc based REST API reference from user menu:


![](../img/rest-api/redoc.gif)


## Swagger UI

Papermerge REST API online reference is available via `swagger ui`.

Same reference can be accessed from your own {{ extra.project }}instance using
following URL:

        <server-url>/api/schema/swagger-ui/


In case when you run {{ extra.project }}locally using default REST API server port
use http://localhost:8000/api/schema/swagger-ui/.

Also, when you run your own instance of {{ extra.project }}you can access
swagger based REST API reference from user menu:


![](../img/rest-api/swagger.gif)

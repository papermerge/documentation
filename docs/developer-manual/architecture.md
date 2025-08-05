# High-Level Architecture

This section describes the different components of {{extra.project}}, their roles, and how they interact.
It is important to understand that the architecture is intentionally designed to avoid a monolithic structure—that is, bundling everything into a single piece.

In this regard, {{extra.project}} adheres to the proven Unix philosophy:
Build small, focused parts with clear interfaces, and combine them as needed.

Please note: Ignore technical details for now and focus on the overall structure.
This section is not intended as a setup guide for your development environment, but rather as a high-level architectural overview.

## The Core Part 1 – REST API

If you have `git`, `python`, and the `poetry` package manager installed on your computer, try the following:

1. `git clone https://github.com/papermerge/papermerge-core`
2. `cd papermerge-core/`
3. `poetry install`
4. `poetry run task server`

The last command attempts to start the REST API server on port **8000**.

Well, almost—it's likely to throw some errors if you don’t have a database configured yet.
For example, you might not have PostgreSQL running, or the required environment variables might be missing.

However, **assuming** you have:

* PostgreSQL up and running,
* a database already created,
* and the correct environment variables (such as `PAPERMERGE__DATABASE__URL`) set,

...then the REST API server should start successfully.

The illustration below shows a basic REST API server waiting for HTTP requests on port **8000**:


![REST API](./architecture/1-core-rest-api.svg)

---

## Two Very Important Points

There are two key things to understand about the Core REST API server:

1. **There is no UI** (i.e. no frontend)
2. **There is no authentication**

Let’s unpack both points.

---

### 1. No UI

I assume you already know what a REST API is. Personally, I find it intuitive to think of a REST API **without any UI**—and you probably do as well.

---

### 2. No Authentication

Now, this is where even experienced developers might get confused.

Let’s start with a very basic REST API call:

```bash
curl http://localhost:8000/users/me
```

This request is meant to return information about the **current user**—that is, the user making the HTTP request.

But wait—didn’t I just say there is **no authentication**?

So… who is the current user?
And is there **any user** at all in the database's `users` table?

Yes, the Core REST API server really **has no authentication**. None. Zero. Nada.

---

### So, who is the current user?

**Answer:** Whoever we say it is.

The REST API is a naive creature—it trusts the information you give it. You can tell it who the current user is by using a custom HTTP header.

Example:

```bash
curl -H "Remote-User: admin" http://localhost:8000/users/me
```

This request informs REST API server to use user with username `admin` as current one.
Assuming you have a user named `admin` in your database, the server will respond with details about `admin`.

In fact, as long as the username exists in your database, you can perform **any REST API call** just by supplying the `Remote-User` header.

> **Note:**
> The REST API server has no concept of authentication.
> It simply receives information about the current user via HTTP headers and trusts it.

---

### What About JWT?

The `Remote-User` example works—but it’s pretty basic.

A more standardized and feature-rich method is to use a **JWT (JSON Web Token)**. JWTs allow you to pass more structured information in the header—like username, user ID, roles, and more.

So instead of:

```http
Remote-User: admin
```

You might pass something like:

```http
Authorization: Bearer <your_jwt_token_here>
```

The principle remains the same:
Whatever information about the current user is provided in the HTTP headers, the REST API server will **extract it and trust it**.

No validation.
No verification.
No actual authentication.

All authentication logic is expected to happen **upstream**—in whatever system is calling the REST API (e.g. an API gateway or a separate auth service).


## The Core Part 2 - UI

This part is basically same as first one - but instead of communicating directly
via REST API, end user interacts with fancy UI. Stated other way
around fancy UI, the frontend, interacts with REST API server on user's behalf.

![REST API and FE](./architecture/2-core-rest-api-and-fe.svg)

Picture above illustrates FE part as it is listens on port 5173. That's true
only in development mode where developer can start frontend server via:

```
yarn install
yarn workspace ui dev
```

Really, this is exactly same as "Part 1" just packed with a beautiful UI.
A few important points:

1. Both frontend (FE = typescript/javascript/css/html etc) and backend (BE = REST API server = python) are in same repository: https://github.com/papermerge/papermerge-core/
2. No authentication there. REST API server accepts whatever upstream passes as current user it via HTTP header
   (e.g. Remote-User header, or Authorization header an JWT token)
3. What was explained so far - lives in one single repo: https://github.com/papermerge/papermerge-core/

## Authentication Server

Here I introduce one more piece of puzzle: the authentication server.
In the end, there must be something which takes user's username
and password and says: yes, 1. this is valid account 2. no, credentials are wrong, go away.
That something is called "authentication server".
The confusing part is that many web frameworks (hello, Django!) include authentication as
part of web framework - the result is that authentication is generally perceived as part of
the same application - and only rarely regarded as separate application.
In {{ extra.project }} universe the "Authentication Server" is just another web application - nothing
more nothing less.

!!! Remember

    Authentication server is just another web application

Authentication Server usually shows you some sort of login UI form where you can
enter username and password and it will check if username + password is a valid combination.
If Authentication Server validates successfully user credentials - it issues a so called
JWT token. This JWT token is cryptographically signed using a secret: in other words,
later on, same authentication server (or maybe other application?) can check - was token signed by it?

!!! Remember

    Authentication server issues JWT tokens

Anyway, all incoming request are checked if they have a valid JWT token. Valid JWT token is one
which was signed by component with same secret. The internal mechanics is irrelevant, what is really
important is that if incoming HTTP request does not have valid JWT token, then http request is redirected
to "login form". If incoming HTTP request is valid - it is routed towards REST API (which stays "behind" UI)
server i.e. towards papermerge core.

Illustration below illustrates what I explained so far.

![REST API and FE and Auth server](./architecture/3-be-fe-auth.svg)

{{ extra.project }} includes very basic authentication server. Its source code is here:

https://github.com/papermerge/auth-server

All components inside the gray area delimited with brown dotted line are included
in papermerge container:

```
docker run -p 12000:80 \
    -e PAPERMERGE__SECURITY__SECRET_KEY=abc \
    -e PAPERMERGE__AUTH__PASSWORD=pass123 \
    papermerge/papermerge:3.5.2
```

!!! Remember

    Core + Auth Server = App Container

    And

    Core = BE + FE

    Where

    BE = Rest API Server
    FE = Frontend application

The beauty of such a solution is that authentication server can be easily replaced.
I have mentioned several times that auth server included by default in {{ extra.project }}
is very basic. What does this mean? It means for example that it does not support 2FA or user
registration flows. But that's not an issue, and the design it conceived so that
basic auth-server may be replaced with full fledged authentication server like Keycloak, Authelia etc

## Workers and Redis

So far I've explained only parts that directly interact with HTTP protocol i.e. the web part of the
equation.

Workers on the other hand have nothing to do with HTTP. They are small applications that run in background and
interact between them and main app via message queues. Here main app is "producer" and workers
are "consumers": in other works main app puts tasks in the queue and workers executes those tasks one by one.

The "message bus" or the transport medium for messages between app and workers (or between workers as they can send messages as well) is Redis. The communication takes place via so called "queues". Each queue has a unique name.

{{ extra.project }} uses following workers:

- [path template worker](https://github.com/papermerge/path-tmpl-worker)
- [s3 worker](https://github.com/papermerge/s3-worker)
- [ocr worker](https://github.com/papermerge/ocr-worker)
- [i3 worker](https://github.com/papermerge/i3-worker)

## Path Template Worker

Every document category has associated a jinja path template. Category path template may looks
like this:

{% raw %}

    {% if document.id %}
    /home/My Documents/Invoices/{{ document.id }}.pdf
    {% else %}
    /home/My Documents/Invoices/
    {% endif %}

{% endraw %}

Or more sophisticated like:

{% raw %}

    {% if document.has_all_cf %}
    /home/Receipts/{{ document.cf['Shop'] }}-{{document.cf['Effective Date']}}.pdf
    {% else %}
    /home/Receipts/{{ document.id }}.pdf
    {% endif %}

{% endraw %}

If you have, say 63000 documents of category "receipts" and you change its path template (say from example 1 above to example 2), then there is no other way, except to go all 63000 documents one by one and to reevaluate its path
so that all documents will be placed correctly according to the new path template. This is serious task - and this is exactly why path template worker is there for.


![Path Template Worker](./architecture/4-path-template-worker.svg)

Path template worker source code: [https://github.com/papermerge/path-tmpl-worker](https://github.com/papermerge/path-tmpl-worker)


## S3 Worker

{{ extra.project }} supports S3 storage. When S3 is enabled, all documents
will be uploaded to S3 storage - uploading documents to s3 storage is the task of s3-worker.


![S3 Worker](./architecture/5-s3-worker-simple.svg)

Notice that S3 Worker must have access to the same local storage as the app (or the entity where
documents are uploaded by the client)

What is designated as "local storage" in the picture - is docker volume in case of deployments based
on docker compose. In case of k8s deployments "local volume" will be the pod storage.

S3-worker source code: [https://github.com/papermerge/s3-worker](https://github.com/papermerge/s3-worker)


## OCR Worker


## i3 Worker
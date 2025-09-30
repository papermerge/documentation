# Version Matrix

The individual {{extra.project}} services, can be executed in Docker containers. To retain version compatibility, use only the listed image tags for {{extra.project}} versions.

!!! Note

    Papermerge 3.6 will not support SQLite databases anymore. Please [migrate to PostgreSQL](/admin-manual/db-migrations/#migrate-from-sqlite-to-postgresql).

## {{extra.project}} Versions

The listed versions have been tested. Other combinations might work as well, but can cause side effects, that are not supported by {{extra.project}}.

| Papermerge Version | Docker Image | Auth Server<br>(used only internally) |OCR Worker | Path Template Worker | S3 Worker | i3 Worker | DB |  Redis | Solr |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [**3.5.3**](https://github.com/papermerge/papermerge-core/releases/tag/3.5.3) | papermerge/papermerge:3.5.3 | papermerge/auth-server:1.1.5 |papermerge/ocrworker:0.3.1 | papermerge/path-tmpl-worker:0.4.1 | papermerge/s3worker:0.5.1 | papermerge/i3worker:0.3 |  postgres:16.1 | redis:7.2 | solr:9.7 |
| [**3.5.2**](https://github.com/papermerge/papermerge-core/releases/tag/3.5.2) | papermerge/papermerge:3.5.2 | papermerge/auth-server:1.1.3 |papermerge/ocrworker:0.3.1 | papermerge/path-tmpl-worker:0.4 | papermerge/s3worker:0.5 | papermerge/i3worker:0.3 |  postgres:16.1 | redis:7.2 | solr:9.7 |
| [**3.4.1**](https://github.com/papermerge/papermerge-core/releases/tag/3.4.1) | papermerge/papermerge:3.4.1 | papermerge/auth-server:1.0.2 | papermerge/ocrworker:0.3.1 | papermerge/path-tmpl-worker:0.3.2 | papermerge/s3worker:0.4.3 | papermerge/i3worker:0.3 | postgres:16.1 | redis:7.2 | solr:9.7 |

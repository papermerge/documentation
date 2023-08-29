Upgrading
==========

Always [backup](backup.md) your database, media directory and configuration files before
upgrading. We try very hard to make sure that all database changes are
non-destructive, but you should always backup beforehand anyway. You will
never regret backing up your database and media directory. You may regret not doing so, so it’s
just better to get into the habit.


## General Instructions

In general, an upgrade involves two parts:

* upgrade application code and dependencies
* apply new database changes (called database migrations)

Upgrading application code is usually something like:

```console
$ git pull
$ export DJANGO_SETTINGS_MODULE=config.settings.prod
$ pip install -r requirements/base.txt
```

Applying new database changes is performed with `migrate` command:


```console
$ export DJANGO_SETTINGS_MODULE=config.settings.prod
$ ./manage.py migrate
```

Note however that above instructions are very generic and may very depending on the release and deployment environment.


## Upgrade via Docker

In case you run Papermerge via docker container, then all you need to do is to
change docker image to the newer version of papermerge docker image. New
docker image means actually new application code (with correct dependencies
already built-in) and, the most important part **docker (startup script) will run database migrations
for you**!


## From 1.5.x to 2.x


!!! danger

    If you run an earlier version then 1.5.x please upgrade to 1.5.5 version first.

It is very important to upgrade exactly from <a href="https://github.com/ciur/papermerge/releases/tag/v1.5.5" target="_blank" class="external-link">1.5.5 </a> to <a href="https://github.com/ciur/papermerge/releases/tag/v2.0.0rc38" target="_blank" class="external-link">2.0.0rc38</a>. The very first 2.x release
candidate (2.0.0rc35) has problems which will result in upgrade failure.

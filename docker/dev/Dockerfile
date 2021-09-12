FROM python:3.8-alpine as build

LABEL author="Eugen Ciur <eugen@papermerge.com>"

WORKDIR /docs

COPY Makefile requirements/base.txt ./
COPY docker/dev/entrypoint.sh .
RUN chmod +x /docs/entrypoint.sh

RUN pip install -r base.txt

VOLUME /docs/src

ENTRYPOINT ["/docs/entrypoint.sh"]
FROM python:3.8-slim as build

LABEL author="Eugen Ciur <eugen@papermerge.com>"
ENV VIRTUAL_ENV=/venv

WORKDIR /docs

RUN apt-get update;
RUN apt-get install -y --no-install-recommends \
    build-essential \
    git

RUN pip install --upgrade poetry
RUN python -m venv /venv

ENV PATH="/venv/bin:$PATH"

COPY poetry.lock pyproject.toml Makefile ./
COPY docker/dev/entrypoint.sh .

RUN poetry install --no-root --no-dev -vvv
RUN chmod +x /docs/entrypoint.sh


VOLUME /docs/src

ENTRYPOINT ["/docs/entrypoint.sh"]
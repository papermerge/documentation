FROM python:3.8 as build

LABEL author="Eugen Ciur <eugen@papermerge.com>"
ENV VIRTUAL_ENV=/venv

# This docker image has 'backed in' Papermerge documentation
# in html format and can serve it via HTTP on port 80.
# The root location is "/".
# In order to start docker containter for port 80 only:
#
#   $ docker run -d  -p 9980:80 papermerge/documenation:latest
#

WORKDIR /docs

RUN apt-get update;
RUN apt-get install -y --no-install-recommends \
    build-essential \
    git

# git cloning here is required
# Sphinx version will look at the repository branches to learn
# about different version (2.0.x, 2.1.x, 2.2.x etc)
RUN git clone https://github.com/papermerge/documentation.git /docs/
RUN git fetch -t

RUN pip install --upgrade poetry
RUN python -m venv /venv

ENV PATH="/venv/bin:$PATH"

COPY poetry.lock pyproject.toml ./
RUN poetry install --no-root --no-dev -vvv

RUN sphinx-multiversion /docs/src/ build

FROM nginx:1.21.1-alpine

COPY --from=build /docs/build/ /usr/share/nginx/html
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

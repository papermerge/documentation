FROM python:3.8 as build

LABEL author="Eugen Ciur <eugen@papermerge.com>"

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

RUN git clone --depth 1 https://github.com/papermerge/documentation.git /docs/
RUN git fetch -t


RUN pip install -r /docs/requirements/base.txt
RUN sphinx-multiversion /docs/src/ build

FROM nginx:1.21.1-alpine

COPY --from=build /docs/build/ /usr/share/nginx/html
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

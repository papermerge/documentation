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

COPY Makefile requirements/base.txt ./
COPY src ./

RUN pip install -r base.txt
RUN sphinx-build -b html . build

FROM nginx:1.21.1-alpine

COPY --from=build /docs/build/ /usr/share/nginx/html
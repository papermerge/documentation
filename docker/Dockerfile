FROM python:3.8 as build

LABEL author="Eugen Ciur <eugen@papermerge.com>"

# This docker image has 'backed in' Papermerge documentation
# in html format and can serve it via HTTP(S).
# It (docker image) exports http ports 80 and 443.
# The root location is "/".
# In order to start docker containter for port 80 only:
#
#   $ docker run -d  -p 9980:80 papermerge/documenation:latest
#
# For port 443 you will need to mount self signed certificates.
# Use ./certs.sh bash script for generating of the certificates.
# When you have certificates:
#
#   $ docker run -d \
#       -p 9980:80 -p 9443:443 \
#       -v "$(pwd)/docker/certs/:/etc/ssl/certs" \
#       papermerge/documentation:latest

WORKDIR /docs

COPY Makefile requirements/base.txt ./
COPY src ./

RUN pip install -r base.txt
RUN sphinx-build -b html . build

FROM nginx:1.21.1-alpine

COPY ./docker/nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /docs/build/ /usr/share/nginx/html
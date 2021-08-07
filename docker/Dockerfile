FROM python:3.8 as build

LABEL author="Eugen Ciur <eugen@papermerge.com>"

WORKDIR /docs
COPY Makefile requirements/base.txt ./
COPY source ./
RUN pip install -r base.txt
RUN sphinx-build -b html . build

FROM nginx:1.21.1-alpine
COPY --from=build /docs/build/ /usr/share/nginx/html
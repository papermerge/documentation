#!/bin/bash

# Generates selfsigned certificates


SUBJ="/C=DE/ST=Berlin/L=Berlin/O=Eugen Ciur/CN=xxx.papermerge.com"

openssl req \
    -newkey rsa:2048 \
    -nodes \
    -keyout certs/selfsigned.key \
    -x509 \
    -days 9365 \
    -out certs/selfsigned.crt \
    -subj $SUBJ
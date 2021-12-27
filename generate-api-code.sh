#!/bin/bash

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i /local/openapi.yaml \
    -g python-flask \
    -o /local/flask_code

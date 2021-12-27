#!/bin/bash

docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
    -i https://github.com/orviz/openapi4pm/raw/main/openapi.yaml \
    -g python-flask \
    -o /local/flask_code

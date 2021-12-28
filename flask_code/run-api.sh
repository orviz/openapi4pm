#!/bin/bash

# building the image
docker build --no-cache -t openapi_server .

# starting up a container
docker run -p 8001:8001 openapi_server

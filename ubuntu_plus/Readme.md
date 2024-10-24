# Ubuntu plus

An updated ubuntu that includes some of the important functions,
like cron and ssh, that will start automatically.

## Dockerfile - Image Creation

The dockerfile is used to build from ubuntu:latest, into ubuntu_plus:v1.0

## Entry.sh - Image Startup

The entry file is created to be placed into the image so that a start point is created.
Each time the image is started, the entry.sh will be launched.

## Docker Build

From the file location:
`docker build -t east252prg/ubuntu:ubuntu-2.0 .` 
or `docker build -t ubuntu_plus:v1.0 .` for local
docker build tag owner/repo:image path
Use a . for the path, if executing at the path location.

## Docker Push

Push the new image to docker hub for safe keeping.
`docker push east252prg/ubuntu:ubuntu-2.0`

## Compose.yaml - Container Creation

The compose file is used to create the container.
Once prepared, use `docker compose up -d` to launch it.

## Log into console

Docker exec has to be used to join the shell.
`docker exec -it ubuntu_plus /bin/bash`
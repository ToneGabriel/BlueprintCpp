#!/bin/bash
set -e

echo "==== Stopping all running containers ===="
CONTAINERS_RUNNING=$(docker ps -q)
if [ -n "$CONTAINERS_RUNNING" ]; then
    echo "Stopping containers: $CONTAINERS_RUNNING"
    echo "$CONTAINERS_RUNNING" | xargs -r docker stop
else
    echo "No running containers found."
fi

echo "==== Removing all containers ===="
CONTAINERS_ALL=$(docker ps -aq)
if [ -n "$CONTAINERS_ALL" ]; then
    echo "Removing containers: $CONTAINERS_ALL"
    echo "$CONTAINERS_ALL" | xargs -r docker rm -f
else
    echo "No containers to remove."
fi

echo "==== Removing all Docker images ===="
IMAGES_ALL=$(docker images -q)
if [ -n "$IMAGES_ALL" ]; then
    echo "Removing images: $IMAGES_ALL"
    echo "$IMAGES_ALL" | xargs -r docker rmi -f
else
    echo "No images to remove."
fi

echo "==== Cleanup complete ===="

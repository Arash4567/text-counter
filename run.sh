#!/bin/bash
echo "Stopping old container ..."
docker compose down
echo "Running new container ..."
docker rmi text-counter-web text-counter-nginx
echo "Running new container ..."
docker compose up -d
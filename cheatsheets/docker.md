# docker.md

## About
**Name:** Docker (refers to dock workers who load and unload containers from ships; Docker 'packages' applications into containers, similar to shipping containers)

**Created:** Released in 2013 by Solomon Hykes, Docker was created to make it easier to package, distribute, and run applications in isolated environments called containers. Its purpose is to simplify software deployment and ensure consistency across different systems.

**Similar Technologies:** Podman, LXC/LXD, rkt, containerd, Vagrant, Kubernetes (for orchestration)

**Plain Language Definition:**
Docker lets you put your app and everything it needs into a container, so it runs the same way anywhere—on your computer, a server, or the cloud.

---

## Container Management

```bash
docker run image             # Run container from image
docker run -it image bash    # Run interactive container
docker run -d image          # Run container in background
docker run -p 8080:80 image  # Map port 8080 to container port 80
docker ps                    # List running containers
docker ps -a                 # List all containers
docker stop container-id     # Stop running container
docker rm container-id       # Remove container
```

## Image Management

```bash
docker images                # List local images
docker build -t name:tag .   # Build image from Dockerfile
docker pull image:tag        # Download image from registry
docker push image:tag        # Upload image to registry
docker rmi image-id          # Remove image
docker history image         # Show image build history
```

## Container Interaction

```bash
docker exec -it container bash # Enter running container
docker logs container        # View container logs
docker logs -f container     # Follow container logs
docker cp file container:/path # Copy file to container
docker cp container:/path file # Copy file from container
```

## Docker Compose

```bash
docker-compose up            # Start all services
docker-compose up -d         # Start services in background
docker-compose down          # Stop and remove services
docker-compose build         # Build all services
docker-compose logs service  # View service logs
docker-compose exec service bash # Enter service container
```

## System Cleanup

```bash
docker system prune          # Remove unused data
docker container prune       # Remove stopped containers
docker image prune           # Remove unused images
docker volume prune          # Remove unused volumes
docker system df             # Show docker disk usage
```

## Data Science Examples

```bash
# Jupyter notebook container
docker run -p 8888:8888 -v $(pwd):/work jupyter/scipy-notebook

# Python environment with dependencies
docker run -it -v $(pwd):/app python:3.11 bash

# PostgreSQL for data storage
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=pwd postgres
```

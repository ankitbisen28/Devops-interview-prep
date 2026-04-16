# Docker Interview Questions (Top 30)

## 1. What is Docker?

Docker is an open-source containerization platform that allows
developers to package applications and their dependencies into
lightweight, portable containers. Containers ensure applications run
consistently across environments.

**Benefits** - Environment consistency - Faster deployment - Lightweight
compared to VMs - Better resource utilization - Easy CI/CD integration

------------------------------------------------------------------------

## 2. Difference between Docker and Virtual Machines

  Feature          Docker Containers   Virtual Machines
  ---------------- ------------------- ------------------
  Virtualization   OS-level            Hardware-level
  Startup Time     Seconds             Minutes
  Resource Usage   Lightweight         Heavy
  OS               Shares host OS      Separate OS
  Performance      Near-native         Slightly slower

------------------------------------------------------------------------

## 3. What is a Docker Image?

A Docker Image is a read-only template used to create containers. It
contains application code, runtime, libraries, and dependencies.

Example:

``` bash
docker pull nginx
```

------------------------------------------------------------------------

## 4. What is a Docker Container?

A container is a running instance of a Docker image.

Example:

``` bash
docker run nginx
```

------------------------------------------------------------------------

## 5. What is a Dockerfile?

A Dockerfile is a text file containing instructions used to build a
Docker image.

Example:

``` dockerfile
FROM node:18
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
CMD ["npm","start"]
```

Build image:

``` bash
docker build -t node-app .
```

------------------------------------------------------------------------

## 6. What is Docker Hub?

Docker Hub is a public registry used to store and share Docker images.

Example:

``` bash
docker pull redis
docker push username/myimage
```

------------------------------------------------------------------------

## 7. Difference between CMD and ENTRYPOINT

  CMD                   ENTRYPOINT
  --------------------- -----------------------
  Default command       Fixed command
  Can be overridden     Harder to override
  Used for parameters   Used for main process

------------------------------------------------------------------------

## 8. What is Docker Volume?

Docker volumes are used to persist container data outside the container
filesystem.

Example:

``` bash
docker volume create myvolume
docker run -v myvolume:/data nginx
```

------------------------------------------------------------------------

## 9. What are Bind Mounts?

Bind mounts map a directory from the host system to the container.

Example:

``` bash
docker run -v /host/path:/container/path nginx
```

------------------------------------------------------------------------

## 10. What is Docker Networking?

Docker networking allows containers to communicate with each other and
external services.

Types: - bridge - host - none - overlay - macvlan

------------------------------------------------------------------------

## 11. What is the Bridge Network?

Bridge is Docker's default network where containers communicate via
internal IP addresses.

------------------------------------------------------------------------

## 12. What is Docker Compose?

Docker Compose is used to manage multi-container applications using a
YAML configuration.

Example:

``` yaml
version: "3"
services:
  web:
    image: nginx
    ports:
      - "80:80"
  redis:
    image: redis
```

Run:

``` bash
docker-compose up
```

------------------------------------------------------------------------

## 13. What is Docker Swarm?

Docker Swarm is Docker's native container orchestration tool used to
manage clusters of Docker nodes.

Initialize:

``` bash
docker swarm init
```

------------------------------------------------------------------------

## 14. What is a Docker Registry?

A Docker registry is a storage and distribution system for Docker
images.

Examples: - Docker Hub - AWS ECR - Azure Container Registry - Google
Container Registry

------------------------------------------------------------------------

## 15. What is Layer Caching?

Each Dockerfile instruction creates a layer. Docker caches these layers
to speed up builds.

------------------------------------------------------------------------

## 16. What is Multi-stage Build?

Multi-stage builds help reduce image size by using multiple build
environments.

Example:

``` dockerfile
FROM node:18 as builder
WORKDIR /app
COPY . .
RUN npm install

FROM node:18-alpine
COPY --from=builder /app /app
CMD ["node","app.js"]
```

------------------------------------------------------------------------

## 17. How to reduce Docker image size?

Best practices: - Use Alpine images - Use multi-stage builds - Remove
unnecessary files - Use `.dockerignore` - Combine RUN commands

------------------------------------------------------------------------

## 18. Difference between COPY and ADD

  COPY               ADD
  ------------------ -----------------------
  Simple file copy   Extra features
  Preferred          Can extract tar files

------------------------------------------------------------------------

## 19. What is .dockerignore?

`.dockerignore` excludes files from the Docker build context.

Example:

    node_modules
    .git
    .env
    logs

------------------------------------------------------------------------

## 20. What is Docker Engine?

Docker Engine is the runtime that builds and runs containers.

Components: - Docker Daemon - Docker CLI - REST API

------------------------------------------------------------------------

## 21. What is Docker Daemon?

Docker daemon (`dockerd`) runs in the background and manages containers,
images, networks, and volumes.

------------------------------------------------------------------------

## 22. Difference between docker run and docker start

  docker run              docker start
  ----------------------- ---------------------------
  Creates new container   Starts existing container
  Pulls image if needed   Uses existing container

------------------------------------------------------------------------

## 23. How to check running containers

``` bash
docker ps
```

All containers:

``` bash
docker ps -a
```

------------------------------------------------------------------------

## 24. How to check container logs

``` bash
docker logs container_id
```

Follow logs:

``` bash
docker logs -f container_id
```

------------------------------------------------------------------------

## 25. What is Docker Inspect?

Shows detailed information about containers.

``` bash
docker inspect container_id
```

------------------------------------------------------------------------

## 26. What is Docker Exec?

Runs commands inside a running container.

``` bash
docker exec -it container_id bash
```

------------------------------------------------------------------------

## 27. Difference between docker stop and docker kill

  docker stop         docker kill
  ------------------- ----------------
  Graceful shutdown   Force shutdown
  SIGTERM             SIGKILL

------------------------------------------------------------------------

## 28. What is Docker Build Context?

Build context is the directory sent to the Docker daemon when building
an image.

Example:

``` bash
docker build .
```

------------------------------------------------------------------------

## 29. What is Docker Tag?

Docker tag assigns a new name or version to an image.

``` bash
docker tag myimage username/myimage:v1
```

------------------------------------------------------------------------

## 30. How to push image to Docker Hub

Login:

``` bash
docker login
```

Tag image:

``` bash
docker tag myimage username/myimage:v1
```

Push:

``` bash
docker push username/myimage:v1
```

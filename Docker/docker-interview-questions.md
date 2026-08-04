# Docker Interview Questions (1–3 Years Experience)

A curated set of commonly asked Docker interview questions for mid-level (1–3 YOE) roles, with clear, interview-ready answers.

---

## 1. Basics & Core Concepts

### Q1. What is Docker and why is it used?
Docker is a containerization platform that packages an application along with its dependencies, libraries, and configuration into a single unit called a **container**. Unlike virtual machines, containers share the host OS kernel, making them lightweight, fast to start, and portable across environments (dev, test, production).

### Q2. What is the difference between a Docker Image and a Docker Container?
- **Image**: A read-only template/blueprint containing the application code, runtime, libraries, and dependencies. It's built in layers.
- **Container**: A running (or stopped) instance of an image. It's the writable, executable layer on top of the image.

> Analogy: An image is like a class in OOP; a container is an object (instance) of that class.

### Q3. What is the difference between Docker and a Virtual Machine?
| Docker (Containers) | Virtual Machine |
|---|---|
| Shares host OS kernel | Has its own guest OS |
| Lightweight (MBs), starts in seconds | Heavy (GBs), takes minutes to boot |
| Process-level isolation | Full hardware-level isolation |
| Less resource overhead | More resource overhead |

### Q4. What is a Dockerfile?
A Dockerfile is a text file containing a set of instructions (`FROM`, `RUN`, `COPY`, `CMD`, etc.) used to automate the building of a Docker image.

### Q5. What is Docker Hub?
Docker Hub is a cloud-based registry service for finding, storing, and sharing Docker images (similar to how GitHub hosts code).

---

## 2. Dockerfile & Image Building

### Q6. Explain common Dockerfile instructions.
- `FROM` – Base image to start from.
- `WORKDIR` – Sets the working directory inside the container.
- `COPY` / `ADD` – Copies files from host to image (`ADD` also supports URLs and auto-extracting tar files).
- `RUN` – Executes a command during **image build** (creates a new layer).
- `CMD` – Default command executed when the container **starts** (can be overridden at runtime).
- `ENTRYPOINT` – Defines the main executable; harder to override than `CMD`, often used together.
- `EXPOSE` – Documents which port the container listens on.
- `ENV` – Sets environment variables.
- `ARG` – Build-time variable (not available at runtime).

### Q7. What is the difference between `CMD` and `ENTRYPOINT`?
- `CMD` provides default arguments that **can be overridden** by the `docker run` command.
- `ENTRYPOINT` defines a fixed executable that **cannot be easily overridden** (without `--entrypoint` flag).
- Best practice: use `ENTRYPOINT` for the main command and `CMD` for default arguments to it.
```dockerfile
ENTRYPOINT ["python3"]
CMD ["app.py"]
```

### Q8. What is the difference between `COPY` and `ADD`?
- `COPY` only copies local files/directories into the image — simple and predictable.
- `ADD` does everything `COPY` does, plus it can fetch files from a URL and auto-extract compressed archives (`.tar.gz`).
- Best practice: prefer `COPY` unless you specifically need `ADD`'s extra features.

### Q9. What are multi-stage builds and why are they useful?
Multi-stage builds let you use multiple `FROM` statements in a single Dockerfile to separate the **build environment** from the **runtime environment**. Only the final stage's artifacts are included in the final image, drastically reducing image size by excluding build tools, compilers, and intermediate files.
```dockerfile
# Stage 1: Build
FROM golang:1.21 AS builder
WORKDIR /app
COPY . .
RUN go build -o myapp

# Stage 2: Run
FROM alpine:latest
COPY --from=builder /app/myapp /myapp
CMD ["/myapp"]
```

### Q10. How do you reduce Docker image size?
- Use smaller base images (e.g., `alpine`, `distroless`).
- Use multi-stage builds.
- Combine `RUN` commands to reduce layers and clean up in the same layer (`apt-get install && rm -rf /var/lib/apt/lists/*`).
- Add a `.dockerignore` file to avoid copying unnecessary files.
- Avoid installing unnecessary packages/dev dependencies in the final image.

### Q11. What is Docker layer caching, and how does it affect build performance?
Each instruction in a Dockerfile creates a cached layer. If a layer hasn't changed (and instructions before it haven't changed), Docker reuses the cache instead of rebuilding it, speeding up builds. This is why it's best practice to place instructions that change less often (like installing dependencies) **before** instructions that change often (like copying source code).

---

## 3. Containers & Runtime

### Q12. What is the difference between `docker stop` and `docker kill`?
- `docker stop` sends a `SIGTERM` first (graceful shutdown), waits a grace period (default 10s), then sends `SIGKILL` if the container hasn't stopped.
- `docker kill` immediately sends `SIGKILL`, forcefully terminating the container.

### Q13. How do you persist data in Docker containers?
By default, data inside a container is lost when the container is removed, since the container's writable layer is ephemeral. To persist data, use:
- **Volumes** – Managed by Docker, stored outside the container's filesystem (`/var/lib/docker/volumes/`). Recommended approach.
- **Bind mounts** – Maps a specific host directory/file into the container.
- **tmpfs mounts** – Stores data in host memory only (non-persistent, useful for sensitive data).

### Q14. What is the difference between a Volume and a Bind Mount?
| Volume | Bind Mount |
|---|---|
| Managed entirely by Docker | Maps to a specific host path |
| Portable across environments | Tied to host directory structure |
| Better for production | Useful for local development (e.g., live code reload) |
| Created via `docker volume create` | Just references an existing host path |

### Q15. How do containers communicate with each other?
- Via **Docker networks** (bridge, custom bridge, overlay for Swarm).
- Containers on the same **user-defined bridge network** can resolve each other by container/service name via Docker's internal DNS.
- Through exposed ports mapped to the host (`-p hostPort:containerPort`).

### Q16. What are the different Docker network types?
- **Bridge** (default) – Isolated network on a single host; containers get internal IPs.
- **Host** – Container shares the host's network namespace directly (no isolation, better performance).
- **None** – No networking at all.
- **Overlay** – Enables communication between containers across multiple Docker hosts (used in Swarm/clustered setups).
- **Macvlan** – Assigns a MAC address to a container, making it appear as a physical device on the network.

### Q17. What happens when you run `docker run` vs `docker start`?
- `docker run` creates a **new container** from an image and starts it.
- `docker start` starts an **existing, stopped** container (keeps its previous state/data).

---

## 4. Docker Compose

### Q18. What is Docker Compose and why is it used?
Docker Compose is a tool for defining and running **multi-container applications** using a single YAML file (`docker-compose.yml`). Instead of running multiple `docker run` commands manually, you define all services, networks, and volumes declaratively and start everything with one command: `docker compose up`.

### Q19. Write a simple `docker-compose.yml` for a web app with a database.
```yaml
version: "3.9"
services:
  web:
    build: .
    ports:
      - "5000:5000"
    depends_on:
      - db
    environment:
      - DB_HOST=db
  db:
    image: postgres:15
    environment:
      - POSTGRES_PASSWORD=secret
    volumes:
      - db_data:/var/lib/postgresql/data

volumes:
  db_data:
```

### Q20. What does `depends_on` do in Docker Compose, and what's a limitation?
`depends_on` controls the **startup order** of services (e.g., starting `db` before `web`). Its limitation is that it only waits for the container to **start**, not for the application inside it to be fully **ready** (e.g., PostgreSQL might still be initializing). For true readiness checks, use `healthcheck` combined with `condition: service_healthy`.

---

## 5. Practical / Scenario-Based

### Q21. How would you debug a container that keeps crashing/restarting?
1. Check logs: `docker logs <container_id>`
2. Inspect exit code and status: `docker inspect <container_id>` or `docker ps -a`
3. Run the container interactively to reproduce the issue: `docker run -it <image> /bin/sh`
4. Check resource limits (OOM kills show exit code `137`).
5. Verify `CMD`/`ENTRYPOINT` and environment variables are correct.

### Q22. Your image size is very large. How do you troubleshoot and fix it?
- Use `docker image history <image>` to see which layers are large.
- Use tools like `dive` to inspect layer contents.
- Apply fixes: multi-stage builds, smaller base images, `.dockerignore`, combining `RUN` layers, removing cache files after installs.

### Q23. How do you pass environment variables/secrets to a container securely?
- Use `--env-file` or `-e` flags for non-sensitive config.
- For secrets, avoid hardcoding in Dockerfiles or images. Use:
  - Docker secrets (in Swarm mode)
  - External secret managers (Vault, AWS Secrets Manager)
  - Runtime-injected environment variables via orchestration tools (Kubernetes Secrets, CI/CD pipeline variables)
- Never commit `.env` files with secrets to version control.

### Q24. How do you clean up unused Docker resources?
```bash
docker system prune          # removes stopped containers, unused networks, dangling images
docker system prune -a       # also removes all unused images (not just dangling)
docker volume prune          # removes unused volumes
docker container prune       # removes stopped containers only
```

### Q25. What's the difference between `docker exec` and `docker attach`?
- `docker exec` runs a **new process** inside a running container (e.g., opening a new shell session) — commonly used for debugging: `docker exec -it <container> bash`.
- `docker attach` connects to the container's **main running process** (PID 1) and its existing stdin/stdout — exiting can sometimes stop the container if it was started in foreground mode.

---

## 6. Quick-Fire Round

| Question | Short Answer |
|---|---|
| How to list running containers? | `docker ps` |
| How to list all containers (including stopped)? | `docker ps -a` |
| How to remove an image? | `docker rmi <image_id>` |
| How to view container logs live? | `docker logs -f <container_id>` |
| How to check image layers? | `docker history <image>` |
| Default network driver? | `bridge` |
| File to exclude files from build context? | `.dockerignore` |
| Command to build an image? | `docker build -t <name>:<tag> .` |

---

## 7. Security

### Q26. What are some Docker security best practices?
- Run containers as a **non-root user** (`USER` instruction in Dockerfile).
- Use **minimal base images** (alpine, distroless) to reduce attack surface.
- Regularly scan images for vulnerabilities (`docker scout`, Trivy, Snyk).
- Avoid storing secrets in images or Dockerfiles.
- Use `--read-only` flag to make container filesystems read-only where possible.
- Keep Docker Engine and base images patched/updated.
- Limit container capabilities with `--cap-drop` and avoid `--privileged` mode unless absolutely necessary.

### Q27. Why is running a container as root risky, and how do you avoid it?
If an attacker breaks out of a container running as root, they may gain root-equivalent access on the host (especially with kernel exploits or misconfigured mounts). To avoid this, create and switch to a non-root user in the Dockerfile:
```dockerfile
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser
```

### Q28. What is Docker Content Trust?
Docker Content Trust (DCT) uses digital signatures to verify the integrity and publisher of images pulled from a registry, protecting against tampered or malicious images. It's enabled by setting `DOCKER_CONTENT_TRUST=1`.

### Q29. What is the risk of using `--privileged` mode?
`--privileged` gives a container almost all capabilities of the host machine, including direct access to host devices, effectively disabling most container isolation. It should only be used for very specific cases (e.g., running Docker-in-Docker, certain hardware access) and avoided in production unless strictly required.

---

## 8. Orchestration & Scaling Basics

### Q30. What is Docker Swarm?
Docker Swarm is Docker's native clustering and orchestration tool that turns a group of Docker hosts into a single virtual system, allowing you to deploy and scale services across multiple nodes with built-in load balancing and service discovery.

### Q31. What is the difference between Docker Compose and Docker Swarm/Kubernetes?
- **Docker Compose** – Defines and runs multi-container apps on a **single host**; great for local dev/testing.
- **Docker Swarm** – Native Docker orchestration for running containers across a **cluster of machines** with scaling and failover.
- **Kubernetes** – A more powerful, industry-standard orchestration platform for managing containerized apps at scale, with advanced scheduling, self-healing, and ecosystem support (works with Docker or other container runtimes).

### Q32. How does health checking work in Docker?
The `HEALTHCHECK` instruction in a Dockerfile (or `healthcheck` key in Compose) tells Docker how to test whether a container is still working correctly, beyond just "is the process running."
```dockerfile
HEALTHCHECK --interval=30s --timeout=5s --retries=3 \
  CMD curl -f http://localhost/ || exit 1
```
Docker reports container status as `healthy`, `unhealthy`, or `starting` based on this check, which orchestrators use to decide whether to restart or reroute traffic.

### Q33. What is service discovery in Docker?
Service discovery allows containers to find and communicate with each other without hardcoding IP addresses. On a user-defined bridge network or in Swarm, Docker's embedded DNS server resolves container/service names to their current IP addresses automatically.

---

## 9. CI/CD & Real-World Workflow

### Q34. How is Docker typically used in a CI/CD pipeline?
1. **Build** – CI pipeline builds a Docker image from the Dockerfile on every commit/PR.
2. **Test** – Run automated tests inside a container for environment consistency.
3. **Scan** – Scan the image for vulnerabilities.
4. **Push** – Push the tagged image to a registry (Docker Hub, ECR, GCR, ACR).
5. **Deploy** – Pull the image in staging/production and deploy via orchestration tools (Kubernetes, ECS, Swarm).

### Q35. What is image tagging and why does it matter?
Tagging labels an image version (e.g., `myapp:1.2.0`, `myapp:latest`). It matters because:
- `latest` is mutable and can change unexpectedly — risky for production.
- Using explicit version tags (semantic versioning or git commit SHA) ensures reproducible deployments and easy rollbacks.

### Q36. How do you version and roll back containers in production?
- Tag every build with a unique, immutable identifier (e.g., commit SHA or semver).
- Keep previous image versions available in the registry.
- To roll back, simply redeploy the previous known-good tag rather than rebuilding — this is much faster and safer.

---

## 10. Common Pitfalls & Gotchas

### Q37. Why might a container work locally but fail in production?
- Different base image or OS packages between environments (mitigated by using the exact same image across environments).
- Environment variables or secrets missing in production.
- Hardcoded `localhost` references that don't resolve correctly inside containers/orchestrated clusters.
- Resource limits (CPU/memory) in production causing OOM kills that don't occur locally.

### Q38. Why did my container exit immediately after starting?
Common causes:
- The main process (`CMD`/`ENTRYPOINT`) finished execution — containers stop when their main process exits (this is by design; a container isn't a VM).
- A missing dependency or misconfiguration causes the app to crash — check `docker logs`.
- Running an interactive shell without `-it` flags, so there's nothing keeping it alive.

### Q39. What does exit code `137` mean?
Exit code `137` typically means the container was killed by `SIGKILL` (128 + 9), most commonly due to running **out of memory** (OOM killer) or a `docker stop`/`docker kill` timeout being exceeded.

### Q40. Why shouldn't you use `latest` tag in production?
Because `latest` is just a mutable label that can point to different image content over time. Deploying `latest` doesn't guarantee reproducibility — a redeploy today could pull a completely different image than yesterday, making rollbacks and debugging unpredictable. Always pin to specific, immutable version tags in production.

---

*Tip for interviews: Be ready to explain concepts with a real example from your own projects (e.g., "In my last project, I used multi-stage builds to reduce our Node.js image from 1.2GB to 180MB").*

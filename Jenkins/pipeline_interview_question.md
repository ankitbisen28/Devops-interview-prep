Jenkins CI/CD Pipeline – Interview Q&A (Markdown)
1. What is this Jenkins pipeline used for?

Answer:
This Jenkins pipeline implements a complete CI/CD workflow. It checks out the source code, builds and tests a Java application using Maven, performs static code analysis with SonarQube, builds and pushes a Docker image to Docker Hub, and finally updates a Kubernetes deployment manifest in GitHub. This enables automated build, quality checks, containerization, and GitOps-based deployment.

2. Why are you using a Docker agent in Jenkins?

Answer:
A Docker agent ensures a consistent and isolated build environment. Instead of depending on Jenkins host tools, the pipeline runs inside a Docker container that already has Java, Maven, and Docker installed. This avoids version mismatch issues and makes the pipeline portable across environments.

3. What is the purpose of mounting /var/run/docker.sock?

Answer:
Mounting /var/run/docker.sock allows the Jenkins Docker container to communicate with the host’s Docker daemon. This enables Docker commands like docker build and docker push from inside the container. This approach is called Docker-outside-of-Docker (DooD).

4. What happens in the Build and Test stage?

Answer:
In this stage, Maven runs mvn clean package, which cleans previous builds, compiles the Java source code, runs unit tests, and packages the application into a JAR file. The generated artifact is stored in the target directory.

5. Why do we use mvn clean package instead of mvn install?

Answer:
mvn clean package is sufficient for CI pipelines because it builds and packages the application without installing the artifact into the local Maven repository. mvn install is mainly required when other projects depend on this artifact locally.

6. What is SonarQube and why is it used in this pipeline?

Answer:
SonarQube is a static code analysis tool used to measure code quality. It detects bugs, security vulnerabilities, code smells, and technical debt. In this pipeline, it ensures only high-quality code moves forward in the CI/CD process.

7. How is SonarQube authentication handled securely?

Answer:
Authentication is handled using Jenkins credentials. The SonarQube token is stored securely in Jenkins and injected into the pipeline using withCredentials, preventing sensitive information from being hardcoded in the pipeline.

8. What does the Docker build stage do?

Answer:
This stage builds a Docker image using the Dockerfile in the application directory. The image includes the packaged JAR file and is tagged with the Jenkins build number, ensuring every build has a unique version.

9. Why is ${BUILD_NUMBER} used as the Docker image tag?

Answer:
Using the Jenkins build number ensures unique and traceable image versions. It helps in rollback, debugging, and tracking which build is deployed in which environment.

10. How is the Docker image pushed to Docker Hub?

Answer:
The pipeline authenticates with Docker Hub using Jenkins-stored credentials and pushes the image to the registry. The docker.withRegistry block securely handles authentication and image push.

11. What is the purpose of updating the deployment YAML file?

Answer:
The deployment YAML file contains the container image reference. This stage updates the image tag with the latest build number so that Kubernetes deploys the new version of the application.

12. Why are you committing deployment changes back to GitHub?

Answer:
This follows a GitOps approach where Git is the single source of truth for deployments. Any change in deployment configuration is version-controlled and auditable, and tools like ArgoCD can automatically sync the changes to the Kubernetes cluster.

13. What is GitOps?

Answer:
GitOps is a deployment strategy where infrastructure and application deployments are managed through Git repositories. Any change pushed to Git automatically triggers deployment, ensuring traceability, rollback, and consistency.

14. What security best practices are followed in this pipeline?

Answer:

Secrets are stored in Jenkins Credentials

Tokens are not hardcoded

Docker images are uniquely versioned

Static code analysis is performed to detect vulnerabilities early

15. How would you improve this pipeline further?

Answer:
I would add SonarQube quality gates, Docker image vulnerability scanning, use non-root Docker users, integrate ArgoCD for automated deployment, and implement rollback strategies.
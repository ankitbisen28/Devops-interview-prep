# Top 50 Jenkins CI/CD Interview Questions and Answers

## 1. What is Jenkins?

Jenkins is an open-source automation server used to build, test, and
deploy software. It helps automate parts of the software development
lifecycle such as building code, running tests, and deploying
applications.

## 2. What is CI/CD?

CI (Continuous Integration) is the practice of automatically integrating
code changes into a shared repository.\
CD (Continuous Delivery/Deployment) automates releasing software to
production or staging environments.

## 3. What are the key features of Jenkins?

-   Easy installation and configuration
-   Large plugin ecosystem
-   Distributed builds
-   Pipeline as Code
-   Integration with many DevOps tools

## 4. What is a Jenkins Pipeline?

A Jenkins Pipeline is a suite of plugins that supports implementing
CI/CD pipelines using code stored in a Jenkinsfile.

## 5. What is a Jenkinsfile?

A Jenkinsfile is a text file stored in a repository that defines the
Jenkins pipeline using Groovy-based syntax.

## 6. What are the types of Jenkins Pipelines?

-   Declarative Pipeline
-   Scripted Pipeline

## 7. What is Declarative Pipeline?

Declarative Pipeline is a structured and opinionated syntax that
simplifies pipeline creation using predefined blocks.

## 8. What is Scripted Pipeline?

Scripted Pipeline uses Groovy scripting and provides more flexibility
but requires deeper programming knowledge.

## 9. What is Jenkins Master-Agent architecture?

Master controls scheduling and monitoring of jobs. Agents execute the
build tasks.

## 10. What are Jenkins Nodes?

Nodes are machines where Jenkins jobs run. They can be master or agent
nodes.

## 11. What is a Jenkins Job?

A job is a task or build process configured in Jenkins.

## 12. What are Jenkins Plugins?

Plugins extend Jenkins functionality such as Git integration, Docker
builds, and Kubernetes deployments.

## 13. What is Blue Ocean in Jenkins?

Blue Ocean is a modern UI for Jenkins that simplifies pipeline
visualization.

## 14. What is Jenkins Workspace?

Workspace is the directory on an agent where Jenkins builds the project.

## 15. What is SCM in Jenkins?

SCM stands for Source Code Management like Git, SVN etc., used to pull
code during builds.

## 16. How does Jenkins trigger builds?

-   SCM polling
-   Webhooks
-   Scheduled builds (CRON)
-   Manual triggers

## 17. What is Webhook in Jenkins?

A webhook allows Git repositories to notify Jenkins automatically when
new commits are pushed.

## 18. What is Jenkins Build?

A build is a single execution of a job.

## 19. What is Jenkins Stage?

Stages divide a pipeline into logical steps like Build, Test, Deploy.

## 20. What is Jenkins Step?

Steps are individual commands executed inside a stage.

## 21. What is Jenkins Agent?

An agent is a machine that performs the actual build tasks.

## 22. What is Jenkins Shared Library?

Shared Libraries allow reuse of pipeline code across multiple projects.

## 23. What is Jenkins Credential Management?

Jenkins securely stores secrets like API keys, passwords, and tokens.

## 24. What is Jenkins Multibranch Pipeline?

Automatically creates pipelines for branches in a repository.

## 25. What is Jenkins Distributed Build?

Builds run across multiple agents to improve performance.

## 26. What is Jenkins Artifact?

Artifacts are files generated during builds such as JARs or Docker
images.

## 27. What is Jenkins Parameterized Build?

Allows users to pass parameters during job execution.

## 28. What is Jenkins Build Trigger?

Defines when and how a job starts.

## 29. What is Jenkins Pipeline Stage View?

Provides visual representation of pipeline stages.

## 30. What is Jenkins Pipeline Parallel Execution?

Runs multiple stages simultaneously.

## 31. What is Jenkins Docker Agent?

Runs pipeline steps inside Docker containers.

## 32. What is Jenkins Pipeline Syntax?

Groovy-based syntax used to define pipeline logic.

## 33. What is Jenkinsfile best practice?

Store Jenkinsfile in Git repository to version control pipelines.

## 34. What is Jenkins Backup?

Backing up Jenkins home directory which contains configurations.

## 35. What is Jenkins Environment Variables?

Variables used to store configuration values inside pipelines.

## 36. What is Jenkins Build History?

Stores logs and results of previous builds.

## 37. What is Jenkins Pipeline Timeout?

Stops pipeline execution if it exceeds a defined time.

## 38. What is Jenkins Pipeline Retry?

Retries failed stages automatically.

## 39. What is Jenkins Pipeline Post Block?

Defines actions after pipeline execution like cleanup or notifications.

## 40. What is Jenkins Integration with Docker?

Jenkins can build Docker images and push them to registries.

## 41. What is Jenkins Integration with Kubernetes?

Jenkins dynamically creates build agents using Kubernetes pods.

## 42. What is Jenkins Role-Based Access Control?

Controls user permissions within Jenkins.

## 43. What is Jenkins Pipeline Library?

Reusable Groovy scripts shared across pipelines.

## 44. What is Jenkins Build Executor?

Executor is a slot for running builds on nodes.

## 45. What is Jenkins Log Rotation?

Automatically deletes old builds and logs.

## 46. What is Jenkins Email Notification?

Sends build status emails.

## 47. What is Jenkins Slack Integration?

Sends pipeline notifications to Slack channels.

## 48. What is Jenkins SonarQube Integration?

Used to perform static code analysis during pipeline execution.

## 49. What is Jenkins Deployment Pipeline?

Automates deployment to staging and production environments.

## 50. What are Jenkins Best Practices?

-   Use pipelines as code
-   Use agents for scalability
-   Secure credentials
-   Use shared libraries
-   Monitor pipelines

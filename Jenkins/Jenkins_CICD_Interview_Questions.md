# Jenkins & CI/CD Interview Questions (1–3 Years Experience)

## 1. What is CI/CD?
- Continuous Integration (CI): Frequently merge code and run automated builds/tests.
- Continuous Delivery (CD): Automatically prepare code for deployment.
- Continuous Deployment: Automatically deploy every successful change.

**Flow:**  
Developer → Git Push → Jenkins Build → Testing → Docker Build → Push Image → Deploy to Kubernetes

---

## 2. What are the benefits of CI/CD?
- Faster software delivery
- Reduced manual work
- Early bug detection
- Better code quality
- Faster rollback
- Consistent deployments

---

## 3. Why do we use Jenkins?
Jenkins is an open-source automation server used to automate:
- Build
- Testing
- Packaging
- Deployment

---

## 4. Explain Jenkins Architecture.
### Components:
1. Jenkins Controller (Master)
2. Jenkins Agents
3. Plugins
4. Jobs/Pipelines

---

## 5. Freestyle Job vs Pipeline Job

| Freestyle | Pipeline |
|------------|-----------|
| GUI based | Code based |
| Hard to maintain | Easy to maintain |
| No version control | Stored in Git |
| Less flexible | Highly flexible |

---

## 6. What is Jenkinsfile?

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }
    }
}
```

---

## 7. Declarative vs Scripted Pipeline

| Declarative | Scripted |
|-------------|-----------|
| Simple syntax | Full Groovy |
| Easier | Complex |
| Recommended | Advanced use cases |

---

## 8. Explain your CI/CD Project

1. Developer pushes code to GitHub.
2. Webhook triggers Jenkins.
3. Checkout code.
4. Build using Maven.
5. Run tests.
6. SonarQube scan.
7. Build Docker image.
8. Push image to DockerHub.
9. Deploy to Kubernetes using Helm/kubectl.
10. Verify deployment.

---

## 9. What is Jenkins Agent?
Agents are machines where Jenkins executes jobs.

Benefits:
- Parallel builds
- Load distribution
- Different environments

---

## 10. How do you connect Jenkins Agent?
- Install Java
- Generate SSH key
- Configure credentials
- Add node in Jenkins

---

## 11. Typical Pipeline Stages

```text
Checkout
Build
Test
Sonar Scan
Docker Build
Docker Push
Deploy
Post Actions
```

---

## 12. What is Blue Ocean?
Modern UI for Jenkins pipelines.

---

## 13. What are Jenkins Plugins?
Common plugins:
- Git Plugin
- Docker Plugin
- Kubernetes Plugin
- SonarQube Plugin
- Pipeline Plugin
- Credentials Plugin

---

## 14. How do you store passwords?

```groovy
withCredentials([
string(credentialsId: 'token',
variable: 'TOKEN')
])
```

---

## 15. How can Jenkins jobs be triggered?
- Manual
- Poll SCM
- Webhook
- Upstream Job
- CRON Schedule

---

## 16. What is Webhook?
Webhook automatically notifies Jenkins when code is pushed.

---

## 17. Poll SCM vs Webhook

| Poll SCM | Webhook |
|-----------|----------|
| Jenkins checks periodically | Git informs Jenkins |
| More resource usage | Efficient |
| Delayed execution | Instant trigger |

---

## 18. What is SonarQube?
Used for:
- Code quality
- Security checks
- Bugs
- Code smells

---

## 19. What is Quality Gate?
Pipeline fails if code quality standards are not met.

---

## 20. SonarQube Integration

```groovy
withSonarQubeEnv('sonar') {
    sh 'mvn sonar:sonar'
}
```

---

## 21. Docker Build in Jenkins

```bash
docker build -t app:v1 .
```

---

## 22. Docker Push

```bash
docker push image:v1
```

---

## 23. Deployment to Kubernetes
Methods:
1. kubectl apply
2. Helm
3. ArgoCD

---

## 24. Rollback Deployment

```bash
kubectl rollout undo deployment app
```

---

## 25. What is Shared Library?
Reusable pipeline code stored in Git.

---

## 26. What is Pipeline as Code?
Pipeline configuration written as code and stored in Git.

---

## 27. What is Jenkins Workspace?
Stores:
- Source code
- Artifacts
- Logs

---

## 28. What happens if Jenkins goes down?
- Restore backup
- HA setup
- Recover Jenkins Home

---

## 29. Jenkins Home Directory

```bash
/var/lib/jenkins
```

Contains:
- jobs
- plugins
- users
- secrets

---

## 30. Important Environment Variables

```text
BUILD_NUMBER
JOB_NAME
BUILD_ID
WORKSPACE
GIT_BRANCH
```

---

## 31. How to secure Jenkins?
- Authentication
- RBAC
- HTTPS
- Restrict anonymous access
- Backup
- Secure credentials

---

## 32. Continuous Delivery vs Deployment

| Delivery | Deployment |
|-----------|-------------|
| Manual approval | Fully automatic |

---

## 33. Post Actions

```groovy
post {
    success {}
    failure {}
    always {}
}
```

---

## 34. Jenkins Backup Strategy
Backup:
```bash
/var/lib/jenkins
```

Important folders:
- jobs
- plugins
- users
- secrets

---

# Production Scenarios

## Build Failure
Check:
1. Console output
2. Git checkout
3. Dependencies
4. Tests
5. Jenkinsfile

---

## Docker Push Failure
Check:
- Docker login
- Credentials
- Image tag
- Repository permission

---

## Slow Pipeline
Check:
- CPU
- Memory
- Disk usage
- Executors
- Plugin issues

---

## Sonar Failure
Check:
- Sonar server status
- Token expiry
- Network issue
- Wrong URL

---

## Deployment Successful But App Not Accessible

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
kubectl logs
kubectl describe pod
```

---

# Most Frequently Asked Questions

1. Explain your CI/CD project.
2. What happens after git push?
3. Difference between CI and CD.
4. Declarative vs Scripted Pipeline.
5. Webhook vs Poll SCM.
6. Jenkins Architecture.
7. SonarQube integration.
8. Kubernetes deployment.
9. Security in Jenkins.
10. Production issue you solved.

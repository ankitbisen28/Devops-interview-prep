# Jenkins: Most Common Day-to-Day Tasks for a DevOps Engineer (with Real-World Examples)

## 1. Monitor Failed Builds

**Task:** Check failed pipelines, identify failed stages, review console
logs, notify developers, and fix pipeline issues.

**Example:** A Java build fails due to a compilation error. Review the
console output, notify the developer, rerun the pipeline after the fix.

## 2. Create New Jenkins Pipelines

-   Connect Git repository
-   Configure webhooks
-   Create a `Jenkinsfile`
-   Add build, test, scan, and deployment stages

**Example Flow**

``` text
GitHub
  ↓
Checkout
  ↓
Build
  ↓
SonarQube
  ↓
Docker Build
  ↓
Push to ECR
  ↓
Deploy to Kubernetes
```

## 3. Update Existing Pipelines

Common updates: - Add Unit Tests - SonarQube Quality Gates - Trivy Image
Scans - Slack Notifications

## 4. Fix Jenkins Build Errors

Typical issues: - Dependency download failures - Permission denied -
Docker daemon stopped - Disk full - Git authentication failures

## 5. Manage Jenkins Agents

Daily checks: - Online/Offline status - Executor availability - Disk
usage - SSH connectivity

## 6. Review Console Logs

Analyze logs to identify: - Build failures - Test failures - Deployment
errors - SonarQube connectivity issues

## 7. Retry Failed Builds

Retry builds for transient issues such as: - Network timeouts - Docker
Hub rate limits - Temporary GitHub outages

## 8. Manage Jenkins Credentials

Maintain: - GitHub Tokens - AWS Credentials - Docker Hub Credentials -
SSH Keys - Kubernetes Configs

## 9. Install & Update Plugins

Common plugins: - Git - Pipeline - Docker - Kubernetes - AWS - Blue
Ocean

## 10. Configure Multibranch Pipelines

Automatically build: - main - develop - feature branches

## 11. Configure Git Webhooks

Automatically trigger builds whenever code is pushed.

## 12. Build Docker Images

``` bash
docker build -t myapp:v1 .
```

## 13. Push Docker Images

Push images to: - Docker Hub - Amazon ECR - Azure ACR - Google Artifact
Registry

## 14. Deploy to Kubernetes

Deploy using: - kubectl - Helm

## 15. Rollback Failed Deployments

``` bash
kubectl rollout undo deployment app
```

## 16. Configure Environment Variables

Examples: - JAVA_HOME - MAVEN_HOME - AWS_REGION - SONAR_URL

## 17. Configure Build Parameters

Allow deployment to: - DEV - QA - UAT - PROD

## 18. Clean Old Builds

Remove: - Old workspaces - Logs - Artifacts

## 19. Archive Build Artifacts

Archive: - JAR - WAR - ZIP - Test Reports

## 20. Publish Test Reports

Examples: - JUnit - JaCoCo - HTML Reports

## 21. Configure Notifications

Notify via: - Slack - Email - Microsoft Teams

## 22. Integrate SonarQube

Pipeline:

``` text
Build
 ↓
Sonar Scan
 ↓
Quality Gate
 ↓
Deploy
```

## 23. Scan Docker Images

Common scanners: - Trivy - Grype - Anchore

## 24. Backup Jenkins

Backup: - Jobs - Plugins - Credentials - Jenkins Home

## 25. Upgrade Jenkins

Typical process: 1. Backup 2. Upgrade Jenkins 3. Upgrade Plugins 4.
Restart 5. Validate Pipelines

## 26. Manage User Access

Configure RBAC for: - Admins - Developers - Read-only users

## 27. Schedule Automated Jobs

Examples: - Nightly backups - Weekly security scans - Monthly cleanup

Cron:

``` text
H 2 * * *
```

## 28. Debug Jenkinsfiles

Common errors: - Missing braces - Invalid syntax - Missing variables

## 29. Optimize Pipeline Performance

Improve build time using: - Parallel stages - Dependency caching -
Docker layer caching

## 30. Monitor Jenkins Health

Daily checklist: - CPU - Memory - Disk - Queue length - Executors -
Agent status

------------------------------------------------------------------------

# Real-World CI/CD Pipeline

``` text
Developer
    │
    ▼
Push Code to GitHub
    │
    ▼
GitHub Webhook
    │
    ▼
Jenkins
    ├── Checkout
    ├── Build
    ├── Unit Tests
    ├── SonarQube Scan
    ├── Quality Gate
    ├── Docker Build
    ├── Trivy Scan
    ├── Push to ECR
    ├── Deploy to Kubernetes
    └── Slack Notification
```

# Common Production Issues

  Issue                          Resolution
  ------------------------------ ---------------------------------
  Git checkout failed            Update credentials
  Maven build failed             Fix compilation/dependencies
  Docker build failed            Restart Docker / fix Dockerfile
  SonarQube failed               Fix quality issues
  Agent offline                  Restore connectivity
  Kubernetes deployment failed   Verify manifests/image tags
  Disk full                      Clean workspaces
  Queue stuck                    Add executors/agents
  Credentials expired            Update secrets
  Plugin incompatibility         Upgrade compatible versions

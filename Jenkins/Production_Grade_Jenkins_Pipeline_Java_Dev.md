# Production-Grade Jenkins Pipeline for Java Application (Dev Branch)

## CI/CD Flow

``` text
Developer
    │
    ▼
Git Push (dev branch)
    ▼
Jenkins Webhook
    ▼
Checkout → Compile → Unit Test → Package
    ▼
SonarQube Analysis → Quality Gate
    ▼
OWASP Dependency Scan
    ▼
Build Docker Image → Trivy Scan
    ▼
Push Image to Registry
    ▼
Deploy to Kubernetes (Dev)
    ▼
Verify Rollout
    ▼
Smoke Test
    ▼
Notification
```

## Sample Jenkinsfile

``` groovy
pipeline {
    agent { label 'docker-agent' }

    options {
        timestamps()
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '20', artifactNumToKeepStr: '10'))
        timeout(time: 45, unit: 'MINUTES')
    }

    environment {
        APP_NAME = "java-demo"
        DOCKER_IMAGE = "dockerhubusername/java-demo"
        IMAGE_TAG = "${BUILD_NUMBER}"
        REGISTRY_CREDENTIALS = "dockerhub-creds"
        SONARQUBE = "SonarQube"
        KUBECONFIG = credentials('kubeconfig')
    }

    triggers {
        githubPush()
    }

    stages {

        stage('Checkout') {
            steps { checkout scm }
        }

        stage('Verify Branch') {
            steps {
                script {
                    if (env.BRANCH_NAME != "dev") {
                        error("This pipeline only runs on dev branch")
                    }
                }
            }
        }

        stage('Clean Workspace') {
            steps { sh 'mvn clean' }
        }

        stage('Compile') {
            steps { sh 'mvn compile' }
        }

        stage('Unit Test') {
            steps { sh 'mvn test' }
            post {
                always {
                    junit '**/target/surefire-reports/*.xml'
                }
            }
        }

        stage('Package') {
            steps { sh 'mvn package -DskipTests' }
        }

        stage('Code Quality Analysis') {
            steps {
                withSonarQubeEnv("${SONARQUBE}") {
                    sh '''
                    mvn sonar:sonar \
                    -Dsonar.projectKey=java-demo \
                    -Dsonar.projectName=java-demo
                    '''
                }
            }
        }

        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage('OWASP Dependency Scan') {
            steps {
                dependencyCheck additionalArguments: '--scan .',
                odcInstallation: 'OWASP'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:${IMAGE_TAG} ."
            }
        }

        stage('Scan Docker Image') {
            steps {
                sh "trivy image --exit-code 1 --severity HIGH,CRITICAL ${DOCKER_IMAGE}:${IMAGE_TAG}"
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', REGISTRY_CREDENTIALS) {
                        sh '''
                        docker push ${DOCKER_IMAGE}:${IMAGE_TAG}
                        docker tag ${DOCKER_IMAGE}:${IMAGE_TAG} ${DOCKER_IMAGE}:latest
                        docker push ${DOCKER_IMAGE}:latest
                        '''
                    }
                }
            }
        }

        stage('Deploy to Dev Kubernetes') {
            steps {
                sh '''
                kubectl apply -f k8s/
                kubectl set image deployment/java-demo \
                java-demo=${DOCKER_IMAGE}:${IMAGE_TAG}
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh 'kubectl rollout status deployment/java-demo'
            }
        }

        stage('Smoke Test') {
            steps {
                sh 'curl http://dev.example.com/actuator/health'
            }
        }
    }

    post {
        success { echo 'Deployment Successful' }
        failure { echo 'Pipeline Failed' }
        always { cleanWs() }
    }
}
```

## Stage Explanation

1.  **Checkout** -- Fetch latest source code.
2.  **Verify Branch** -- Ensures only the `dev` branch is deployed.
3.  **Clean Workspace** -- Removes previous build artifacts.
4.  **Compile** -- Validates Java compilation.
5.  **Unit Test** -- Executes JUnit tests and publishes reports.
6.  **Package** -- Generates deployable JAR.
7.  **SonarQube Analysis** -- Performs static code analysis.
8.  **Quality Gate** -- Stops pipeline if quality thresholds fail.
9.  **OWASP Dependency Scan** -- Detects vulnerable dependencies.
10. **Build Docker Image** -- Creates container image.
11. **Trivy Scan** -- Scans image for HIGH/CRITICAL vulnerabilities.
12. **Push Docker Image** -- Publishes image to registry.
13. **Deploy to Kubernetes** -- Performs rolling update in Dev.
14. **Verify Deployment** -- Waits for rollout completion.
15. **Smoke Test** -- Confirms application health.

## Production Best Practices

-   Store secrets in Jenkins Credentials.
-   Use immutable Docker image tags.
-   Enforce SonarQube Quality Gates.
-   Scan dependencies and images for vulnerabilities.
-   Archive test reports and artifacts.
-   Configure build retention and timeouts.
-   Use rolling deployments with readiness/liveness probes.
-   Send Slack/Teams/Email notifications after each pipeline run.

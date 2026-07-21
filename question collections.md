A production application is down. What will you do?
A pod is restarting continuously.
Users cannot access the application.
One node becomes NotReady.
CPU usage suddenly spikes.
Disk is full.
SSL certificate expired.
Deployment failed.
Namespace deleted accidentally.
Database connection failed.
Service is not reachable.

What happens when you run kubectl apply -f deployment.yaml?
What is the difference between a Pod and a Deployment?
What is the difference between a ClusterIP, NodePort, and LoadBalancer Service?
How does a Service discover Pods?
How do you troubleshoot a Pod stuck in CrashLoopBackOff?
What is the purpose of kubelet?
What is the role of etcd in Kubernetes?
What is a ConfigMap and when would you use a Secret instead?
How does a rolling update work, and how can you roll back a failed deployment?
Walk me through a production incident where an application became unavailable and explain how you diagnosed and resolved it.

Candidate Experience: "Can you please go ahead about your experience?" (0:17)
Day-to-day Responsibilities: "What are the day-to-day activities like?" (2:33)
Troubleshooting: "See uh my pod is running okay but application not accessible, okay what exact steps you will follow?" (3:28)
HPA Issues: "I have enabled my HPA... but HPA not scaling. Now what are the first three checks you will do?" (4:32)
Traffic Flow: "How traffic flows from internet to pod?" (5:19)
Kubernetes Architecture: "What is the different between like deployment versus stateful set?" (6:12)
Terraform State Management: "How do you manage terraform state in team environment?" (7:05)
Terraform Plan Analysis: "If terraform plan show like unexpected changes like what do you do on the...?" (8:18)
Multi-environment Strategy: "How do you organize like terraform code for multiple environments?" (9:48)
Terraform/AWS Setup: "I have to do the setup of the terraform... and it should connect with the AWS... what you do and the things you have to concentrate before?" (11:08)
Networking: "What is the difference between net gateway and internet gateway?" (12:51)
Cost Optimization: "My AWS cost... was like $10,000 it was suddenly increased to $15,000... how you investigate this one?" (14:27)
Migration Scenarios: "We have to do the migration like AWS to AWS... How you will do like what are the configuration before you will do and after that how will you achieve this one?" (16:13)
AMI Migration: "It will be uh if you want to move the uh images directly like AMI images directly to the another account?" (19:03)
S3 Bucket Constraints: "See if S3 bucket also I need same name... Is it possible?" (19:15)
Branching Strategy: "While they're merging their code into the dev branch, they are getting conflicts. As a development engineer, what will you suggest?" (20:11)
Database Migration: "What would be the command you will use to take the dump?" (21:38)
Version Control Cleanup: "See if my developer push wrong commit into the main branch... How will you fix that?" (22:24)
Deployment Strategy: "How do you achieve zero downtime deployment?" (23:13)
Blue-Green Deployment Details: "Can you explain me about blue-green how it will be possible?" (23:24)
Target Group Logic: "Why we are why we have to change the load balancer target groups?" (24:32)
Project Planning: "How much time it will take to write the code and how much time it will take to complete this task?" 


1. A Pod is in CrashLoopBackOff. Explain your troubleshooting steps.
2. All Pods are Running, but the application is inaccessible. Where do you start?
3. One replica receives traffic while another does not. How do you debug it?
4. Explain Liveness, Readiness, and Startup Probes with real production examples.
5. A node becomes NotReady. What happens to the Pods?
6. A Pod is OOMKilled repeatedly. How would you investigate? Is increasing memory
always correct?
7. Explain the complete request flow: User -> Ingress -> Service -> Pod.
8. One Deployment has 3 replicas. One Pod crashes. What happens behind the scenes?
9. When would you use Deployment vs StatefulSet vs DaemonSet? Give production use
cases.
10. Which kubectl commands do you use first during production troubleshooting, and
why?
11. A rollout failed after deployment. How would you roll back safely?
12. ImagePullBackOff occurs in production. List all possible reasons.
13. How do Requests and Limits affect scheduling and runtime?
14. How would you debug a DNS issue inside a cluster?
15. How do you troubleshoot a Service that has no endpoints?

# Git 
• Which tool do you use for version control?
• Explain git pull vs git fetch.
• How do you clone a Git repository?
• How do you configure a remote repository locally?
• What is a .gitignore file, why use it, and how does it work?
• How do you revert changes? What's the command?
• What are the stages involved in pushing code to remote (working dir → staging → commit →
push)?
• How do you check the diff between files?
• How do you check the status/tracking of files?
• What is git merge vs git rebase — which one rewrites history?
• What is the use of 'origin' in Git?
• What is your team's branching and merging strategy?
• How do you sync a branch that is several commits behind another?
• Which branch does a user check code into, and how does code flow to production (given no direct
push to prod)?

# AWS 
• What is EC2, and what are the types of EC2 instances?
• What is a VPC, and what is a subnet?
• Why do we create subnets (public vs private, external access)?
• How do you define/derive CIDR ranges for a VPC?
• Difference between IAM role and IAM user?
• Difference between Security Groups and NACLs?
• What is Route 53, and how do you create a record in it?
• Are you aware of DNS fundamentals?
• What is AWS Lambda?
• What is an AMI (Amazon Machine Image)?
• How do you enable communication between overlapping VPCs?
• Steps to build a highly available web app using EC2 + ALB + Auto Scaling.
• How do you verify AWS is correctly routing traffic to an ALB?
• What is the use of an Ingress controller?
• How does a multi-AZ architecture behave if one AZ goes down?
• Can you provide internet access to a private subnet without a NAT Gateway?
• What is VPC peering?

Storage, Cost & Other Services
• What is DynamoDB, and what work have you done on it?
• Differences between EBS, EFS, and S3 — can all be mounted to EC2?
• S3 lifecycle policies and storage classes (Glacier, Infrequent Access)?
• Cost-optimization strategies (e.g., Auto Scaling to cut usage in off-hours)?
• Do you have cost-optimization experience specifically after moving from GCP?
• How do you filter resources in the cloud console/CLI?
• Do you have experience with architecture design — e.g., design a basic microservices/AWS
architecture for an app like Tinder or a payments app?
• Have you worked with machine learning / AI / data science / Databricks / Snowflake?

# 4. Terraform / Infrastructure as Code
Core Concepts
• Which IaC tools have you used (Terraform, CloudFormation, etc.)?
• How do you provision resources on AWS with Terraform — basic file structure and commands?
• Syntax to create an EC2 instance in Terraform.
• How do you fetch/reference an AMI ID?
• How do you declare and use variables in Terraform?
• What are Terraform modules, and how do you reuse them? How do you call a module from
another path/source?
• What is the Terraform state file, and how do you secure it? Why does it need securing?
• Where is the Terraform state file stored, and where is the state lock stored?
• What steps do you take to unlock a locked Terraform state?
• What is a Terraform provisioner?
• What is terraform taint, and when do you use it?
• What are dynamic blocks, and when do you use them?
• What does terraform refresh do? What is terraform fmt and why does it matter?
• Have you used lifecycle rules? How do you protect critical resources from accidental destroy?
• What is the purpose of Terraform workspaces, and how do you manage dev/qa/stage/prod with
them?
• How do you detect and resolve configuration drift (manual console changes)?

# Scenario-Based
• You already have EC2/VPC/Security Groups created manually — how do you bring them under
Terraform management (import)?
• Multiple engineers work on the same Terraform codebase — how do you manage state safely
(remote backend + locking)?
• Someone ran terraform apply directly in production by mistake — how do you prevent this?
• terraform apply is deploying 20 VMs and gets terminated mid-run due to a connection issue. What
happens on rerun — does it redeploy everything, error on a locked state, or resume from where it
left off?
• Does terraform apply continuing after a failure require terraform taint, or does it work without it?

terraform apply fails partway through — what is the impact, and how do you recover?
• How do you manage secrets in Terraform without hardcoding them?
• How does Terraform decide the order in which resources are created (dependency graph)?
• Difference between count and for_each?
• When do you use merge, concat, and toset?
• How do you pass subnet IDs (for RDS/EC2/EKS/LB) without hardcoding them, especially per
environment?
• After applying Terraform code for a VPC (subnets, IGW, NAT, endpoints), does AWS create anything
automatically that you didn't explicitly define?
• You deployed 20 VMs and need to delete only the compute (VM + root disk) while preserving other
attached data disks — how?
• How do you launch two servers in two different regions?
• What are the prerequisites to pass in Terraform code to create RDS, EKS, ECS, and EC2?
• How do you pass sensitive information into Terraform without hardcoding it?
• In a 4-environment setup (dev/qa/stage/prod), how do you confirm a change actually reflects in
the dev environment specifically (terraform plan targeting)?
• You need EC2 to launch before RDS — how do you express that dependency in Terraform
(depends_on)?

5. Docker
Fundamentals & Troubleshooting
• Difference between a Docker image and a container?
• Common issues faced when deploying an image in Docker?
• What is the Docker daemon?
• What is a Docker volume, and what kind of data is stored there?
• In what format is container data stored?
• Difference between CMD and ENTRYPOINT in a Dockerfile?
• Commonly used Docker commands (list ~5).
• What are layers in a Docker image, and how are they created during build?
• Difference between the default bridge network and host network — how do containers
communicate in each?
• What is docker.sock, and what is it used for?
• What is Docker Compose?
• How do you create a Dockerfile, and what's the command to run an image in detached mode with
port mapping?

6. Kubernetes (EKS)
Core Concepts
• What is a pod, and what is its life cycle?
• What are labels and selectors?
• What are resource requests/limits (CPU, memory)?
• What are Kubernetes Services, and what are the types (ClusterIP, NodePort, LoadBalancer)?
• Difference between DaemonSet and Deployment? Alternatives if you need 2 pods per node instead
of 1?
• What is RBAC (Role-Based Access Control), and how do you implement it?
• What is CNI (Container Network Interface) — examples?
• What is a StorageClass, and how do PV/PVC work together?
• Explain Kubernetes architecture — control plane vs data plane.
• How does the Kubernetes scheduler decide pod placement?
• How does kube-proxy relate to a Service?
• How do pods in different namespaces communicate via DNS?
• Difference between LoadBalancer and Ingress?
• Where do you store sensitive vs non-sensitive config (Secrets vs ConfigMaps)?
• How do you handle autoscaling in Kubernetes?
• What is a ReplicaSet?
• How do you handle certificate rotation in a cluster?


Troubleshooting & Operations
• How do you resolve a CrashLoopBackOff error?
• Replica count is set to 3 but only 1 pod is running — how do you troubleshoot?
• How do you troubleshoot a 502 error when hitting an API through the cluster?
• A ConfigMap update isn't reflecting in the running pod — why, and how do you fix it?
• Difference between a liveness probe and a readiness probe?
• How do you handle a node going down in the cluster?
• How do you ensure a front-end app only starts after the back-end is up (init containers / readiness
gates)?
• How do you plan for High Availability / zero downtime?
• Explain Helm chart structure. Have you written Helm charts?
• Do you use kubectl describe or kubectl logs first when troubleshooting — and why?
• If an app fails to start inside a pod, do logs still print to the terminal?
• How do you persist logs generated inside a pod so they survive container restarts?
• If a Docker container / pod is in a crash loop, what steps do you take to identify the root cause?
• How do you determine if an issue is application-level vs a Kubernetes configuration issue?
• How would you design centralized logging for a multi-cluster setup?
• How do you debug pod issues related to CPU/memory limits?
• How do you handle rollbacks in your project?
7. CI/CD — Jenkins & ArgoCD
Pipeline Design
• Explain your CI/CD pipeline end-to-end, including architecture.
• What is the sequence / call flow of your CI/CD pipeline?
• What is Jenkins, and what types of projects/jobs can you configure (freestyle, pipeline,
multibranch)?
• What is a multibranch pipeline?
• How do you write a Jenkinsfile? Basic Groovy syntax for build/test/deploy stages?
• How do you create a dependency between one Jenkins stage/job and another (ensure job A
completes before job B)?
• How do you integrate Jenkins with Git/GitHub?
• How do you trigger a build automatically once a branch is merged to master?
• How do you configure a pipeline to trigger based on a comment in a Merge Request?
• How do you use webhooks for automatic pipeline triggers?
• What are Jenkins shared libraries, and why use them?
• How does SonarQube notify Jenkins if a quality gate fails?
• What is your tagging and rollback strategy for deployments?
• How do you implement ArgoCD and integrate it with Jenkins?
• Have you created Helm charts and configured ArgoCD?
• Describe the environment flow: Dev → Staging/Test → Production, and how code reaches each
without direct prod pushes.
Scenario / Logic Tasks
• Write pipeline logic that skips a build if only documentation files changed.
• Write pipeline logic that fails the build if the commit message doesn't contain a Jira ticket ID.
• CI pipeline passes but the production deployment fails — how do you approach and resolve it?
• How do you debug a failed Maven build stage?
• What is your process to trigger a build once a branch is merged into master?
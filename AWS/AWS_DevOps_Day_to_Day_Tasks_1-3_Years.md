# AWS DevOps Engineer - Day-to-Day Tasks (1--3 Years Experience)

## 1. Provision AWS Infrastructure

-   Launch EC2 instances
-   Create VPCs and subnets
-   Configure Route Tables
-   Configure Internet Gateway and NAT Gateway
-   Create Security Groups
-   Allocate Elastic IPs
-   Configure Network ACLs
-   Attach IAM Roles

**AWS Services:** EC2, VPC, IAM, Elastic IP, NAT Gateway

------------------------------------------------------------------------

## 2. Infrastructure as Code (Terraform)

Daily tasks: - Write Terraform code - Create reusable Terraform
modules - Run:

``` bash
terraform init
terraform validate
terraform plan
terraform apply
terraform destroy
```

-   Store Terraform state in S3
-   Configure DynamoDB state locking
-   Review Terraform plans

------------------------------------------------------------------------

## 3. CI/CD Pipeline Management

-   Create and maintain Jenkins pipelines
-   Update Jenkinsfile
-   Fix failed builds
-   Configure build agents
-   Trigger builds
-   Monitor pipeline execution
-   Configure webhooks
-   Manage credentials

Typical stages:

``` text
Checkout → Build → Test → SonarQube → Docker Build → Push Image → Deploy → Notification
```

------------------------------------------------------------------------

## 4. Docker

-   Build Docker images
-   Run containers
-   Push images to Amazon ECR
-   Clean unused images
-   Troubleshoot Docker issues
-   Update Dockerfiles

------------------------------------------------------------------------

## 5. Amazon ECR

-   Create repositories
-   Push Docker images
-   Configure lifecycle policies
-   Manage permissions
-   Delete old images

------------------------------------------------------------------------

## 6. Amazon EKS / Kubernetes

-   Deploy applications
-   Check pods and services
-   Restart deployments
-   Scale deployments
-   Debug failed pods
-   View logs
-   Manage ConfigMaps and Secrets

Useful commands:

``` bash
kubectl get pods
kubectl get svc
kubectl apply -f
kubectl rollout restart deployment/<name>
```

------------------------------------------------------------------------

## 7. Helm

-   Install Helm charts
-   Upgrade applications
-   Rollback deployments
-   Update values.yaml

------------------------------------------------------------------------

## 8. IAM

-   Create users and roles
-   Attach policies
-   Configure AssumeRole
-   Rotate access keys
-   Review permissions

------------------------------------------------------------------------

## 9. Amazon S3

-   Create buckets
-   Upload artifacts
-   Enable versioning
-   Configure lifecycle policies
-   Enable encryption

------------------------------------------------------------------------

## 10. Monitoring (CloudWatch)

-   Check dashboards
-   Review alarms
-   Monitor CPU/Memory
-   Investigate application logs
-   Create dashboards

------------------------------------------------------------------------

## 11. CloudWatch Logs

-   Search logs
-   Debug failures
-   Configure log retention
-   Create metric filters

------------------------------------------------------------------------

## 12. Auto Scaling

-   Configure Auto Scaling Groups
-   Update Launch Templates
-   Review scaling events

------------------------------------------------------------------------

## 13. Load Balancer

-   Configure ALB
-   Manage Target Groups
-   Health check troubleshooting
-   Attach SSL certificates

------------------------------------------------------------------------

## 14. Route 53

-   Manage Hosted Zones
-   Create DNS records
-   Verify DNS propagation

------------------------------------------------------------------------

## 15. SSL Certificate Management

-   Request ACM certificates
-   Validate certificates
-   Renew certificates
-   Attach certificates to ALB

------------------------------------------------------------------------

## 16. Secrets Manager / Parameter Store

-   Store secrets
-   Rotate credentials
-   Retrieve secrets securely

------------------------------------------------------------------------

## 17. Linux Administration

-   SSH into EC2
-   Restart services
-   Check logs
-   Manage users
-   Clean disk space

Useful commands:

``` bash
ssh
systemctl status
systemctl restart
journalctl
```

------------------------------------------------------------------------

## 18. Git & GitHub

``` bash
git clone
git pull
git add
git commit
git push
git checkout
git merge
```

-   Resolve merge conflicts
-   Review Pull Requests

------------------------------------------------------------------------

## 19. Ansible

-   Run playbooks
-   Update inventory
-   Create roles
-   Install packages
-   Patch servers

------------------------------------------------------------------------

## 20. Deployment Activities

-   Deploy to Dev/QA/UAT/Production
-   Rollback if needed
-   Verify deployment

------------------------------------------------------------------------

## 21. Troubleshooting

Common issues: - Jenkins pipeline failures - Docker build failures -
CrashLoopBackOff - ImagePullBackOff - EC2 SSH issues - IAM permission
errors - Terraform apply failures - ALB health check failures

------------------------------------------------------------------------

## 22. Log Analysis

Useful commands:

``` bash
tail -f
cat
less
grep
find
```

------------------------------------------------------------------------

## 23. Backup & Recovery

-   Create EBS snapshots
-   Verify backups
-   Restore snapshots
-   Validate database backups

------------------------------------------------------------------------

## 24. Cost Optimization

-   Stop unused EC2 instances
-   Delete unused EBS volumes
-   Remove unused Elastic IPs
-   Clean old snapshots
-   Review AWS Cost Explorer

------------------------------------------------------------------------

## 25. Security

-   Review Security Groups
-   Patch Linux servers
-   Review IAM policies
-   Enable MFA
-   Rotate secrets
-   Enable encryption

------------------------------------------------------------------------

## 26. Documentation

-   Update SOPs
-   Deployment guides
-   Architecture diagrams
-   Incident reports
-   RCA documents

------------------------------------------------------------------------

## 27. Team Collaboration

-   Daily stand-ups
-   Coordinate releases
-   Review PRs
-   Support developers and QA

------------------------------------------------------------------------

## 28. Incident Handling

-   Investigate alerts
-   Restore services
-   Rollback deployments
-   Prepare RCA

------------------------------------------------------------------------

## 29. Common AWS CLI Commands

``` bash
aws configure
aws ec2 describe-instances
aws s3 ls
aws s3 cp
aws iam list-users
aws eks update-kubeconfig
aws ecr get-login-password
aws sts get-caller-identity
```

------------------------------------------------------------------------

## 30. Sample Daily Workflow

  Time    Activity
  ------- --------------------------
  09:30   Daily Stand-up
  10:00   Check Jenkins pipelines
  10:30   Review CloudWatch alarms
  11:00   Deploy to EKS
  12:00   Troubleshoot Kubernetes
  13:00   Lunch
  14:00   Terraform changes
  15:00   IAM & Security updates
  16:00   Git PR Reviews
  17:00   Production Deployment
  18:00   Documentation & Handover

------------------------------------------------------------------------

# Skills Expected (1--3 Years)

-   Linux
-   AWS (EC2, IAM, VPC, S3, ECR, EKS, ALB, Route53, CloudWatch)
-   Terraform
-   Docker
-   Kubernetes
-   Helm
-   Jenkins / GitHub Actions
-   Git & GitHub
-   Ansible
-   Bash Scripting
-   Networking Basics
-   Monitoring & Logging
-   Troubleshooting

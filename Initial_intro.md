## Introduction
I have around 2 years of experience as a DevOps engineer, currently working at Tata Consultancy Services for the Morgan Stanley project, where I've been building and maintaining CI/CD pipelines, automating infrastructure, and supporting cloud-native application deployments.

I have hands-on experience with tools like Jenkins for continuous integration and deployment, where I've created and optimized pipelines for different microservice applications. I've also worked with Ansible for configuration management and automation, helping provision and maintain consistent environments across systems.

In terms of infrastructure, I've been using Terraform to implement Infrastructure as Code, mainly on AWS. I've worked with services like EC2, S3, VPC, RDS, EKS, ALB, and IAM to build scalable and secure cloud environments. My focus has been on writing reusable and modular IaC code to improve efficiency and reduce manual effort.

I have also worked with Kubernetes, primarily on Amazon EKS, where I've deployed and managed containerized applications. My responsibilities included working with Kubernetes resources such as Deployments, Services, ConfigMaps, and Secrets, using kubectl for cluster management and troubleshooting pod and deployment issues to ensure reliable application availability.

I'm also familiar with core DevOps practices such as automation, monitoring, container orchestration, and improving deployment workflows. Alongside my professional work, I've been part of the TCS AI Friday mentorship program, where I gained exposure to GenAI concepts and collaborated with peers, helping me broaden my understanding of emerging technologies.

## Day to Day activity 
My day usually starts by checking the health of the production environment. I verify that Kubernetes pods, nodes, Jenkins pipelines, and monitoring dashboards are healthy and that there are no overnight production alerts. After that, I attend the daily stand-up meeting with developers, QA, and other DevOps engineers to discuss ongoing work and planned deployments.

During the day, I work on infrastructure requests using Terraform to provision or modify AWS resources such as IAM roles, EC2 instances, EKS node groups, security groups, or S3 buckets. I also monitor Jenkins CI/CD pipelines triggered by developer code commits. If a build fails because of compilation errors, test failures, or Docker issues, I troubleshoot the pipeline or coordinate with the development team.

Once the application is built, Jenkins creates a Docker image and pushes it to Amazon ECR. ArgoCD then detects the updated image from the GitOps repository and deploys it to the EKS cluster. I verify that the deployment completes successfully, all pods are healthy, services and ingress are working, and the application is accessible. Throughout the day, I also monitor CloudWatch and Grafana dashboards, respond to production alerts, troubleshoot Kubernetes issues, and document completed work. My main goal is to ensure reliable deployments, stable infrastructure, and high application availability.

## Project Introduction 
I am currently working as a DevOps Engineer in the Morgan Stanley project through TCS. Our team is responsible for supporting and maintaining the infrastructure, CI/CD pipelines, and application deployment process for internal banking applications. The project follows Agile methodology, where we work closely with developers, QA engineers, infrastructure teams, and application support teams to ensure smooth software delivery and high availability of the applications.

Our team consists of around 8 members, including a Project Manager, Scrum Master, DevOps Engineers, Software Developers, QA Engineers, and Production Support Engineers. As a DevOps Engineer, I primarily handle infrastructure automation, CI/CD implementation, container orchestration, and deployment activities. I work independently on assigned DevOps tasks while collaborating with developers and cloud teams to resolve deployment and infrastructure-related issues.

## Project Workflow 
In a production environment, we manage infrastructure using Terraform. Terraform provisions the AWS networking, IAM roles, EKS cluster, ECR repositories, load balancers, and supporting services. Developers commit code to GitHub, which triggers a Jenkins pipeline through a webhook. Jenkins checks out the code, builds the application, runs unit tests, performs static analysis with SonarQube, builds a Docker image, scans it with Trivy, and pushes the approved image to Amazon ECR. Instead of deploying directly to Kubernetes, Jenkins updates the image tag in a separate GitOps repository containing Helm charts. ArgoCD continuously monitors that repository, detects the change, and synchronizes the EKS cluster by performing a Helm upgrade. Kubernetes then performs a rolling update, creating new pods, validating readiness probes, shifting traffic gradually, and terminating old pods without downtime. The application is exposed through an Ingress backed by an AWS Application Load Balancer. Monitoring is handled with Prometheus, Grafana, and CloudWatch, while centralized logging and alerting help us identify and resolve issues quickly. This GitOps-based workflow provides automation, version control, auditability, and reliable production deployments.





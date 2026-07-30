# AWS Interview Questions (1–3 Years Experience)

A curated list of the most commonly asked AWS interview questions for candidates with 1–3 years of experience, organized by the most frequently used AWS services (EC2, S3, IAM, VPC, RDS, Lambda, CloudWatch, ELB/Auto Scaling, and general architecture).

---

## 1. EC2 (Elastic Compute Cloud)

**Q1. What is EC2 and what are the different pricing models available?**
EC2 (Elastic Compute Cloud) is a virtual server in the AWS cloud that lets you run applications without owning physical hardware. Pricing models:
- **On-Demand** – Pay per hour/second, no commitment, good for unpredictable workloads.
- **Reserved Instances** – 1 or 3-year commitment for a discount (up to ~72%), good for steady-state workloads.
- **Spot Instances** – Bid for unused capacity at up to 90% discount, can be terminated by AWS anytime; good for fault-tolerant, flexible workloads.
- **Savings Plans** – Flexible pricing model committing to consistent usage (in $/hr) for 1 or 3 years across instance families.
- **Dedicated Hosts/Instances** – Physical server dedicated to your use, often for compliance needs.

**Q2. What is the difference between a Security Group and a Network ACL?**
| Feature | Security Group | Network ACL |
|---|---|---|
| Level | Instance level | Subnet level |
| Rules | Only "Allow" rules | Both "Allow" and "Deny" rules |
| State | Stateful (return traffic auto-allowed) | Stateless (return traffic must be explicitly allowed) |
| Evaluation | All rules evaluated before decision | Rules processed in order (lowest number first) |

**Q3. How do you connect to an EC2 instance and what happens if you lose the key pair?**
You connect via SSH (Linux) using the `.pem` key file or RDP (Windows) using a decrypted password. If you lose the key pair, you cannot directly recover it. Common workaround: stop the instance, detach the root volume, attach it to another instance as a secondary volume, update the `authorized_keys` file with a new public key, then reattach it back as the root volume and start the instance.

**Q4. What are EC2 instance types and how do you choose one?**
Instance types are grouped into families based on use case:
- **General Purpose (T, M)** – Balanced compute/memory/network (web servers, small databases).
- **Compute Optimized (C)** – High-performance processors (batch processing, gaming servers).
- **Memory Optimized (R, X)** – Large memory workloads (in-memory databases, real-time big data).
- **Storage Optimized (I, D)** – High sequential read/write (data warehousing, distributed file systems).
Choice depends on workload: CPU-bound → Compute Optimized; memory-bound → Memory Optimized, etc.

**Q5. What is the difference between Stopping and Terminating an EC2 instance?**
**Stopping** shuts down the instance but retains the EBS root volume — you can start it again later, and data on EBS persists (though instance store data is lost). Billing stops for compute but EBS storage is still charged. **Terminating** permanently deletes the instance; the root EBS volume is deleted by default (unless "Delete on Termination" is disabled), and the instance cannot be recovered.

**Q6. What is an EBS volume and what types are available?**
EBS (Elastic Block Store) is persistent block-level storage attached to EC2 instances. Types:
- **gp3/gp2 (General Purpose SSD)** – Balanced price/performance for most workloads.
- **io2/io1 (Provisioned IOPS SSD)** – High-performance, low-latency for critical database workloads.
- **st1 (Throughput Optimized HDD)** – Low-cost, for frequently accessed, throughput-intensive workloads (big data, log processing).
- **sc1 (Cold HDD)** – Lowest cost, for infrequently accessed data.

**Q7. What is the difference between an Elastic IP and a Public IP?**
A **Public IP** is dynamically assigned to an instance and changes (or is released) when the instance is stopped/started or terminated. An **Elastic IP** is a static, persistent public IP address you allocate to your account that remains associated with your instance even after a stop/start, until you explicitly release it.

**Q8. How do you perform a rolling deployment/update on EC2 instances behind a Load Balancer?**
Typically done via an Auto Scaling Group with a Launch Template update: gradually replace old instances with new ones (using instance refresh) while keeping a minimum number of healthy instances in service, so the ALB continues routing traffic without downtime. Health checks ensure only healthy new instances receive traffic before old ones are terminated.

---

## 2. S3 (Simple Storage Service)

**Q9. What is S3 and what are its key features?**
S3 is an object storage service offering scalability, data availability, security, and performance. Key features: 99.999999999% (11 nines) durability, versioning, lifecycle policies, cross-region replication, encryption (SSE-S3, SSE-KMS, SSE-C), and storage classes for cost optimization.

**Q10. What are the different S3 storage classes?**
- **S3 Standard** – Frequently accessed data.
- **S3 Intelligent-Tiering** – Automatically moves data between tiers based on access patterns.
- **S3 Standard-IA (Infrequent Access)** – Lower cost, retrieval fee, for infrequently accessed data.
- **S3 One Zone-IA** – Same as IA but stored in a single AZ (cheaper, less resilient).
- **S3 Glacier Instant/Flexible/Deep Archive** – Long-term archival with varying retrieval times (milliseconds to hours) and lowest cost for Deep Archive.

**Q11. How do you secure an S3 bucket?**
- Block Public Access settings (enabled by default).
- Bucket policies and IAM policies to control access.
- Enable encryption at rest (SSE-S3/SSE-KMS).
- Enable versioning to protect against accidental deletion.
- Use S3 Access Points or pre-signed URLs for temporary controlled access.
- Enable server access logging and use CloudTrail for auditing.

**Q12. What is the difference between S3 bucket policy and IAM policy?**
A **bucket policy** is a resource-based policy attached directly to the S3 bucket, controlling access to that specific bucket from any principal (including cross-account). An **IAM policy** is an identity-based policy attached to a user/role/group defining what actions that identity can perform across AWS resources, including S3.

**Q13. What is S3 Versioning and why is it important?**
Versioning keeps multiple variants of an object in the same bucket, protecting against accidental overwrites and deletions. When enabled, a delete only adds a "delete marker" (recoverable) instead of permanently removing the object, and every overwrite creates a new version rather than replacing the old one. Once enabled, it can only be suspended, not fully disabled.

**Q14. What is the difference between S3 Cross-Region Replication (CRR) and Same-Region Replication (SRR)?**
**CRR** automatically replicates objects to a bucket in a different AWS Region — used for compliance, lower-latency access for global users, or disaster recovery. **SRR** replicates objects to a bucket within the same Region — used for log aggregation, production/test environment syncing, or maintaining copies under different accounts. Both require versioning to be enabled on source and destination buckets.

**Q15. What is a pre-signed URL in S3?**
A pre-signed URL grants temporary, time-limited access to a private S3 object without changing bucket permissions. It's generated using AWS credentials (via SDK/CLI) and is commonly used to let users upload/download specific files securely without exposing the bucket publicly.

**Q16. How does S3 achieve high durability and availability?**
S3 Standard automatically stores objects redundantly across a minimum of 3 Availability Zones within a region, providing 99.999999999% (11 nines) durability and 99.99% availability. This design protects against the loss of an entire AZ.

---

## 3. IAM (Identity and Access Management)

**Q17. What is the principle of least privilege and how do you implement it in IAM?**
It means granting only the minimum permissions required to perform a task. Implementation: create fine-grained IAM policies scoped to specific actions/resources, use IAM roles instead of long-term access keys, regularly review permissions using IAM Access Analyzer, and avoid using the root account for daily tasks.

**Q18. What is the difference between an IAM Role and an IAM User?**
An **IAM User** represents a person or application with permanent long-term credentials (username/password or access keys). An **IAM Role** is an identity with temporary credentials that can be assumed by users, applications, or AWS services (like EC2 or Lambda) — no long-term credentials are attached, making it more secure for cross-service or cross-account access.

**Q19. What is an IAM policy and what are its main components?**
A JSON document defining permissions. Main components:
- **Version** – Policy language version.
- **Statement** – One or more permission statements.
- **Effect** – Allow or Deny.
- **Action** – The API actions permitted/denied.
- **Resource** – The AWS resource(s) the policy applies to.
- **Condition** (optional) – Conditions under which the policy is in effect.

**Q20. What is IAM MFA and why is it recommended?**
MFA (Multi-Factor Authentication) requires a second verification factor (e.g., a code from a virtual/hardware MFA device) in addition to a password. It's recommended especially for the root account and privileged IAM users to protect against compromised credentials, since a stolen password alone won't grant access.

**Q21. What is the difference between an IAM Policy attached to a Group vs. directly to a User?**
Attaching a policy to a **Group** applies the permissions to all users who are members of that group, making it easier to manage permissions at scale (add/remove users from groups instead of editing individual policies). Attaching directly to a **User** applies only to that specific user — useful for exceptions but harder to manage/audit at scale. Best practice: manage permissions via groups (or roles), not individual users.

**Q22. What is cross-account access in IAM and how do you set it up?**
Cross-account access allows users/services in one AWS account to access resources in another account without creating duplicate IAM users. It's set up by creating an IAM Role in the target account with a trust policy specifying the source account (or specific IAM entity) as a trusted principal, then users in the source account assume that role using `sts:AssumeRole` to get temporary credentials.

**Q23. What is the difference between Authentication and Authorization in AWS IAM?**
**Authentication** verifies *who* you are (e.g., logging in with a username/password, access keys, or MFA). **Authorization** determines *what* you're allowed to do once authenticated (governed by IAM policies attached to your user/role defining permitted actions and resources).

---

## 4. VPC (Virtual Private Cloud)

**Q24. What is a VPC and what are its core components?**
A VPC is a logically isolated virtual network within AWS where you can launch resources. Core components: Subnets (public/private), Route Tables, Internet Gateway (IGW), NAT Gateway/Instance, Security Groups, Network ACLs, and VPC Peering/Endpoints.

**Q25. What is the difference between a public and private subnet?**
A **public subnet** has a route to an Internet Gateway, allowing resources with public IPs to communicate directly with the internet. A **private subnet** has no direct route to the internet; resources access the internet (if needed) through a NAT Gateway/Instance placed in a public subnet.

**Q26. What is a NAT Gateway and why is it needed?**
A NAT (Network Address Translation) Gateway allows instances in a private subnet to initiate outbound traffic to the internet (e.g., for updates) while preventing the internet from initiating connections to those instances, thus keeping them secure.

**Q27. What is VPC Peering and what are its limitations?**
VPC Peering connects two VPCs (same or different accounts/regions) so resources can communicate as if on the same network, using private IPs. Limitations: no transitive peering (if A-B and B-C are peered, A cannot reach C through B directly), CIDR blocks must not overlap, and each peering connection must be individually established and its routes manually configured.

**Q28. What is a VPC Endpoint and why would you use one?**
A VPC Endpoint allows private connectivity between your VPC and supported AWS services (like S3 or DynamoDB) without traversing the public internet or requiring a NAT Gateway/IGW. Two types: **Gateway Endpoints** (for S3 and DynamoDB, added to route tables, free) and **Interface Endpoints** (powered by AWS PrivateLink, for most other services, uses ENIs, incurs hourly cost).

**Q29. What is the difference between an Internet Gateway and a NAT Gateway?**
An **Internet Gateway (IGW)** enables two-way communication between resources in a VPC and the internet (used for public subnets). A **NAT Gateway** allows only one-way outbound internet access for instances in private subnets, while blocking unsolicited inbound connections initiated from the internet.

**Q30. How would you design a highly available VPC architecture?**
Deploy across at least 2 Availability Zones, with public and private subnets in each AZ. Place a NAT Gateway in each AZ's public subnet (to avoid a single point of failure), use an ALB/NLB spanning multiple AZs to distribute traffic, and use an Auto Scaling Group to launch instances across AZs in the private subnets.

---

## 5. RDS (Relational Database Service)

**Q31. What is Multi-AZ deployment in RDS and how is it different from Read Replicas?**
**Multi-AZ** creates a synchronous standby replica in a different Availability Zone purely for high availability/failover — it's not used for read scaling, and only the primary is accessible for read/write. **Read Replicas** are asynchronous copies used to scale read traffic; they can be promoted to standalone databases and can even be created in different regions.

**Q32. How does RDS handle backups?**
RDS provides automated backups (daily snapshots + transaction logs, allowing point-in-time recovery) with a configurable retention period (up to 35 days), and manual DB snapshots that persist until explicitly deleted.

**Q33. What is the difference between RDS and DynamoDB?**
**RDS** is a managed relational (SQL) database service (MySQL, PostgreSQL, MariaDB, Oracle, SQL Server, Aurora) suited for structured data with complex relationships/transactions (ACID compliance). **DynamoDB** is a fully managed NoSQL key-value/document database designed for massive scale, single-digit millisecond latency, and flexible schema — better suited for high-throughput applications without complex joins.

**Q34. What is Amazon Aurora and how is it different from standard RDS engines?**
Aurora is AWS's proprietary, cloud-native relational database engine (MySQL and PostgreSQL compatible) offering up to 5x the throughput of standard MySQL and 3x that of standard PostgreSQL. It automatically replicates data 6 ways across 3 AZs, offers storage auto-scaling up to 128TB, and supports faster failover and Aurora Serverless for variable workloads.

**Q35. How do you secure an RDS database?**
- Deploy in a private subnet (not publicly accessible).
- Use Security Groups to restrict inbound access to specific application servers.
- Enable encryption at rest (via KMS) and in transit (SSL/TLS).
- Use IAM database authentication where supported.
- Enable automated backups and Multi-AZ for resilience.
- Rotate credentials using AWS Secrets Manager.

---

## 6. Lambda & Serverless

**Q36. What is AWS Lambda and what are its limitations?**
Lambda is a serverless compute service that runs code in response to events without provisioning servers. Limitations: max execution timeout of 15 minutes, deployment package size limits (250MB unzipped with layers, 50MB zipped), memory range 128MB–10,240MB, and cold start latency for infrequently invoked functions.

**Q37. What triggers can invoke a Lambda function?**
API Gateway, S3 events (object created/deleted), DynamoDB Streams, CloudWatch Events/EventBridge (scheduled or event-based), SNS/SQS messages, Kinesis Streams, and ALB, among others.

**Q38. What is a cold start in Lambda and how can you reduce it?**
A cold start occurs when Lambda has to initialize a new execution environment (download code, start the runtime, run initialization code) before processing a request, adding latency. Ways to reduce it: use Provisioned Concurrency (keeps environments warm), reduce package size/dependencies, choose faster-starting runtimes, and keep functions "warm" using scheduled invocations for critical low-latency use cases.

**Q39. What is the difference between Lambda concurrency and throttling?**
**Concurrency** is the number of instances of your function running simultaneously. Each account has a default concurrency limit (e.g., 1000 per region). **Throttling** occurs when incoming requests exceed the available concurrency — AWS returns a `TooManyRequestsException`, and for asynchronous invocations, the event is automatically retried.

**Q40. What are Lambda Layers?**
Layers let you package and share common code, libraries, or dependencies separately from your function code, reducing deployment package size and enabling reuse across multiple Lambda functions. A function can use up to 5 layers.

---

## 7. Monitoring & Scaling

**Q41. What is the difference between CloudWatch and CloudTrail?**
**CloudWatch** monitors performance and operational health (metrics, logs, alarms, dashboards) — it tells you *what* is happening to your resources. **CloudTrail** logs API calls and user activity across your AWS account for auditing and compliance — it tells you *who did what*.

**Q42. How does Auto Scaling work with Load Balancers?**
An Auto Scaling Group (ASG) automatically adds/removes EC2 instances based on defined policies (target tracking, step scaling, or scheduled scaling) tied to CloudWatch metrics (e.g., CPU utilization). An Elastic Load Balancer (ALB/NLB) sits in front of the ASG, distributing incoming traffic evenly across all healthy instances and performing health checks to route traffic only to instances that pass.

**Q43. What is the difference between a CloudWatch Alarm and a CloudWatch Event/EventBridge rule?**
A **CloudWatch Alarm** watches a single metric over time and triggers an action (SNS notification, Auto Scaling policy, etc.) when the metric breaches a defined threshold. A **CloudWatch Event/EventBridge rule** reacts to state changes or events (e.g., an EC2 instance starting, an S3 object being created) and routes them to targets like Lambda, SNS, or SQS — it's event-driven rather than metric-threshold-driven.

**Q44. What is the difference between Scaling Policies: Target Tracking, Step Scaling, and Scheduled Scaling?**
- **Target Tracking** – Automatically adjusts capacity to keep a metric (e.g., average CPU) at a target value, similar to a thermostat.
- **Step Scaling** – Adds/removes capacity in defined steps based on the size of the alarm breach (more granular control).
- **Scheduled Scaling** – Scales capacity based on a known schedule (e.g., scale up every weekday at 9 AM for predictable traffic patterns).

---

## 8. DynamoDB

**Q45. What is DynamoDB and what are its key features?**
DynamoDB is a fully managed, serverless NoSQL key-value/document database offering single-digit millisecond performance at any scale. Key features: automatic scaling, on-demand or provisioned capacity modes, built-in encryption, global tables for multi-region replication, DynamoDB Streams for change data capture, and Point-in-Time Recovery.

**Q46. What is the difference between Partition Key and Sort Key in DynamoDB?**
The **Partition Key** (hash key) determines which physical partition an item is stored in — DynamoDB uses it to distribute data evenly. The **Sort Key** (range key) is optional and, combined with the partition key, forms a composite primary key, allowing multiple items to share the same partition key while being uniquely identified and sorted by the sort key.

**Q47. What is the difference between DynamoDB On-Demand and Provisioned capacity modes?**
**On-Demand** automatically scales to handle traffic without capacity planning — you pay per request, ideal for unpredictable workloads. **Provisioned** requires you to specify Read/Write Capacity Units (RCUs/WCUs) in advance — cheaper for predictable, steady traffic, and can use Auto Scaling to adjust within set bounds.

---

## 9. ECS / EKS / Containers

**Q48. What is the difference between ECS and EKS?**
**ECS (Elastic Container Service)** is AWS's proprietary container orchestration service, simpler to set up, tightly integrated with other AWS services. **EKS (Elastic Kubernetes Service)** is a managed Kubernetes service, better suited for teams that need Kubernetes-native tooling, portability across clouds, or already have Kubernetes expertise. ECS has lower operational overhead; EKS offers more flexibility and a larger ecosystem.

**Q49. What is the difference between Fargate and EC2 launch types in ECS?**
**Fargate** is a serverless compute engine for containers — AWS manages the underlying infrastructure, and you just define CPU/memory requirements; no server management needed. The **EC2 launch type** requires you to provision and manage the underlying EC2 instances that host your containers, giving more control (e.g., custom AMIs, instance types) but more operational overhead.

---

## 10. CloudFormation & Infrastructure as Code

**Q50. What is AWS CloudFormation and what are its benefits?**
CloudFormation lets you define AWS infrastructure as code using JSON/YAML templates, which are then deployed as a "stack." Benefits: repeatable and consistent deployments, version control for infrastructure, automatic rollback on failure, dependency management between resources, and the ability to easily replicate environments (dev/test/prod).

**Q51. What is the difference between CloudFormation and Terraform?**
**CloudFormation** is AWS-native, tightly integrated with AWS services, and free to use (you only pay for resources created). **Terraform** (by HashiCorp) is cloud-agnostic, supporting multi-cloud deployments (AWS, Azure, GCP, etc.) with a large community module ecosystem, using its own HCL syntax. Terraform is often preferred for multi-cloud strategies; CloudFormation for AWS-only shops wanting native support.

---

## 11. Route 53 & Networking Extras

**Q52. What is Route 53 and what routing policies does it support?**
Route 53 is AWS's scalable DNS and domain registration service. Routing policies:
- **Simple** – Single resource, no health checks.
- **Weighted** – Distribute traffic across resources based on assigned weights (e.g., A/B testing).
- **Latency-based** – Routes to the region with lowest latency for the user.
- **Failover** – Routes to a healthy primary resource; fails over to secondary if primary is unhealthy.
- **Geolocation** – Routes based on the user's geographic location.
- **Multi-value answer** – Returns multiple healthy records, providing simple load balancing.

**Q53. What is the difference between an Application Load Balancer (ALB) and a Network Load Balancer (NLB)?**
**ALB** operates at Layer 7 (HTTP/HTTPS), supports content-based routing (path/host-based), and is ideal for web applications and microservices. **NLB** operates at Layer 4 (TCP/UDP), handles millions of requests with ultra-low latency, and is ideal for extreme performance needs or when a static IP is required.

---

## 12. Scenario-Based Questions

**Q54. Your application on EC2 is experiencing high latency during peak hours. How would you troubleshoot and fix it?**
1. Check CloudWatch metrics (CPU, memory via custom metrics, network) to identify the bottleneck.
2. Check if the instance type is undersized — consider vertical scaling.
3. Verify if an Auto Scaling Group is configured; if not, set one up with a Load Balancer for horizontal scaling.
4. Check database performance (RDS) — consider read replicas or caching (ElastiCache) to reduce load.
5. Enable enhanced monitoring/X-Ray tracing to pinpoint application-level bottlenecks.

**Q55. How would you design a cost-effective and highly available 3-tier web application on AWS?**
- **Web tier:** ALB + Auto Scaling Group of EC2 instances (or ECS/Fargate) across multiple AZs in public subnets.
- **App tier:** EC2/ECS instances in private subnets, scaled independently, communicating with the web tier.
- **Database tier:** RDS Multi-AZ (or Aurora) in private subnets with Read Replicas for scaling reads.
- Use S3 + CloudFront for static assets, ElastiCache for caching frequent queries, and Route 53 for DNS with health checks.
- Use Reserved Instances/Savings Plans for baseline load and Spot Instances for non-critical batch workloads to optimize cost.

**Q56. How would you migrate an on-premises database to AWS with minimal downtime?**
Use **AWS Database Migration Service (DMS)** with **Schema Conversion Tool (SCT)** if changing engines. Set up continuous data replication (CDC - Change Data Capture) from the source to the target RDS instance while the source stays live, validate data consistency, then perform a final cutover during a short maintenance window by switching the application's connection endpoint.

---

## Most Commonly Used AWS Services (by real-world usage & interview frequency)

| Rank | Service | Category |
|---|---|---|
| 1 | **EC2** | Compute |
| 2 | **S3** | Storage |
| 3 | **IAM** | Security/Identity |
| 4 | **VPC** | Networking |
| 5 | **RDS** | Database |
| 6 | **Lambda** | Serverless Compute |
| 7 | **CloudWatch** | Monitoring |
| 8 | **CloudFormation** | Infrastructure as Code |
| 9 | **Route 53** | DNS |
| 10 | **DynamoDB** | NoSQL Database |

> **Tip for 1–3 YOE interviews:** Interviewers usually focus heavily on **EC2, S3, IAM, and VPC** since these form the backbone of almost every AWS architecture. Be ready to explain concepts with real examples from your own project experience (e.g., "In my last project, I used an ASG with an ALB to handle traffic spikes...").

---

*Generated for interview preparation — review AWS official documentation for the latest service updates.*

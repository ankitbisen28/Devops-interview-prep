# AWS Scenario-Based Interview Questions and Answers (1–5 Years Experience)

## 1. EC2 Instance Suddenly Becomes Unreachable
### Scenario
A production application hosted on EC2 suddenly becomes inaccessible.

### Answer
- Check EC2 status checks (System and Instance status).
- Verify Security Groups (22, 80, 443).
- Check Network ACLs and Route Tables.
- SSH into the server and verify application services.
- Check disk utilization using `df -h`.

**Interview Answer:**  
"I would first verify infrastructure health checks, networking, security groups, application status, and logs to identify whether the issue is infrastructure or application related."

---

## 2. Website is Slow During Peak Hours
### Scenario
Users report application slowness during evening traffic.

### Answer
- Analyze CloudWatch metrics:
  - CPU Utilization
  - Memory
  - Network metrics
- Check database performance.
- Configure Auto Scaling and Load Balancer.

**Interview Answer:**  
"I would investigate CloudWatch metrics and implement Auto Scaling policies to handle traffic spikes."

---

## 3. RDS Database Connection Failure
### Scenario
Application cannot connect to Amazon RDS.

### Answer
- Verify RDS status.
- Check security groups for port 3306.
- Verify endpoint and credentials.
- Test connectivity using:

```bash
nc -zv <rds-endpoint> 3306
```

**Interview Answer:**  
"I would verify database availability, networking, credentials, and security group rules."

---

## 4. S3 Bucket Accidentally Became Public
### Answer
- Enable Block Public Access.
- Review Bucket Policy and ACLs.
- Use CloudTrail to identify who changed permissions.

**Interview Answer:**  
"I would immediately block public access and investigate the root cause using CloudTrail logs."

---

## 5. Auto Scaling Not Launching New Instances
### Answer
- Verify CloudWatch alarms.
- Check ASG desired/max capacity.
- Validate Launch Template configuration.

**Interview Answer:**  
"I would verify scaling policies, alarms, and maximum capacity configuration."

---

## 6. EC2 CPU Utilization Reaches 100%
### Answer
Investigate using:

```bash
top
htop
ps -ef
```

Possible causes:
- Traffic spike
- Infinite loop
- Memory leak
- Malware

**Interview Answer:**  
"I would identify the process consuming CPU and determine whether it is application or infrastructure related."

---

## 7. EBS Volume Becomes Full
### Answer

```bash
df -h
du -sh *
```

Increase EBS size and extend filesystem:

```bash
growpart /dev/xvda 1
resize2fs /dev/xvda1
```

**Interview Answer:**  
"I would identify large files, clean unnecessary data, and extend storage if required."

---

## 8. Load Balancer Returning 503 Errors
### Answer
Check:
- Target group health
- Health check path
- Security Groups
- Application service status

**Interview Answer:**  
"I would start troubleshooting from target group health status."

---

## 9. Unable to SSH into EC2
### Answer
Verify:
- Port 22 in Security Group
- Public IP/Elastic IP
- Network ACLs
- SSH daemon status

```bash
systemctl status sshd
```

**Interview Answer:**  
"I would verify networking and SSH service configuration."

---

## 10. CloudFormation Stack Creation Failed
### Answer
Review:

AWS Console → CloudFormation → Events

Common causes:
- IAM permission issues
- Existing resources
- Wrong dependencies

**Interview Answer:**  
"I always start troubleshooting using CloudFormation Events because they provide exact failure information."

---

## 11. Data Accidentally Deleted from S3
### Answer
If Versioning is enabled:
- Restore previous versions.

Best Practices:
- Enable Versioning
- Cross Region Replication
- Backup policies

**Interview Answer:**  
"S3 versioning protects against accidental deletions and should always be enabled for critical data."

---

## 12. Multi-AZ RDS Failover
### Answer
AWS automatically:
1. Promotes standby instance.
2. Updates DNS endpoint.
3. Redirects traffic.

Typical downtime:
- 60–120 seconds

**Interview Answer:**  
"Multi-AZ provides high availability, whereas Read Replicas provide read scalability."

---

## 13. AWS Bill Suddenly Increased
### Answer
Use:
- AWS Cost Explorer
- AWS Trusted Advisor

Check:
- Large EC2 instances
- Data transfer charges
- NAT Gateway costs
- Unused EBS volumes

**Interview Answer:**  
"I would use Cost Explorer to identify abnormal spending patterns."

---

## 14. One Availability Zone Went Down
### Answer
Production design should include:
- Multi-AZ EC2 deployment
- Application Load Balancer
- Multi-AZ RDS

**Interview Answer:**  
"Critical applications should always be architected across multiple Availability Zones."

---

## 15. IAM User Receiving Access Denied
### Answer
Check:
- IAM policies
- Bucket policies
- SCP policies
- Permission boundaries
- Explicit Deny statements

**Interview Answer:**  
"AWS always evaluates explicit deny before allow permissions."

---

# Most Frequently Asked AWS Production Scenarios
1. EC2 inaccessible
2. High CPU usage
3. EBS full issue
4. RDS connectivity problems
5. ALB unhealthy targets
6. Auto Scaling failures
7. S3 accidental deletion
8. AWS cost optimization
9. IAM access issues
10. Disaster recovery and Multi-AZ design

# Additional AWS Scenario-Based Interview Questions (Continued)

## 16. Users Cannot Access Application After Deployment
### Scenario
A new application version is deployed and users immediately receive 502/503 errors.

### Troubleshooting
1. Verify application service status.
2. Review application and web server logs.
3. Check ALB target group health checks.
4. Validate environment variables and database connectivity.
5. Roll back deployment if necessary.

### Interview Answer
I would first determine whether the issue is application-level or infrastructure-level by checking logs, service status, and ALB target health.

---

## 17. NAT Gateway Failure – Private Instances Cannot Access Internet

### Troubleshooting
- Verify route table contains:
  `0.0.0.0/0 → NAT Gateway`
- Check NAT Gateway state.
- Verify Elastic IP association.

### Interview Answer
I would verify route tables, NAT Gateway health, and ensure private subnet traffic is routed correctly.

---

## 18. Lambda Function Suddenly Starts Timing Out

### Troubleshooting
- Review CloudWatch logs.
- Check Lambda timeout configuration.
- Verify VPC and NAT configuration.
- Investigate slow external APIs or database connections.

### Interview Answer
I would determine whether the issue is due to application code or networking delays.

---

## 19. Route53 DNS Not Resolving

### Troubleshooting
- Verify Hosted Zone records.
- Validate registrar nameservers.
- Ensure ALB endpoint still exists.
- Check DNS propagation and TTL.

### Interview Answer
I would first verify Route53 records and domain nameserver configuration.

---

## 20. CloudFront Users Seeing Old Content

### Troubleshooting
- Review cache behavior and TTL.
- Create cache invalidation.

```bash
aws cloudfront create-invalidation --distribution-id <id> --paths "/*"
```

### Interview Answer
CloudFront serves cached data, so cache invalidation is required after deployments.

---

## 21. Application Lost Connectivity After Security Group Change

### Troubleshooting
- Verify EC2 to RDS communication.
- Verify ALB to EC2 communication.
- Review recently modified Security Group rules.

### Interview Answer
Security Group changes are among the most common causes of production outages.

---

## 22. SQS Queue Messages Are Not Being Processed

### Troubleshooting
- Verify consumers are running.
- Review CloudWatch queue metrics.
- Check IAM permissions.
- Inspect Dead Letter Queue.

### Interview Answer
I would investigate worker health, permissions, and failed messages in DLQ.

---

## 23. ECS Tasks Continuously Restarting

### Troubleshooting
- Review ECS events.
- Check CloudWatch logs.
- Investigate Exit Code 137 (OOM).

### Interview Answer
Exit code 137 usually indicates memory exhaustion or OOMKilled containers.

---

## 24. Cross Account S3 Access Not Working

### Troubleshooting
- Verify IAM policy.
- Verify Bucket policy.
- Check KMS permissions if encryption is enabled.

### Interview Answer
Cross-account access requires both IAM permissions and resource-based permissions.

---

## 25. Application Stops Working After IAM Role Modification

### Troubleshooting
- Verify attached IAM role.
- Check required permissions.
- Validate temporary credentials.

### Interview Answer
IAM role changes can immediately affect production workloads.

---

## 26. EFS Mount Suddenly Fails

### Troubleshooting
- Verify port 2049 access.
- Check mount targets.
- Verify DNS resolution.

### Interview Answer
I would verify NFS connectivity, security groups, and mount targets.

---

## 27. AWS Backup Failed Overnight

### Troubleshooting
- Review AWS Backup jobs.
- Check IAM permissions.
- Verify backup plans and vault policies.

### Interview Answer
Backup failures should be treated as critical incidents because they impact disaster recovery.

---

## 28. API Gateway Suddenly Returning 500 Errors

### Troubleshooting
- Review integration backend health.
- Check CloudWatch logs.
- Verify Lambda or ECS backend availability.

### Interview Answer
API Gateway issues are often caused by backend failures.

---

## 29. Application Facing Intermittent Connectivity Issues

### Troubleshooting
- Check DNS issues.
- Investigate network latency.
- Review packet loss and CloudWatch network metrics.

### Interview Answer
Intermittent issues are usually related to networking, DNS, or overloaded resources.

---

## 30. AWS Secrets Manager Credentials Not Rotating

### Troubleshooting
- Review rotation Lambda logs.
- Verify permissions.
- Test manual rotation.

```bash
aws secretsmanager rotate-secret
```

### Interview Answer
I would verify Lambda execution logs and ensure required permissions exist between Secrets Manager and the database.

---

# Additional Frequently Asked AWS Production Scenarios

16. Deployment failures after release
17. NAT Gateway failures
18. Lambda timeout issues
19. Route53 DNS issues
20. CloudFront cache problems
21. Security Group misconfigurations
22. SQS message backlog
23. ECS task restart issues
24. Cross-account S3 access problems
25. IAM role modification impact
26. EFS connectivity failures
27. Backup failures
28. API Gateway backend failures
29. Intermittent network issues
30. Secrets Manager rotation failures

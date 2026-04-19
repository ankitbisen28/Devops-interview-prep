# AWS Interview Questions & Answers (50+)

## EC2 (Elastic Compute Cloud)

1. **What is EC2?**  
EC2 is a service that provides virtual servers (instances) in the cloud where you can run applications.

2. **What are EC2 instance types?**  
They are different configurations of CPU, memory, storage (e.g., General Purpose, Compute Optimized, Memory Optimized).

3. **What is AMI?**  
Amazon Machine Image is a pre-configured template used to launch EC2 instances.

4. **What is EBS?**  
Elastic Block Store is persistent block storage attached to EC2.

5. **Difference between EBS and Instance Store?**  
- EBS → persistent  
- Instance Store → temporary (lost on stop/terminate)

6. **What is Security Group in EC2?**  
It acts as a virtual firewall at instance level.

7. **What happens when you stop vs terminate EC2?**  
- Stop → data preserved  
- Terminate → data deleted (unless EBS retained)

---

## IAM (Identity and Access Management)

8. **What is IAM?**  
IAM controls access to AWS services securely.

9. **What are IAM components?**  
- Users  
- Groups  
- Roles  
- Policies  

10. **Difference between Role and User?**  
- User → permanent identity  
- Role → temporary access (assumed)

11. **What is IAM Policy?**  
JSON document that defines permissions.

12. **What is least privilege principle?**  
Give only required permissions, nothing extra.

13. **What is MFA?**  
Multi-Factor Authentication adds extra security layer.

---

## VPC (Virtual Private Cloud)

14. **What is VPC?**  
A logically isolated network in AWS.

15. **What are VPC components?**  
- Subnets  
- Route Tables  
- Internet Gateway  
- NAT Gateway  

16. **What is CIDR block?**  
Defines IP range (e.g., 10.0.0.0/16)

17. **What is Internet Gateway?**  
Allows communication between VPC and internet.

18. **What is NAT Gateway?**  
Allows private subnet instances to access internet.

---

## Subnets

19. **What is a subnet?**  
A subdivision of VPC.

20. **Difference between public and private subnet?**  
- Public → internet access  
- Private → no direct internet

21. **How do you make a subnet public?**  
Attach route to Internet Gateway.

---

## NACL vs Security Groups

22. **What is NACL?**  
Network ACL is a subnet-level firewall.

23. **Difference between NACL and Security Group?**

| Feature | NACL | Security Group |
|--------|------|--------------|
| Level | Subnet | Instance |
| Type | Stateless | Stateful |
| Rules | Allow + Deny | Allow only |

24. **What is stateless vs stateful?**  
- Stateless → rules for both inbound/outbound  
- Stateful → response traffic allowed automatically  

---

## Auto Scaling Group (ASG)

25. **What is Auto Scaling?**  
Automatically adjusts number of EC2 instances.

26. **Types of scaling?**  
- Dynamic  
- Scheduled  
- Predictive  

27. **What is Launch Template?**  
Defines configuration for instances.

28. **What is Desired, Min, Max capacity?**  
- Desired → target instances  
- Min → minimum instances  
- Max → upper limit  

---

## Route 53

29. **What is Route 53?**  
AWS DNS service.

30. **What is DNS?**  
Maps domain name to IP.

31. **Types of routing policies?**  
- Simple  
- Weighted  
- Latency  
- Failover  

32. **What is health check?**  
Monitors endpoint health and routes traffic accordingly.

---

## AWS CLI

33. **What is AWS CLI?**  
Command-line tool to interact with AWS.

34. **How do you configure AWS CLI?**  
```bash
aws configure
```

35. **What credentials are required?**  
- Access Key  
- Secret Key  
- Region  

36. **Example command to list EC2 instances?**  
```bash
aws ec2 describe-instances
```

---

## ECR (Elastic Container Registry)

37. **What is ECR?**  
Docker container registry in AWS.

38. **Difference between ECR and Docker Hub?**  
- ECR → AWS managed  
- Docker Hub → public registry  

39. **How to push image to ECR?**  
- Authenticate  
- Tag image  
- Push  

40. **Why use ECR?**  
Secure, scalable, integrates with ECS/EKS.

---

## Scenario-Based Questions

41. **How do you secure EC2 instance?**  
- Use Security Groups  
- IAM roles  
- Disable root login  
- Use SSH key  

42. **How do you design highly available architecture?**  
- Use multiple AZs  
- Load Balancer  
- Auto Scaling  

43. **How do you connect private EC2 to internet?**  
Use NAT Gateway.

44. **How do you restrict access to S3/EC2?**  
Using IAM policies.

---

## Advanced / Practical Questions

45. **What happens if Security Group blocks traffic?**  
Instance becomes inaccessible.

46. **Can we attach multiple SG to EC2?**  
Yes.

47. **Can NACL deny traffic?**  
Yes (unlike SG).

48. **How does Route53 failover work?**  
Routes traffic to healthy resource.

49. **What is Bastion Host?**  
Jump server to access private instances.

50. **What is Elastic IP?**  
Static public IP for EC2.

---

## Bonus Questions (DevOps)

51. **How do you integrate ECR with CI/CD?**  
Use Jenkins/GitHub Actions to build & push image.

52. **How do you automate infrastructure?**  
Using Terraform (IaC).

53. **What is blue-green deployment?**  
Deploy new version alongside old, switch traffic.

54. **How do you monitor EC2?**  
Using CloudWatch.

# Terraform Scenario-Based Interview Questions (1–3 Years Experience)

## 1. Terraform Apply Failed After Creating Some Resources

### Scenario
Terraform successfully created:
- VPC
- Subnets
- Security Groups

But failed while creating an EC2 instance due to an invalid AMI.

### Answer
Terraform stores successfully created resources in the state file. Only failed resources will be retried after fixing the issue.

**Commands:**
```bash
terraform state list
terraform apply
```

**Reason:** Desired state reconciliation.

**Production Example:** AMI was deleted or permissions changed, so only EC2 creation failed.

---

## 2. Someone Deleted an EC2 Instance Manually

### Scenario
An engineer deleted an EC2 instance from AWS Console.

### Answer
Terraform detects infrastructure drift.

```bash
terraform plan
terraform apply
```

Terraform will recreate the EC2 instance.

**Reason:** State and actual infrastructure are different.

---

## 3. Terraform State File Got Deleted

### Scenario
`terraform.tfstate` was accidentally removed.

### Solution
1. Restore from backup.
2. Import resources:
```bash
terraform import aws_instance.web i-123456
```
3. Use remote backend.

```hcl
backend "s3" {
  bucket = "terraform-state"
}
```

**Best Practice:** S3 + Versioning + DynamoDB locking.

---

## 4. Two Engineers Run Apply Simultaneously

### Problem
State corruption may occur.

### Solution
Use state locking:

```hcl
backend "s3" {
  bucket         = "terraform-state"
  dynamodb_table = "terraform-lock"
}
```

Second user gets:

```bash
Error acquiring state lock
```

---

## 5. Terraform Wants to Replace EC2

### Scenario
Terraform shows:

```bash
-/+ aws_instance.web
```

### Reasons
Changing:
- AMI
- Subnet
- Root volume

can force replacement.

### Solution

```hcl
lifecycle {
  ignore_changes = [tags]
}
```

---

## 6. Terraform Apply Takes Too Long

### Troubleshooting

Enable logs:

```bash
export TF_LOG=DEBUG
```

Check AWS resources:

```bash
aws rds describe-db-instances
```

### Possible Reasons
- API throttling
- Quota exceeded
- Dependency issue
- RDS provisioning time

---

## 7. Terraform Destroy Failed

### Error
```bash
VPC cannot be deleted because ENI exists.
```

### Solution
Find dependencies:

```bash
terraform graph
aws ec2 describe-network-interfaces
```

Delete dependent resources first.

---

## 8. Terraform Works Locally but Fails in Jenkins

### Reasons
- Missing IAM permissions
- AWS credentials not configured
- Variables not passed
- Backend access issue

### Verify

```bash
aws sts get-caller-identity
```

---

## 9. Terraform Always Shows Changes

### Reasons
- timestamp() function
- AWS auto-generated tags
- Ordering changes

### Solution

```hcl
lifecycle {
  ignore_changes = [tags]
}
```

---

## 10. Terraform State Became Inconsistent

### Scenario
Terraform crashed in the middle of deployment.

### Recovery

Check AWS resources:

```bash
aws ec2 describe-instances
```

Import resources:

```bash
terraform import
```

Run:

```bash
terraform plan
```

---

## 11. Managing Dev, QA and Prod

### Best Practice

Use modules:

```hcl
module "vpc" {
  source = "./modules/vpc"
}
```

Use separate variable files:

```bash
terraform apply -var-file=prod.tfvars
```

---

## 12. Sensitive Data in State File

### Problem
Database passwords are visible.

### Solution

```hcl
variable "db_password" {
  sensitive = true
}
```

Use:
- AWS Secrets Manager
- Parameter Store
- Vault

Enable backend encryption.

---

## 13. Resources Created in Wrong AWS Account

### Prevention

```hcl
provider "aws" {
  allowed_account_ids = ["123456789012"]
}
```

Terraform fails if wrong account is used.

---

## 14. Zero Downtime During Replacement

### Solution

```hcl
lifecycle {
  create_before_destroy = true
}
```

Terraform creates new infrastructure first and then deletes old resources.

---

## 15. Module Change Broke Production

### Solution
Pin versions:

```hcl
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.2.0"
}
```

Never use:

```hcl
version = "latest"
```

---

# Common Follow-Up Questions

### What is Infrastructure Drift?
Changes made outside Terraform.

### Why Remote Backend?
- Collaboration
- Security
- Backup
- State Locking

### Why DynamoDB?
Prevents simultaneous state modifications.

### What if State Gets Corrupted?
Restore backup or import resources.

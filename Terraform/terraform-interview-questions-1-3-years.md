# Terraform Interview Questions (1–3 Years Experience)

A curated set of the most commonly asked Terraform interview questions for candidates with 1–3 years of hands-on experience, along with clear, practical answers.

---

## 1. What is Terraform and how is it different from other IaC tools like Ansible or CloudFormation?

**Answer:**
Terraform is an open-source Infrastructure as Code (IaC) tool by HashiCorp used to provision and manage cloud and on-prem infrastructure using a declarative configuration language (HCL).

Key differences:
- **Terraform vs CloudFormation:** Terraform is cloud-agnostic (works with AWS, Azure, GCP, etc.), while CloudFormation is AWS-specific.
- **Terraform vs Ansible:** Terraform is primarily a **provisioning** tool (declarative, focused on infrastructure state), while Ansible is a **configuration management** tool (procedural/imperative, focused on configuring servers). Terraform maintains a state file to track resources; Ansible does not.

---

## 2. What is the Terraform state file and why is it important?

**Answer:**
The state file (`terraform.tfstate`) is a JSON file that stores the current state of your infrastructure as managed by Terraform. It maps real-world resources to your configuration, tracks metadata, and helps Terraform determine what changes need to be made during `terraform plan`/`apply`.

It's important because:
- It enables Terraform to detect drift between actual infrastructure and configuration.
- It improves performance by caching resource attributes instead of querying the provider every time.
- It's required for Terraform to know what to update, destroy, or recreate.

---

## 3. What is remote state and why would you use it over local state?

**Answer:**
Remote state stores the `.tfstate` file in a shared remote backend (like AWS S3, Azure Blob Storage, Terraform Cloud, GCS) instead of locally on disk.

Reasons to use it:
- **Team collaboration** – multiple engineers can access the same state.
- **State locking** – prevents concurrent operations from corrupting state (e.g., using S3 + DynamoDB for locking).
- **Security** – state can contain sensitive data, so remote backends allow encryption and access control.
- **Backup and durability** – avoids losing state if a local machine fails.

---

## 4. What is the difference between `terraform plan` and `terraform apply`?

**Answer:**
- `terraform plan` creates an **execution plan**, showing what actions Terraform will take (create, update, destroy) without actually making changes. It's a dry run.
- `terraform apply` executes the actions proposed in the plan and actually provisions/modifies the infrastructure.

---

## 5. What are Terraform providers?

**Answer:**
Providers are plugins that allow Terraform to interact with APIs of cloud platforms, SaaS providers, or other services (e.g., `aws`, `azurerm`, `google`, `kubernetes`). They are responsible for understanding API interactions and exposing resources.

Example:
```hcl
provider "aws" {
  region = "us-east-1"
}
```

---

## 6. What is the difference between a Terraform module and a resource?

**Answer:**
- A **resource** is a single infrastructure object (e.g., an EC2 instance, an S3 bucket).
- A **module** is a container for multiple resources that are grouped together and reused. Every Terraform configuration has at least a root module, and you can call child modules from it to promote reusability and organization.

```hcl
module "vpc" {
  source = "./modules/vpc"
  cidr_block = "10.0.0.0/16"
}
```

---

## 7. What is the difference between `count` and `for_each`?

**Answer:**
Both are used to create multiple instances of a resource, but:

- `count` uses a numeric index and works well for identical resources.
```hcl
resource "aws_instance" "server" {
  count = 3
  ami   = "ami-123456"
}
```
- `for_each` iterates over a map or set of strings, giving each resource a unique key, making it more stable when adding/removing items (avoids re-indexing issues that `count` can cause).
```hcl
resource "aws_instance" "server" {
  for_each = toset(["web1", "web2"])
  ami      = "ami-123456"
}
```

**Best practice:** Prefer `for_each` when resources are not identical or when list order might change, since `count` can cause unwanted resource recreation.

---

## 8. What are input variables and output values in Terraform?

**Answer:**
- **Input variables** (`variable` block) allow you to parameterize configurations, making them reusable.
```hcl
variable "instance_type" {
  type    = string
  default = "t2.micro"
}
```
- **Output values** (`output` block) expose specific values from your configuration, useful for passing data between modules or displaying info after `apply`.
```hcl
output "instance_ip" {
  value = aws_instance.server.public_ip
}
```

---

## 9. What is a `data` source in Terraform?

**Answer:**
A `data` source allows Terraform to fetch/read information from existing resources that are **not managed** by the current Terraform configuration (e.g., an existing VPC created manually or by another team).

```hcl
data "aws_vpc" "existing" {
  filter {
    name   = "tag:Name"
    values = ["prod-vpc"]
  }
}
```

---

## 10. What is Terraform state locking?

**Answer:**
State locking prevents multiple users/processes from running `terraform apply` simultaneously on the same state file, which could corrupt it. When using a remote backend like S3, DynamoDB is commonly used to implement locking — Terraform acquires a lock before modifying state and releases it after the operation completes.

---

## 11. What happens if two team members run `terraform apply` at the same time without state locking?

**Answer:**
Without locking, simultaneous applies can lead to **race conditions** — both processes could read the same state, make conflicting changes, and overwrite each other's updates, resulting in a corrupted or inconsistent state file that no longer matches real infrastructure.

---

## 12. What is `terraform.tfvars` and how is it used?

**Answer:**
`terraform.tfvars` (or any `*.auto.tfvars` file) is used to define values for input variables so you don't have to pass them manually via CLI flags every time.

```hcl
# terraform.tfvars
instance_type = "t3.medium"
region        = "us-west-2"
```
Terraform automatically loads `terraform.tfvars` and `*.auto.tfvars` files during `plan`/`apply`.

---

## 13. What is the difference between `terraform destroy` and removing a resource block from configuration?

**Answer:**
- `terraform destroy` destroys **all** resources tracked in the state file.
- Removing a resource block from `.tf` files and running `terraform apply` will destroy **only that specific resource**, since Terraform detects it's no longer in the desired configuration.

---

## 14. What is `terraform taint` (or the modern equivalent) used for?

**Answer:**
`terraform taint <resource>` manually marks a resource as "tainted," forcing it to be destroyed and recreated on the next `apply` — useful when a resource is corrupted or misconfigured outside of Terraform's knowledge.

Note: In newer Terraform versions (0.15.2+), the recommended approach is:
```bash
terraform apply -replace="aws_instance.server"
```
since `terraform taint` is being deprecated in favor of this more explicit workflow.

---

## 15. What is `terraform import` used for?

**Answer:**
`terraform import` brings existing infrastructure (created manually or outside Terraform) under Terraform management by adding it to the state file, without recreating the resource.

```bash
terraform import aws_instance.my_server i-0abcd1234efgh5678
```
Note: You still need to manually write the matching resource configuration block; `import` only updates the state, not the `.tf` files.

---

## 16. What are Terraform workspaces?

**Answer:**
Workspaces allow you to manage multiple distinct state files using the same configuration — useful for maintaining separate environments (dev, staging, prod) without duplicating code.

```bash
terraform workspace new dev
terraform workspace select prod
```
**Caveat:** Workspaces alone aren't always sufficient for large multi-environment setups; many teams prefer separate state files/backends per environment for better isolation.

---

## 17. What is the purpose of the `lifecycle` block?

**Answer:**
The `lifecycle` block customizes how Terraform handles resource creation, updates, and destruction. Common arguments:

- `create_before_destroy` – creates a replacement resource before destroying the old one (avoids downtime).
- `prevent_destroy` – blocks accidental destruction of critical resources.
- `ignore_changes` – tells Terraform to ignore changes to specific attributes (useful when an external process modifies a resource).

```hcl
resource "aws_instance" "server" {
  lifecycle {
    create_before_destroy = true
    prevent_destroy        = true
  }
}
```

---

## 18. How does Terraform determine the order in which resources are created?

**Answer:**
Terraform builds a **dependency graph** based on implicit dependencies (references between resources, like `aws_instance.server.id` used in another resource) and explicit dependencies declared using `depends_on`. It then creates/updates resources in the correct order based on this graph, parallelizing independent resources where possible.

---

## 19. What is `depends_on` and when would you use it?

**Answer:**
`depends_on` explicitly defines a dependency between resources when Terraform cannot automatically infer it from the configuration (e.g., no direct attribute reference exists, but there's still a logical ordering requirement).

```hcl
resource "aws_s3_bucket" "example" {
  bucket = "my-bucket"
}

resource "aws_s3_bucket_policy" "example" {
  bucket     = aws_s3_bucket.example.id
  policy     = data.aws_iam_policy_document.example.json
  depends_on = [aws_s3_bucket.example]
}
```

---

## 20. What is drift in Terraform and how do you detect/handle it?

**Answer:**
**Drift** occurs when actual infrastructure changes outside of Terraform (e.g., manual console changes) and no longer matches the state file.

Detection: Run `terraform plan` — Terraform compares real infrastructure with state and configuration, and shows any differences.

Handling drift:
- Update the Terraform configuration to reflect the manual change, then apply.
- Or revert the manual change so it matches Terraform's expected state.
- Use `terraform refresh` (or `terraform apply -refresh-only` in newer versions) to sync the state file with real infrastructure without changing resources.

---

## 21. What is the difference between `variable` validation and `precondition`/`postcondition`?

**Answer:**
- `validation` blocks inside a `variable` check the input value itself before any plan/apply logic runs.
```hcl
variable "env" {
  type = string
  validation {
    condition     = contains(["dev", "staging", "prod"], var.env)
    error_message = "env must be dev, staging, or prod."
  }
}
```
- `precondition`/`postcondition` (inside `lifecycle` blocks on resources/data sources, introduced in Terraform 1.2+) validate assumptions about resource behavior/state during plan or after apply — more advanced, resource-level checks.

---

## 22. How do you manage secrets/sensitive data in Terraform?

**Answer:**
- Mark variables as `sensitive = true` so their values are hidden in CLI output and plan/apply logs.
```hcl
variable "db_password" {
  type      = string
  sensitive = true
}
```
- Avoid hardcoding secrets in `.tf` files; use environment variables, a secrets manager (AWS Secrets Manager, HashiCorp Vault, Azure Key Vault), or CI/CD secret stores instead.
- Note: sensitive values are still stored in **plaintext in the state file**, so state file encryption and restricted access are essential.

---

## 23. What is the difference between `local-exec` and `remote-exec` provisioners?

**Answer:**
- `local-exec` runs a command on the machine running Terraform (the local machine/CI runner).
- `remote-exec` runs a command on the remote resource being created (e.g., via SSH into a new EC2 instance).

```hcl
provisioner "local-exec" {
  command = "echo Instance created: ${self.id}"
}
```

**Best practice:** Provisioners are a last resort — HashiCorp recommends using native provider features, cloud-init/user_data, or configuration management tools instead, since provisioners aren't tracked well by Terraform's dependency graph.

---

## 24. What are Terraform modules' `source` types?

**Answer:**
Modules can be sourced from:
- Local paths: `source = "./modules/vpc"`
- Terraform Registry: `source = "terraform-aws-modules/vpc/aws"`
- Git repositories: `source = "git::https://github.com/org/repo.git"`
- S3 buckets, HTTP URLs, etc.

---

## 25. What's the difference between `terraform fmt`, `terraform validate`, and `terraform plan`?

**Answer:**
- `terraform fmt` – formats `.tf` files to a canonical style (doesn't check logic).
- `terraform validate` – checks configuration syntax and internal consistency (e.g., missing required arguments) without accessing remote state/providers deeply.
- `terraform plan` – performs a full comparison against real infrastructure/state and shows what changes would be applied; requires provider authentication.

---

## 26. How would you structure a Terraform project for a real production application (multiple environments)?

**Answer:**
Common approach:
```
project/
├── modules/
│   ├── vpc/
│   ├── ec2/
│   └── rds/
├── environments/
│   ├── dev/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── terraform.tfvars
│   ├── staging/
│   └── prod/
```
- Reusable logic lives in `modules/`.
- Each environment has its own state file/backend and `.tfvars` for environment-specific values.
- This avoids relying solely on workspaces and gives full isolation between environments (separate state, separate blast radius).

---

## 27. What is the purpose of `terraform.lock.hcl`?

**Answer:**
The dependency lock file records the exact provider versions (and their checksums) used in a configuration, ensuring consistent provider versions across team members and CI/CD pipelines, similar to `package-lock.json` in Node.js. It should be committed to version control.

---

## 28. How do you handle a situation where `terraform apply` partially fails midway?

**Answer:**
Terraform applies changes based on the dependency graph, and if a failure occurs partway through:
1. Terraform updates the state file with whatever resources were **successfully** created/modified before the failure — state stays consistent with real infrastructure up to that point.
2. Review the error (often a provider/API issue, quota limit, or misconfiguration).
3. Fix the underlying issue and re-run `terraform apply` — Terraform will resume by only creating/modifying the remaining resources, since it compares current state against desired state.

---

## 29. What is the difference between a shared/remote backend and a `null_resource`?

**Answer:**
These are unrelated concepts often confused by candidates:
- A **backend** (e.g., S3, Terraform Cloud) defines *where* Terraform stores its state file.
- A **`null_resource`** is a resource with no direct infrastructure representation, often used with `provisioners` or `triggers` to run arbitrary logic (e.g., trigger a script when a specific value changes).

```hcl
resource "null_resource" "example" {
  triggers = {
    always_run = timestamp()
  }
  provisioner "local-exec" {
    command = "echo Triggered"
  }
}
```

---

## 30. How do you upgrade Terraform provider or core versions safely in an existing project?

**Answer:**
1. Check the changelog/upgrade guide for breaking changes.
2. Pin version constraints in `required_providers`/`required_version` blocks and update incrementally rather than jumping many major versions at once.
```hcl
terraform {
  required_version = ">= 1.5.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```
3. Run `terraform init -upgrade` to update the lock file.
4. Run `terraform plan` in a non-production environment first to catch unexpected diffs before applying to production.

---

## Bonus: Quick Concept Recap Table

| Concept | One-Line Summary |
|---|---|
| State file | Tracks real infra mapped to config |
| Provider | Plugin to talk to a specific platform's API |
| Module | Reusable group of resources |
| `count` | Index-based resource repetition |
| `for_each` | Key-based resource repetition (more stable) |
| `depends_on` | Explicit dependency declaration |
| `lifecycle` | Customizes create/update/destroy behavior |
| Workspace | Multiple state files from one config |
| Drift | Real infra diverges from Terraform state |
| `terraform.lock.hcl` | Locks provider versions for consistency |

---

*Tip for interviews: Be ready to not just define these terms but explain a real scenario where you used them — interviewers at the 1-3 year level often ask "have you actually run into this?" as a follow-up.*

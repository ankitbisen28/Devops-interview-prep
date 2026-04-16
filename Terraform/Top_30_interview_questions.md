✅ 1. What is Terraform?
-----------------------

Terraform is an **Infrastructure as Code (IaC) tool developed by HashiCorp** that allows us to **provision and manage cloud infrastructure using code** instead of manual configuration.

It supports multiple cloud providers like AWS, Azure, and GCP.

✅ 2. What is Infrastructure as Code (IaC)?
------------------------------------------

IaC is the process of **managing infrastructure using configuration files instead of manual setup**.

Benefits:

*   Automation
    
*   Version Control
    
*   Consistency
    
*   Faster provisioning
    

✅ 3. What are Terraform Providers?
----------------------------------

Providers are **plugins that allow Terraform to interact with APIs of cloud platforms**.

Example:

*   AWS Provider
    
*   Azure Provider
    
```provider "aws" {  region = "ap-south-1"}   ```

✅ 4. What is Terraform State File?
----------------------------------

Terraform state file (terraform.tfstate) stores:

*   Infrastructure current status
    
*   Resource mapping
    
*   Metadata
    

It helps Terraform understand **what already exists**.

✅ 5. Why Remote State is important?
-----------------------------------

Remote state helps in:

*   Team collaboration
    
*   State locking
    
*   Security
    
*   Centralized storage
    

Example:

*   S3 backend
    
*   Terraform Cloud
    

✅ 6. Difference between terraform plan and terraform apply?
-----------------------------------------------------------

*   **terraform plan** → Shows execution preview
    
*   **terraform apply** → Actually creates/modifies infrastructure
    

✅ 7. What is terraform init?
----------------------------

It initializes the project by:

*   Downloading providers
    
*   Configuring backend
    
*   Preparing working directory
    

✅ 8. What is terraform destroy?
-------------------------------

Used to **delete all infrastructure managed by Terraform**.

✅ 9. What are Terraform Modules?
--------------------------------

Modules are reusable Terraform configurations.

Benefits:

*   Code reuse
    
*   Standardization
    
*   Easy maintenance
    

✅ 10. What is Terraform Workspace?
----------------------------------

Workspaces allow **multiple environments using same code**.

Example:

*   dev
    
*   stage
    
*   prod
    

✅ 11. What are Input Variables?
-------------------------------

Variables allow dynamic configuration.

`   variable "instance_type" {  default = "t2.micro"}   `

✅ 12. What are Output Variables?
--------------------------------

Outputs display useful information after apply.

Example:

*   Instance IP
    
*   Load balancer DNS
    

✅ 13. What is terraform refresh?
--------------------------------

It updates the state file according to **real infrastructure changes**.

✅ 14. What is terraform taint?
------------------------------

Marks resource as **damaged → recreate on next apply**.

✅ 15. What is terraform import?
-------------------------------

Used to bring **existing manually created infrastructure into Terraform management**.

✅ 16. Difference between count and for\_each?
---------------------------------------------

*   count → index based
    
*   for\_each → key/value based (preferred)
    

✅ 17. What is dependency in Terraform?
--------------------------------------

Terraform automatically creates dependency using **resource references**.

Manual dependency:

`   depends_on = []   `

✅ 18. What is backend in Terraform?
-----------------------------------

Backend defines **where state file is stored**.

Example:

*   local
    
*   S3
    
*   remote
    

✅ 19. What is State Locking?
----------------------------

Prevents multiple users from modifying state simultaneously.

Example:

*   DynamoDB locking
    

✅ 20. What is Terraform Provisioner?
------------------------------------

Provisioners execute scripts on resources.

Example:

*   remote-exec
    
*   file
    

⚠️ Not recommended as primary method.

✅ 21. What is Null Resource?
----------------------------

Used for **running scripts or orchestration tasks**.

✅ 22. What is Data Source?
--------------------------

Fetch existing infrastructure info.

Example:

*   Existing VPC
    
*   AMI lookup
    

✅ 23. What is Terraform Registry?
---------------------------------

Public repository for:

*   Modules
    
*   Providers
    

✅ 24. How Terraform handles drift?
----------------------------------

Using:
`   terraform plan   `

It detects differences between **state vs real infra**.

✅ 25. What is lifecycle block?
------------------------------

Controls resource behavior.

Example:

`   lifecycle {  prevent_destroy = true}   `

✅ 26. What is dynamic block?
----------------------------

Used to generate nested blocks dynamically.

✅ 27. What is locals in Terraform?
----------------------------------

Local values simplify complex expressions.

✅ 28. What is Terraform Cloud?
------------------------------

Managed SaaS platform from **HashiCorp** for:

*   Remote execution
    
*   State management
    
*   Collaboration
    

✅ 29. What are best practices in Terraform?
-------------------------------------------

*   Use remote backend
    
*   Use modules
    
*   Follow naming standards
    
*   Store secrets in vault
    
*   Keep state secure
    

✅ 30. Difference between Terraform and Ansible?
-----------------------------------------------

TerraformAnsibleProvision infraConfigure infraDeclarativeProceduralUses state fileNo stateBest for infra creationBest for config management
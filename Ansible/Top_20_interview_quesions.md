# Top 20 Ansible Interview Questions and Answers

## 1. What is Ansible?

**Answer:**
Ansible is an open-source configuration management and automation tool used for:

* Server configuration
* Application deployment
* Infrastructure provisioning
* Orchestration

It follows an **agentless architecture** and connects to managed nodes using **SSH**.

---

## 2. What are the main components of Ansible?

**Answer:**

* **Control Node** – Machine where Ansible is installed
* **Managed Nodes** – Target servers
* **Inventory** – List of servers
* **Playbooks** – YAML automation scripts
* **Modules** – Units of work
* **Tasks** – Execution steps

---

## 3. What is Inventory in Ansible?

**Answer:**
Inventory is a file that contains a list of hosts and groups where Ansible runs tasks.

```ini
[web]
192.168.1.10
192.168.1.11
```

---

## 4. What is a Playbook?

**Answer:**
A playbook is a **YAML file** that defines automation steps in a structured and reusable way.

It can include:

* Hosts
* Tasks
* Variables
* Handlers
* Roles

---

## 5. Difference between Ad-hoc Command and Playbook?

**Answer:**

| Ad-hoc               | Playbook                   |
| -------------------- | -------------------------- |
| One-time execution   | Reusable automation        |
| CLI based            | YAML based                 |
| Used for quick tasks | Used for complex workflows |

Example:

```bash
ansible all -m ping
```

---

## 6. What are Ansible Modules?

**Answer:**
Modules are small programs used to perform tasks such as:

* Package installation
* Service management
* File operations
* User creation

Examples: `yum`, `apt`, `copy`, `service`

---

## 7. What is Idempotency in Ansible?

**Answer:**
Idempotency means running the same playbook multiple times will **not change the system state** if it is already configured.

Example:
If Nginx is already installed, Ansible will skip the installation.

---

## 8. What is an Ansible Role?

**Answer:**
A role is a structured way to organize playbooks into reusable components.

Example structure:

```
roles/
  web/
    tasks/
    handlers/
    vars/
    templates/
```

---

## 9. What are Handlers?

**Answer:**
Handlers are tasks that run **only when notified** by another task.

Example use case:

* Restart Nginx only when the configuration file changes.

---

## 10. What is Ansible Galaxy?

**Answer:**
Ansible Galaxy is a repository where you can **download and share reusable roles**.

```bash
ansible-galaxy install geerlingguy.nginx
```

---

## 11. How does Ansible connect to Remote Nodes?

**Answer:**

* SSH (for Linux servers)
* WinRM (for Windows servers)

No agent installation is required.

---

## 12. What is YAML?

**Answer:**
YAML is a human-readable data serialization format used to write playbooks.

Rules:

* Use spaces (not tabs)
* Maintain proper indentation
* Follow key-value format

---

## 13. What are Variables in Ansible?

**Answer:**
Variables help make playbooks **dynamic and reusable**.

```yaml
vars:
  package_name: nginx
```

---

## 14. What is the `register` Keyword?

**Answer:**
`register` is used to store the output of a task into a variable.

```yaml
- command: uptime
  register: output
```

---

## 15. What is the `when` Condition?

**Answer:**
Used to execute a task conditionally.

```yaml
when: ansible_os_family == "Debian"
```

---

## 16. What is the Template Module?

**Answer:**
The template module is used to copy **dynamic configuration files** using Jinja2 templating.

Common use cases:

* Nginx configuration
* Application config files

---

## 17. Difference between Copy and Template Module?

**Answer:**

| Copy                 | Template                    |
| -------------------- | --------------------------- |
| Static file transfer | Dynamic file transfer       |
| No variable support  | Supports variables (Jinja2) |

---

## 18. What is Ansible Vault?

**Answer:**
Ansible Vault is used to **encrypt sensitive data** such as:

* Passwords
* API Keys
* Secrets

```bash
ansible-vault encrypt vars.yml
```

---

## 19. What is Facts Gathering?

**Answer:**
Ansible automatically collects system information (facts), such as:

* OS details
* IP address
* CPU
* Memory

These facts can be used in conditions and variables.

---

## 20. What is `become` in Ansible?

**Answer:**
`become` is used for **privilege escalation (sudo access)**.

```yaml
become: yes
```

---

## ⭐ Real Interview Tip

For **1–2 years DevOps experience**, be ready to explain a real project like:

* Provisioned EC2 instances
* Installed Docker using Ansible playbooks
* Deployed Nginx container
* Used inventory grouping
* Ensured idempotent automation

---

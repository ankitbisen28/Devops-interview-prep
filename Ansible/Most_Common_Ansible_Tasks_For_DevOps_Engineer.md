# Most Common Ansible Tasks for a DevOps Engineer (1--3 Years Experience)

This guide covers the most common real-world tasks performed using
Ansible.

## 1. Install Packages

``` yaml
- hosts: webservers
  become: yes
  tasks:
    - name: Install Nginx
      apt:
        name: nginx
        state: present
```

## 2. Update Packages

``` yaml
- name: Update Ubuntu packages
  apt:
    update_cache: yes
    upgrade: dist
```

## 3. Create Users

``` yaml
- name: Create DevOps User
  user:
    name: devops
    password: "{{ 'Password123' | password_hash('sha512') }}"
    shell: /bin/bash
```

## 4. Delete Users

``` yaml
- name: Remove User
  user:
    name: john
    state: absent
```

## 5. Copy Configuration Files

``` yaml
- name: Copy nginx config
  copy:
    src: nginx.conf
    dest: /etc/nginx/nginx.conf
```

## 6. Deploy Applications

Typical workflow:

``` text
CI Pipeline
   ↓
Build Artifact
   ↓
Copy to Server
   ↓
Restart Service
```

``` yaml
- name: Copy JAR
  copy:
    src: app.jar
    dest: /opt/app/app.jar

- name: Restart application
  service:
    name: myapp
    state: restarted
```

## 7. Restart Services

``` yaml
- service:
    name: nginx
    state: restarted
```

## 8. Start / Stop Services

``` yaml
- service:
    name: docker
    state: stopped
```

## 9. Enable Services at Boot

``` yaml
- service:
    name: docker
    enabled: yes
```

## 10. Manage Firewall

``` yaml
- ufw:
    rule: allow
    port: "80"
```

## 11. Create Directories

``` yaml
- file:
    path: /opt/application
    state: directory
```

## 12. Delete Directories

``` yaml
- file:
    path: /tmp/test
    state: absent
```

## 13. Change File Permissions

``` yaml
- file:
    path: /opt/app
    mode: "0755"
```

## 14. Manage SSH Keys

``` yaml
- authorized_key:
    user: ubuntu
    key: "{{ lookup('file','id_rsa.pub') }}"
```

## 15. Create Cron Jobs

``` yaml
- cron:
    name: Backup
    minute: "0"
    hour: "2"
    job: "/opt/backup.sh"
```

## 16. Download Files

``` yaml
- get_url:
    url: https://example.com/app.jar
    dest: /opt/app.jar
```

## 17. Extract Archives

``` yaml
- unarchive:
    src: app.zip
    dest: /opt/
```

## 18. Install Docker

``` yaml
- apt:
    name: docker.io
    state: present
```

## 19. Deploy Docker Containers

``` yaml
- docker_container:
    name: nginx
    image: nginx
    state: started
    ports:
      - "80:80"
```

## 20. Install Kubernetes Tools

Install: - kubeadm - kubelet - kubectl

## 21. Configure Kubernetes Nodes

Typical tasks: - Disable swap - Configure kernel parameters - Install
container runtime

## 22. Provision AWS Resources

-   Launch EC2
-   Stop/Start EC2
-   Terminate EC2
-   Create S3 Buckets
-   Manage Security Groups

## 23. Install Jenkins

Install Java, Jenkins, start service, and configure plugins.

## 24. Configure Web Servers

-   Nginx
-   Apache
-   Reverse Proxy
-   SSL

## 25. Configure Databases

-   MySQL
-   PostgreSQL
-   MariaDB
-   Create databases and users

## 26. Backup Files

``` yaml
- archive:
    path: /var/www
    dest: /backup/www.tar.gz
```

## 27. Check Server Health

``` yaml
- shell: df -h
```

``` yaml
- shell: free -m
```

## 28. Gather Facts

``` bash
ansible all -m setup
```

Collects: - OS - CPU - RAM - Disk - IP Address

## 29. Execute Commands

``` yaml
- shell: uptime
```

``` yaml
- command: hostname
```

## 30. Rolling Deployments

Deploy one server at a time to avoid downtime.

## 31. Blue-Green Deployments

-   Deploy new version
-   Switch traffic
-   Remove old version

## 32. Manage Environment Variables

Use templates and variables.

## 33. Manage Secrets

Use **Ansible Vault** for: - Passwords - API Keys - SSH Keys

## 34. Use Jinja2 Templates

``` yaml
- template:
    src: nginx.conf.j2
    dest: /etc/nginx/nginx.conf
```

## 35. CI/CD Integration

``` text
Git Push
   ↓
Jenkins
   ↓
Build
   ↓
Test
   ↓
Docker Image
   ↓
Push to Docker Hub
   ↓
Ansible Deployment
   ↓
Restart Services
```

# Most Frequently Asked Ansible Interview Topics

  Task                       Frequency
  -------------------------- ------------
  Install Packages           ⭐⭐⭐⭐⭐
  Copy Configuration Files   ⭐⭐⭐⭐⭐
  Restart Services           ⭐⭐⭐⭐⭐
  Deploy Applications        ⭐⭐⭐⭐⭐
  Variables & Inventory      ⭐⭐⭐⭐⭐
  Roles                      ⭐⭐⭐⭐⭐
  Jinja2 Templates           ⭐⭐⭐⭐⭐
  Ansible Vault              ⭐⭐⭐⭐
  Docker Installation        ⭐⭐⭐⭐
  Nginx Configuration        ⭐⭐⭐⭐
  Rolling Deployment         ⭐⭐⭐⭐
  Shell/Command Modules      ⭐⭐⭐

## Recommended Learning Order

1.  Inventory
2.  Ad-hoc Commands
3.  Playbooks
4.  Variables
5.  Handlers
6.  Templates (Jinja2)
7.  Roles
8.  Ansible Vault
9.  Docker Automation
10. Kubernetes Node Configuration
11. AWS Automation
12. CI/CD Integration with Jenkins

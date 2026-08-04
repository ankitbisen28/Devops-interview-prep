# Kubernetes Interview Questions (1–3 Years Experience)

A curated list of commonly asked Kubernetes interview questions for candidates with 1–3 years of hands-on experience, along with clear, practical answers.

---

## 1. What is Kubernetes and why is it used?

**Answer:**
Kubernetes (K8s) is an open-source container orchestration platform used to automate the deployment, scaling, and management of containerized applications. It solves problems like load balancing, self-healing, service discovery, and rolling updates that become hard to manage manually when running containers at scale.

---

## 2. What is the difference between a Pod, a Container, and a Node?

**Answer:**
- **Container**: A lightweight, standalone package that runs an application (e.g., via Docker).
- **Pod**: The smallest deployable unit in Kubernetes. It can contain one or more containers that share the same network namespace and storage volumes.
- **Node**: A worker machine (VM or physical server) that runs Pods. A cluster consists of a control plane and multiple nodes.

---

## 3. What is the difference between a Deployment, ReplicaSet, and StatefulSet?

**Answer:**
- **ReplicaSet**: Ensures a specified number of identical Pod replicas are running at all times.
- **Deployment**: A higher-level object that manages ReplicaSets, enabling rolling updates, rollbacks, and declarative updates to Pods.
- **StatefulSet**: Used for stateful applications (like databases) that need stable, unique network identities and persistent storage across Pod restarts, unlike Deployments which treat Pods as interchangeable.

---

## 4. What are Kubernetes Services and what types are available?

**Answer:**
A Service is an abstraction that defines a logical set of Pods and a policy to access them, providing stable networking even as Pods are created/destroyed.

Types:
- **ClusterIP** (default): Exposes the service internally within the cluster.
- **NodePort**: Exposes the service on a static port on each node's IP.
- **LoadBalancer**: Provisions an external load balancer (typically via cloud provider).
- **ExternalName**: Maps the service to an external DNS name.

---

## 5. What is a Namespace in Kubernetes?

**Answer:**
A Namespace is a way to logically divide cluster resources between multiple users, teams, or projects. It helps organize resources and apply resource quotas, access control, and naming isolation. Common default namespaces include `default`, `kube-system`, and `kube-public`.

---

## 6. How does Kubernetes handle self-healing?

**Answer:**
Kubernetes continuously monitors the actual state of the cluster against the desired state defined in manifests. If a Pod crashes, the controller (like a ReplicaSet) automatically recreates it. Liveness and readiness probes also help Kubernetes detect and restart unhealthy containers.

---

## 7. What are Liveness, Readiness, and Startup Probes?

**Answer:**
- **Liveness Probe**: Checks if a container is still running correctly; if it fails, Kubernetes restarts the container.
- **Readiness Probe**: Checks if a container is ready to accept traffic; if it fails, the Pod is removed from Service endpoints.
- **Startup Probe**: Used for slow-starting containers, it delays liveness/readiness checks until the app has fully started.

---

## 8. What is a ConfigMap and a Secret? What's the difference?

**Answer:**
- **ConfigMap**: Stores non-sensitive configuration data (like environment variables or config files) as key-value pairs, which can be injected into Pods.
- **Secret**: Similar to ConfigMap but designed for sensitive data (passwords, tokens, keys). Secrets are base64-encoded (not encrypted by default) and can be encrypted at rest if configured.

---

## 9. What is the role of kubelet, kube-proxy, and the API server?

**Answer:**
- **kube-apiserver**: The front-end of the control plane; all cluster communication goes through it.
- **kubelet**: An agent running on each node that ensures containers are running in a Pod as expected.
- **kube-proxy**: Maintains network rules on nodes, enabling communication to Pods from inside or outside the cluster.

---

## 10. How do you perform a rolling update and rollback in Kubernetes?

**Answer:**
Rolling updates are done by updating the Deployment's Pod template (e.g., a new image version):
```bash
kubectl set image deployment/my-app my-app=myimage:v2
```
Kubernetes gradually replaces old Pods with new ones based on the update strategy (`maxSurge`, `maxUnavailable`).

To rollback:
```bash
kubectl rollout undo deployment/my-app
```

---

## 11. What is a Persistent Volume (PV) and Persistent Volume Claim (PVC)?

**Answer:**
- **PV**: A piece of storage provisioned in the cluster, independent of Pod lifecycle.
- **PVC**: A request for storage by a user; it binds to a matching PV based on size and access mode.

This decouples storage management from Pod configuration, allowing data persistence even if Pods are deleted.

---

## 12. What is the difference between `kubectl apply` and `kubectl create`?

**Answer:**
- `kubectl create`: Creates a resource; fails if the resource already exists.
- `kubectl apply`: Applies configuration changes declaratively — creates the resource if it doesn't exist, or updates it if it does. `apply` is preferred for managing resources via version-controlled YAML files.

---

## 13. How does Kubernetes handle scaling?

**Answer:**
- **Manual scaling**: `kubectl scale deployment my-app --replicas=5`
- **Horizontal Pod Autoscaler (HPA)**: Automatically scales the number of Pods based on CPU/memory usage or custom metrics.
- **Vertical Pod Autoscaler (VPA)**: Adjusts resource requests/limits for containers automatically.
- **Cluster Autoscaler**: Adjusts the number of nodes in the cluster based on resource demand.

---

## 14. What are Labels and Selectors used for?

**Answer:**
Labels are key-value pairs attached to objects (like Pods) for identification and grouping. Selectors are used by Services, Deployments, and other controllers to find and manage the objects matching specific labels — this is core to how Kubernetes links resources together.

---

## 15. What happens when a node goes down in a Kubernetes cluster?

**Answer:**
The control plane detects the node failure (via missed heartbeats from kubelet). After a grace period, the node is marked `NotReady`, and the scheduler reschedules the Pods that were running on it onto healthy nodes (assuming they're managed by a controller like a Deployment or ReplicaSet, not standalone Pods).

---

## 16. What is an Ingress and how is it different from a Service?

**Answer:**
An **Ingress** manages external HTTP/HTTPS access to services within the cluster, providing features like URL-based routing, SSL termination, and virtual hosting — all through a single external IP. A **Service** (like LoadBalancer) typically exposes one application, whereas Ingress can route to multiple services based on rules, reducing the need for multiple load balancers.

---

## 17. What are Taints and Tolerations?

**Answer:**
- **Taints** are applied to nodes to repel Pods that don't have a matching toleration, preventing certain Pods from being scheduled there.
- **Tolerations** are applied to Pods, allowing (but not requiring) them to be scheduled on nodes with matching taints.

This mechanism is often used to dedicate nodes for specific workloads.

---

## 18. How do you debug a Pod that is in `CrashLoopBackOff` state?

**Answer:**
1. Check logs: `kubectl logs <pod-name> --previous`
2. Describe the pod for events: `kubectl describe pod <pod-name>`
3. Check resource limits, misconfigured environment variables, or missing dependencies.
4. Verify the container's entrypoint/command and readiness/liveness probe configuration.
5. Exec into the pod (if it stays up briefly): `kubectl exec -it <pod-name> -- /bin/sh`

---

## 19. What is the difference between `resources.requests` and `resources.limits`?

**Answer:**
- **requests**: The minimum amount of CPU/memory guaranteed to a container; used by the scheduler to decide node placement.
- **limits**: The maximum amount of CPU/memory a container can use; if exceeded, the container may be throttled (CPU) or killed (memory - OOMKilled).

---

## 20. How would you troubleshoot a Service that is not routing traffic to Pods?

**Answer:**
1. Verify the Service's selector matches the Pod's labels: `kubectl describe svc <service-name>`
2. Check if the Pods are in `Running` state and passing readiness probes.
3. Confirm the Endpoints object has valid Pod IPs: `kubectl get endpoints <service-name>`
4. Check network policies that might be blocking traffic.
5. Test connectivity from within the cluster using a temporary debug Pod.

---

## 21. What is a DaemonSet and when would you use one?

**Answer:**
A DaemonSet ensures that a copy of a Pod runs on all (or a selected subset of) nodes in the cluster. It's commonly used for cluster-wide utilities like log collectors (Fluentd), monitoring agents (Node Exporter), or networking components (CNI plugins). When a new node joins the cluster, the DaemonSet automatically schedules the Pod on it.

---

## 22. What is the difference between a Job and a CronJob?

**Answer:**
- **Job**: Creates one or more Pods and ensures a specified number of them successfully complete (used for batch/one-time tasks).
- **CronJob**: Schedules Jobs to run periodically based on a cron expression (e.g., backups, report generation, cleanup tasks).

```bash
kubectl create job my-job --image=busybox -- echo "hello"
```

---

## 23. What are Init Containers and why are they used?

**Answer:**
Init containers run and complete before the main application containers start in a Pod. They're used for setup tasks like waiting for a dependency to be available, cloning a repo, or setting file permissions. If an init container fails, the Pod restarts it until it succeeds (or according to the Pod's restart policy).

---

## 24. What is the purpose of a multi-container Pod, and what are common patterns?

**Answer:**
Multiple containers in a Pod share network and storage, useful when containers need to work closely together. Common patterns:
- **Sidecar**: A helper container that extends the main container (e.g., log shipper).
- **Ambassador**: Proxies network requests to/from the main container.
- **Adapter**: Standardizes/transforms output from the main container (e.g., formatting logs/metrics).

---

## 25. What is RBAC in Kubernetes?

**Answer:**
Role-Based Access Control (RBAC) regulates who can perform which actions on which resources in the cluster. Key objects:
- **Role / ClusterRole**: Define a set of permissions (verbs like get, list, create) on resources, scoped to a namespace (Role) or cluster-wide (ClusterRole).
- **RoleBinding / ClusterRoleBinding**: Bind a Role/ClusterRole to a user, group, or service account.

---

## 26. What is a NetworkPolicy?

**Answer:**
A NetworkPolicy controls traffic flow at the IP/port level between Pods, namespaces, or external endpoints. By default, all Pods can communicate with each other; NetworkPolicies let you restrict this — for example, allowing only frontend Pods to talk to backend Pods on a specific port. Requires a CNI plugin that supports NetworkPolicy (e.g., Calico, Cilium).

---

## 27. What is the difference between Node Affinity, Pod Affinity, and Pod Anti-Affinity?

**Answer:**
- **Node Affinity**: Schedules Pods onto nodes matching specific labels (e.g., only nodes with `disktype=ssd`).
- **Pod Affinity**: Schedules Pods close to other Pods (e.g., same node/zone) based on labels — useful for latency-sensitive apps.
- **Pod Anti-Affinity**: Prevents Pods from being scheduled together (e.g., spreading replicas across nodes/zones for high availability).

---

## 28. What is a PodDisruptionBudget (PDB)?

**Answer:**
A PDB limits the number of Pods of a replicated application that can be voluntarily disrupted at the same time (e.g., during node drains or cluster upgrades), ensuring a minimum number of Pods stay available. Example: `minAvailable: 2` ensures at least 2 Pods are always running during maintenance.

---

## 29. What is etcd and why is it important?

**Answer:**
etcd is a distributed, consistent key-value store used as Kubernetes' primary datastore — it holds the entire cluster state (all objects, configs, and secrets). If etcd is lost or corrupted without a backup, the cluster loses all state, so etcd backup and high availability are critical for production clusters.

---

## 30. How do resource quotas and limit ranges work at the namespace level?

**Answer:**
- **ResourceQuota**: Limits the total amount of compute resources (CPU, memory), object counts (Pods, Services), or storage that can be consumed within a namespace.
- **LimitRange**: Sets default, minimum, and maximum resource requests/limits for individual containers/Pods within a namespace, so users don't have to set them explicitly, and no single Pod can consume excessive resources.

---

## 31. What is a Horizontal Pod Autoscaler and how does it decide when to scale?

**Answer:**
HPA automatically adjusts the number of Pod replicas in a Deployment/ReplicaSet/StatefulSet based on observed metrics (CPU utilization, memory, or custom/external metrics via the Metrics Server or Prometheus Adapter). It periodically checks metrics against a target threshold and scales replicas up or down accordingly, within defined min/max bounds.

---

## 32. What is Helm and why is it used?

**Answer:**
Helm is a package manager for Kubernetes that simplifies deploying and managing applications using "charts" — pre-configured, reusable YAML templates with configurable values. It helps with versioning, templating, and rollback of complex application deployments, avoiding repetitive manual manifest writing.

---

## 33. What is the difference between `kubectl exec`, `kubectl logs`, and `kubectl describe`?

**Answer:**
- `kubectl exec -it <pod> -- <command>`: Runs a command inside a running container (e.g., open a shell).
- `kubectl logs <pod>`: Retrieves stdout/stderr logs from a container.
- `kubectl describe <resource> <name>`: Shows detailed configuration and recent events for a resource — key for troubleshooting scheduling or startup issues.

---

## 34. How does Kubernetes secret management work, and what are its limitations?

**Answer:**
Secrets are stored in etcd, base64-encoded (not encrypted) by default, which means anyone with etcd or API access could decode them. Limitations can be mitigated by:
- Enabling encryption at rest for etcd.
- Using RBAC to restrict Secret access.
- Integrating external secret managers (HashiCorp Vault, AWS Secrets Manager) via tools like External Secrets Operator.

---

## 35. What happens during a `kubectl drain` on a node?

**Answer:**
`kubectl drain` safely evicts all Pods from a node (respecting PodDisruptionBudgets) so it can be maintained or removed — typically used before upgrades or decommissioning. It marks the node unschedulable (`cordon`) and evicts Pods, which are then rescheduled onto other available nodes by their controllers.

---

## 36. What is the difference between `Recreate` and `RollingUpdate` deployment strategies?

**Answer:**
- **Recreate**: Terminates all existing Pods before creating new ones — causes downtime but ensures no two versions run simultaneously (useful when app versions are incompatible).
- **RollingUpdate** (default): Gradually replaces old Pods with new ones with zero downtime, controlled by `maxSurge` (extra Pods allowed during update) and `maxUnavailable` (Pods allowed to be down during update).

---

## 37. How do you set up a container to restart only under certain conditions?

**Answer:**
This is controlled by the Pod's `restartPolicy`:
- **Always** (default for Deployments): Always restart the container on failure or completion.
- **OnFailure**: Restart only if the container exits with a non-zero (error) status — common for Jobs.
- **Never**: Never restart automatically, regardless of exit status.

---

## 38. What's the difference between a StatefulSet's stable network identity and a Deployment's Pods?

**Answer:**
StatefulSet Pods get a stable, predictable hostname and DNS entry (e.g., `mysql-0`, `mysql-1`) that persists across restarts/rescheduling, along with a dedicated PVC per Pod. Deployment Pods get random names/IPs and are treated as interchangeable — none of them have a persistent identity, which is unsuitable for stateful workloads like databases.

---

## 39. How would you troubleshoot high memory/CPU usage causing Pods to be OOMKilled?

**Answer:**
1. Check Pod status/events: `kubectl describe pod <pod-name>` (look for `OOMKilled` under last state).
2. Review current usage: `kubectl top pod <pod-name>`.
3. Compare against defined `resources.limits` — the limit may be too low for actual usage.
4. Check for memory leaks in application logs/metrics over time.
5. Adjust limits/requests or optimize the application, and consider using an HPA/VPA for dynamic scaling.

---

## 40. What is the difference between a ClusterIP Service and headless Service?

**Answer:**
A standard **ClusterIP** Service gets a single virtual IP and load-balances traffic across matching Pods. A **headless Service** (`clusterIP: None`) doesn't get a virtual IP — instead, DNS lookups return the individual Pod IPs directly, which is essential for StatefulSets where clients need to address specific Pods directly (e.g., connecting to a specific database replica).

---

## Tips for This Experience Level

Interviewers at the 1–3 year level typically focus on:
- Practical, hands-on knowledge (kubectl commands, YAML manifests)
- Debugging and troubleshooting scenarios
- Core object types (Pods, Deployments, Services, ConfigMaps, Secrets)
- Basic architecture understanding (control plane vs. worker nodes)

Be ready to walk through real examples from your own project experience, not just definitions.

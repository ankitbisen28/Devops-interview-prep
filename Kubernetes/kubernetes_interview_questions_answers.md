# Kubernetes Interview Questions and Answers (1–3 Years DevOps Experience)

## 1. What is Kubernetes?

Kubernetes is a container orchestration tool used to automate deployment, scaling, and management of containerized applications.

In simple words:
- Docker helps run containers.
- Kubernetes helps manage many containers automatically.

Example:
If one container crashes, Kubernetes restarts it automatically.

---

## 2. Why do we use Kubernetes?

We use Kubernetes because it helps:
- Auto-heal applications
- Scale applications automatically
- Manage containers easily
- Deploy applications with minimum downtime
- Balance traffic between containers

---

## 3. What is a Pod in Kubernetes?

A Pod is the smallest unit in Kubernetes.

It contains:
- One or more containers
- Shared network
- Shared storage

Usually, one application container runs inside one Pod.

---

## 4. What is the difference between Docker and Kubernetes?

| Docker | Kubernetes |
|---|---|
| Runs containers | Manages containers |
| Single host mainly | Multiple servers/clusters |
| Container engine | Orchestration platform |
| No auto-healing | Auto-healing supported |

Simple answer:
Docker creates containers, Kubernetes manages them.

---

## 5. What is a Kubernetes Cluster?

A Kubernetes cluster is a group of machines (nodes) working together.

It contains:
- Master Node (Control Plane)
- Worker Nodes

---

## 6. What is a Master Node?

Master node controls the Kubernetes cluster.

It manages:
- Scheduling
- Monitoring
- API requests
- Cluster state

Main components:
- API Server
- Scheduler
- Controller Manager
- etcd

---

## 7. What is a Worker Node?

Worker node is where applications actually run.

It contains:
- Pods
- Container runtime
- kubelet
- kube-proxy

---

## 8. What is kubelet?

kubelet is an agent running on every worker node.

Responsibilities:
- Talks with master node
- Ensures Pods are running properly
- Reports node status

---

## 9. What is kube-proxy?

kube-proxy manages networking inside Kubernetes.

It helps:
- Route traffic
- Load balance traffic between Pods

---

## 10. What is etcd?

etcd is a key-value database used by Kubernetes.

It stores:
- Cluster configuration
- Secrets
- Current cluster state

---

## 11. What is Deployment in Kubernetes?

Deployment is used to manage Pods and ReplicaSets.

It helps:
- Create Pods
- Update Pods
- Rollback changes
- Scale applications

---

## 12. What is ReplicaSet?

ReplicaSet ensures desired number of Pods are always running.

Example:
If one Pod crashes, ReplicaSet creates another automatically.

---

## 13. Difference between Pod and Deployment?

| Pod | Deployment |
|---|---|
| Single running unit | Manages Pods |
| No auto-scaling | Supports scaling |
| Manual management | Automatic management |

---

## 14. What is a Service in Kubernetes?

Service exposes Pods internally or externally.

Types:
- ClusterIP
- NodePort
- LoadBalancer

---

## 15. Explain ClusterIP Service.

ClusterIP is the default service type.

- Accessible only inside cluster
- Used for internal communication

---

## 16. Explain NodePort Service.

NodePort exposes application on worker node port.

Example:
`NodeIP:30007`

---

## 17. Explain LoadBalancer Service.

LoadBalancer exposes application externally using cloud load balancer.

Mostly used in:
- AWS
- Azure
- GCP

---

## 18. What is Namespace?

Namespace is used to logically separate resources inside cluster.

Example:
- dev namespace
- test namespace
- prod namespace

---

## 19. What is ConfigMap?

ConfigMap stores non-sensitive configuration data.

Example:
- Application URLs
- Environment variables
- Port numbers

---

## 20. What is Secret in Kubernetes?

Secrets store sensitive information securely.

Example:
- Passwords
- API keys
- Tokens

---

## 21. Difference between ConfigMap and Secret?

| ConfigMap | Secret |
|---|---|
| Non-sensitive data | Sensitive data |
| Plain text | Encoded |
| Public configs | Passwords/tokens |

---

## 22. What is Ingress?

Ingress manages external HTTP/HTTPS access to applications.

Benefits:
- URL-based routing
- SSL termination
- Single entry point

---

## 23. What is Helm?

Helm is a package manager for Kubernetes.

It helps:
- Simplify deployments
- Reuse templates
- Manage complex applications

---

## 24. What is a Helm Chart?

Helm Chart is a collection of Kubernetes YAML files.

It contains:
- Deployments
- Services
- ConfigMaps
- Templates

---

## 25. What is Horizontal Pod Autoscaler (HPA)?

HPA automatically increases or decreases Pods based on CPU or memory usage.

---

## 26. What is Rolling Update?

Rolling update updates application gradually without downtime.

Old Pods are replaced slowly with new Pods.

---

## 27. What is Rollback in Kubernetes?

Rollback means reverting application to previous stable version.

Useful when new deployment fails.

Example:
```bash
kubectl rollout undo deployment nginx
```

---

## 28. What is DaemonSet?

DaemonSet ensures one Pod runs on every worker node.

Common use cases:
- Monitoring agents
- Log collectors

---

## 29. What is StatefulSet?

StatefulSet is used for stateful applications.

Examples:
- MySQL
- MongoDB
- Kafka

---

## 30. What is Persistent Volume (PV)?

Persistent Volume provides permanent storage in Kubernetes.

Data remains safe even if Pod restarts.

---

## 31. What is Persistent Volume Claim (PVC)?

PVC is a request for storage by a Pod.

Pod uses PVC to access storage.

---

## 32. What is Taint and Toleration?

Taint:
Applied on node to restrict Pod scheduling.

Toleration:
Allows Pod to run on tainted node.

---

## 33. What is Node Selector?

Node Selector forces Pod to run on a specific node using labels.

---

## 34. What is kubectl?

`kubectl` is Kubernetes command line tool.

Used for:
- Creating resources
- Viewing Pods
- Checking logs
- Managing cluster

---

## 35. Common kubectl Commands

```bash
kubectl get pods
kubectl get nodes
kubectl describe pod pod-name
kubectl logs pod-name
kubectl apply -f file.yaml
kubectl delete pod pod-name
```

---

## 36. How do you troubleshoot a Pod not starting?

Steps:
1. Check Pod status
2. Describe Pod
3. Check logs
4. Check events and image issues

Commands:
```bash
kubectl get pods
kubectl describe pod pod-name
kubectl logs pod-name
```

---

## 37. What happens if a Pod crashes?

Kubernetes automatically restarts the Pod.

This feature is called self-healing.

---

## 38. What is CNI in Kubernetes?

CNI stands for Container Network Interface.

It manages networking between Pods.

Popular plugins:
- Calico
- Flannel
- Weave

---

## 39. What is the use of Labels in Kubernetes?

Labels are key-value pairs attached to resources.

Used for:
- Identification
- Filtering
- Grouping resources

Example:
```yaml
app: nginx
env: prod
```

---

## 40. Explain Kubernetes Architecture in Simple Words.

Kubernetes architecture mainly has:
- Master Node → controls everything
- Worker Nodes → runs applications

Master handles:
- Scheduling
- Monitoring
- API

Workers handle:
- Running containers
- Networking
- Communication

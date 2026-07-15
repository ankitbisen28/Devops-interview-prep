# 10 Most Common Kubernetes Production Issues with Solutions and Examples

For a **0–2 years DevOps/Kubernetes interview**, production troubleshooting is one of the most frequently tested topics. Interviewers often present a real-world issue and expect you to explain **how you would diagnose it step by step**, not just the final answer.

---

# 1. Pod is in Pending State

## Scenario
Your application deployment completed successfully, but the Pod remains in the **Pending** state and never starts.

Example:
```bash
kubectl get pods
NAME          READY   STATUS    RESTARTS
frontend      0/1     Pending   0
```

## Step 1: Check Pod Details
```bash
kubectl describe pod frontend
```

Focus on the **Events** section.

Example:
```text
Warning FailedScheduling
0/3 nodes are available:
Insufficient memory.
```

## Step 2: Check Node Status
```bash
kubectl get nodes
```

## Step 3: Check Resource Availability
```bash
kubectl top nodes
```

## Step 4: Check Resource Requests
```bash
kubectl describe pod frontend
```

### Other Possible Causes
- Persistent Volume Claim is Pending
- Node Selector mismatch
- Taints and tolerations
- Affinity rules
- ImagePullSecret issues

### Solution
- Increase cluster resources
- Reduce CPU/Memory requests
- Fix PVC
- Remove invalid nodeSelector
- Add tolerations if required

---

# 2. CrashLoopBackOff

## Scenario
The Pod starts but continuously crashes.

```bash
kubectl get pods
frontend   CrashLoopBackOff
```

## Step 1
```bash
kubectl logs frontend
```

Example:
```text
Database connection refused
```

## Step 2
```bash
kubectl describe pod frontend
```

Look for:
- Last State
- Exit Code
- Restart Count

## Step 3
Check ConfigMaps and Secrets.

## Step 4
Verify Database Connectivity:
```bash
kubectl exec -it frontend -- sh
ping mysql
nc -zv mysql 3306
```

## Step 5
Check application configuration.

### Solution
```bash
kubectl rollout restart deployment frontend
```

---

# 3. ImagePullBackOff

## Scenario
Pod cannot download Docker image.

## Step 1
```bash
kubectl describe pod frontend
```

Example:
```text
Failed to pull image
manifest unknown
```

## Step 2
Verify deployment image.

```bash
kubectl get deployment frontend -o yaml
```

## Step 3
Verify image manually:
```bash
docker pull myrepo/frontend:v100
```

## Step 4
Check imagePullSecrets:
```bash
kubectl get secrets
```

### Solution
- Fix image tag
- Push image
- Create imagePullSecret
- Update deployment

---

# 4. Application Not Accessible

## Troubleshooting Flow

1. Check Pods
```bash
kubectl get pods
```

2. Check Deployment
```bash
kubectl get deployment
```

3. Check Service
```bash
kubectl get svc
```

4. Check Endpoints
```bash
kubectl get endpoints
```

5. Test Service
```bash
kubectl port-forward svc/frontend 8080:80
```

6. Check Ingress
```bash
kubectl get ingress
```

7. Check DNS
```bash
nslookup app.company.com
```

### Common Causes
- Wrong selector
- Wrong service port
- Pod not ready
- Ingress issue
- DNS issue

---

# 5. Service Has No Endpoints

Example:
```bash
kubectl get endpoints frontend
```

## Step 1
```bash
kubectl describe svc frontend
```

## Step 2
Check labels:
```bash
kubectl get pods --show-labels
```

### Root Cause
Selector mismatch.

### Solution
Ensure labels match:

Deployment:
```yaml
app: frontend
```

Service:
```yaml
selector:
  app: frontend
```

---

# 6. Node NotReady

Example:
```bash
kubectl get nodes
worker-2   NotReady
```

## Step 1
```bash
kubectl describe node worker-2
```

Check:
- MemoryPressure
- DiskPressure
- PIDPressure

## Step 2
SSH into node:
```bash
systemctl status kubelet
```

## Step 3
Check disk:
```bash
df -h
```

## Step 4
Check kubelet logs:
```bash
journalctl -u kubelet
```

### Solution
```bash
systemctl restart kubelet
```

Free disk space or reboot if necessary.

---

# 7. OOMKilled

## Meaning
Container exceeded memory limit.

## Step 1
```bash
kubectl describe pod frontend
```

## Step 2
Check resource usage:
```bash
kubectl top pod
```

Example:
- Usage: 800Mi
- Limit: 512Mi

### Solution
Increase memory limits:

```yaml
resources:
  limits:
    memory: 1Gi
```

---

# 8. ConfigMap or Secret Changes Not Reflected

## Reason
Pods do not automatically restart after ConfigMap changes.

### Solution
```bash
kubectl rollout restart deployment frontend
```

or

```bash
kubectl delete pod <pod-name>
```

---

# 9. Persistent Volume Claim Pending

## Step 1
```bash
kubectl describe pvc
```

## Step 2
```bash
kubectl get storageclass
```

## Step 3
```bash
kubectl get pv
```

### Solution
- Create PV
- Correct StorageClass
- Install CSI Driver

---

# 10. Deployment Failed After New Release

## Step 1
```bash
kubectl rollout status deployment frontend
```

## Step 2
```bash
kubectl get rs
```

## Step 3
Rollback:
```bash
kubectl rollout undo deployment frontend
```

### Root Causes
- Bad image
- Bad ConfigMap
- Wrong Secret
- Application bug
- Failed database migration

### Solution
Rollback to previous version and investigate.

---

# Production Troubleshooting Checklist

## 1. Understand the problem
- What is failing?
- When did it start?
- Was there a recent deployment?

## 2. Check cluster health
```bash
kubectl get nodes
kubectl get pods -A
kubectl get events --sort-by=.metadata.creationTimestamp
```

## 3. Inspect workload
```bash
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl logs <pod-name> --previous
```

## 4. Verify networking
```bash
kubectl get svc
kubectl get endpoints
kubectl get ingress
```

## 5. Check resources
```bash
kubectl top nodes
kubectl top pods
```

## 6. Review configuration
```bash
kubectl get configmap
kubectl get secret
```

## 7. Implement fix
Update configuration, image, or resources.

## 8. Validate
```bash
kubectl rollout status deployment <deployment-name>
kubectl get pods
curl http://<service-endpoint>
```

## 9. Monitor
Ensure application stability.

## 10. Document
Record RCA, fix, and preventive actions.

---

# Interview Framework

When troubleshooting, follow this approach:

1. Identify symptom
2. Collect evidence (`kubectl get`, `describe`, `logs`, `events`)
3. Find root cause
4. Apply fix
5. Validate fix
6. Explain prevention steps

This structured troubleshooting methodology is highly valued for Kubernetes L2 Support and DevOps roles.

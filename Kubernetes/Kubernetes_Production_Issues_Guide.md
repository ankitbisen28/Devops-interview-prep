# Top 10 Common Kubernetes Production Issues with Solutions

## 1. Pod Stuck in Pending State
### Symptoms
```bash
kubectl get pods
```
Output:
```text
frontend   0/1   Pending
```

### Troubleshooting Steps
1. Check pod events:
```bash
kubectl describe pod frontend
```

2. Check node status:
```bash
kubectl get nodes
```

3. Check cluster resources:
```bash
kubectl top nodes
```

4. Verify resource requests and limits.

### Common Causes
- Insufficient CPU/Memory
- PVC Pending
- Node Selector mismatch
- Taints and tolerations
- Node NotReady

### Solution
- Increase cluster capacity
- Reduce resource requests
- Fix PVC or node selector configuration

---

## 2. CrashLoopBackOff

### Symptoms
```bash
kubectl get pods
```

### Troubleshooting Steps
```bash
kubectl logs <pod>
kubectl describe pod <pod>
kubectl logs <pod> --previous
```

Check:
- Application errors
- ConfigMap/Secret values
- Database connectivity
- Startup commands

### Example
Application unable to connect to MySQL because wrong hostname is configured.

### Solution
Fix configuration and restart deployment:
```bash
kubectl rollout restart deployment frontend
```

---

## 3. ImagePullBackOff

### Symptoms
Pod unable to pull image.

### Troubleshooting
```bash
kubectl describe pod <pod>
```

Verify:
- Image name
- Image tag
- ImagePullSecret
- Registry accessibility

### Example
```yaml
image: myrepo/frontend:v100
```
Tag does not exist.

### Solution
Push correct image or update deployment.

---

## 4. Application Not Accessible

### Troubleshooting Flow

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

5. Check Ingress
```bash
kubectl get ingress
```

6. Verify DNS
```bash
nslookup app.company.com
```

### Common Causes
- Wrong selector
- Service port mismatch
- Ingress issue
- DNS issue

---

## 5. Service Has No Endpoints

### Symptoms
```bash
kubectl get endpoints frontend
```

Output:
```text
No endpoints available
```

### Root Cause
Label mismatch between Service and Pods.

### Verification
```bash
kubectl describe svc frontend
kubectl get pods --show-labels
```

### Solution
Ensure labels match:

```yaml
selector:
  app: frontend
```

---

## 6. Node NotReady

### Troubleshooting

```bash
kubectl describe node worker-1
journalctl -u kubelet
systemctl status kubelet
df -h
```

### Possible Causes
- Disk full
- Kubelet down
- Network issue
- Resource pressure

### Solution
Restart kubelet:

```bash
systemctl restart kubelet
```

---

## 7. OOMKilled

### Symptoms
```bash
kubectl describe pod <pod>
```

Output:
```text
Last State: OOMKilled
```

### Troubleshooting

```bash
kubectl top pod
```

Compare usage with limits.

### Solution

Increase limits:

```yaml
resources:
  limits:
    memory: 1Gi
```

---

## 8. ConfigMap/Secret Changes Not Reflected

### Cause
Pods do not reload configuration automatically.

### Solution

```bash
kubectl rollout restart deployment frontend
```

or

```bash
kubectl delete pod <pod>
```

---

## 9. PVC Pending

### Troubleshooting

```bash
kubectl get pvc
kubectl describe pvc
kubectl get pv
kubectl get storageclass
```

### Causes
- No StorageClass
- No available PV
- CSI driver issue

### Solution
Create PV or configure proper StorageClass.

---

## 10. Failed Deployment After Release

### Troubleshooting

```bash
kubectl rollout status deployment frontend
kubectl get rs
kubectl logs <pod>
```

### Rollback

```bash
kubectl rollout undo deployment frontend
```

### Common Causes
- Bad image
- Incorrect ConfigMap
- Application bug
- Database migration failure

---

# Production Troubleshooting Checklist

## Step 1: Understand the Issue
- What is failing?
- When did it start?
- Was there a recent deployment?

## Step 2: Cluster Health

```bash
kubectl get nodes
kubectl get pods -A
kubectl get events --sort-by=.metadata.creationTimestamp
```

## Step 3: Investigate Pods

```bash
kubectl describe pod <pod>
kubectl logs <pod>
kubectl logs <pod> --previous
```

## Step 4: Verify Networking

```bash
kubectl get svc
kubectl get endpoints
kubectl get ingress
```

## Step 5: Resource Usage

```bash
kubectl top nodes
kubectl top pods
```

## Step 6: Validate Configuration

```bash
kubectl get configmap
kubectl get secret
```

## Step 7: Apply Fix and Validate

```bash
kubectl rollout status deployment <deployment>
curl http://service-url
```

## Step 8: Monitor and Document RCA
- Root Cause
- Resolution
- Preventive Actions

---

# Interview Approach

1. Identify symptoms
2. Gather evidence
3. Find root cause
4. Fix issue
5. Validate solution
6. Document RCA

This structured troubleshooting methodology is commonly expected from Kubernetes L2 Support and DevOps Engineers.

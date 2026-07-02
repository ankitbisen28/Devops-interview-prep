# Kubernetes Scenario-Based Interview Questions (0--2 Years Experience)

## 1. Pod is stuck in Pending state

### Question

A pod has been in the **Pending** state for several minutes. How will
you troubleshoot it?

### Answer

First, check the pod details.

``` bash
kubectl get pods
kubectl describe pod <pod-name>
```

Possible reasons: - No worker node has enough CPU or memory. - PVC is
not bound. - Node is NotReady. - Taints without tolerations. - Scheduler
issue.

Check nodes:

``` bash
kubectl get nodes
```

If it's a PVC issue:

``` bash
kubectl get pvc
```

------------------------------------------------------------------------

## 2. Pod is in CrashLoopBackOff

### Question

How do you troubleshoot CrashLoopBackOff?

### Answer

``` bash
kubectl logs <pod-name>
kubectl logs <pod-name> --previous
kubectl describe pod <pod-name>
```

Common causes: - Wrong environment variables - Database connection
failure - Application bug - Missing Secret - Missing ConfigMap

------------------------------------------------------------------------

## 3. ImagePullBackOff

### Question

A pod shows ImagePullBackOff. What will you do?

### Answer

``` bash
kubectl describe pod <pod-name>
```

Possible reasons: - Wrong image name - Wrong image tag - Private
repository authentication issue - Docker Hub rate limit

Verify image:

``` bash
docker pull <image-name>
```

------------------------------------------------------------------------

## 4. Service is not accessible

### Answer

``` bash
kubectl get svc
kubectl get endpoints
kubectl get pods --show-labels
```

Common issue: - Service selector doesn't match Deployment labels.

------------------------------------------------------------------------

## 5. Node becomes NotReady

### Answer

``` bash
kubectl get nodes
kubectl describe node <node-name>
systemctl status kubelet
df -h
systemctl status containerd
```

------------------------------------------------------------------------

## 6. Deployment update failed

### Answer

``` bash
kubectl rollout status deployment <deployment-name>
kubectl rollout undo deployment <deployment-name>
kubectl rollout history deployment <deployment-name>
```

------------------------------------------------------------------------

## 7. Application cannot connect to database

### Answer

Check: - Service - Endpoint - DNS - Secret - Network Policy

``` bash
kubectl exec -it <pod-name> -- nslookup mysql
kubectl exec -it <pod-name> -- curl mysql:3306
```

------------------------------------------------------------------------

## 8. ConfigMap updated but application still shows old configuration

Restart the Deployment.

``` bash
kubectl rollout restart deployment <deployment-name>
```

------------------------------------------------------------------------

## 9. Secret updated

Restart the Deployment.

``` bash
kubectl rollout restart deployment <deployment-name>
```

------------------------------------------------------------------------

## 10. Pod consuming high CPU

``` bash
kubectl top pod
kubectl logs <pod-name>
```

Verify CPU requests and limits.

------------------------------------------------------------------------

## 11. Pod gets OOMKilled

``` bash
kubectl describe pod <pod-name>
```

Increase memory limits or investigate memory leaks.

------------------------------------------------------------------------

## 12. PVC remains Pending

``` bash
kubectl get pvc
kubectl describe pvc <pvc-name>
```

Possible reasons: - No StorageClass - No PersistentVolume - Wrong
StorageClass

------------------------------------------------------------------------

## 13. Ingress not working

``` bash
kubectl get ingress
kubectl get pods -n ingress-nginx
kubectl describe ingress <ingress-name>
```

------------------------------------------------------------------------

## 14. DNS resolution fails

``` bash
kubectl get pods -n kube-system
kubectl exec -it <pod-name> -- nslookup <service-name>
```

Check CoreDNS health.

------------------------------------------------------------------------

## 15. Pod keeps restarting

``` bash
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

Common reasons: - Liveness probe failure - Application crash - OOMKilled

------------------------------------------------------------------------

## 16. Deployment has 0 available pods

``` bash
kubectl rollout status deployment <deployment-name>
kubectl describe deployment <deployment-name>
```

------------------------------------------------------------------------

## 17. Kubernetes deployment successful but browser shows 404

Check: - Service - Ingress - Backend port - Path mapping

------------------------------------------------------------------------

## 18. One pod works while another fails

Compare:

``` bash
kubectl describe pod <pod-name>
kubectl logs <pod-name>
```

Possible reasons: - Different node - Different image - Missing Secret -
Corrupted cache

------------------------------------------------------------------------

## 19. Application is slow

``` bash
kubectl top pod
kubectl top node
```

Look for: - CPU bottleneck - Memory pressure - Database latency

------------------------------------------------------------------------

## 20. Namespace deleted accidentally

Recover only if backups (such as etcd snapshots) are available.
Otherwise, recreate resources using manifests or Helm charts.

------------------------------------------------------------------------

## 21. Readiness probe failing but liveness passing

The application is running but not ready to receive traffic. Check
readiness endpoint, startup time, and dependencies.

------------------------------------------------------------------------

## 22. One pod cannot communicate with another

Check: - Service - DNS - Network Policies - Firewall rules - Pod health

------------------------------------------------------------------------

## 23. Pods are scheduled unevenly

Check: - Node resources - Affinity/Anti-affinity - Taints/Tolerations -
Topology spread constraints

------------------------------------------------------------------------

## 24. Deployment update is stuck

Check: - Rollout status - Events - Image pull errors - Readiness probe
failures - Cluster resources

------------------------------------------------------------------------

## 25. Node is under DiskPressure

``` bash
df -h
```

Clean unused images, containers, and logs.

------------------------------------------------------------------------

## 26. Helm deployment fails

``` bash
helm status <release-name>
helm history <release-name>
helm template .
kubectl describe pod <pod-name>
kubectl get events
```

------------------------------------------------------------------------

## 27. Pods are not receiving traffic after deployment

Verify: - Pod readiness - Service selectors - Endpoints - Load Balancer
or Ingress - Readiness probes

------------------------------------------------------------------------

## 28. Debug inside a running pod

``` bash
kubectl exec -it <pod-name> -- /bin/sh
```

or

``` bash
kubectl exec -it <pod-name> -- /bin/bash
```

Check environment variables, files, DNS, and connectivity.

------------------------------------------------------------------------

## 29. Scale an application during high traffic

``` bash
kubectl scale deployment <deployment-name> --replicas=5
```

Or configure a Horizontal Pod Autoscaler (HPA).

------------------------------------------------------------------------

## 30. Production deployment failed at 2 AM

Recommended approach: 1. Assess impact. 2. Check pod status, events, and
logs. 3. Verify recent deployments or configuration changes. 4. Roll
back if needed. 5. Restore services. 6. Perform root cause analysis. 7.
Document findings and implement preventive measures.

------------------------------------------------------------------------

# Interview Answer Framework

For every Kubernetes troubleshooting scenario, answer using this
structure:

1.  **Identify the problem**
2.  **Investigate using commands** (`kubectl describe`, `kubectl logs`,
    `kubectl get events`, etc.)
3.  **Find the root cause**
4.  **Fix the issue**
5.  **Explain how to prevent it in the future**

Following this approach demonstrates practical troubleshooting skills
expected from a Kubernetes/DevOps engineer with 0--2 years of
experience.

# Kubernetes Scenario-Based Interview Questions (0--2 Years)

## Scenario 1: Pod is in Pending State

**Question:** Your Pod is stuck in `Pending` state. How will you
troubleshoot?

### Commands

``` bash
kubectl get pods
kubectl describe pod <pod-name>
kubectl get nodes
kubectl get events --sort-by=.metadata.creationTimestamp
```

### Common Causes

-   Insufficient CPU/Memory
-   PVC not bound
-   Node NotReady
-   Taints/Tolerations
-   Resource quota exceeded

### Solution

-   Check events and node status.
-   Reduce resource requests or add worker nodes.
-   Fix PVC, taints, or quotas.

------------------------------------------------------------------------

## Scenario 2: Pod in CrashLoopBackOff

**Commands**

``` bash
kubectl logs <pod-name>
kubectl logs <pod-name> --previous
kubectl describe pod <pod-name>
```

**Common Causes** - Application crash - Wrong environment variables -
Database unavailable - Startup command failure

**Solution** - Review logs, fix application/configuration, redeploy.

------------------------------------------------------------------------

## Scenario 3: ImagePullBackOff

``` bash
kubectl describe pod <pod-name>
```

**Causes** - Incorrect image tag - Private registry authentication
missing - Image doesn't exist

**Solution** - Correct image name/tag. - Configure `imagePullSecrets`.

------------------------------------------------------------------------

## Scenario 4: Node NotReady

``` bash
kubectl get nodes
kubectl describe node <node-name>
```

On the node:

``` bash
systemctl status kubelet
sudo systemctl restart kubelet
```

Check: - Disk space - Memory - Network connectivity

------------------------------------------------------------------------

## Scenario 5: Service Not Accessible

``` bash
kubectl get svc
kubectl get endpoints
kubectl describe svc <service-name>
```

Verify the Service selector matches Pod labels.

------------------------------------------------------------------------

## Scenario 6: ConfigMap Updated but Application Didn't Change

``` bash
kubectl rollout restart deployment <deployment-name>
```

Pods must restart to pick up updated environment variables from a
ConfigMap.

------------------------------------------------------------------------

## Scenario 7: Secret Updated

``` bash
kubectl rollout restart deployment <deployment-name>
```

------------------------------------------------------------------------

## Scenario 8: Deployment Rollback

``` bash
kubectl rollout status deployment <deployment-name>
kubectl rollout history deployment <deployment-name>
kubectl rollout undo deployment <deployment-name>
```

------------------------------------------------------------------------

## Scenario 9: Application Cannot Reach Database

``` bash
kubectl exec -it <pod-name> -- sh
nslookup mysql
```

Verify Service, Endpoints, DNS, and NetworkPolicy.

------------------------------------------------------------------------

## Scenario 10: DNS Resolution Failure

``` bash
kubectl exec <pod-name> -- nslookup kubernetes.default
kubectl get pods -n kube-system
```

Check CoreDNS health.

------------------------------------------------------------------------

## Scenario 11: PVC Pending

``` bash
kubectl get pvc
kubectl describe pvc <pvc-name>
```

Common reasons: - Missing StorageClass - No available PersistentVolume -
Size mismatch

------------------------------------------------------------------------

## Scenario 12: High CPU Usage

``` bash
kubectl top pods
kubectl top nodes
```

Increase CPU limits or investigate application performance.

------------------------------------------------------------------------

## Scenario 13: Pod Evicted

Usually caused by node memory or disk pressure.

``` bash
kubectl describe pod <pod-name>
```

------------------------------------------------------------------------

## Scenario 14: Ingress Returning 404

``` bash
kubectl describe ingress
kubectl get pods -n ingress-nginx
```

Verify host, path, backend service, and ingress controller.

------------------------------------------------------------------------

## Scenario 15: LoadBalancer External IP Pending

For Minikube:

``` bash
minikube tunnel
```

Or use a NodePort service.

------------------------------------------------------------------------

## Scenario 16: Pod Cannot Access Internet

``` bash
kubectl exec <pod-name> -- ping google.com
kubectl get networkpolicy
```

------------------------------------------------------------------------

## Scenario 17: Scaling Deployments

Manual scaling:

``` bash
kubectl scale deployment <deployment-name> --replicas=5
```

HPA:

``` bash
kubectl autoscale deployment <deployment-name> --cpu-percent=70 --min=2 --max=10
```

------------------------------------------------------------------------

## Scenario 18: Liveness Probe Failure

``` bash
kubectl describe pod <pod-name>
```

Verify the probe path, port, and application health.

------------------------------------------------------------------------

## Scenario 19: Readiness Probe Failure

Application is running but not receiving traffic.

Verify readiness probe configuration.

------------------------------------------------------------------------

## Scenario 20: OOMKilled

``` bash
kubectl describe pod <pod-name>
```

Increase memory requests/limits or optimize the application.

------------------------------------------------------------------------

# Frequently Used kubectl Commands

``` bash
kubectl get all
kubectl get pods -A
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl logs <pod-name> --previous
kubectl exec -it <pod-name> -- bash
kubectl get svc
kubectl get endpoints
kubectl get deployment
kubectl rollout status deployment <deployment-name>
kubectl rollout history deployment <deployment-name>
kubectl rollout undo deployment <deployment-name>
kubectl scale deployment <deployment-name> --replicas=3
kubectl top pods
kubectl top nodes
kubectl get events --sort-by=.metadata.creationTimestamp
kubectl get pvc
kubectl get pv
kubectl get ingress
kubectl get nodes
kubectl describe node <node-name>
```

# Rapid-Fire Interview Questions

1.  Pod stuck in Pending. What will you check first?
2.  CrashLoopBackOff troubleshooting steps?
3.  How do you verify Service selectors?
4.  ConfigMap updated but application unchanged. Why?
5.  How do you roll back a Deployment?
6.  What does OOMKilled mean?
7.  How do you troubleshoot a NotReady node?
8.  How do you debug DNS issues?
9.  Why does a PVC remain Pending?
10. Why is Ingress returning 404?

# Interview Strategy

Always follow this troubleshooting order:

1.  `kubectl get`
2.  `kubectl describe`
3.  `kubectl logs`
4.  Verify dependent resources (Service, Endpoints, PVC, Ingress,
    ConfigMap, Secret)
5.  Fix the issue and validate the solution.

# Kubernetes Day-to-Day Tasks for a DevOps Engineer (1--3 Years Experience)

## Overview

For a DevOps Engineer with 1--3 years of experience, Kubernetes work
mainly involves deployments, monitoring, troubleshooting, scaling, and
automation rather than designing clusters from scratch.

------------------------------------------------------------------------

## 1. Deploy Applications

``` bash
kubectl apply -f deployment.yaml
kubectl get pods
kubectl get svc
kubectl rollout status deployment/frontend
```

------------------------------------------------------------------------

## 2. Check Pod Health

``` bash
kubectl get pods -A
kubectl get pods -n production
kubectl describe pod frontend-76c6d8
kubectl logs frontend-76c6d8
```

Check for: - CrashLoopBackOff - Error - Pending - OOMKilled -
ImagePullBackOff

------------------------------------------------------------------------

## 3. Restart Pods

``` bash
kubectl rollout restart deployment frontend
kubectl delete pod frontend-xxxxx
```

------------------------------------------------------------------------

## 4. Check Logs

``` bash
kubectl logs pod-name
kubectl logs -f pod-name
kubectl logs pod-name -c nginx
```

Common errors: - Database connection failed - Connection timeout -
Authentication failed - Out of memory

------------------------------------------------------------------------

## 5. Troubleshoot CrashLoopBackOff

``` bash
kubectl describe pod pod-name
kubectl logs pod-name
```

Possible causes: - Wrong environment variable - Database unreachable -
Application bug - Wrong ConfigMap - Secret missing - Wrong image

------------------------------------------------------------------------

## 6. Rollout New Version

``` bash
kubectl set image deployment/frontend frontend=myrepo/frontend:v2
kubectl rollout status deployment/frontend
kubectl rollout undo deployment/frontend
```

------------------------------------------------------------------------

## 7. Scale Applications

``` bash
kubectl scale deployment frontend --replicas=5
kubectl get hpa
```

------------------------------------------------------------------------

## 8. Monitor Resource Usage

``` bash
kubectl top pods
kubectl top nodes
```

------------------------------------------------------------------------

## 9. Check Node Health

``` bash
kubectl get nodes
kubectl describe node worker-1
```

------------------------------------------------------------------------

## 10. Manage Namespaces

``` bash
kubectl get ns
kubectl create ns dev
kubectl delete ns test
```

------------------------------------------------------------------------

## 11. Update ConfigMap

``` bash
kubectl edit configmap app-config
kubectl apply -f configmap.yaml
kubectl rollout restart deployment frontend
```

------------------------------------------------------------------------

## 12. Manage Secrets

``` bash
kubectl create secret generic db-secret --from-literal=password=myPassword
kubectl get secrets
```

------------------------------------------------------------------------

## 13. Check Services

``` bash
kubectl get svc
kubectl describe svc frontend
```

------------------------------------------------------------------------

## 14. Verify Ingress

``` bash
kubectl get ingress
kubectl describe ingress app
```

------------------------------------------------------------------------

## 15. Debug Network Issues

``` bash
kubectl get endpoints
kubectl exec -it pod-name -- bash
curl service-name
nslookup service-name
```

------------------------------------------------------------------------

## 16. Execute Commands Inside a Pod

``` bash
kubectl exec -it frontend -- sh
```

------------------------------------------------------------------------

## 17. Check Events

``` bash
kubectl get events
kubectl get events --sort-by=.metadata.creationTimestamp
```

------------------------------------------------------------------------

## 18. Verify Persistent Volumes

``` bash
kubectl get pv
kubectl get pvc
```

------------------------------------------------------------------------

## 19. Manage Helm Releases

``` bash
helm install frontend ./frontend
helm upgrade frontend ./frontend
helm rollback frontend 1
helm list
```

------------------------------------------------------------------------

## 20. Check Deployment Status

``` bash
kubectl get deployments
kubectl describe deployment frontend
```

------------------------------------------------------------------------

## 21. Delete Unused Resources

``` bash
kubectl delete pod pod-name
kubectl delete deployment app
kubectl delete service app
```

------------------------------------------------------------------------

## 22. Monitor the Cluster

Monitor: - CPU - Memory - Disk - Network - Pod Restarts

------------------------------------------------------------------------

## 23. Investigate Alerts

Common alerts: - Node Not Ready - Pod Restarting - High CPU - High
Memory - Disk Full

------------------------------------------------------------------------

## 24. Investigate Failed Deployments

Flow:

Deployment → ReplicaSet → Pods → Logs → Events

------------------------------------------------------------------------

## 25. CI/CD Deployment Flow

Developer Push → GitHub → Jenkins → Docker Build → Docker Push → Helm
Upgrade → Kubernetes Deployment → Verify Pods → Smoke Test

------------------------------------------------------------------------

## 26. Backup Kubernetes Resources

``` bash
kubectl get all -A -o yaml > cluster-backup.yaml
```

------------------------------------------------------------------------

## 27. Drain a Node

``` bash
kubectl drain worker-1 --ignore-daemonsets
kubectl uncordon worker-1
```

------------------------------------------------------------------------

## 28. Verify Autoscaling

``` bash
kubectl get hpa
kubectl describe hpa
```

------------------------------------------------------------------------

## 29. Check Image Version

``` bash
kubectl describe deployment frontend
```

Verify the deployed image tag.

------------------------------------------------------------------------

## 30. Daily Health Check Checklist

1.  Check node status
2.  Check all pods
3.  Review restarting or failed pods
4.  Check CPU and memory usage
5.  Review monitoring dashboards
6.  Investigate overnight alerts
7.  Verify application health
8.  Review failed CI/CD pipelines
9.  Verify Ingress and Services
10. Confirm backups completed

------------------------------------------------------------------------

# Common Production Scenarios

  Scenario                      Action
  ----------------------------- -----------------------------------------------------
  CrashLoopBackOff              Check logs, events, ConfigMaps, Secrets
  New deployment                Perform rollout and verify status
  High CPU                      Check metrics and scale if needed
  Database connectivity issue   Verify Secrets, Services, and network
  Application downtime          Check Ingress, Services, Pods, and logs
  Pod Pending                   Check scheduler events and resources
  ImagePullBackOff              Verify image name, tag, and registry credentials
  Node NotReady                 Investigate kubelet, networking, and node resources

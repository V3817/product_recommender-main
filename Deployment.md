# Full Deployment Guide — Flipkart Product Recommendation System

# 1. Initial Setup

## Step 1 — Push Code to GitHub

### What Was Done

The complete project code was pushed to GitHub.

### Why This Step Was Needed

GitHub acts as:
- code backup
- version control
- deployment source for VM

This allows:
- cloning code inside VM
- easier updates
- collaboration
- CI/CD integration later

---

## Step 2 — Create Dockerfile

### What Was Done

A Dockerfile was created to containerize the Flask application.

### Why This Step Was Needed

Docker ensures:
- same environment everywhere
- dependency consistency
- portability
- easier Kubernetes deployment

Without Docker:
- package mismatch issues occur
- deployment becomes unstable

---

## Step 3 — Create Kubernetes Deployment File

### What Was Done

A Kubernetes deployment YAML file was created.

Example:
- deployment
- service
- environment variables
- secrets

### Why This Step Was Needed

Kubernetes manages:
- containers
- scaling
- networking
- orchestration

This allows:
- production-style deployment
- automatic pod management
- service exposure

---

# 2. Create GCP VM Instance

## What Was Done

A VM instance was created on Google Cloud Platform.

### Configuration Used

| Setting | Value |
|---|---|
| Machine Series | E2 |
| RAM | 16 GB |
| Disk | 256 GB |
| OS | Ubuntu 24.04 LTS |

HTTP and HTTPS traffic were enabled.

---

## Why This Step Was Needed

The VM acts as:
- cloud server
- Kubernetes host
- Docker runtime environment

The VM provides:
- compute power
- networking
- public accessibility

---

# 3. Connect to VM

## What Was Done

SSH connection was established using GCP browser terminal.

---

## Why This Step Was Needed

SSH access allows:
- package installation
- Docker setup
- Kubernetes setup
- deployment management

---

# 4. Clone GitHub Repository

## Commands Used

```bash
git clone <your_repo_url>

ls

cd <repo_name>

ls
```

---

## Why This Step Was Needed

The VM must contain:
- source code
- Dockerfile
- Kubernetes YAML files

This step downloads the project into the VM.

---

# 5. Install Docker

## What Was Done

Docker was installed on Ubuntu VM.

Docker service was enabled.

---

## Why This Step Was Needed

Docker is required because:
- Minikube internally uses Docker
- application runs inside containers
- Kubernetes manages containers

Without Docker:
- Kubernetes cannot run workloads

---

# 6. Verify Docker

## Commands Used

```bash
docker run hello-world

systemctl status docker

docker ps
```

---

## Why This Step Was Needed

Verification confirms:
- Docker daemon active
- containers can run properly

---

# 7. Install Minikube

## What Was Done

Minikube was installed inside the VM.

---

## Why This Step Was Needed

Minikube creates:
- local Kubernetes cluster
- single-node Kubernetes environment

This allows:
- Kubernetes deployment inside VM
- local orchestration testing

---

# 8. Start Minikube

## Command Used

```bash
minikube start
```

---

## Why This Step Was Needed

This starts:
- Kubernetes control plane
- Kubernetes node
- internal networking

Without starting Minikube:
- kubectl commands will fail

---

# 9. Install kubectl

## Command Used

```bash
sudo snap install kubectl --classic
```

---

## Why This Step Was Needed

kubectl is required to:
- communicate with Kubernetes
- deploy YAML files
- manage pods and services

---

# 10. Verify Kubernetes Cluster

## Commands Used

```bash
minikube status

kubectl get nodes

kubectl cluster-info
```

---

## Why This Step Was Needed

Verification ensures:
- Kubernetes cluster is healthy
- node is active
- API server running

---

# 11. Configure GitHub on VM

## Commands Used

```bash
git config --global user.email "your_email"

git config --global user.name "your_name"
```

---

## Why This Step Was Needed

This allows:
- pushing updates
- version control inside VM

---

# 12. Build Docker Image

## Commands Used

```bash
eval $(minikube docker-env)

docker build -t flask-app:latest .
```

---

## Why This Step Was Needed

### eval $(minikube docker-env)

This points Docker CLI to Minikube Docker daemon.

Without this:
- image builds locally outside Minikube
- Kubernetes cannot access image

---

### docker build

Creates container image containing:
- Flask app
- dependencies
- LangChain
- AstraDB integration
- RAG pipeline

---

# 13. Create Kubernetes Secrets

## Commands Used

```bash
kubectl create secret generic llmops-secrets \
--from-literal=GROQ_API_KEY="" \
--from-literal=ASTRA_DB_APPLICATION_TOKEN="" \
--from-literal=ASTRA_DB_KEYSPACE="default_keyspace" \
--from-literal=ASTRA_DB_API_ENDPOINT="" \
--from-literal=HF_TOKEN=""
```

---

## Why This Step Was Needed

Secrets securely store:
- API keys
- database tokens
- authentication credentials

Without secrets:
- credentials become exposed in YAML files

---

# 14. Deploy Flask Application

## Command Used

```bash
kubectl apply -f flask-deployment.yaml
```

---

## Why This Step Was Needed

This creates:
- deployment
- pods
- Kubernetes service

Kubernetes then:
- starts containers
- monitors health
- restarts failed pods automatically

---

# 15. Verify Pods

## Command Used

```bash
kubectl get pods
```

---

## Why This Step Was Needed

This checks:
- pod health
- deployment success
- crash status

Healthy pods show:

```text
Running
```

---

# 16. Check Logs

## Command Used

```bash
kubectl logs <pod-name>
```

---

## Why This Step Was Needed

Logs help debug:
- startup failures
- missing dependencies
- environment variable issues
- authentication errors

---

# 17. Port Forward Flask App

## Command Used

```bash
kubectl port-forward svc/flask-service 5000:80 --address 0.0.0.0
```

---

## Why This Step Was Needed

Port forwarding exposes:
- Kubernetes service
- externally through VM IP

This allows browser access using:

```text
http://<VM-IP>:5000
```

---

# 18. Firewall Configuration

## What Was Done

Firewall rules were manually configured inside GCP.

Enabled:
- HTTP traffic
- HTTPS traffic
- IPv4 access
- Load Balancer traffic

Source range:

```text
0.0.0.0/0
```

Applied to:
- all VM instances

---

## Why This Step Was Needed

By default:
- GCP blocks external incoming traffic

Even if:
- Flask works
- Kubernetes works
- Docker works

the application still remains inaccessible publicly.

Firewall rules were required to expose:
- Flask app
- Prometheus
- Grafana

---

## What 0.0.0.0/0 Means

```text
Allow traffic from anywhere on the internet
```

This publicly exposes the application.

---

## Ports Opened

| Port | Purpose |
|---|---|
| 5000 | Flask application |
| 9090 | Prometheus |
| 3000 | Grafana |
| 30000-32767 | Kubernetes NodePort range |

---

## Why Each Port Was Needed

### Port 5000

Used by Flask backend.

Accessible via:

```text
http://<VM-IP>:5000
```

---

### Port 9090

Used by Prometheus.

Allows:
- monitoring
- metrics inspection
- target health checking

---

### Port 3000

Used by Grafana.

Allows:
- dashboard visualization
- metric graphs
- observability panels

---

### Port Range 30000–32767

Required by Kubernetes NodePort services.

Without this:
- external Kubernetes access fails

---

# 19. Create Monitoring Namespace

## Command Used

```bash
kubectl create namespace monitoring
```

---

## Why This Step Was Needed

Namespaces separate:
- application workloads
- monitoring workloads

This improves:
- organization
- isolation
- management

---

# 20. Deploy Prometheus

## Commands Used

```bash
kubectl apply -f prometheus/prometheus-configmap.yaml

kubectl apply -f prometheus/prometheus-deployment.yaml
```

---

## Why This Step Was Needed

Prometheus collects:
- application metrics
- HTTP request count
- Kubernetes metrics

---

# 21. Access Prometheus

## Command Used

```bash
kubectl port-forward --address 0.0.0.0 svc/prometheus-service -n monitoring 9090:9090
```

---

## Why This Step Was Needed

This exposes Prometheus dashboard publicly.

Accessible through:

```text
http://<VM-IP>:9090
```

---

# 22. Deploy Grafana

## Command Used

```bash
kubectl apply -f grafana/grafana-deployment.yaml
```

---

## Why This Step Was Needed

Grafana visualizes:
- Prometheus metrics
- request counts
- monitoring dashboards

---

# 23. Access Grafana

## Command Used

```bash
kubectl port-forward --address 0.0.0.0 svc/grafana-service -n monitoring 3000:3000
```

---

## Why This Step Was Needed

This exposes Grafana publicly.

Accessible through:

```text
http://<VM-IP>:3000
```

---

# 24. Configure Grafana Data Source

## What Was Done

Prometheus was added as Grafana data source.

URL used:

```text
http://prometheus-service.monitoring.svc.cluster.local:9090
```

---

## Why This Step Was Needed

Grafana needs:
- Prometheus connection
- metric source

Without data source:
- dashboards cannot display metrics

---

# 25. Create Dashboards

## What Was Done

Visualization panels were created for:
- HTTP request count
- application monitoring
- Prometheus metrics

---

## Why This Step Was Needed

Dashboards provide:
- real-time monitoring
- observability
- system analytics
- traffic visualization

---

# Final Outcome

Successfully deployed:

- Flask AI application
- LangChain RAG pipeline
- AstraDB vector search
- Kubernetes orchestration
- Prometheus monitoring
- Grafana visualization
- Public cloud deployment on GCP

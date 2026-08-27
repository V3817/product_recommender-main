# Flipkart Product Recommendation System

An AI-powered Flipkart Product Recommendation System built using Retrieval-Augmented Generation (RAG), AstraDB, LangChain, Flask, Kubernetes, Prometheus, and Grafana.

## Features

- Semantic product search using embeddings
- Conversational product recommendations
- AstraDB vector database integration
- Llama 3 via Groq
- Session-aware chat memory
- Flask backend API
- Docker and Kubernetes deployment
- Prometheus monitoring
- Grafana visualization dashboard

---

## Tech Stack

- Flask
- LangChain
- AstraDB
- HuggingFace Embeddings
- Groq Llama 3
- Docker
- Kubernetes
- Prometheus
- Grafana
- GCP VM

---

## Project Structure

```text
flipkart_product_recommender/
│
├── app/
├── data/
├── k8s/
├── monitoring/
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
└── PRD.md
```

---

## Installation

### Clone Repository

```bash
git clone <repo_url>
cd flipkart_product_recommender
```

### Create Virtual Environment

```bash
uv venv
source .venv/bin/activate
```

### Install Dependencies

```bash
uv pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
ASTRA_DB_API_ENDPOINT=
ASTRA_DB_APPLICATION_TOKEN=
ASTRA_DB_KEYSPACE=

HF_TOKEN=
GROQ_API_KEY=
```

---

## Run Application

```bash
python app.py
```

---

## Monitoring

### Prometheus
- Collects metrics
- Tracks request count
- Exposes `/metrics` endpoint

### Grafana
- Visualizes Prometheus metrics
- Displays monitoring dashboards

---

## Deployment

- Dockerized application
- Kubernetes deployment support
- GCP VM deployment
- Minikube support

---

## Future Improvements

- Redis caching
- CI/CD pipeline
- Hybrid search
- Authentication system
- GKE deployment

---

## Author

Aryal Katkar
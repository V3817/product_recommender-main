# PRD — Flipkart Product Recommendation System using RAG, AstraDB, LangChain, Kubernetes, Prometheus & Grafana

## 1. Project Overview

The Flipkart Product Recommendation System is a Retrieval-Augmented Generation (RAG)-based AI application designed to provide intelligent product recommendations using product reviews and conversational context.

The system utilizes:
- Vector similarity search
- Conversational AI
- Retrieval-Augmented Generation (RAG)
- Cloud-native deployment
- Monitoring and observability

Users can ask product-related questions such as:
- "Suggest good wireless headphones under ₹2000"
- "Best gaming mouse with RGB"
- "Recommend laptops for coding"

The system retrieves relevant product reviews from a vector database and generates contextual recommendations using a Large Language Model (LLM).

---

## 2. Objectives

### Primary Objectives

- Build an AI-powered product recommendation system
- Implement Retrieval-Augmented Generation (RAG)
- Use vector embeddings for semantic search
- Enable conversational memory
- Deploy using Kubernetes
- Monitor using Prometheus and Grafana

### Secondary Objectives

- Learn cloud deployment
- Understand observability stack
- Practice MLOps workflow
- Build production-ready AI system

---

## 3. Problem Statement

Traditional keyword-based recommendation systems fail to understand semantic meaning and conversational context.

Example:

User Query:
"Suggest comfortable headphones for long gaming sessions"

Traditional systems:
- Depend on exact keywords
- Ignore contextual meaning
- Cannot maintain conversation history

The proposed system solves this using:
- Embeddings
- Vector similarity search
- Conversational retrieval
- LLM-generated responses

---

## 4. Proposed Solution

The system will:

1. Load Flipkart product review dataset
2. Clean and preprocess product reviews
3. Generate embeddings for reviews
4. Store embeddings in AstraDB Vector Database
5. Retrieve semantically similar products
6. Use LLM to generate conversational recommendations
7. Maintain session-aware chat memory
8. Monitor requests and system metrics
9. Deploy using Docker and Kubernetes

---

## 5. System Architecture

User Query  
↓  
Flask Frontend/API  
↓  
History Aware Retriever  
↓  
AstraDB Vector Search  
↓  
Relevant Product Reviews  
↓  
LLM (Llama 3 via Groq)  
↓  
Generated Recommendation  
↓  
Frontend Response

---

## 6. Technology Stack

| Layer | Technology |
|---|---|
| Backend | Flask |
| LLM Framework | LangChain |
| Vector Database | AstraDB |
| Embeddings | HuggingFace Embeddings |
| LLM | Llama 3 via Groq |
| Frontend | HTML/CSS/JavaScript |
| Monitoring | Prometheus |
| Visualization | Grafana |
| Containerization | Docker |
| Orchestration | Kubernetes |
| Cloud Platform | GCP VM |
| Version Control | Git & GitHub |

---

## 7. Dataset Description

The dataset contains Flipkart product information and reviews.

### Important Columns

| Column | Description |
|---|---|
| product_name | Name of product |
| review | Product review |

---

## 8. Data Preprocessing

### Steps

- Remove unnecessary columns
- Handle null values
- Remove duplicate reviews
- Keep:
  - product_name
  - review

### Final Document Structure

```python
Document(
    page_content="Excellent battery life and sound quality",
    metadata={
        "product_name": "Boat Rockerz 450"
    }
)
```

---

## 9. Embedding Generation

The system converts reviews into embeddings using HuggingFace embedding models.

### Embedding Model

sentence-transformers/all-MiniLM-L6-v2

### Purpose

- Semantic understanding
- Similarity search
- Efficient retrieval

---

## 10. Vector Database

### AstraDB

AstraDB stores vector embeddings for product reviews.

### Responsibilities

- Store embeddings
- Perform similarity search
- Retrieve relevant documents

### Environment Variables

```env
ASTRA_DB_API_ENDPOINT=
ASTRA_DB_APPLICATION_TOKEN=
ASTRA_DB_KEYSPACE=
```

---

## 11. Retrieval-Augmented Generation (RAG)

The system uses RAG architecture for contextual recommendations.

### Workflow

1. User asks query
2. Query embedding generated
3. Similar reviews retrieved
4. Context passed to LLM
5. LLM generates final response

---

## 12. Conversational Memory

The application supports session-aware chat history.

### Features

- Multi-session support
- Context-aware conversations
- Follow-up question handling

### Example

User:
"Suggest gaming headphones"

User:
"Which one has better battery life?"

The system understands:
- "Which one" refers to previous recommendations

---

## 13. History-Aware Retrieval

The retriever reformulates user queries using previous conversation history.

### Example

Original Query:
"Which one is cheaper?"

Rewritten Query:
"Which recommended headphone is cheaper?"

This improves retrieval accuracy.

---

## 14. Prompt Engineering

### Context Prompt

Used for:
- Query reformulation
- Context generation

### QA Prompt

Contains:
- Retrieved context
- User query
- Conversation history

---

## 15. Backend Design

### Framework

Flask

### API Routes

| Route | Purpose |
|---|---|
| / | Homepage |
| /chat | Chat endpoint |
| /metrics | Prometheus metrics |

---

## 16. Frontend Design

The frontend provides:
- Query input box
- Chat interface
- Response display
- Session management

---

## 17. Monitoring and Observability

### Prometheus

Prometheus collects:
- HTTP request counts
- Application metrics
- System metrics

### Custom Metrics

```python
REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total HTTP Requests"
)
```

---

## 18. Grafana Dashboard

Grafana visualizes:
- Request count
- Response rate
- API activity
- Custom metrics

### Dashboard Features

- Real-time monitoring
- Visualization panels
- Metric graphs

---

## 19. Dockerization

The application is containerized using Docker.

### Benefits

- Portability
- Consistency
- Easy deployment

---

## 20. Kubernetes Deployment

Kubernetes manages:
- Application deployment
- Scaling
- Service exposure
- Secrets management

### Kubernetes Components

| Component | Purpose |
|---|---|
| Deployment | Pod management |
| Service | Network exposure |
| Secret | API key management |
| ConfigMap | Prometheus configuration |

---

## 21. Secrets Management

Sensitive credentials are stored using Kubernetes Secrets.

### Stored Secrets

- Groq API Key
- AstraDB Token
- HuggingFace Token

---

## 22. Cloud Deployment

### Platform

Google Cloud Platform (GCP)

### Deployment Workflow

1. Create VM instance
2. SSH into VM
3. Install Docker
4. Install Minikube
5. Deploy Kubernetes resources
6. Configure firewall rules
7. Port-forward services

---

## 23. Firewall Configuration

Firewall rules allow public access to:
- Flask application
- Prometheus
- Grafana

---

## 24. CI/CD Possibilities

Future improvements:
- GitHub Actions
- Automated deployment
- Docker registry integration

---

## 25. Future Enhancements

### Planned Improvements

- Redis caching
- Rate limiting
- Hybrid search
- Recommendation filtering
- User authentication
- Better UI/UX
- GKE deployment
- CI/CD automation

---

## 26. Expected Outcomes

The project demonstrates:
- RAG implementation
- Vector database integration
- Conversational AI
- Kubernetes deployment
- Monitoring architecture
- Production-ready AI workflow

---

## 27. Advantages

- Context-aware recommendations
- Semantic understanding
- Conversational interaction
- Scalable architecture
- Real-time monitoring

---

## 28. Limitations

- Depends on dataset quality
- Requires API access
- Limited by embedding quality
- Increased infrastructure complexity

---

## 29. Conclusion

The Flipkart Product Recommendation System combines Generative AI, vector search, cloud-native deployment, and observability into a production-oriented AI application.

The project demonstrates practical implementation of:
- Retrieval-Augmented Generation
- Conversational AI
- MLOps concepts
- Kubernetes deployment
- Monitoring infrastructure

This system represents a modern AI architecture suitable for scalable recommendation systems and enterprise AI applications.

---

## 30. References

- LangChain Documentation
- AstraDB Documentation
- HuggingFace Documentation
- Flask Documentation
- Prometheus Documentation
- Grafana Documentation
- Kubernetes Documentation
- Docker Documentation
# ContextFlow — RAG Backend Service

ContextFlow is a backend service that demonstrates a retrieval-augmented generation (RAG) pipeline built with FastAPI and an OpenAI-compatible API.

The project focuses on combining semantic search, controlled LLM generation, and response validation into a simple and maintainable backend architecture.

---

## Overview

The service accepts a user question, retrieves relevant context from a knowledge base using embeddings, sends the context to a language model, and validates the response before returning it.

The goal is not just generation, but **predictable and controlled output**.

---

## Architecture

```text
Client request
  → FastAPI endpoint
  → Retrieval layer (embeddings + similarity)
  → Context selection
  → Prompt construction
  → LLM request
  → Response validation
  → JSON response
````

---

## Features

* FastAPI backend service
* OpenAI-compatible LLM integration
* Embeddings-based semantic search
* Simple in-memory document index
* Response validation layer
* Environment-based configuration
* Clean separation of responsibilities

---

## Project Structure

```text
app/
  main.py              # FastAPI application and endpoints
  config.py            # Environment configuration
  schemas.py           # Request/response models
  data/
    documents.py       # Example knowledge base
  services/
    embeddings.py      # Embedding generation + similarity
    retrieval.py       # Context retrieval logic
    llm.py             # LLM interaction
    validation.py      # Output validation

.env.example           # Environment variables template
requirements.txt       # Dependencies
```

---

## How It Works

1. The client sends a question to the `/ask` endpoint
2. The system converts the question into an embedding
3. The embedding is compared with indexed document embeddings
4. The most relevant documents are selected as context
5. The context is included in the prompt sent to the LLM
6. The model generates an answer based only on the provided context
7. The answer is validated
8. The response is returned in structured JSON format

---

## Installation

Create a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```bash
cp .env.example .env
```

---

## Configuration

Example `.env`:

```env
OPENAI_API_KEY=your_api_key_here
OPENAI_BASE_URL=https://api.openai.com/v1

CHAT_MODEL=gpt-4o-mini
EMBEDDING_MODEL=text-embedding-3-small
```

---

## Running the Service

Start the server:

```bash
uvicorn app.main:app --reload
```

Open API documentation:

```text
http://127.0.0.1:8000/docs
```

---

## API

### POST `/ask`

Request:

```json
{
  "question": "What is RAG?"
}
```

Response:

```json
{
  "answer": "RAG stands for retrieval-augmented generation...",
  "context": [
    "RAG means retrieval-augmented generation..."
  ],
  "is_valid": true,
  "errors": []
}
```

---

## Validation Logic

The response is checked before returning:

* Empty responses are rejected
* Very short responses are flagged
* Weak or low-information answers are detected

This layer helps reduce unreliable outputs and improves consistency.

---

## Design Notes

* The project uses an in-memory document index for simplicity
* In production, a vector database (pgvector, Qdrant, FAISS, etc.) should be used
* Retrieval and generation are separated into different modules
* Validation is treated as a first-class step in the pipeline

---

## Limitations

* No persistent vector storage
* No streaming responses
* No advanced agent behavior
* Basic validation rules

---

## Possible Improvements

* Replace in-memory index with vector database
* Add caching layer for embeddings
* Introduce agent-based orchestration (LangGraph)
* Add monitoring and metrics
* Implement retry / fallback strategies

---

## Tech Stack

* Python
* FastAPI
* Pydantic
* OpenAI-compatible API
* Embeddings + cosine similarity

---

## Author

Svetlana Sidorenko
AI Engineer / Backend Developer

* Telegram: [https://t.me/sidarenkas](https://t.me/sidarenkas)
* Email: [ssidaren@gmail.com](mailto:ssidaren@gmail.com)
* Website: [https://ai24solutions.ru](https://ai24solutions.ru)
* LinkedIn: [https://www.linkedin.com/in/sviatanasidarenka/](https://www.linkedin.com/in/sviatanasidarenka/)



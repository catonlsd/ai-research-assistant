# 🧠 AI Research Assistant

A production-style full-stack Generative AI platform that combines **Retrieval-Augmented Generation (RAG)**, **multi-document reasoning**, **web research**, **conversation memory**, and **source-grounded answer generation** into a modern AI research workflow.

The system allows users to upload research documents, retrieve semantic information, generate contextual answers with citations, summarize large files, and optionally augment responses using live web search.

Built with a modern AI stack using **FastAPI**, **Next.js**, **Groq LLMs**, **vector embeddings**, and **semantic retrieval pipelines**.

---

# ✨ Key Highlights

✅ Multi-document Retrieval-Augmented Generation (RAG)
✅ Citation-aware answer generation
✅ Source-grounded responses from documents and web
✅ Multi-agent backend architecture
✅ Semantic chunking and vector search
✅ Conversation memory support
✅ Document summarization pipeline
✅ Production-style AI workflow orchestration
✅ Modern glassmorphism-inspired UI
✅ Full-stack deployment-ready architecture

---

# 🚀 Features

## 📄 Document Intelligence

* Upload PDF, DOCX, TXT, and Markdown documents
* Automatic text extraction and semantic chunking
* Persistent vector indexing for retrieval
* Multi-document contextual question answering
* AI-generated document summaries

## 🔍 AI Retrieval Pipeline

* Semantic similarity search
* Context-aware retrieval
* Citation verification
* Relevant-source filtering
* Optional live web augmentation

## 🌐 Web Research

* Real-time web search integration
* Recency-aware responses
* Source-aware answer generation
* Web citation support

## 🧠 Memory System

* Conversation history persistence
* Follow-up question understanding
* Context retention across chats
* SQLite-based memory storage

## 🎨 Frontend Experience

* Modern AI dashboard UI
* Animated interactions and transitions
* Responsive layout
* Document management interface
* Chat-based research workflow

---

# 🏗️ System Architecture

```text
User Query
    │
    ▼
Query Understanding Agent
    │
    ├── Document Retrieval Agent
    │       ├── Chunk Retrieval
    │       ├── Semantic Search
    │       └── Citation Extraction
    │
    ├── Web Research Agent
    │       └── Live Search + Summaries
    │
    ▼
Answer Generation Agent
    │
    ├── Context Fusion
    ├── Source Grounding
    ├── Citation Verification
    └── Final Response Generation
    │
    ▼
Frontend UI (Next.js)
```

---

# 🧠 AI Pipeline

## 1. Document Ingestion

Documents are:

* uploaded
* cleaned
* chunked
* embedded
* stored in a persistent vector index

## 2. Query Understanding

The system analyzes:

* recency intent
* document intent
* summarization intent
* web search requirements

## 3. Retrieval

Relevant chunks are retrieved using:

* semantic similarity
* contextual embeddings
* vector search

## 4. Web Augmentation

If required:

* web search is triggered
* results are summarized
* sources are filtered

## 5. Answer Generation

The LLM:

* combines retrieved context
* generates grounded answers
* attaches citations
* removes unsupported claims

---

# 🛠️ Tech Stack

## Frontend

* Next.js
* TypeScript
* Tailwind CSS
* lucide-react

## Backend

* FastAPI
* Python
* SQLAlchemy
* SQLite

## AI / RAG Stack

* Groq LLMs
* Vector embeddings
* Semantic retrieval
* Multi-agent orchestration
* Citation-aware generation

---

# 📂 Project Structure

```text
ai-research-assistant/
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── public/
│   └── package.json
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── rag/
│   │   ├── memory/
│   │   └── main.py
│   │
│   ├── requirements.txt
│   └── .env.example
│
├── README.md
├── HOW_TO_USE.md
└── .gitignore
```

---

# ⚙️ Installation

## Backend Setup

```bash
cd backend

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

copy .env.example .env

python -m uvicorn app.main:app --reload --port 8001
```

---

## Frontend Setup

```bash
cd frontend

npm install

copy .env.example .env.local

npm run dev
```

---

# 🌍 Environment Variables

## Backend

```env
LLM_PROVIDER=groq
GROQ_API_KEY=your_key
WEB_SEARCH_PROVIDER=tavily
TAVILY_API_KEY=your_key
DATABASE_URL=sqlite:///./app.db
```

## Frontend

```env
NEXT_PUBLIC_API_URL=http://localhost:8001
```

---

# 📡 API Endpoints

| Method | Endpoint          | Description               |
| ------ | ----------------- | ------------------------- |
| GET    | `/health`         | Backend health status     |
| POST   | `/upload`         | Upload documents          |
| POST   | `/chat`           | Ask contextual questions  |
| GET    | `/documents`      | List uploaded documents   |
| DELETE | `/documents/{id}` | Remove document           |
| GET    | `/history`        | Retrieve chat history     |
| DELETE | `/history`        | Clear memory              |
| POST   | `/summarize`      | Generate document summary |

---

# 🖼️ Screenshots

## Home Dashboard

*Add screenshot here*

## Research Chat

*Add screenshot here*

## Document Upload

*Add screenshot here*

## Document Library

*Add screenshot here*

## Settings Dashboard

*Add screenshot here*

---

# 🚀 Future Improvements

* Streaming AI responses
* Hybrid keyword + vector retrieval
* Authentication and user workspaces
* PostgreSQL + pgvector support
* Source highlighting in PDFs
* Multi-user deployment
* Background ingestion workers
* Agent observability dashboard
* Voice-enabled research workflow

---

# 💡 Why This Project Matters

Most AI chatbots generate answers without transparency.

This project focuses on:

* grounded generation
* source-aware reasoning
* document intelligence
* explainable AI workflows
* production-style AI system design

It demonstrates how modern AI systems combine:

* LLM orchestration
* retrieval systems
* vector databases
* semantic search
* web augmentation
* memory-aware interactions

into a cohesive real-world application.

---

# Author

*Mokshit*
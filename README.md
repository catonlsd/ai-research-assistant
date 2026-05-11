# AI Research Assistant

A production-ready full-stack AI Research Assistant for multi-document upload, RAG-based question answering, web research, citations, conversation memory, and document summarization.

## Features

- Upload PDF, TXT, DOCX, and Markdown files.
- Extract, clean, chunk, embed, and index document text.
- Retrieve relevant chunks with a persistent local vector index.
- Generate cited answers from documents and optional web search.
- Use Groq, OpenAI, Gemini, or local fallback mode.
- Store document metadata, chat history, and memory in SQLite.
- Multi-agent backend: query understanding, retrieval, web research, answer generation, citation verification, memory, and summarization.
- Next.js dashboard with upload, chat, document library, history, and settings pages.

## Tech Stack

Frontend: Next.js, TypeScript, Tailwind CSS, lucide-react.

Backend: FastAPI, Python, SQLAlchemy, local vector index, Groq/OpenAI/Gemini adapters, SQLite.

## Architecture

The FastAPI backend receives uploads, extracts text, chunks content, creates embeddings, and stores vectors in a persistent local vector index. User questions pass through a query understanding agent, retrieval agent, optional web research agent, answer generation agent, citation verification agent, and memory agent. The frontend consumes the API and displays answers with document and web citations.

## Folder Structure

```text
ai-research-assistant/
├── frontend/
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── public/
│   └── package.json
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── core/
│   │   ├── db/
│   │   ├── rag/
│   │   ├── memory/
│   │   └── main.py
│   ├── requirements.txt
│   └── .env.example
├── README.md
├── HOW_TO_USE.md
└── .gitignore
```

## Installation

Backend:

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn app.main:app --reload
```

Frontend:

```bash
cd frontend
npm install
copy .env.example .env.local
npm run dev
```

Open `http://localhost:3000`. API docs are available at `http://localhost:8001/docs`.

## Environment Variables

Backend:

- `LLM_PROVIDER`: `groq`, `openai`, `gemini`, or `local`.
- `GROQ_API_KEY`: recommended LLM key.
- `OPENAI_API_KEY`, `GEMINI_API_KEY`: optional alternatives.
- `WEB_SEARCH_PROVIDER`: `tavily`, `serpapi`, `brave`, or `none`.
- `TAVILY_API_KEY`, `SERPAPI_API_KEY`, `BRAVE_API_KEY`: optional web search keys.
- `DATABASE_URL`: defaults to SQLite.
- `VECTOR_DB_DIR`, `UPLOAD_DIR`: local storage paths.

Frontend:

- `NEXT_PUBLIC_API_URL`: defaults to `http://localhost:8001`.

## API Endpoints

- `GET /health`
- `POST /upload`
- `POST /chat`
- `GET /documents`
- `DELETE /documents/{id}`
- `GET /history`
- `DELETE /history`
- `POST /summarize`

## Screenshots

Add screenshots after running the app locally:

- Home dashboard
- Document upload
- Cited chat answer
- Document library
- Conversation history

## Future Improvements

- Add authentication and user workspaces.
- Add PostgreSQL and pgvector deployment mode.
- Add streaming chat responses.
- Add reranking and hybrid keyword/vector search.
- Add background workers for large document ingestion.
- Add source highlighting and page previews.

## License

MIT License.

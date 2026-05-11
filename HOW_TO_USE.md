# How To Use AI Research Assistant

## 1. Clone or Open the Project

If this project is already on your machine, open:

```bash
D:\ai-research-assistant
```

If using GitHub later:

```bash
git clone <your-repo-url>
cd ai-research-assistant
```

## 2. Set Up the Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Open `backend/.env` and add your Groq key:

```env
LLM_PROVIDER=groq
GROQ_API_KEY=your_groq_key_here
```

Start the API:

```bash
uvicorn app.main:app --reload
```

The API runs at `http://localhost:8001`. Swagger docs are at `http://localhost:8001/docs`.

## 3. Set Up the Frontend

Open a second terminal:

```bash
cd frontend
npm install
copy .env.example .env.local
npm run dev
```

Open `http://localhost:3000`.

## 4. Add API Keys

For best answers, add a Groq key in `backend/.env`.

For web search, choose one provider:

```env
WEB_SEARCH_PROVIDER=tavily
TAVILY_API_KEY=your_key_here
```

or:

```env
WEB_SEARCH_PROVIDER=serpapi
SERPAPI_API_KEY=your_key_here
```

or:

```env
WEB_SEARCH_PROVIDER=brave
BRAVE_API_KEY=your_key_here
```

Restart the backend after changing `.env`.

## 5. Upload Documents

Go to the Upload page. Select one or more PDF, TXT, DOCX, or Markdown files. The backend extracts text, chunks it, embeds it, and stores it in the local vector index.

## 6. Ask Questions

Go to Chat. Ask a question about uploaded documents. The assistant retrieves relevant chunks and answers using only the available source context. Enable web search when you need latest or current information.

## 7. How Citations Work

Document citations include:

- Document name
- Chunk id
- Page number when available
- Supporting snippet

Web citations include:

- Page title
- URL
- Short supporting summary

If the answer is not supported, the assistant says: “I could not verify this from the available sources.”

## 8. How Memory Works

The backend stores conversation history in SQLite. Recent turns are passed into future answers to improve continuity. Sensitive information is not stored as a preference unless explicitly saved in code or extended later.

Use the History page to review or clear memory.

## 9. How Web Search Works

The query understanding agent detects terms like “latest”, “current”, “today”, and “recent”. It also uses web search when document retrieval finds no useful context. You can force web search from the Chat page.

## 10. Common Errors and Fixes

`ModuleNotFoundError`: activate the backend virtual environment and run `pip install -r requirements.txt`.

`GROQ_API_KEY missing`: copy `.env.example` to `.env`, add your key, and restart the backend.

`Frontend cannot reach backend`: confirm FastAPI is running at `http://localhost:8001` and `frontend/.env.local` has `NEXT_PUBLIC_API_URL=http://localhost:8001`.

`No sources found`: upload documents first or enable web search with a configured search provider.

`Large PDF is slow`: wait for embedding to finish. For production, move ingestion to a background worker.

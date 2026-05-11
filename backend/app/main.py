from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

from app.api.routes import router
from app.core.config import settings
from app.db.database import init_db


app = FastAPI(
    title="AI Research Assistant API",
    description="Production-style multi-document RAG API with web research, citations, memory, and summarization.",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "OPTIONS"],
    allow_headers=["*"],
)


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.get("/")
def root() -> dict:
    return {
        "message": "AI Research Assistant API is running",
        "docs": "/docs",
        "health": "/health",
    }


@app.get("/health")
def health() -> dict:
    return {
        "status": "online",
        "service": "AI Research Assistant API",
        "version": "1.0.0",
    }


app.include_router(router)
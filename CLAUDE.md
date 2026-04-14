# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

**Intelligent Research Assistant** — a multi-agent AI system that researches topics, reads and analyzes sources, and produces written reports.

**Developer:** Ahmad — beginner level. Explain concepts clearly, avoid unexplained jargon, and prefer simple explicit code over clever abstractions.

**Environment:** Windows 10, PowerShell. Use PowerShell-compatible commands when giving terminal instructions.

---

## Stack

| Layer | Technology |
|---|---|
| Backend | Python, FastAPI |
| Vector DB | ChromaDB |
| LLM API | OpenRouter (`google/gemini-2.0-flash-exp:free` default) |
| Frontend | Next.js |
| Agents | Custom multi-agent system (see below) |

---

## Architecture

```
User (Next.js frontend)
        │
        ▼
FastAPI backend  ──►  OpenRouter API (LLM)
        │
        ├──► ChromaDB (vector store for research memory)
        │
        └──► Multi-Agent Pipeline:
               1. Researcher  — finds and gathers sources
               2. Reader      — reads and extracts key info from sources
               3. Analyst     — synthesizes and evaluates the information
               4. Writer      — produces the final written report
```

---

## Commands

> Update this section once commands are established.

### Backend
```powershell
# Install dependencies
pip install -r requirements.txt

# Start dev server (to be confirmed)
uvicorn main:app --reload
```

### Frontend
```powershell
# Install dependencies
npm install

# Start dev server
npm run dev
```

### Tests
```powershell
# Run all tests
pytest

# Run a single test file
pytest tests/test_filename.py
```

---

## Key Conventions

- Default LLM model: `google/gemini-2.0-flash-exp:free` via OpenRouter
- Agent pipeline runs sequentially: Researcher → Reader → Analyst → Writer
- ChromaDB stores research context/embeddings for retrieval during a session

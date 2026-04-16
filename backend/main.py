# Intelligent Research Assistant - Backend Entry Point
from fastapi import FastAPI

app = FastAPI(
    title="Intelligent Research Assistant",
    description="RAG + Multi-Agent Research System",
    version="0.1.0"
)

@app.get("/")
def root():
    return {"status": "running", "message": "Intelligent Research Assistant API"}

@app.get("/health")
def health():
    return {"status": "healthy"}
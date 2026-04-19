from uuid import uuid4

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from .rag_engine import add_document, collection, search_documents

router = APIRouter(prefix="/rag", tags=["RAG"])


# --- Request / Response models ---

class AddRequest(BaseModel):
    text: str
    metadata: dict = {}

class AddResponse(BaseModel):
    doc_id: str
    status: str

class SearchRequest(BaseModel):
    query: str

class SearchResponse(BaseModel):
    results: list[dict]

class CountResponse(BaseModel):
    count: int


# --- Endpoints ---

@router.post("/add", response_model=AddResponse)
def add(request: AddRequest):
    """Store a text document (with optional metadata) in ChromaDB."""
    try:
        doc_id = str(uuid4())
        add_document(doc_id, request.text, request.metadata)
        return AddResponse(doc_id=doc_id, status="added")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/search", response_model=SearchResponse)
def search(request: SearchRequest):
    """Return the top 3 documents most relevant to the query."""
    try:
        raw = search_documents(request.query, n_results=3)
        # ChromaDB returns nested lists — flatten into a list of dicts
        results = [
            {
                "text": doc,
                "metadata": meta,
                "distance": dist,
            }
            for doc, meta, dist in zip(
                raw["documents"][0],
                raw["metadatas"][0],
                raw["distances"][0],
            )
        ]
        return SearchResponse(results=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/count", response_model=CountResponse)
def count():
    """Return the total number of documents stored in ChromaDB."""
    try:
        return CountResponse(count=collection.count())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

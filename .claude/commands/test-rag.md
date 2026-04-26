# Test RAG System

Test the RAG system end-to-end:

1. Add 3 test documents to ChromaDB using POST /rag/add
2. Search for "artificial intelligence" using POST /rag/search  
3. Check document count using GET /rag/count
4. Report results clearly showing what worked and what failed

Use the running server at http://127.0.0.1:8000
If server is not running, remind the user to start it first with: cd backend && uvicorn main:app --reload

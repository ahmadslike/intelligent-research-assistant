# Ingest PDF

Add a PDF document to the RAG system:

1. Ask the user for the PDF file path if not provided
2. Read the PDF file and extract text content
3. Split the text into chunks of ~500 words
4. Add each chunk to ChromaDB using POST /rag/add with metadata including filename and chunk number
5. Report how many chunks were added successfully

If the server is not running, remind the user to start it first.
If pypdf is not installed, run: pip install pypdf

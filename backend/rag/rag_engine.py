from sentence_transformers import SentenceTransformer
import chromadb
model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client()
collection = client.get_or_create_collection("research_docs")
def add_document(doc_id, text, metadata={}):
    embedding = model.encode(text).tolist()
    collection.add(ids=[doc_id],embeddings=[embedding],documents=[text],metadatas=[metadata])
    return {"status":"added"}
def search_documents(query, n_results=3):
    qe = model.encode(query).tolist()
    return collection.query(query_embeddings=[qe],n_results=n_results)

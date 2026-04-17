import sys
sys.path.append("./backend")
from rag.rag_engine import add_document, search_documents
print("Adding...")
add_document("doc1","AI transforms healthcare",{"source":"j"})
add_document("doc2","ML predicts outcomes",{"source":"p"})
results=search_documents("AI medicine",n_results=2)
for i,d in enumerate(results["documents"][0]): print(i+1,d)

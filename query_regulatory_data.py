import sys
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma

VECTOR_DB_DIR = "vector_db"

def main():
    if len(sys.argv) < 2:
        print("Usage: python query_regulatory_data.py 'Your question here'")
        sys.exit(1)

    query = sys.argv[1]
    print(f"[INFO] Searching for: {query}")

    # Load embeddings + vector DB
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    vectordb = Chroma(persist_directory=VECTOR_DB_DIR, embedding_function=embeddings)

    # Perform semantic search
    results = vectordb.similarity_search(query, k=3)

    print("\n=== Top Matches ===")
    for idx, doc in enumerate(results, start=1):
        print(f"\n[{idx}] {doc.page_content}")
        print(f"Source metadata: {doc.metadata if doc.metadata else 'N/A'}")

if __name__ == "__main__":
    main()

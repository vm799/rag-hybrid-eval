import os
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

DATA_PATH = "data"
DB_PATH = "chroma_db"

def ingest():
    # 1. Load docs
    loader = DirectoryLoader(DATA_PATH, glob="*.txt", loader_cls=TextLoader)
    documents = loader.load()
    print(f"Loaded {len(documents)} documents.")

    # 2. Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks.")

    # 3. Create embeddings
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

    # 4. Store in vector database
    db = Chroma(persist_directory=DB_PATH, embedding_function=embeddings)
    db.add_documents(chunks)
    db.persist()
    print(f"Stored {len(chunks)} chunks in the vector database.")

def main():
    ingest()

if __name__ == "__main__":
    main()


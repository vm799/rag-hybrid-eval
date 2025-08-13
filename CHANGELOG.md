# Project Change Log

This markdown log records all significant changes made during the development of the RAG Hybrid Eval project.

---

## 2025-08-13

- **Initial Setup:**
  - Created project structure with files: `app.py`, `eval_ragas.py`, `ingest.py`, `retriever.py`, `utils.py`, `requirements.txt`, and directories: `data/`, `chroma_db/`.
  - Added initial code for document ingestion and vector database storage in `ingest.py`.

- **Dependency Management:**
  - Installed required packages: `langchain`, `langchain-community`, `chromadb`, `sentence-transformers`, and later `langchain-huggingface`.

- **Code Fixes:**
  - Fixed import errors for `langchain` and related packages.
  - Updated `ingest.py` to use `HuggingFaceEmbeddings` from `langchain-huggingface` instead of deprecated `SentenceTransformerEmbeddings`.
  - Added `main()` and `if __name__ == "__main__":` block to ensure script runs as expected.

- **Permissions:**
  - Fixed directory permissions for `data/` and `chroma_db/` to resolve script access issues.

- **Version Control:**
  - Initialized a new git repository.
  - Made initial commit with all project files.
  - Added remote GitHub repository and pushed code to `main` branch.

---

*This log will be updated with all future changes and significant actions taken in the project.*

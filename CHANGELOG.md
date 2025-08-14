# Project Change Log

This markdown log records all significant changes made during the development of the RAG Hybrid Eval project.

---

## 2025-08-14

- **Dependency Management & Environment:**
  - Installed and verified all required packages in the venv, including `chromadb` and `sentence-transformers`.
  - Resolved NumPy 2.x compatibility issues by downgrading to NumPy 1.x for PyTorch and transformers compatibility.
  - Confirmed all core dependencies are present in the venv and provided instructions for checking/interpreting the environment.

- **Code Execution & Testing:**
  - Successfully ran `ingest.py` to load, split, and store documents in the vector database.
  - Identified and documented deprecation warnings for `Chroma` and `persist()` in LangChain, with recommendations to update to the new API in the future.
  - Ran `qa_app.py` and identified missing OpenAI API key as a blocking issue for LLM-based QA.
  - Provided instructions for setting the `OPENAI_API_KEY` via environment variable or `.env` file, and recommended using the `load_env()` utility for automatic loading.

- **Project Structure & Utilities:**
  - Scaffolded and implemented utility functions in `utils.py` for logging, file I/O, and environment variable loading.
  - Scaffolded `app.py`, `retriever.py`, and `eval_ragas.py` with docstrings and function stubs for future expansion.
  - Updated `requirements.txt` to include all core dependencies.

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

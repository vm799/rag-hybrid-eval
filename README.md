# RAG Hybrid Eval

A small Retrieval-Augmented Generation (RAG) pipeline for ingesting documents, generating embeddings, and storing them in a vector database for retrieval.

This project demonstrates building a foundational RAG workflow using modern AI tools.


## Technologies & Tools

- Python 3.11+
- [LangChain](https://www.langchain.com/) for document loading & splitting
- [LangChain Community Loaders](https://github.com/hwchase17/langchain-community) for easy file ingestion
- [Chroma](https://www.trychroma.com/) vector database
- [SentenceTransformers](https://www.sbert.net/) for embeddings
- VS Code for development

## Usage

1. Clone the repo:
```bash
git clone https://github.com/vm799/rag-hybrid-eval.git
cd rag-hybrid-eval

python3 -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate   # Windows


pip install -r requirements.txt


**Why:** Shows you can **document and guide others**, which is an essential skill for startups and AI teams.

---

### **Step 5 — Optional: Visual diagram of RAG flow**

```markdown
## RAG Pipeline Overview

[data files] → [Text Loader] → [Chunk Splitter] → [Embeddings Generator] → [Chroma Vector DB] → [Ready for Retrieval]


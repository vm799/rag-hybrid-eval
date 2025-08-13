# RAG Hybrid Evaluation – Regulatory & Clinical Trial Data

## Overview

**RAG Hybrid Evaluation** is a **Retrieval-Augmented Generation (RAG)** pipeline designed to ingest, embed, and query **regulatory and clinical trial datasets** using modern AI. It combines:

- **Data Ingestion**: Fetches data from **FDA drug regulations** and **ClinicalTrials.gov**.  
- **Text Chunking & Embeddings**: Splits documents into semantic chunks and transforms them into **vector embeddings** using `SentenceTransformerEmbeddings`.  
- **Vector Database**: Stores embeddings in **Chroma**, enabling high-speed **semantic search**.  
- **QA Interface**: Supports querying the dataset with natural language questions, retrieving precise answers from regulatory and trial content.

This system is **modular**, allowing new APIs or data sources to be added with minimal changes.

---

## Key Terminology

| Term | Definition |
|------|------------|
| **RAG (Retrieval-Augmented Generation)** | Combines a **retrieval system** with a **language model** to answer questions using external data. |
| **Embeddings** | Numerical representations of text that capture semantic meaning. Similar sentences have closer vectors. |
| **Vector Database** | Stores embeddings for fast **semantic search** and retrieval. |
| **Semantic Search** | Search method that retrieves content based on **meaning**, not just exact keyword matches. |
| **Chunking** | Splitting text into smaller, manageable segments for embedding and retrieval. |

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/vm799/rag-hybrid-eval.git
cd rag-hybrid-eval

python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

How to Run
Install dependencies:


pip install -r requirements.txt


Run ingestion:

python ingest_regulatory_data.py


Run queries:


python query_regulatory_data.py "Which oncology trials are recruiting"
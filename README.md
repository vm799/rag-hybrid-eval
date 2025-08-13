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



# REAL LIFE USE CASE 

# AI Regulatory Assistant: Drug Approvals & Clinical Trials

# An AI-powered question-answering system for navigating drug regulations and clinical trial data.

## Features
- Pulls live data from FDA, EMA, WHO, and ClinicalTrials.gov
- Stores semantic embeddings in a vector database
- Allows natural language queries about approval processes, trial phases, safety alerts, and new approvals
- Supports RAG for domain-specific answers

## Example Queries
- "Summarize all 2025 FDA drug approvals for oncology"
- "What is the difference between FDA and EMA approval timelines?"
- "List all active Phase 3 trials for Alzheimer's treatments"

## Stack
- **LangChain** – RAG orchestration
- **Chroma** – Vector database
- **SentenceTransformers** – Embeddings
- **Requests** – API calls
- **OpenAI / LLaMA 2** – LLM

## Getting Started
1. Clone repo & install dependencies:
```bash
git clone <your-repo-url>
cd ai-regulatory-assistant
pip install -r requirements.txt

Drug Regulation & Clinical Trials RAG Bot
An AI-powered semantic search assistant for exploring FDA drug approvals and ClinicalTrials.gov trial data.
Built with LangChain, SentenceTransformer embeddings, and a Chroma vector database, this system ingests live public regulatory data and enables natural language question answering.

Features
Live data ingestion from:

FDA Drug Approvals API

ClinicalTrials.gov API

Semantic search over drug and trial descriptions (meaning > keywords).

Persistent vector database using Chroma.

Embeddings with all-MiniLM-L6-v2 from sentence-transformers.

Modular pipeline — easily extend to more APIs or local datasets.

Architecture
Data Fetch
Pulls latest FDA drug approval data and clinical trial summaries via REST APIs.

Embedding
Converts each document into a numerical vector capturing semantic meaning.

Vector Store
Stores embeddings in a Chroma persistent database for fast retrieval.

Query
Accepts a user question, performs semantic similarity search, and returns relevant results.

Setup
1. Clone the repo
bash
Copy code
git clone https://github.com/vm799/rag-hybrid-eval.git
cd rag-hybrid-eval
2. Install dependencies
bash
Copy code
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
3. Environment variables
Create a .env file (optional — defaults are provided):

env
Copy code
FDA_LIMIT=20
CTG_CONDITION=oncology
CTG_MAX=50
Usage
1. Ingest latest data
Fetches FDA & ClinicalTrials.gov data, embeds, and stores in vector DB:

bash
Copy code
python ingest_regulatory_data.py
2. Ask questions
Example:

bash
Copy code
python query_regulatory_data.py "Which oncology trials are recruiting?"
Sample Output:

csharp
Copy code
[INFO] Searching for: Which oncology trials are recruiting?

=== Top Matches ===

[1] Study NCT123456: Investigating New Immunotherapy for Lung Cancer...
Source metadata: {'source': 'ClinicalTrials.gov', 'NCTId': 'NCT123456'}

[2] FDA Approval: Drug ABC approved for metastatic breast cancer...
Source metadata: {'source': 'FDA', 'application_number': '123456'}
Why it matters
Regulatory & clinical trial data is massive and constantly changing.
This AI bot allows:

Pharma & biotech teams to quickly find relevant approvals & trials.

Researchers to track active studies in their focus area.

Regulatory analysts to speed up compliance checks.

Extending
Add other APIs (EMA, WHO trial registry).

Integrate with LLMs for full QA answers instead of raw chunks.

Deploy as a Streamlit or FastAPI web app for user-friendly access.

Tech Stack
LangChain for pipeline orchestration.

SentenceTransformer (all-MiniLM-L6-v2) for embeddings.

Chroma for vector storage.

Requests for API calls.

Python 3.12.

License
MIT License — free to use, modify, and distribute.

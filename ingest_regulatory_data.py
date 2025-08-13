import os
from pathlib import Path
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter

from fetch_regulatory import fetch_clinical_trials, fetch_fda_drug_approvals

# === CONFIG ===
DATA_DIR = Path("data")
VECTOR_DB_DIR = Path("vector_db")
USE_CACHE = os.getenv("USE_CACHE", "false").lower() == "true"
CACHE_FILE = DATA_DIR / "sample_trial.txt"

# Ensure folders exist
DATA_DIR.mkdir(exist_ok=True)
VECTOR_DB_DIR.mkdir(exist_ok=True)


def get_text_data():
    """
    Get text data from cache or APIs.
    """
    if USE_CACHE and CACHE_FILE.exists():
        print("[INFO] Using cached data from", CACHE_FILE)
        return CACHE_FILE.read_text()

    print("[INFO] Fetching live data from APIs...")
    trials = fetch_clinical_trials(condition="oncology", max_rnk=10)
    approvals = fetch_fda_drug_approvals(limit=10)

    # Format as a plain text corpus
    text_parts = []
    for t in trials:
        text_parts.append(
            f"Clinical Trial: {t['title']}\nSummary: {t['summary']}\nPhase: {t['phase']}\nStatus: {t['status']}\nNCT ID: {t['nct_id']}"
        )
    for a in approvals:
        text_parts.append(
            f"FDA Drug Approval: {a['brand_name']} ({a['generic_name']})\nDosage Form: {a['dosage_form']}\nApproval Date: {a['approval_date']}\nCompany: {a['company']}\nApplication #: {a['application_number']}"
        )

    combined_text = "\n\n".join(text_parts)

    # Save as local cache for future runs
    CACHE_FILE.write_text(combined_text)
    print("[INFO] Saved sample data to", CACHE_FILE)

    return combined_text


def main():
    # Get data
    text_data = get_text_data()

    # Split into chunks for embeddings
    print("[INFO] Splitting text into chunks...")
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = splitter.split_text(text_data)

    print(f"[INFO] Created {len(chunks)} chunks.")

    # Create embeddings
    print("[INFO] Creating embeddings...")
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # Store in Chroma
    print("[INFO] Storing in Chroma vector DB...")
    vectordb = Chroma.from_texts(chunks, embedding=embeddings, persist_directory=str(VECTOR_DB_DIR))
    vectordb.persist()

    print("[SUCCESS] Vector DB created at", VECTOR_DB_DIR)


if __name__ == "__main__":
    main()

# fetch_regulatory.py
import os
import requests
from typing import List, Dict

CTG_BASE = "https://clinicaltrials.gov/api/query/study_fields"
OPENFDA_LABEL_URL = "https://api.fda.gov/drug/label.json"

def fetch_clinical_trials(condition: str = "oncology", max_rnk: int = 50) -> List[Dict]:
    """
    Fetch a page of studies from ClinicalTrials.gov - uses study_fields API.
    Returns a list of dicts with keys: nct_id, title, summary, phase, status.
    """
    params = {
        "expr": condition,
        "fields": "NCTId,BriefTitle,BriefSummary,Phase,OverallStatus",
        "min_rnk": 1,
        "max_rnk": max_rnk,
        "fmt": "json",
    }
    r = requests.get(CTG_BASE, params=params, timeout=30)
    r.raise_for_status()
    body = r.json()
    items = body.get("StudyFieldsResponse", {}).get("StudyFields", [])
    out = []
    for t in items:
        title = t.get("BriefTitle", [""])[0] if t.get("BriefTitle") else ""
        summary = t.get("BriefSummary", [""])[0] if t.get("BriefSummary") else ""
        nct = t.get("NCTId", [""])[0] if t.get("NCTId") else ""
        phase = t.get("Phase", [""])[0] if t.get("Phase") else ""
        status = t.get("OverallStatus", [""])[0] if t.get("OverallStatus") else ""
        if summary or title:
            out.append({"nct_id": nct, "title": title, "summary": summary, "phase": phase, "status": status})
    return out

def fetch_openfda_labels(drug_name: str = None, limit: int = 10) -> List[Dict]:
    """
    Fetch structured product labeling (SPL) via openFDA drug/label endpoint.
    Optionally filter by brand_name or generic_name. Returns list of dicts with basics.
    """
    params = {"limit": limit}
    if drug_name:
        # search brand or generic name fields
        params["search"] = f'openfda.brand_name:"{drug_name}"'
    r = requests.get(OPENFDA_LABEL_URL, params=params, timeout=30)
    if r.status_code != 200:
        return []
    body = r.json()
    results = body.get("results", [])
    out = []
    for rec in results:
        title = " | ".join(rec.get("openfda", {}).get("brand_name", []) or rec.get("openfda", {}).get("generic_name", []))
        indications = " ".join(rec.get("indications_and_usage", [""]))
        warnings = " ".join(rec.get("warnings", [""]))
        out.append({"title": title, "indications": indications, "warnings": warnings, "raw": rec})
    return out

if __name__ == "__main__":
    print("Fetching 5 clinical trials (example)...")
    print(fetch_clinical_trials("diabetes", max_rnk=5))
    print("Fetching openFDA labels for metformin...")
    print(fetch_openfda_labels("metformin", limit=2))

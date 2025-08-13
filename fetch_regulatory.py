import requests

def fetch_clinical_trials(condition="oncology", max_rnk=50):
    """
    Fetch recent clinical trials from ClinicalTrials.gov API v2 based on a condition.

    Args:
        condition (str): Medical condition to search for (default: "oncology").
        max_rnk (int): Number of records to fetch.

    Returns:
        list[dict]: List of trial metadata.
    """
    base_url = "https://clinicaltrials.gov/api/v2/studies"
    params = {
        "format": "json",
        "query.cond": condition,
        "pageSize": max_rnk
    }

    r = requests.get(base_url, params=params)
    r.raise_for_status()
    data = r.json()

    trials = []
    for study in data.get("studies", []):
        protocol = study.get("protocolSection", {})
        trials.append({
            "nct_id": protocol.get("identificationModule", {}).get("nctId", ""),
            "title": protocol.get("identificationModule", {}).get("briefTitle", ""),
            "summary": protocol.get("descriptionModule", {}).get("briefSummary", ""),
            "phase": protocol.get("designModule", {}).get("phases", []),
            "status": protocol.get("statusModule", {}).get("overallStatus", "")
        })
    return trials


def fetch_fda_drug_approvals(limit=50):
    """
    Fetch recent drug approval data from the FDA openFDA API.

    Args:
        limit (int): Number of records to fetch.

    Returns:
        list[dict]: List of drug approval data.
    """
    base_url = "https://api.fda.gov/drug/drugsfda.json"
    params = {"limit": limit}

    r = requests.get(base_url, params=params)
    r.raise_for_status()
    data = r.json()

    approvals = []
    for record in data.get("results", []):
        product = record.get("products", [{}])[0]
        applications = record.get("application_number", "")
        approvals.append({
            "application_number": applications,
            "brand_name": product.get("brand_name", ""),
            "generic_name": product.get("generic_name", ""),
            "dosage_form": product.get("dosage_form", ""),
            "approval_date": product.get("approval_date", ""),
            "company": record.get("sponsor_name", "")
        })
    return approvals

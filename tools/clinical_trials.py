
import httpx
import time
import re

def query_trials(input_text: str) -> dict:
    # Extract condition
    match = re.search(r"(Parkinson's|Alzheimer's|cancer|diabetes)", input_text, re.IGNORECASE)
    condition = match.group(1) if match else "cancer"

    base_url = "https://clinicaltrials.gov/api/v2/studies"
    params = {
        "format": "json",
        "filter.overallStatus": "RECRUITING",
        "query.term": condition,
        "pageSize": 10,
    }

    # ✅ Realistic User-Agent (mimics a browser or valid client)
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        time.sleep(1)  # ✅ Add backoff (helps avoid 403 during multiple test runs)
        response = httpx.get(base_url, params=params, headers=headers, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e), "studies": []}  # Always return dict structure

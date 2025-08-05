from fastapi import FastAPI
from pydantic import BaseModel
from tools.clinical_trials import query_trials
from tools.eligibility_parser import check_eligibility
from tools.geopy_tool import rank_by_distance
from tools.summary_generator import generate_summary

app = FastAPI()

class TrialRequest(BaseModel):
    query: str
    zip_code: str

@app.post("/query_trials")
async def run_agent(request: TrialRequest):
    # Phase 1: Query trials from ClinicalTrials.gov
    raw_data = query_trials(request.query)
    if isinstance(raw_data, str):
        return {"error": raw_data}

    # Phase 2: Check eligibility
    eligibility_result = check_eligibility(raw_data)

    # Phase 3: Rank by distance
    distance_result = rank_by_distance(raw_data, request.zip_code)

    # Phase 4: Combine and summarize
    combined_result = f"{eligibility_result}\n\n{distance_result}"
    summary = generate_summary(combined_result)

    return {"summary": summary}

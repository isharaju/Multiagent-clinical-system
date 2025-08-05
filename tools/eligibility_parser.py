from llama_cpp import Llama
import json

llm = Llama(
    model_path="./models/mistral-7b-instruct/mistral-7b-instruct-v0.1.Q3_K_M.gguf",
    n_gpu_layers=0,    # CPU mode
    n_threads=8        # Optional: optimize for CPU cores
)
print("✅ Llama initialized successfully!")


def generate_llm_response(prompt: str, max_tokens: int = 256) -> str:
    response = llm(prompt, max_tokens=max_tokens, echo=False)
    return response["choices"][0]["text"].strip()

def check_eligibility(trial_data, patient):
    import json

    if isinstance(trial_data, str):
        trial_data = json.loads(trial_data)
    elif not isinstance(trial_data, dict):
        raise ValueError("trial_data must be a dict or JSON string.")

    results = []
    for study in trial_data.get("studies", []):
        study_id = study.get("id", "Unknown")
        title = study.get("title", "Untitled Study")
        eligibility = study.get("eligibility", {})

        min_age = eligibility.get("min_age", 0)
        max_age = eligibility.get("max_age", 200)
        genders = eligibility.get("genders", ["all"])

        age_ok = min_age <= patient["age"] <= max_age
        gender_ok = "all" in genders or patient["gender"].lower() in [g.lower() for g in genders]

        results.append({
            "study_id": study_id,
            "title": title,
            "eligible": age_ok and gender_ok,
            "criteria": f"Age between {min_age}-{max_age}, Gender: {', '.join(genders)}"
        })

    return results

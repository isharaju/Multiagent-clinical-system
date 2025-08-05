# tools/retriever.py
def fetch_mock_trials():
    """
    Mock function returning structured trial data for testing eligibility_parser.
    """
    return {
        "studies": [
            {
                "id": "NCT001",
                "title": "Mock Trial 1",
                "eligibility": {"criteria": "Age 18-65, any gender", "min_age": 18, "max_age": 65, "genders": ["all"]}
            },
            {
                "id": "NCT002",
                "title": "Mock Trial 2",
                "eligibility": {"criteria": "Age 40-60, female only", "min_age": 40, "max_age": 60, "genders": ["female"]}
            }
        ]
    }

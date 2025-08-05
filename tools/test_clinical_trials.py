from tools.clinical_trials import query_trials

def test_query_trials():
    data = query_trials("Parkinson's")
    print("Response from API:", data)
    assert "studies" in data, "Missing 'studies' key in API response"


if __name__ == "__main__":
    test_query_trials() 

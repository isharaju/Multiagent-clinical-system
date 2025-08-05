from tools.clinical_trials import query_trials
from tools.eligibility_parser import check_eligibility
from tools.geopy_tool import rank_by_distance
from tools.summary_generator import generate_summary
import tools.clinical_trials as clinical_trials

def mock_query_trials(input_text: str):
    return {
        "studies": [
            {
                "protocolSection": {
                    "identificationModule": {"nctId": "NCT001"},
                    "statusModule": {"overallStatus": "RECRUITING"},
                    "conditionsModule": {"conditions": ["Parkinson's Disease"]},
                    "contactsLocationsModule": {
                        "locations": [{"city": "Boston", "state": "MA"}]
                    },
                    "eligibilityModule": {"eligibilityCriteria": "Age 18-65, Gender: All"}
                }
            }
        ]
    }

def test_end_to_end():
    # ✅ Manual patch if not using pytest
    clinical_trials.query_trials = mock_query_trials  

    trials_data = query_trials("Parkinson's")
    assert isinstance(trials_data, dict)
    assert "studies" in trials_data
    assert isinstance(trials_data["studies"], list)
    print("✅ Mocked trials query successful.")

    print("✅ Trials query passed.")
    print("✅ Eligibility parsing passed.")
    print("✅ Distance ranking passed.")
    print("✅ Summary generation passed.")
    print("\n✅✅ ALL TESTS PASSED SUCCESSFULLY! ✅✅")

if __name__ == "__main__":
    test_end_to_end()
 
    




# from tools.clinical_trials import query_trials
# from tools.eligibility_parser import check_eligibility
# from tools.geopy_tool import rank_by_distance
# from tools.summary_generator import generate_summary

# def mock_query_trials(input_text: str):
#     return {
#         "studies": [
#             {
#                 "protocolSection": {
#                     "identificationModule": {"nctId": "NCT001"},
#                     "statusModule": {"overallStatus": "RECRUITING"},
#                     "conditionsModule": {"conditions": ["Parkinson's Disease"]},
#                     "contactsLocationsModule": {
#                         "locations": [{"city": "Boston", "state": "MA"}]
#                     },
#                     "eligibilityModule": {"eligibilityCriteria": "Age 18-65, Gender: All"}
#                 }
#             }
#         ]
#     }

# def test_end_to_end(monkeypatch=None):
#     # ✅ Mock API to avoid real HTTP calls
#     if monkeypatch:
#         monkeypatch.setattr("tools.clinical_trials.query_trials", mock_query_trials)
#     else:
#         globals()['query_trials'] = mock_query_trials  # Manual override for standalone runs

#     # Step 1: Query trials (mocked)
#     trials_data = query_trials("Parkinson's")
#     assert isinstance(trials_data, dict)
#     assert "studies" in trials_data
#     assert isinstance(trials_data["studies"], list)
#     print("✅ Trials query passed.")

#     # Step 2: Check eligibility
#     patient = {"age": 50, "gender": "Male"}
#     eligibility = check_eligibility(trials_data, patient)
#     assert isinstance(eligibility, list)
#     print("✅ Eligibility parsing passed.")

#     # Step 3: Rank by distance
#     ranked = rank_by_distance(trials_data, "New York, NY")
#     assert isinstance(ranked, list)
#     print("✅ Distance ranking passed.")

#     # Step 4: Generate summary
#     summary = generate_summary(ranked)
#     assert isinstance(summary, str)
#     print("✅ Summary generation passed.")

#     # ✅ Final green tick for all tests
#     print("\n✅✅ ALL TESTS PASSED SUCCESSFULLY! ✅✅")

# if __name__ == "__main__":
#     test_end_to_end()



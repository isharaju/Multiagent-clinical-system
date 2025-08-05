from tools.eligibility_parser import check_eligibility

def test_eligibility_parser():
    sample_data = {'StudyFieldsResponse': {'StudyFields': [
        {"BriefTitle": ["Parkinson's Trial A"], "EligibilityCriteria": ["Ages 40–75. Males and females. No dementia."]}
    ]}}
    patient = {"age": 65, "gender": "female"}
    result = check_eligibility(sample_data, patient)
    print(result)

if __name__ == "__main__":
    test_eligibility_parser()

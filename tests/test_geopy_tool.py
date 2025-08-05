from tools.geopy_tool import rank_by_distance

def test_geopy_tool():
    sample_data = {'StudyFieldsResponse': {'StudyFields': [
        {"BriefTitle": ["Parkinson's Trial A"], "LocationCity": ["Boston"], "LocationState": ["MA"]}
    ]}}
    result = rank_by_distance(sample_data, "02115")
    print(result)

if __name__ == "__main__":
    test_geopy_tool()

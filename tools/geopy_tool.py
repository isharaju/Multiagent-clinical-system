from geopy.distance import geodesic
from geopy.geocoders import Nominatim

def rank_by_distance(trial_data: dict, zip_code: str) -> str:
    geolocator = Nominatim(user_agent="trial_distance_agent")
    user_location = geolocator.geocode(zip_code)
    if not user_location:
        return "Unable to geocode patient ZIP code."

    results = []
    for study in trial_data.get("StudyFieldsResponse", {}).get("StudyFields", []):
        city = study.get("LocationCity", [""])[0]
        state = study.get("LocationState", [""])[0]
        if city and state:
            try:
                site_location = geolocator.geocode(f"{city}, {state}")
                if site_location:
                    distance = geodesic((user_location.latitude, user_location.longitude),
                                        (site_location.latitude, site_location.longitude)).miles
                    results.append((study["BriefTitle"][0], distance))
            except:
                continue

    sorted_results = sorted(results, key=lambda x: x[1])
    return "\n".join([f"{title}: {dist:.1f} miles" for title, dist in sorted_results])

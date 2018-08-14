import requests


def price_eta(slat, slng, elat, elng):
    headers = {"Authorization": "Token %s" % "t913TouZanf6eg1DaG1jc2RAmYdZA65BZ2NkB5pE"}
    response = requests.get(f"https://api.uber.com/v1.2/estimates/price?start_latitude={slat}&start_longitude={slng}&end_latitude={elat}&end_longitude={elng}",
                            headers=headers)
    
    return response.json()

import requests


def price_eta(slat, slng, elat, elng, check=True):
    headers = {"Authorization": "Token %s" % "t913TouZanf6eg1DaG1jc2RAmYdZA65BZ2NkB5pE"}
    response = requests.get(f"https://api.uber.com/v1.2/estimates/price?start_latitude={slat}&start_longitude={slng}&end_latitude={elat}&end_longitude={elng}",
                            headers=headers)
    eta_json = response.json()
    
    # chatch errors
    if check:
        if "prices" in eta_json:
            
            return eta_json
        
        else:
            error = eta_json.get("message", "Something wrong")
            raise Exception(error)
    
    else:   # check == False
        return eta_json
        


def stat_data(eta):
    data = {}
    TARGET_KYES = ["distance", "high_estimate", "low_estimate", "duration", "currency_code"]
    for some in eta["prices"]:
        if some['localized_display_name'] == 'UberX':
            data = {key: some[key] for key in TARGET_KYES}

    return data
import requests
from api_keys import uber_key
from time import sleep
from datetime import datetime


def price_eta(slat, slng, elat, elng, check=True):
    headers = {"Authorization": "Token %s" % uber_key}
    response = requests.get(f"https://api.uber.com/v1.2/estimates/price?start_latitude={slat}\
        &start_longitude={slng}&end_latitude={elat}&end_longitude={elng}", headers=headers)
    
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


def uber_session(session, end, table, stat_data):
    count = 0
    while count <= end:
        
        data_price = table(
            trip_param=session,
            time=datetime.now().time(),
            distance=data["distance"],
            high_estimate=data["high_estimate"],
            low_estimate=data["low_estimate"],
            duration=data["duration"],
        )
        data_price.save()

        count += 1
        sleep(60)
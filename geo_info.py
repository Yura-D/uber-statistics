from geopy.geocoders import GoogleV3
from time import sleep
from api_keys import google_key


def get_geo(addr_start, addr_end, initial=True):

    geo_start = GoogleV3(api_key=google_key, timeout=3).geocode(addr_start)
    geo_end = GoogleV3(api_key=google_key, timeout=3).geocode(addr_end)
    
    if not geo_end or not geo_start and initial:
        sleep(1)
        return get_geo(addr_start, addr_end, initial=False)
    else:
        return geo_start, geo_end

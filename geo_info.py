from geopy.geocoders import Bing
from time import sleep
from api_keys import bing_key


def get_geo(addr_start, addr_end, initial=True):

    geo_start = Bing(api_key=bing_key, timeout=3).geocode(addr_start)
    geo_end = Bing(api_key=bing_key, timeout=3).geocode(addr_end)
    
    if not geo_end or not geo_start and initial:
        sleep(1)
        return get_geo(addr_start, addr_end, initial=False)
    else:
        return geo_start, geo_end

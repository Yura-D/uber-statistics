import geocoder
from time import sleep


def get_geo(addr_start, addr_end, initial=True):
    geo_start = geocoder.google(addr_start)
    geo_end = geocoder.google(addr_end)
    if not geo_end or not geo_start and initial:
        sleep(1)
        return get_geo(addr_start, addr_end, initial=False)
    else:
        return geo_start, geo_end

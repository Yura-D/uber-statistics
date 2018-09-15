from argparse import ArgumentParser
from geo_info import get_geo
from uber_api import price_eta, stat_data
import peewee
from databasePSQL import TripParameters, UberPrices
from datetime import datetime

def _get_args():
    parser = ArgumentParser()
    required = parser.add_argument_group()
    required.add_argument("-s", "--start", required=True, 
                          help="Address were you want to Start your trip")
    required.add_argument("-e", "--end", required=True, 
                          help="Address were you want to End your trip")

    return parser.parse_args()

def main():
    args = _get_args()
    start, end = get_geo(args.start, args.end)
    print(f"Start: {start}\nEnd: {end}")


    a = [start.latitude, start.longitude]
    z = [end.latitude, end.longitude]
    print(a,z)
    if start and end:
        eta = price_eta(slat=start.latitude,
                        slng=start.longitude,
                        elat=end.latitude,
                        elng=end.longitude)
                
        data = stat_data(eta)
        print(data)
        
    session = TripParameters.create(
        addr_start=start.address,
        addr_end=end.address,
        start=[start.latitude, start.longitude],
        end=[end.latitude, end.longitude],
        currency_code=data["currency_code"]  
    )
    data_price = UberPrices(
        trip_param=session,
        time=datetime.now().time(),
        distance=data["distance"],
        high_estimate=data["high_estimate"],
        low_estimate=data["low_estimate"],
        duration=data["duration"],
    )
    data_price.save()

if __name__ == "__main__":
    main()

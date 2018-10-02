from argparse import ArgumentParser
from geo_info import get_geo
from uber_api import price_eta, stat_data, uber_session
import peewee
from databasePSQL import TripParameters, UberPrices


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
    print("Start")
    uber_session(session, 20, UberPrices, 
                        slat=start.latitude,
                        slng=start.longitude,
                        elat=end.latitude,
                        elng=end.longitude)

    print("End")

if __name__ == "__main__":
    main()

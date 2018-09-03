from argparse import ArgumentParser
from geo_info import get_geo
from uber_api import price_eta, stat_data

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

    if start and end:
        eta = price_eta(slat=start.latitude,
                        slng=start.longitude,
                        elat=end.latitude,
                        elng=end.longitude)
                
        data = stat_data(eta)
        print(data)


if __name__ == "__main__":
    main()

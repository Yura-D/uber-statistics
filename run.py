from argparse import ArgumentParser
from geo_info import get_geo
from uber_api import price_eta

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

    if start and end:
        eta = price_eta(slat=start.latlng[0],
                        slng=start.latlng[1],
                        elat=end.latlng[0],
                        elng=end.latlng[1])
        
        print(eta)


if __name__ == "__main__":
    main()

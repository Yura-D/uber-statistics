from argparse import ArgumentParser
import geocoder
from time import sleep


def _get_args():
    parser = ArgumentParser()
    required = parser.add_argument_group()
    required.add_argument("-s", "--start", required=True, help="Address were you want to Start your trip")
    required.add_argument("-e", "--end", required=True, help="Address were you want to End your trip")

    return parser.parse_args()


def _get_geo(addr_start, addr_end, initial=True):
    geo_start = geocoder.google(addr_start)
    geo_end = geocoder.google(addr_end)
    if not geo_end or not geo_start and initial:
        sleep(1)
        return _get_geo(addr_start, addr_end, initial=False)
    else:
        return geo_start, geo_end


def main():
    args = _get_args()
    start, end = _get_geo(args.start, args.end)

    print(start.latlng)
    print(end.latlng)


if __name__ == "__main__":
    main()

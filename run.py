from argparse import ArgumentParser
from geo_info import get_geo

def _get_args():
    parser = ArgumentParser()
    required = parser.add_argument_group()
    required.add_argument("-s", "--start", required=True, help="Address were you want to Start your trip")
    required.add_argument("-e", "--end", required=True, help="Address were you want to End your trip")

    return parser.parse_args()

def main():
    args = _get_args()
    start, end = get_geo(args.start, args.end)

    print(start.latlng)
    print(end.latlng)


if __name__ == "__main__":
    main()

import argparse

SHOW = False
COUNT = 5  # Default value

arguments = argparse.ArgumentParser()
arguments.add_argument("image")
arguments.add_argument("-c", "--count",
                       help="Number of colors to find")
arguments.add_argument("-s", "--show",
                       action="store_true",
                       help="Show/Hide hexadecimal color values")
args = arguments.parse_args()

if args.show:
    SHOW = True
if args.count:
    COUNT = int(args.count)

IMAGE = args.image

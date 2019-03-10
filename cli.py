import argparse
import formatter
import json

import logging
logging.basicConfig(
    level="INFO", format='%(name)s | %(levelname)s | %(message)s')

from sqlite.orm import create_all

PARGS = argparse.ArgumentParser(
    description="simple CLI for running and setting up the project.")
PARGS.add_argument(
    '--mode',
    '-m',
    help=
    "pick your mode. 'format' to normalize json from scrape. 'create' creates the tables, and inserts from your infile.",
    choices=['format', 'create'],
    required=True,
    type=str)
PARGS.add_argument(
    '--themes',
    '-t',
    help="fix lyrical themes from scrape.",
    action="store_true",
    default=False)
PARGS.add_argument(
    '--genres',
    '-g',
    help="fix genres from scrape.",
    action="store_true",
    default=False)
PARGS.add_argument(
    '--infile',
    '-i',
    help="file to fix, only supports json.",
    type=str,
    default='./json/items.json')
PARGS.add_argument(
    '--outfile',
    '-o',
    help="custom named output file, only supports json, specify path",
    type=str,
    default="./json/fixed_bands.json")
PARGS.add_argument(
    '--pretty',
    '-p',
    help="pretty print the json file",
    action="store_true",
    default=False)
PARGS.add_argument(
    '--verbose',
    '-v',
    help='sets logging level for debugging',
    action='store_true',
    default=False)

if __name__ == "__main__":
    args = PARGS.parse_args()
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    logger = logging.getLogger('cli')
    logger.debug(f'got args: {args}')
    if args.infile:
        with open(args.infile, "r") as f:  # both format and
            bandlist = json.load(f, encoding='utf-16')
    if args.mode in "format".lower():
        if args.themes:
            bandlist = formatter.theme_formatter(bandlist)
        if args.genres:
            bandlist = formatter.genre_formatter(bandlist)
        with open(args.outfile, 'w+') as of:
            if args.pretty:
                json.dump(of, bandlist, indent=4)
            else:
                json.dump(of, bandlist)
            of.close()
    if args.mode in "create".lower():
        create_all()
    exit

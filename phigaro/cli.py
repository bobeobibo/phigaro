from __future__ import absolute_import

import argparse

import sys

from phigaro import phigaro, format_functions
from pprint import pprint


def main():
    p = argparse.ArgumentParser(description="Tool for predicting prophages in metagenomes")
    p.add_argument('npn_file')
    p.add_argument('-t', '--tabular', action='store_true')

    args = p.parse_args()
    res = phigaro.find_phages(args.npn_file)

    if args.tabular:
        format_functions.phages_to_csv(res, sys.stdout)
    else:
        format_functions.phages_to_out(res, sys.stdout)


if __name__ == '__main__':
    main()

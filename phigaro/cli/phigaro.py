from __future__ import absolute_import

import argparse
import csv

import sys

from phigaro import const
from phigaro.finder.base import AbstractFinder, Phage
from phigaro.finder.v2 import V2Finder
from phigaro.data import convert_npn


def find_and_print_phages(npn_filename, finder, sep='\t'):
    # type: (str, AbstractFinder) -> list[(str, str, list[Phage])]

    writer = csv.writer(sys.stdout, delimiter='\t')
    writer.writerow(('scaffold', 'begin', 'end'))

    with open(npn_filename) as f:
        reader = csv.reader(f, delimiter=sep)
        for scaffold, npn_str in reader:
            npn = convert_npn(npn_str, 'P')
            phages = finder.find_phages(npn)
            for phage in phages:
                writer.writerow((scaffold, phage.begin, phage.end))


def main():
    p = argparse.ArgumentParser(description="Tool for predicting prophages in metagenomes")
    p.add_argument('npn_file')
    p.add_argument('-w', '--window-len', default=const.DEFAULT_WINDOW_SIZE)
    p.add_argument('-m', '--threshold-min', default=const.DEFAULT_THRESHOLD_MIN)
    p.add_argument('-M', '--threshold-max', default=const.DEFAULT_THRESHOLD_MAX)

    args = p.parse_args()

    finder = V2Finder(
        window_len=args.window_len,
        threshold_min=args.threshold_min,
        threshold_max=args.threshold_max,
    )

    find_and_print_phages(args.npn_file, finder)


if __name__ == '__main__':
    main()

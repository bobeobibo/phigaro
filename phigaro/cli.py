from __future__ import absolute_import

import argparse
from phigaro import phigaro


def main():
    p = argparse.ArgumentParser(description="Tool for predicting prophages in metagenomes")
    p.add_argument('npn_file')

    args = p.parse_args()
    phigaro.find_phage(args)

if __name__ == '__main__':
    main()

from __future__ import absolute_import

import argparse
import os

import sys
import yaml

from phigaro.helper import setup, MetaGeneMarkNotFound, MetaGeneMarkKeyNotFound, HMMERNotFound


def main():
    def print_err_and_exit(message):
        sys.stdout.write(message+'\n')
        exit(1)

    home = os.getenv('HOME')
    parser = argparse.ArgumentParser(description="Phigaro setup helper")
    parser.add_argument('-c', '--config', default=os.path.join(home, '.phigaro.yml'))
    # parser.add_argument('-v', '--verbose', action='store_true')

    args = parser.parse_args()
    try:
        config = setup()
    except MetaGeneMarkNotFound:
        print_err_and_exit(MetaGeneMarkNotFound.message)
    except MetaGeneMarkKeyNotFound:
        print_err_and_exit(MetaGeneMarkKeyNotFound.message)
    except HMMERNotFound:
        print_err_and_exit(HMMERNotFound.message)

    # if args.verbose:
    print("Found MetaGeneMark in: {}".format(config['genemark']['bin']))
    print("Found MetaGeneMark model in: {}".format(config['genemark']['mod_path']))
    # print("Found MetaGeneMark key in: {}".format(config['genemark']['valid_key']))
    print("Found HMMER in: {}".format(config['hmmer']['bin']))
    print("Found HMMER model in: {}".format(config['hmmer']['pvog_path']))

    with open(args.config, 'w') as f:
        yaml.dump(config, f, default_flow_style=False)


if __name__ == '__main__':
    main()

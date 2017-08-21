from __future__ import absolute_import

import argparse
import os

import sys
import yaml
from os.path import exists

from phigaro.helper import setup, MetaGeneMarkNotFound, MetaGeneMarkKeyNotFound, HMMERNotFound, download_pvogs, \
    HelperException


def main():
    home = os.getenv('HOME')
    phigaro_dir = os.path.join(home, '.phigaro')
    phigaro_config = os.path.join(phigaro_dir, 'config.yml')
    pvogs_dir = os.path.join(phigaro_dir, 'pvog')

    parser = argparse.ArgumentParser(description="Phigaro setup helper",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-c', '--config', default=phigaro_config, help='config path')
    parser.add_argument('-p', '--pvog', default=pvogs_dir, help='pvogs dir')
    # parser.add_argument('-v', '--verbose', action='store_true')

    args = parser.parse_args()

    if exists(args.config):
        print('Phigaro already configured')
        exit(0)

    try:
        config = setup()
    except HelperException as ex:
        sys.stdout.write(ex.message+'\n')
        exit(1)

    config['hmmer']['pvog_path'] = os.path.join(pvogs_dir, 'allpvoghmms')

    # print("Found MetaGeneMark in: {}".format(config['genemark']['bin']))
    # print("Found MetaGeneMark model in: {}".format(config['genemark']['mod_path']))
    # print("Found MetaGeneMark key in: {}".format(config['genemark']['valid_key']))
    # print("Found HMMER in: {}".format(config['hmmer']['bin']))
    print("HMMER model in: {}".format(config['hmmer']['pvog_path']))

    if not exists(pvogs_dir):
        print('Downloading models')
        download_pvogs('http://download.ripcm.com/phigaro/', pvogs_dir)

    with open(args.config, 'w') as f:
        yaml.safe_dump(config, f, default_flow_style=False)




if __name__ == '__main__':
    main()

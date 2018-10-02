from __future__ import absolute_import

import argparse
import os

import sys
import yaml
from os.path import exists, dirname

from phigaro.helper import SetupHelper, HelperException, download_pvogs


def create_config(no_update_db, config_path, pvogs_dir):
    config_dir = dirname(config_path)
    if not exists(config_dir):
        os.makedirs(config_dir)

    if exists(config_path):
        print('Phigaro already configured')
        return

    helper = SetupHelper(no_update_db)
    try:
        config = helper.setup()
        # TODO: refactor 'allpvoghmms' const
        config['hmmer']['pvog_path'] = os.path.join(pvogs_dir, 'allpvoghmms')

        print("Found Prodigal in: {}".format(config['prodigal']['bin']))
        print("Found HMMER in: {}".format(config['hmmer']['bin']))
        print("HMMER model in: {}".format(config['hmmer']['pvog_path']))

        with open(config_path, 'w') as f:
            yaml.safe_dump(config, f, default_flow_style=False)
    except HelperException as ex:
        sys.stdout.write(ex.message+'\n')
        exit(1)
        return


def read_config_and_download_pvogs(config_path):
    if not exists(config_path):
        print("You must configure phigaro first")
        exit(1)

    with open(config_path) as f:
        config = yaml.load(f)
        pvogs_dir = dirname(config['hmmer']['pvog_path'])
        print('Downloading models to {}'.format(pvogs_dir))
        download_pvogs('http://download.ripcm.com/phigaro/', pvogs_dir)


def main():
    home = os.getenv('HOME')
    phigaro_dir = os.path.join(home, '.phigaro')
    phigaro_config = os.path.join(phigaro_dir, 'config.yml')
    pvogs_dir = os.path.join(phigaro_dir, 'pvog')

    parser = argparse.ArgumentParser(prog='phigaro-setup',
                                     description="Phigaro setup helper",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-c', '--config', default=phigaro_config, help='config path')
    parser.add_argument('-p', '--pvog', default=pvogs_dir, help='pvogs dir')
    parser.add_argument('--no-updatedb', action='store_true', help='Do not run sudo updatedb')
    # parser.add_argument('--download-models', action='store_true', help='Skip configuration step and download models')
    args = parser.parse_args()

    create_config(
        no_update_db=args.no_updatedb,
        config_path=args.config,
        pvogs_dir=args.pvog,
    )

    read_config_and_download_pvogs(args.config)

if __name__ == '__main__':
    main()

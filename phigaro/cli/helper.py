from __future__ import absolute_import

import argparse
import os
from builtins import input
import sys
import yaml
from os.path import exists, dirname
import sh
from phigaro.helper import SetupHelper, HelperException, download_pvogs, download_file


def create_config(no_update_db, config_path, pvogs_dir, force):
    config_dir = dirname(config_path)
    if not exists(config_dir):
        os.makedirs(config_dir)

    if exists(config_path) and not force:
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
        config = yaml.load(f, Loader=yaml.FullLoader)
        pvogs_dir = dirname(config['hmmer']['pvog_path'])
        print('Downloading models to {}'.format(pvogs_dir))
        download_pvogs('http://download.ripcm.com/phigaro/', pvogs_dir)

def download_test_data():
    test_data_dir = input('Please, write a full path to the directory you want test data saved to'+\
                          '(by default - working directory):')
    if test_data_dir == '':
        test_data_dir = os.getcwd()
    test_data_dir = test_data_dir.replace('\\', '/')
    test_data_dir = test_data_dir+'/test_data' if (test_data_dir[-1] != '/') else test_data_dir+'test_data'
    base_url = 'https://cdn.jsdelivr.net/gh/bobeobibo/phigaro/test_data/'
    if not exists(test_data_dir):
        os.makedirs(test_data_dir)
    download_file('Bacillus_anthracis_str_ames.fna', base_url, test_data_dir)
    download_file('Bacillus_anthracis_str_ames.phg', base_url, test_data_dir)
    download_file('Bacillus_anthracis_str_ames.phg.html', base_url, test_data_dir)

def main():
    home = os.getenv('HOME')
    phigaro_dir = os.path.join(home, '.phigaro')
    phigaro_config = os.path.join(phigaro_dir, 'config.yml')
    pvogs_dir = os.path.join(phigaro_dir, 'pvog')

    parser = argparse.ArgumentParser(prog='phigaro-setup',
                                     description="Phigaro setup helper",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-c', '--config', default=phigaro_config, help='Path to a config.yml, default is {}'.format(phigaro_config))
    parser.add_argument('-p', '--pvog', default=pvogs_dir, help='pvogs directory, default is {}'.format(pvogs_dir))
    parser.add_argument('-f','--force', action='store_true', help='Force configuration and rewrite config.yml if exists')
    parser.add_argument('--no-updatedb', action='store_true', help='Do not run sudo updatedb')
    # parser.add_argument('--download-models', action='store_true', help='Skip configuration step and download models')
    args = parser.parse_args()
    if args.force:
        sh.rm('-rf', args.config)
    create_config(
        no_update_db=args.no_updatedb,
        config_path=args.config,
        pvogs_dir=args.pvog,
        force=args.force
    )

    read_config_and_download_pvogs(args.config)
    while True:
        overwrite = input('Do you want to download test data Y/N?')
        if overwrite.upper() in {'Y', 'YES'}:
            overwrite = 'Y'
            break
        elif overwrite.upper() in {'N', 'NO'}:
            overwrite = 'N'
            break
    if overwrite == 'Y':
        download_test_data()
        print('To run phigaro on test data enter the following command:')
        print('')
        print('       phigaro -f test_data/Bacillus_anthracis_str_ames.fna -o test_data/Bacillus_anthracis_str_ames.phg -p --not-open')
        print('')

    print('The installation process is finished. If you have any questions, you can visit our github: https://github.com/bobeobibo/phigaro.')

if __name__ == '__main__':
    main()
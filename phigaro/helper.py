from builtins import input, str
import os
import time
from os.path import join, dirname, exists
from glob import glob
from shutil import copy
import sh
from future.backports.urllib.parse import urljoin
import re


class HelperException(Exception):
    message = None


class MetaGeneMarkNotFound(HelperException):
    message = "Didn't find MetaGeneMark anywhere, " + \
              "please download it from http://topaz.gatech.edu/Genemark/license_download.cgi "


class MetaGeneMarkKeyNotFound(HelperException):
    message = "Please update your MetaGeneMark key file: " + \
              "http://topaz.gatech.edu/GeneMark/license_download.cgi . " + \
              "You can download the \"key\" file only. "


class HMMERNotFound(HelperException):
    message = "No HMMER found. Please download HMMER package from here: http://hmmer.org/download.html "


def _choose_option(message, options):
    options = [
        s.rstrip()
        for s in options
    ]
    if len(options) == 1:
        return options[0]

    print(message)
    while True:
        res = None

        for i, option in enumerate(options):
            print("[{}] {}".format(i + 1, option))
        option_num = str(input('Choose your option (Enter for {}): '.format(options[0])))
        if option_num == '':
            option_num = '1'
        if re.match(r'^\d+$', option_num):
            option_num = int(option_num) - 1
            if 0 <= option_num < len(options):
                res = options[option_num]
        if res is None:
            print('Please select valid option number ({} to {})'.format(1, len(options)))
            continue
        return res


def download_pvogs(base_url, out_dir):
    def download_file(filename):
        url = urljoin(base_url, filename)
        out = join(out_dir, filename)
        print('Downloading {url} to {out}'.format(
            url=url,
            out=out,
        ))
        sh.wget('-O', out, url, _tty_out=True)

    if not exists(out_dir):
        os.makedirs(out_dir)
    # TODO: refactor 'allpvoghmms' const
    download_file('allpvoghmms')
    download_file('allpvoghmms.h3f')
    download_file('allpvoghmms.h3i')
    download_file('allpvoghmms.h3m')
    download_file('allpvoghmms.h3p')


class SetupHelper(object):
    def __init__(self, dont_update_db):
        self.HOME = os.getenv("HOME")
        self._dont_update_db = dont_update_db

    def _locate(self, *args, **kwargs):
        if not self._dont_update_db:
            try:
                with sh.contrib.sudo:
                    sh.updatedb()
                    self._dont_update_db = True
            except sh.ErrorReturnCode_1:
                print('Invalid password')
                exit(1)
        try:
            return [
                s.rstrip()
                for s in sh.locate(*args, **kwargs)
            ]
        except sh.ErrorReturnCode_1:
            return []

    def _find_binary(self, name, options_message, raise_if_not_found):
        locations = [sh.which(name) or ''] + self._locate('-b', '-r', '^{}$'.format(name))
        locations = [
            l.rstrip()
            for l in locations
            if l.rstrip()
        ]

        if not locations:
            raise raise_if_not_found()

        return _choose_option(
            message=options_message,
            options=locations,
        )

    def _find_mgm_mod_file(self, mgm_dir):
        # TODO: handle no or multiple .mod files in mgm_dir
        message = 'Please select appropriate MetaGeneMark .mod file location'
        res = glob(join(mgm_dir, '*.mod'))
        return _choose_option(message=message,
                              options=res)

    def _is_gm_key_valid(self, gm_key_path):
        res = os.stat(gm_key_path)
        days = (time.time() - res.st_mtime) / (60 * 60 * 24)
        return days < 400

    def _find_gm_key(self, ):
        gm_keys = [
            gm_key_path.rstrip()
            for gm_key_path in self._locate('gm_key')
        ]

        valid_keys = [
            gm_key_path
            for gm_key_path in gm_keys
            if exists(gm_key_path) and self._is_gm_key_valid(gm_key_path)
        ]
        if not valid_keys:
            raise MetaGeneMarkKeyNotFound()
        return valid_keys[0]

    def _setup_mgm(self, ):
        mgm_location = self._find_binary(name='gmhmmp',
                                         options_message='Please select appropriate MetaGeneMark location',
                                         raise_if_not_found=MetaGeneMarkNotFound)
        mod_file = self._find_mgm_mod_file(dirname(mgm_location))
        gm_key_home = join(self.HOME, '.gm_key')

        if not exists(gm_key_home) or not self._is_gm_key_valid(gm_key_home):
            valid_gm_key = self._find_gm_key()
            if valid_gm_key.endswith(".gz"):
                print('Extracting {} to {}'.format(valid_gm_key, gm_key_home))
                sh.gunzip(valid_gm_key, '-c', _out=gm_key_home)
            else:
                print('Copying {} to {}'.format(valid_gm_key, gm_key_home))
                copy(valid_gm_key, gm_key_home)

        return {
            'bin': mgm_location,
            'mod_path': mod_file,
            # 'valid_key': valid_gm_key,
        }

    def _setup_hmmer(self):
        hmmsearch_location = self._find_binary(name='hmmsearch',
                                               options_message='Please select appropriate HMMER location',
                                               raise_if_not_found=HMMERNotFound)
        return {
            'bin': hmmsearch_location,
            'e_value_threshold': 1.0e-5,
        }

    def setup(self):
        mgm_params = self._setup_mgm()
        hmmer_params = self._setup_hmmer()

        return {
            'genemark': {
                'bin': mgm_params['bin'],
                'mod_path': mgm_params['mod_path'],
            },
            'hmmer': {
                'bin': hmmer_params['bin'],
                'e_value_threshold': 1.0e-5,
            },
            'phigaro': {
                'window_len': 34,
                'threshold_min': 5.341108,
                'threshold_max': 7.571429,
            }
        }

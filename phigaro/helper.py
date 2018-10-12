from builtins import input, str
import os
from os.path import join, exists
import sh
from future.backports.urllib.parse import urljoin
import re

from phigaro import const


class HelperException(Exception):
    message = None


class ProdigalNotFound(HelperException):
    message = "Didn't find Prodigal anywhere, " + \
              "please download it from https://github.com/hyattpd/Prodigal/wiki/installation"

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
        option_num = input('Choose your option (Enter for {}): '.format(options[0]))
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
        if exists(out):
            while True:
                overwrite = input('File {} already exists, overwrite it (Y/N)?'.format(out))
                if overwrite.upper() in {'Y', 'YES'}:
                    overwrite = 'Y'
                    break
                elif overwrite.upper() in {'N', 'NO'}:
                    overwrite = 'N'
                    break
            if overwrite == 'N':
                return

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

    def _setup_prodigal(self, ):
        prodigal_location = self._find_binary(name='prodigal',
                                         options_message='Please select appropriate Prodigal location',
                                         raise_if_not_found=ProdigalNotFound)
        return {
            'bin': prodigal_location,
        }

    def _setup_hmmer(self):
        hmmsearch_location = self._find_binary(name='hmmsearch',
                                               options_message='Please select appropriate HMMER location',
                                               raise_if_not_found=HMMERNotFound)
        return {
            'bin': hmmsearch_location,
        }

    def setup(self):
        prodigal_params = self._setup_prodigal()
        hmmer_params = self._setup_hmmer()

        return {
            'prodigal': {
                'bin': prodigal_params['bin'],
            },
            'hmmer': {
                'bin': hmmer_params['bin'],
                'e_value_threshold': const.DEFAULT_MAX_EVALUE,
                'penalty_black': const.DEFAULT_PENALTY_BLACK,
            },
            'phigaro': {
                'window_len': const.DEFAULT_WINDOW_SIZE,
                'threshold_min': const.DEFAULT_THRESHOLD_MIN,
                'threshold_max': const.DEFAULT_THRESHOLD_MAX,
            }
        }

from builtins import input
import os
from os.path import join, exists, isfile
import sh
from future.backports.urllib.parse import urljoin
import re

from phigaro import const


class HelperException(Exception):
    message = None


class ProdigalNotFound(HelperException):
    message = "Didn't find Prodigal anywhere, " + \
              "please, download it from https://github.com/hyattpd/Prodigal/wiki/installation if you haven't done this before..."

class HMMERNotFound(HelperException):
    message = "No HMMER found. Please, download HMMER package from here: http://hmmer.org/download.html if you haven't done this before..."


def _choose_option(message, options):
    options = [
        s.rstrip()
        for s in options[:-1]
        if isfile(s.rstrip())
    ] + [options[-1]]

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
            if int(option_num) == len(options):
                which_program = 'prodigal' if 'Prodigal' in message else 'hmmsearch'
                res = input('Please, write a path to {}: '.format(which_program))
                return res
            option_num = int(option_num) - 1
            if 0 <= option_num < len(options):
                res = options[option_num]
        if res is None:
            print('Please select valid option number ({} to {})'.format(1, len(options)))
            continue
        return res

def download_file(filename, base_url, out_dir):
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

def download_pvogs(base_url, out_dir):
    if not exists(out_dir):
        os.makedirs(out_dir)
    # TODO: refactor 'allpvoghmms' const
    download_file('allpvoghmms', base_url, out_dir)
    download_file('allpvoghmms.h3f', base_url, out_dir)
    download_file('allpvoghmms.h3i', base_url, out_dir)
    download_file('allpvoghmms.h3m', base_url, out_dir)
    download_file('allpvoghmms.h3p', base_url, out_dir)


class SetupHelper(object):
    def __init__(self, dont_update_db):
        self.HOME = os.getenv("HOME")
        self._dont_update_db = dont_update_db

    def _locate(self, *args, **kwargs):
        if not self._dont_update_db:
            try:
                print('If you do not want to run sudo, use the following command to configure Phigaro:')
                print('       phigaro-setup --no-updatedb')
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
            # raise raise_if_not_found()
            print(raise_if_not_found)
            which_program = 'prodigal' if 'Prodigal' in raise_if_not_found else 'hmmsearch'
            locations = input('Write a full path to {}:'.format(which_program))
            return locations

        locations.append('Add another path manually')
        return _choose_option(
            message=options_message,
            options=locations,
        )

    def _setup_prodigal(self, ):
        prodigal_location = self._find_binary(name='prodigal',
                                         options_message='Please select appropriate Prodigal location',
                                         raise_if_not_found=ProdigalNotFound.message)
        return {
            'bin': prodigal_location,
        }

    def _setup_hmmer(self):
        hmmsearch_location = self._find_binary(name='hmmsearch',
                                               options_message='Please select appropriate HMMER location',
                                               raise_if_not_found=HMMERNotFound.message)
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
            },
            'phigaro': {
                'window_len': const.DEFAULT_WINDOW_SIZE,
                'threshold_min_basic': const.DEFAULT_THRESHOLD_MIN_BASIC,
                'threshold_max_basic': const.DEFAULT_THRESHOLD_MAX_BASIC,
                'threshold_min_abs': const.DEFAULT_THRESHOLD_MIN_ABS,
                'threshold_max_abs': const.DEFAULT_THRESHOLD_MAX_ABS,
                'threshold_min_without_gc': const.DEFAULT_THRESHOLD_MIN_WITHOUT_GC,
                'threshold_max_without_gc': const.DEFAULT_THRESHOLD_MAX_WITHOUT_GC,
                'mean_gc': const.DEFAULT_MEAN_GC,
                'penalty_black': const.DEFAULT_PENALTY_BLACK,
                'penalty_white': const.DEFAULT_PENALTY_WHITE
            }
        }
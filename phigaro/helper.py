import os
import time
from os.path import join, dirname, exists
from glob import glob
from shutil import copy
import sh
from future.backports.urllib.parse import urljoin

HOME = os.getenv("HOME")

# TODO: refactor this to class
is_updated_db = False


class HelperException(Exception):
    message = None


class MetaGeneMarkNotFound(HelperException):
    message = "Didn't find MetaGeneMark anywhere, " + \
              "please download it from http://topaz.gatech.edu/Genemark/license_download.cgi "


class MetaGeneMarkKeyNotFound(HelperException):
    message = "Please update your MetaGeneMark key file: "+ \
              "http://topaz.gatech.edu/GeneMark/license_download.cgi . " + \
              "You can download the \"key\" file only. "


class HMMERNotFound(HelperException):
    message = "No HMMER found. Please download HMMER package from here: http://hmmer.org/download.html "


def select_from_many(message, options):
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
        if option_num.isdecimal():
            option_num = int(option_num) - 1
            if 0 <= option_num < len(options):
                res = options[option_num]
        if res is None:
            print('Please select valid option number ({} to {})'.format(1, len(options)))
            continue
        return res


def locate(*args, **kwargs):
    # TODO: refactor this to class
    global is_updated_db
    if not is_updated_db:
        try:
            with sh.contrib.sudo:
                sh.updatedb()
                is_updated_db = True
        except sh.ErrorReturnCode_1:
            print('Invalid password')
            exit(1)
    return sh.locate(*args, **kwargs)


def find_gmhmmp_bin():
    mgm_location = sh.which("gmhmmp")
    if mgm_location:
        return mgm_location
    # print("MetaGeneMark is not in the PATH")
    try:
        message = 'Please select appropriate MetaGeneMark location'
        res = select_from_many(message=message,
                               options=locate("mgm/gmhmmp"))
        return res
    except sh.ErrorReturnCode_1 as ex:
        raise MetaGeneMarkNotFound()


def find_mgm_mod_file(mgm_dir):
    # TODO: handle no or multiple .mod files in mgm_dir
    message = 'Please select appropriate MetaGeneMark .mod file location'
    res = glob(join(mgm_dir, '*.mod'))
    return select_from_many(message=message,
                            options=res)


def is_gm_key_valid(gm_key_path):
    res = os.stat(gm_key_path)
    days = (time.time() - res.st_mtime) / (60 * 60 * 24)
    return days < 400


def find_gm_key():
    gm_keys = [
        gm_key_path.rstrip()
        for gm_key_path in locate('gm_key')
    ]

    valid_keys = [
        gm_key_path
        for gm_key_path in gm_keys
        if exists(gm_key_path) and is_gm_key_valid(gm_key_path)
    ]
    if not valid_keys:
        raise MetaGeneMarkKeyNotFound()
    return valid_keys[0]


def setup_mgm():
    mgm_location = find_gmhmmp_bin()
    mod_file = find_mgm_mod_file(dirname(mgm_location))
    gm_key_home = join(HOME, '.gm_key')

    if not exists(gm_key_home) or not is_gm_key_valid(gm_key_home):
        valid_gm_key = find_gm_key()
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


def setup_hmmer():
    # TODO: pVOG files
    hmmsearch_location = sh.which("hmmsearch")

    if hmmsearch_location is None:
        try:
            # in case hmmscan is in several places
            message = 'Please select appropriate HMMER location'
            hmmsearch_location = select_from_many(message=message,
                                                  options=locate("-r", "/hmmsearch$"))
        except sh.ErrorReturnCode_1:
            raise HMMERNotFound()

    return {
            'bin': hmmsearch_location,
            'e_value_threshold': 1.0e-5,
        }


def download_pvogs(base_url, out_dir):
    def download_file(filename):
        url = urljoin(base_url, filename)
        out = join(out_dir, filename)
        print('Downloading {url} to {out}'.format(
            url=url,
            out=out,
        ))
        sh.curl('-o', out, url, _tty_out=True)

    if not exists(out_dir):
        os.makedirs(out_dir)
    download_file('allpvoghmms')
    download_file('allpvoghmms.h3f')
    download_file('allpvoghmms.h3i')
    download_file('allpvoghmms.h3m')
    download_file('allpvoghmms.h3p')


def setup():
    mgm_params = setup_mgm()
    hmmer_params = setup_hmmer()

    return {
        'genemark': {
            'bin': mgm_params['bin'],
            'mod_path': mgm_params['mod_path'],
        },
        'hmmer': {
            'bin': hmmer_params['bin'],
            'pvog_path': hmmer_params['pvog_path'],
            'e_value_threshold': 1.0e-5,
        },
        'phigaro': {
            'window_len': 34,
            'threshold_min': 5.341108,
            'threshold_max': 7.571429,
        }
    }

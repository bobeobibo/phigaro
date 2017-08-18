import os
from os.path import join
from shutil import copy
import time

import sh


def locate_valid_key(cles_en_ord):
    # input:
    # list of key filenames
    bestbefore = 400
    fichier_frais = 'spacer'
    for cle in cles_en_ord:
        if cle:
            seconds = os.stat(cle)
            if ((time.time() - seconds.st_mtime) / (60 * 60 * 24)) < bestbefore:
                bestbefore = ((time.time() - seconds.st_mtime) / (60 * 60 * 24))
                fichier_frais = cle
    return (bestbefore, fichier_frais)


def setup():
    mgm_location = sh.which("gmhmmp")
    home = os.getenv("HOME")
    if mgm_location is None:
        print("MetaGeneMark is not in the PATH")
        try:
            not_in_path = sh.locate("mgm/gmhmmp")
        except sh.ErrorReturnCode_1:
            exit("Didn't find MetaGeneMark anywhere, "
                 "please download it from http://topaz.gatech.edu/Genemark/license_download.cgi ")
        print("Found MetaGeneMark location:")
        mgm_location = str(not_in_path).split('\n')[0]
        print(mgm_location)
        mod_file = str(sh.find(mgm_location[:-7], "-name", "*.mod")).rstrip()
        print("Found model file")
        print(mod_file)
        # courant = time.time()

        gmkey_path = join(home, '.gm_key')
        gmk = [line.rstrip() for line in sh.ls("-a", home) if line.rstrip() == '.gm_key']
        if gmk:
            dat = os.stat(home + "/" + gmk[0])
            if ((time.time() - dat.st_mtime) / (60 * 60 * 24)) < 400:
                print("Found valid MetaGeneMark key in the right place")
            else:
                # in case a valid MetaGeneMark file is availiable somewhere, but not in home
                # no need to "try" because we know some gm_key file is definitely there
                var_gm_keys = str(sh.locate('gm_key')).split('\n')
                print(var_gm_keys)
                ttt = locate_valid_key(var_gm_keys)
                best_before = ttt[0]
                fresh_file = ttt[1]
                print(ttt)
                if best_before == 400:
                    exit("Please update your MetaGeneMark key file: "
                         "http://topaz.gatech.edu/GeneMark/license_download.cgi . "
                         "You can download the “key” file only. ")
                else:
                    # in case the new keyfile is gzipped
                    print("Found a valid key file, copying to home directory.....")
                    if fresh_file[-3:] == ".gz":
                        sh.gunzip(fresh_file)
                        sh.cp(fresh_file[:-3], "~/.gm_key")
                    else:
                        sh.cp(fresh_file, "~/.gm_key")
        else:
            # if gm_key is somewhere but not in home
            try:
                var_gm_keys = str(sh.locate('gm_key')).split('\n')
            except sh.ErrorReturnCode_1:
                exit("Couldn't find MetaGeneMark license key, please download it: "
                     "http://topaz.gatech.edu/GeneMark/license_download.cgi . "
                     "You can download the “key” file only.")
            ttt = locate_valid_key(var_gm_keys)
            best_before = ttt[0]
            fresh_file = ttt[1]
            if best_before == 400:
                exit("Please update your MetaGeneMark key file: "
                     "http://topaz.gatech.edu/GeneMark/license_download.cgi . "
                     "You can download the “key” file only. ")
            else:
                print("Found a valid key file, copying to home directory.....")
                print(fresh_file)
                if fresh_file[-3:] == ".gz":
                    sh.gunzip(fresh_file, '-c', _out=gmkey_path)
                    # copy(fresh_file[:-3], gmkey_path)
                    # sh.cp(fresh_file[:-3], "~/.gm_key")
                else:
                    sh.cp(fresh_file, gmkey_path)
                    # copy(fresh_file, gmkey_path)
                    pass
    hmmsearch_location = sh.which("hmmsearch")
    if hmmsearch_location is None:
        try:
            # in case hmmscan is in several places
            print("Found HMMER")
            hs_not_in_path = sh.locate("-r", "/hmmsearch$")
            hmmsearch = hs_not_in_path.split('\n')[0]
            print(hmmsearch)
        except sh.ErrorReturnCode_1:
            exit("No HMMER found. Please download HMMER package from here: http://hmmer.org/download.html ")
    else:
        print("Found HMMER")
        print(hmmsearch_location)

    return {
        'genemark': {
            'bin': mgm_location,
            'mod_path': mod_file,
        },
        'hmmer': {
            'bin': hmmsearch_location,
            'pvog_path': 'software/hmmer/data/allprofiles.hmm',
            'e_value_threshold': 1.0e-5,
        },
        'phigaro': {
            'window_len': 34,
            'threshold_min': 5.341108,
            'threshold_max': 7.571429,
        }
    }
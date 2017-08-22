import csv
from itertools import groupby


def read_npn(filename, sep=None, as_dict=True):
    sep = sep or ' '
    with open(filename) as f:
        reader = csv.reader(f, delimiter=sep)
        if as_dict:
            return dict(reader)
        else:
            return reader


def read_coords(filename, sep=None):
    sep = sep or '\t'
    with open(filename) as f:
        reader = csv.reader(f, delimiter=sep)
        res = {}
        for phage, group in groupby(reader, key=lambda x: x[0]):
            res[phage] = sorted((
                (int(begin), int(end))
                for _, begin, end in group
            ), key=lambda x: x[0])
    return res


def convert_npn(phage, ph_sym):
    return [
        int(c == ph_sym)
        for c in phage
    ]

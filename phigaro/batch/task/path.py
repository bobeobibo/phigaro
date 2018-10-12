from os.path import join, basename
from os import makedirs, unlink
import re
import errno


def sample_name(sample_path):
    sample_path = basename(sample_path)
    tokens = sample_path.split('.')
    if len(tokens) == 1:
        return sample_path
    else:
        return '.'.join(tokens[:-1])


def path(*items):
    items = ('proc', ) + items
    return join(*items)


def remove(*items):
    target = path(*items)
    unlink(target)


def directory(*items):
    dir_name = path(*items)
    # https://stackoverflow.com/a/2383829
    try:
        makedirs(dir_name)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    return dir_name


def file(*items):
    directory(*items[:-1])
    return path(*items)

from os.path import join, basename, exists
from os import makedirs, unlink
import re
import errno


def sample_name(sample_path):
    sample_path = basename(sample_path)
    return re.match(r'(\w+)', sample_path).group(1)


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

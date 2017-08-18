from builtins import range

from .base import AbstractFinder, Phage
from functools import partial
import numpy as np


class V2Finder(AbstractFinder):
    def __init__(self, window_len, threshold_min, threshold_max):
        """
        :type window_len: int
        :type threshold_min: float
        :type threshold_max: float
        """
        self.window_len = window_len
        self.threshold_min = threshold_min
        self.threshold_max = threshold_max

    def find_phages(self, bacteria_npn):
        scores = calc_scores(bacteria_npn, self.window_len, score_tri)
        ranges = scan_phages(scores, self.threshold_min, self.threshold_max)
        for (begin, end) in ranges:
            yield Phage(
                begin=begin,
                end=end,
                is_prophage=True,
            )


def calc_scores(npn, window_len, score_func):
    scores = []
    len_d2 = window_len // 2
    tphage = np.concatenate([np.zeros(len_d2), npn, np.zeros(len_d2)])
    for i in range(len_d2, len(npn) + len_d2):
        begin = i-len_d2
        end = i+len_d2 + 1
        part = tphage[begin: end]
        scores.append(score_func(part))
    return np.array(scores)


def plane_kernel(pos):
    return 1


def tri_kernel(pos):
    return 1 - abs(pos - 0.5)/0.5


def score(part, kernel_func):
    return sum(
        c * kernel_func(i/(len(part) - 1))
        for i, c in enumerate(part)
    )


score_tri = partial(score, kernel_func=tri_kernel)
score_plane = partial(score, kernel_func=plane_kernel)


def scan_phages(scores, threshold_min, threshold_max):
    ranges = []

    begin = None
    end = None
    has_peak = False

    scores += [0]
    for i, v in enumerate(scores):
        if v >= threshold_max:
            has_peak = True
        if v >= threshold_min:
            if begin is None:
                begin = i
            end = i
        else:
            if begin is not None and has_peak:
                ranges.append((begin, end))
            begin = None
            end = None
            has_peak = False

    return ranges

from __future__ import division
from builtins import range
import numpy as np

from .base import AbstractFinder, Phage


class V2Finder(AbstractFinder):
    def __init__(self, window_len, threshold_min, threshold_max, mode):
        """
        :type window_len: int
        :type threshold_min: float
        :type threshold_max: float
        """
        self.window_len = window_len
        self.threshold_min = threshold_min
        self.threshold_max = threshold_max
        self.mode = mode

    def find_phages(self, bacteria_npn, bacteria_gc):
        scores = calc_scores(bacteria_npn, self.window_len)
        if self.mode != "without_gc":
            gc_scores = calc_scores(bacteria_gc, self.window_len)
            ranges = scan_phages(
                np.array(scores) * np.array(gc_scores),
                self.threshold_min,
                self.threshold_max,
            )
        else:
            ranges = scan_phages(
                np.array(scores), self.threshold_min, self.threshold_max
            )
        for (begin, end) in ranges:
            yield Phage(
                begin=begin,
                end=end,
                is_prophage=True,
            )


def calc_scores(npn, window_len):
    scores = []
    len_d2 = window_len // 2
    tphage = np.concatenate([np.zeros(len_d2), npn, np.zeros(len_d2)])

    kernel_koeffs = tri_kernel(np.arange(len_d2 * 2 + 1) / (len_d2 * 2))
    for i in range(len_d2, len(npn) + len_d2):
        begin = i - len_d2
        end = i + len_d2 + 1
        part = tphage[begin:end]
        scores.append(np.sum(part * kernel_koeffs))
    return scores


def tri_kernel(pos):
    return 1 - abs(pos - 0.5) / 0.5


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

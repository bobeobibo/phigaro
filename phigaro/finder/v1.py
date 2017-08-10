from __future__ import print_function, absolute_import

from .base import AbstractFinder, Phage
import math

WINDOW_SIZE = 37  # optimize this
MIN_PHAGE_IN_WINDOW = 14  # optimize this


class V1Finder(AbstractFinder):
    def __init__(self, window_size=WINDOW_SIZE, min_phage_in_window=MIN_PHAGE_IN_WINDOW):
        self.window_size = window_size
        self.min_phage_in_window = min_phage_in_window

    def find_phages(self, bacteria_npn):
        kkz, ar_positions = convert_npn(bacteria_npn)

        grad = count_grad(kkz, self.window_size)
        norm_grad = count_norm_grad(grad, self.window_size, self.min_phage_in_window)
        phages = get_phages(kkz, norm_grad)

        for phage in phages:
            # ar_here = any(
            #     phage['end'] + 2 >= pos >= phage['start'] - 2
            #     for pos in ar_positions
            # )

            yield Phage(
                begin=phage['start'],
                end=phage['end'],
                is_prophage=phage['end'] - phage['start'] < 0.8 * len(kkz),
            )


def count_grad(sequence, window_size):
    # input: 'NPPPNNPNPN??NP'-like sequence converted to [0,1,1,1,0,0,1,0,1,0,0,0,0,1], list type
    grad = []
    offset = math.floor(window_size / 2)
    for i in range(0, len(sequence)):  # for all values
        grad.append(0)
        start = int(i - offset)
        if start < 0:  # if start is negative
            start = 0
        end = int(i + offset)
        if end > len(sequence) - 1:  # if end is out of range
            end = len(sequence) - 1
        grad[i] += sum(sequence[start:end + 1])  # count sum of elements in window
    return grad


# delete all elements from grad which do not have neighbors that > minVal
def count_norm_grad(grad, window_size, min_val):
    # input: grad from previous function, window size, number of phage sequences in a window threshold
    norm_grad = list(grad)  # copy gradient
    offset = math.floor(window_size / 2)
    for i in range(0, len(norm_grad)):  # same as in previous function
        start = int(i - offset)
        if start < 0:
            start = 0
        end = int(i + offset)
        if end > len(grad) - 1:
            end = len(grad) - 1
        delete = True
        for j in range(start, end):  # check neighbors
            if norm_grad[j] > min_val:  # if at least one is bigger than minVal
                delete = False
        if delete:
            norm_grad[i] = 0
    return norm_grad


def get_phages(sequence, norm_grad):  # get coordinates of phages
    phages = []
    i = 0
    while i < len(norm_grad):
        if norm_grad[i] != 0:  # bump into not zero
            start = i
            if start < 0:
                start = 0
            end = find_end_of_range(norm_grad, start)
            if start >= end:
                break
            phage_start = find_phage_start(sequence, start)
            phage_end = find_phage_end(sequence, end)
            if phage_start < 0:
                phage_start = 0
            phages.append({"start": phage_start, "end": phage_end})
            i = end + 1
        else:
            i += 1
    return phages


def find_end_of_range(norm_grad, i_start):  # find where the sequence stops (12345321*here*0000)
    # takes normGrad and putative end position
    i = i_start
    while norm_grad[i] != 0 and i < (len(norm_grad) - 1):
        i += 1
    return i - 1


def find_phage_start(sequence, i_start):  # find first phage protein in sequence
    i = i_start
    while sequence[i] == 0 and i < (len(sequence) - 1):
        i += 1
    return i - 1


def find_phage_end(sequence, i_end):  # find last phage protein in sequence
    i = i_end
    while sequence[i] == 0:
        i -= 1
    return i + 1


def convert_npn(npn):
    # type: (str)->(list[int], list[int])

    kkz = []
    ar_positions = []

    for i, letter in enumerate(npn):
        if letter == 'P':
            kkz.append(1)
        else:
            kkz.append(0)
        if letter == 'r':
            ar_positions.append(i)
    return kkz, ar_positions



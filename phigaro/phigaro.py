from __future__ import print_function, absolute_import

import csv
import math
from phigaro import const


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
    # type: (str)->(list[int], list[int)

    kkz = []
    ar_positions = []

    for i, letter in enumerate(npn):
        if letter == 'P':
            kkz.append(1)
        elif letter == 'r':
            ar_positions.append(i)
        else:
            kkz.append(0)
    return kkz, ar_positions


def process_scaffold(npn):
    # type: (str, str)->list[dict[str, str]]
    kkz, ar_positions = convert_npn(npn)

    grad = count_grad(kkz, const.WINDOW_SIZE)
    norm_grad = count_norm_grad(grad, const.WINDOW_SIZE, const.MIN_PHAGE_IN_WINDOW)
    phages = get_phages(kkz, norm_grad)

    # res = {
    #     'phage': False,
    #     'pro_phage': False,
    #     'ar_phage': False,
    # }
    res = []

    # res['phage'] = True
    # if ar_positions:
    #     pass
    for phage in phages:
        # if ar_positions:
        #     print(scaffold, npn[phage['start']:phage['end'] + 1])
        # if phage['end'] - phage['start'] > 0.8 * len(kkz):  # this is not nessesary
        #     print("It is a phage")
        # else:
        #     print("It is a prophage")
        # ar_here = False
        # for ar_pos in ar_positions:
        #     if (ar_pos >= (phage['start'] - 2)) and (ar_pos <= (phage['end'] + 2)):
        #         ar_here = True
        #         print("AR-gene inside")
        # if ar_here:
        #     count_ar_phage += 1

        ar_here = any(
            phage['end'] + 2 >= pos >= phage['start'] - 2
            for pos in ar_positions
        )

        res.append({
            'start': phage['start'],
            'end': phage['end'],
            'is_pro_phage': phage['end'] - phage['start'] < 0.8 * len(kkz),
            'ar_here': ar_here
        })
    return res


def find_phages(filename):
    # type: (str) -> list[(str, str, list[dict])]

    with open(filename) as f:
        lines = f.read().split("\n")

    scaffolds_npns = [x.split(' ') for x in lines if x]

    scaffold_phages = []

    for scaffold, npn in scaffolds_npns:
        phages = process_scaffold(npn)
        if phages:
            scaffold_phages.append(
                (scaffold, npn, phages)
            )

    return scaffold_phages

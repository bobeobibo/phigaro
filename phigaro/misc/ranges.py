from __future__ import division
import numpy as np


def first(x):
    return x[0]


def second(x):
    return x[1]


def intersection_range(range1, range2):
    begin = max(range1[0], range2[0])
    end = min(range1[1], range2[1])
    if begin > end:
        return None
    return begin, end


def negate(ranges, max_len):
    end = 0
    for rbegin, rend in ranges:
        if end != rbegin:
            yield (end, rbegin)
        end = rend
    if end != max_len:
        yield (end, max_len)


def intersection(ranges1, ranges2):
    if not ranges1 or not ranges2:
        return
    it_a = iter(ranges1)
    it_b = iter(ranges2)

    ra = next(it_a)
    rb = next(it_b)

    while True:
        try:
            inter = intersection_range(ra, rb)

            if inter is not None:
                yield inter
            if second(ra) > second(rb):
                rb = next(it_b)
            else:
                ra = next(it_a)
        except StopIteration:
            break


def union(ranges1, ranges2):
    if not ranges1:
        return ranges2
    if not ranges2:
        return ranges1

    max_len = max(ranges1[-1][1], ranges2[-1][1])
    ranges1 = negate(ranges1, max_len)
    ranges2 = negate(ranges2, max_len)
    inter = (r for r in intersection(ranges1, ranges2) if r[0] != r[1])
    return negate(inter, max_len)


def len_ranges(ranges):
    return sum(
        end - begin + 1
        for begin, end in ranges
    )


def jakkard_index(ranges1, ranges2):
    intersection_len = len_ranges(intersection(ranges1, ranges2))
    union_len = len_ranges(union(ranges1, ranges2))

    if intersection_len != 0 and union_len == 0:
        print(ranges1, ranges2)
        raise Exception('union error')

    if intersection_len == 0:
        return 0
    return intersection_len / union_len


def minus(ranges1, ranges2):
    if not ranges1:
        return
    if not ranges2:
        for r in ranges1:
            yield r
        return

    max_len = max(ranges1[-1][1], ranges2[-1][1]) + 1
    ranges2 = intersection(ranges1, ranges2)
    ranges2 = negate(ranges2, max_len)
    ranges2 = [
        (begin + 1, end - 1)
        for (begin, end) in ranges2
        if end - begin >= 2
        ]
    for (begin, end) in intersection(ranges1, ranges2):
        yield (begin, end)


def true_positives_rate(test_ranges, real_ranges):
    return (
        len_ranges(intersection(test_ranges, real_ranges)) /
        len_ranges(real_ranges)
    )


def false_positives_rate(test_ranges, real_ranges, max_len=None):
    if not test_ranges:
        return 0
    return (
        len_ranges(minus(test_ranges, real_ranges)) /
        len_ranges(negate(real_ranges, max_len))
    )


def false_discovery_rate(test_ranges, real_ranges):
    test_ranges_length = len_ranges(test_ranges)
    if not test_ranges_length:
        return np.nan
    return (
        len_ranges(minus(test_ranges, real_ranges)) /
        test_ranges_length
    )


def positive_predictive_value(test_ranges, real_ranges):
    test_ranges_length = len_ranges(test_ranges)
    if not test_ranges_length:
        return np.nan

    true_positives = len_ranges(intersection(test_ranges, real_ranges))
    return true_positives / test_ranges_length


def false_negatives_rate(test_ranges, real_ranges):
    return 1 - true_positives_rate(test_ranges, real_ranges)




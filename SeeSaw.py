import itertools


def seesaw(sequence):
    odd, even = itertools.tee(sequence)
    res = itertools.zip_longest((x for x in even if x % 2 == 0),
                                (y for y in odd if y % 2 != 0),
                                fillvalue=None)
    for x, y in res:
        if x is not None:
            yield x
        if y is not None:
            yield y

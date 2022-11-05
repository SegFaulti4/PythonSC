def nomore(sequence):
    for ceil in sequence:
        for el in sequence:
            if el <= ceil:
                yield el

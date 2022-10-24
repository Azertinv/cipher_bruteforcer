#!/usr/bin/python3

from common import *

def measure(cts):
    assert len(cts) > 1
    values = []
    for i in range(max([len(ct) for ct in cts])):
        values.append(set())
    for ct in cts:
        for i, l in enumerate(ct):
            values[i].add(l)
    holes = []
    for index in values:
        index = list(index)
        index.sort()
        index_holes = []
        for i in range(len(index)):
            index_holes.append((index[i] - index[i - 1]) % CT_ALPHABET_SIZE)
        holes.append(index_holes)
    bounds = []
    for index in holes:
        if len(index) <= 1:
            bounds.append(0)
        else:
            index.remove(max(index))
            bounds.append(sum(index))
    mean = sum(bounds) / len(bounds)
    median = bounds[(len(bounds)+1) // 2]
    return [mean, median, min(bounds), max(bounds)]

if __name__ == "__main__":
    print(measure(get_stdin_texts()))

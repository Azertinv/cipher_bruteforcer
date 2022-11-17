#!/usr/bin/python3

from common import *

def measure(cts):
    values = []
    for i in range(max([len(ct) for ct in cts])):
        values.append(set())
    for ct in cts:
        for i, l in enumerate(ct):
            values[i].add(l)
    counts = [0] * CT_ALPHABET_SIZE
    for index in values:
        for letter in index:
            counts[letter] += 1
    counts_sum = sum(counts)
    counts = [x / counts_sum for x in counts]
    return data_to_info(counts)

if __name__ == "__main__":
    print(measure(get_stdin_texts()))

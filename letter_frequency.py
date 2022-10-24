#!/usr/bin/python3

from common import *

def measure(cts):
    counts = [0] * CT_ALPHABET_SIZE
    for ct in cts:
        for letter in ct:
            counts[letter] += 1
    sample_size = sum([len(ct) for ct in cts])
    for i in range(len(counts)):
        counts[i] /= sample_size
    return counts

if __name__ == "__main__":
    print(measure(get_stdin_texts()))

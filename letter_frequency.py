#!/usr/bin/python3

from common import *

def measure(cts):
    counts = [0] * CT_ALPHABET_SIZE
    for ct in cts:
        for letter in ct:
            counts[letter] += 1
    # TODO FIXME return raw values too
    return data_to_info(counts)

if __name__ == "__main__":
    print(measure(get_stdin_texts()))

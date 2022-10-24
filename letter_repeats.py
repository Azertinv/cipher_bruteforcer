#!/usr/bin/python3

from common import *

def measure(cts):
    sample_size = sum([len(ct) for ct in cts])
    dg_repeats_count = 0
    for ct in cts:
        for i in range(len(ct) - 1):
            if ct[i] == ct[i+1]:
                dg_repeats_count += 1
    dg_repeats_count /= sample_size
    return [dg_repeats_count]

if __name__ == "__main__":
    print(measure(get_stdin_texts()))

#!/usr/bin/python3

from common import *

def measure(cts):
    sample_size = sum([len(ct) for ct in cts])
    isomorphs = [get_isomorphs(ct, 50) for ct in cts]
    isomorphs_size = [0]*50
    for i in isomorphs:
        for index, size in i:
            if size - 1 < len(isomorphs_size):
                isomorphs_size[size] += 1
    # TOO return raw values too
    return data_to_info(isomorphs_size)

if __name__ == "__main__":
    print(measure(get_stdin_texts()))

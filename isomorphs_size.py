#!/usr/bin/python3

from common import *

def measure(cts):
    sample_size = sum([len(ct) for ct in cts])
    isomorphs = [get_isomorphs(ct) for ct in cts]
    isomorphs_size = [0]*150
    for i in isomorphs:
        for index, size in i:
            if size - 1 < len(isomorphs_size):
                isomorphs_size[size - 1] += 1
    return isomorphs_size

if __name__ == "__main__":
    print(measure(get_ciphertexts()))

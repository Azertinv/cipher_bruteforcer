#!/usr/bin/python3

from common import *

def measure(cts):
    sample_size = sum([len(ct) for ct in cts])
    isomorphs = [get_isomorphs(ct) for ct in cts]
    isomorphs_count = sum([len(i) for i in isomorphs])
    score = 0.0
    for i in range(len(cts)):
        for index, size in isomorphs[i]:
            # test the shared isomorph 25 letter left and right
            for offset in range(25):
                # only test for the shared isomorphs in the other messages
                for j in range(i + 1, len(cts)):
                    if (index + offset, size) in isomorphs[j]:
                        score += 1/(offset + 1)
                    if (index - offset, size) in isomorphs[j]:
                        score += 1/(offset + 1)
    score /= sample_size
    isomorphs_count /= sample_size
    return [score, isomorphs_count]

if __name__ == "__main__":
    print(measure(get_ciphertexts()))

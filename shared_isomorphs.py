#!/usr/bin/python3

from common import *

def measure(cts):
    sample_size = sum([len(ct) for ct in cts])
    # for performance reasons we only look for isomorphs size 15 and under
    isomorphs = [get_isomorphs(ct, 15) for ct in cts]
    isomorphs_count = sum([len(i) for i in isomorphs])
    score = 0.0
    cts_len = len(cts)
    for i in range(len(isomorphs)):
        for index, size in isomorphs[i]:
            # test the shared isomorph 20 letter left and right
            for offset in range(20):
                # only test for the shared isomorphs in the other messages
                for j in range(i + 1, cts_len):
                    if (index + offset, size) in isomorphs[j]:
                        score += 1/(offset + 1)
                    if (index - offset, size) in isomorphs[j]:
                        score += 1/(offset + 1)
    return {"score": score, "count": isomorphs_count}

if __name__ == "__main__":
    print(measure(get_stdin_texts()))

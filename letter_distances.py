#!/usr/bin/python3

from common import *

def modulo_distance(v1, v2):
    i = (v1 - v2) % CT_ALPHABET_SIZE
    j = (v2 - v1) % CT_ALPHABET_SIZE
    return min(i, j)

def measure(cts):
    distances = []
    for ct in cts:
        for i in range(len(ct) - 1):
            distances.append(modulo_distance(ct[i], ct[i + 1]))
            # distances.append(ct[i] - ct[i + 1])
    mean = sum(distances) / len(distances)
    distances.sort()
    median = distances[len(distances) // 2]
    return [mean, median, min(distances), max(distances)]

if __name__ == "__main__":
    print(measure(get_stdin_texts()))

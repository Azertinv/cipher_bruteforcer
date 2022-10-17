#!/usr/bin/python3

import sys
from matplotlib import pyplot as plt

CT_ALPHABET = bytes(range(83))
CT_ALPHABET_SIZE = len(CT_ALPHABET)

def get_ciphertexts():
    cts = sys.stdin.buffer.read().splitlines()
    cts = [[y-32 for y in x] for x in cts]
    return cts

def get_isomorphs(ct):
    isomorphs = []
    for i, l in enumerate(ct):
        if l in ct[i+1:]:
            next_i = ct.index(l, i + 1)
            if next_i != -1:
                isomorphs.append((i, next_i - i))
    return isomorphs

# takes a ciphertext
# returns a dictionnary, key is letter, value is count
def get_letters_count(ct):
    counts = dict.fromkeys(range(CT_ALPHABET_SIZE), 0)
    for l in ct:
        counts[l] += 1
    return counts

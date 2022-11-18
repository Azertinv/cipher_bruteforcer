#!/usr/bin/python3

from common import *
import random

def generate():
    return [random.randrange(0, 2**31)]

def mutate(params):
    params = params.copy()
    params[0] = random.randrange(0, 2**31)
    return params

def encrypt(pts, params):
    seed = params[0]
    def ct_alphabet_generator(i):
        random.seed(seed * 0x1000 + i)
        shift = random.randrange(CT_ALPHABET_SIZE)
        return CT_ALPHABET[-shift:] + CT_ALPHABET[:-shift]
    return poly_substitute(pts, ct_alphabet_generator)

if __name__ == "__main__":
    cts = encrypt(get_stdin_texts(), [1337])
    for ct in cts:
        print(bytes([l + READABLE_OFFSET for l in ct]).decode())

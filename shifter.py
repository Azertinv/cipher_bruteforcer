#!/usr/bin/python3

from common import *
import random

def generate():
    return [random.randrange(0, CT_ALPHABET_SIZE)]

MUTATION_COUNT = 3

def mutate(params, choice):
    params = params.copy()
    if choice == -1:
        choice = 2
    if choice == 0:
        params[0] += 1
    elif choice == 1:
        params[0] -= 1
    elif choice == 2:
        params[0] = random.randrange(CT_ALPHABET_SIZE)
    params[0] %= CT_ALPHABET_SIZE
    return params

def encrypt(pts, params):
    key = params[0]
    def ct_alphabet_generator(i):
        shift = (i * key) % CT_ALPHABET_SIZE
        return CT_ALPHABET[-shift:] + CT_ALPHABET[:-shift]
    return poly_substitute(pts, ct_alphabet_generator)

if __name__ == "__main__":
    cts = encrypt(get_stdin_texts(), [1])
    for ct in cts:
        print(bytes([l + READABLE_OFFSET for l in ct]).decode())

#!/usr/bin/python3

from common import *
import random

def generate():
    return [random.randrange(0, 2**31)]

MUTATION_COUNT = 5

def mutate(params, _):
    params = params.copy()
    params[0] = random.randrange(0, 2**31)
    return params

rng = random.Random()

def encrypt(pts, params):
    scrambled_ct_alphabet = list(CT_ALPHABET)
    rng.seed(params[0])
    rng.shuffle(scrambled_ct_alphabet)
    return substitute(pts, scrambled_ct_alphabet)

if __name__ == "__main__":
    cts = encrypt(get_stdin_texts(), [42])
    for ct in cts:
        print(bytes([l + READABLE_OFFSET for l in ct]).decode())

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
    seed = params[0]
    def ct_alphabet_generator(i):
        scrambled_ct_alphabet = list(CT_ALPHABET)
        rng.seed(seed * 0x1000 + i)
        rng.shuffle(scrambled_ct_alphabet)
        return scrambled_ct_alphabet
    return poly_substitute(pts, ct_alphabet_generator)

if __name__ == "__main__":
    print_cts(encrypt(get_stdin_texts(), [1337]))

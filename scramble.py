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
    scrambled_ct_alphabet = list(CT_ALPHABET)
    random.seed(params[0])
    random.shuffle(scrambled_ct_alphabet)
    return substitute(pts, scrambled_ct_alphabet)

if __name__ == "__main__":
    cts = encrypt(get_stdin_texts(), [42])
    for ct in cts:
        print(bytes([l + READABLE_OFFSET for l in ct]).decode())

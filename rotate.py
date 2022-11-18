#!/usr/bin/python3

from common import *
import random

def generate():
    return [random.randrange(CT_ALPHABET_SIZE)]

def mutate(params):
    params = params.copy()
    choice = random.randint(0, 2)
    if choice == 0:
        params[0] += 1
    elif choice == 1:
        params[0] -= 1
    elif choice == 2:
        params[0] = random.randrange(CT_ALPHABET_SIZE)
    params[0] %= CT_ALPHABET_SIZE
    return params

def encrypt(pts, params):
    ct_alphabet = list(CT_ALPHABET)
    shift = params[0] % CT_ALPHABET_SIZE
    ct_alphabet = ct_alphabet[-shift:] + ct_alphabet[:-shift]
    return substitute(pts, ct_alphabet)

if __name__ == "__main__":
    cts = encrypt(get_stdin_texts(), [42])
    for ct in cts:
        print(bytes([l + READABLE_OFFSET for l in ct]).decode())

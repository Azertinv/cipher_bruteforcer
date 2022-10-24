#!/usr/bin/python3

from common import *
import random

def generate():
    return [random.randrange(0, 2**31)]

def encrypt(pts, params):
    ct_alphabet = list(CT_ALPHABET)
    shift = params[0] % CT_ALPHABET_SIZE
    ct_alphabet = ct_alphabet[-shift:] + ct_alphabet[:-shift]
    return substitute(pts, ct_alphabet)

if __name__ == "__main__":
    cts = encrypt(get_stdin_texts(), [42])
    for ct in cts:
        print(bytes([l + READABLE_OFFSET for l in ct]).decode())

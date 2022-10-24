#!/usr/bin/python3

from common import *
import random

def generate():
    return [random.randrange(0, 83)]

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

#!/usr/bin/python3

from common import *

import random

import autokey_rotate
import poly_scramble
import random_shift
import rotate
import scramble
import shifter
import vigenere

ciphers = [
    autokey_rotate,
    poly_scramble,
    random_shift,
    rotate,
    scramble,
    shifter,
    vigenere,
]

for c in ciphers:
    assert hasattr(c, "generate")
    assert hasattr(c, "encrypt")

def main():
    pts = get_stdin_texts()
    random.seed(44)
    cipher_stack = []
    for _ in range(5):
        cipher = random.choice(ciphers)
        params = cipher.generate()
        cipher_stack.append((cipher, params))
    for (cipher, params) in cipher_stack:
        pts = cipher.encrypt(pts, params)
    print_cts(pts)

if __name__ == "__main__":
    main()

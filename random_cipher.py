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

def random_cipher_stack(n=5):
    cipher_stack = []
    for _ in range(n):
        cipher = random.choice(ciphers)
        params = cipher.generate()
        cipher_stack.append((cipher, params))
    return cipher_stack

def encrypt_with_cipher_stack(cipher_stack, pts):
    for (cipher, params) in cipher_stack:
        pts = cipher.encrypt(pts, params)
    return pts

if __name__ == "__main__":
    pts = get_stdin_texts()
    random.seed(44)
    cipher_stack = random_cipher_stack(5)
    cts = encrypt_with_cipher_stack(cipher_stack, pts)
    print_cts(cts)

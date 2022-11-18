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
    assert hasattr(c, "mutate")
    assert hasattr(c, "generate")
    assert hasattr(c, "encrypt")

MAX_CIPHER_STACK_SIZE = 10

def mutate_cipher_stack(cipher_stack):
    cipher_stack = cipher_stack.copy()
    choice = random.randint(0, 2)
    random_index = random.randrange(0, len(cipher_stack))
    if choice == 0 and len(cipher_stack) < MAX_CIPHER_STACK_SIZE: # insert step
        cipher_stack.insert(random_index, random_cipher_step())
    elif choice == 1 and len(cipher_stack) > 1: # remove step
        cipher_stack.pop(random_index)
    else: # mutate step
        (cipher, params) = cipher_stack[random_index]
        cipher_stack[random_index] = (cipher, cipher.mutate(params))
    return cipher_stack

def random_cipher_step():
    cipher = random.choice(ciphers)
    return (cipher, cipher.generate())

def random_cipher_stack(n=5):
    return [random_cipher_step() for _ in range(n)]

def encrypt_with_cipher_stack(cipher_stack, pts):
    for (cipher, params) in cipher_stack:
        pts = cipher.encrypt(pts, params)
    return pts

def main():
    random.seed(44)
    cipher_stack = random_cipher_stack(5)
    pts = get_stdin_texts()
    cts = encrypt_with_cipher_stack(cipher_stack, pts)
    print_cts(cts)

if __name__ == "__main__":
    main()

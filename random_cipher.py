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

MAX_CIPHER_STACK_SIZE = 10

MUTATION_MULT = 10
MUTATION_COUNT = 3 * MUTATION_MULT

for c in ciphers:
    assert hasattr(c, "MUTATION_COUNT")
    assert hasattr(c, "mutate")
    assert hasattr(c, "generate")
    assert hasattr(c, "encrypt")

def get_mutation_count(cipher_stack):
    count = MUTATION_COUNT
    for (cipher, _) in cipher_stack:
        count += cipher.MUTATION_COUNT
    return count

def mutate_cipher_stack(cipher_stack, iteration=-1):
    cipher_stack = cipher_stack.copy()
    if iteration == -1:
        choice = random.randint(0, 3)
    else:
        choice = 0
        while iteration >= MUTATION_MULT and choice < 3:
            choice += 1
            iteration -= MUTATION_MULT
    random_index = random.randrange(0, len(cipher_stack))
    if choice == 0 and len(cipher_stack) < MAX_CIPHER_STACK_SIZE: # insert step
        cipher_stack.insert(random_index, random_cipher_step())
    elif choice == 1 and len(cipher_stack) > 1: # remove step
        cipher_stack.pop(random_index)
    elif choice == 2: # change step
        cipher_stack[random_index] = random_cipher_step()
    elif choice == 3: # mutate step
        if iteration == -1:
            (cipher, params) = cipher_stack[random_index]
            choice = random.randrange(0, cipher.MUTATION_COUNT)
            cipher_stack[random_index] = (cipher, cipher.mutate(params, choice))
        else:
            for i, (cipher, params) in enumerate(cipher_stack):
                if iteration >= cipher.MUTATION_COUNT:
                    iteration -= cipher.MUTATION_COUNT
                else:
                    cipher_stack[i] = (cipher, cipher.mutate(params, iteration))
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
    cipher_stack = random_cipher_stack(2)
    pts = get_stdin_texts()
    cts = encrypt_with_cipher_stack(cipher_stack, pts)
    print_cts(cts)

if __name__ == "__main__":
    main()

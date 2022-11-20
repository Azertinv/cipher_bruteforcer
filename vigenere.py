#!/usr/bin/python3

from common import *
import random

MAX_KEY_SIZE = 50

def generate():
    return random.choices(CT_ALPHABET, k=random.randrange(1, MAX_KEY_SIZE))

MUTATION_COUNT = 10

def mutate(params, choice):
    params = params.copy()
    random_index = random.randrange(len(params))
    if choice == -1:
        choice = random.randint(0, 2)
    if choice % 3 == 0 and len(params) > 1: # remove char
        params.pop(random_index)
    elif choice % 3 == 1 and len(params) < MAX_KEY_SIZE: # insert char
        params.insert(random_index, random.choice(CT_ALPHABET))
    elif choice % 3 == 2: # mutate char
        params[random_index] = random.choice(CT_ALPHABET)
    return params

def encrypt(pts, params):
    key = params
    def ct_alphabet_generator(i):
        shift = key[i % len(key)] % CT_ALPHABET_SIZE
        return CT_ALPHABET[-shift:] + CT_ALPHABET[:-shift]
    return poly_substitute(pts, ct_alphabet_generator)

if __name__ == "__main__":
    cts = encrypt(get_stdin_texts(), [b"Ayylmao"])
    for ct in cts:
        print(bytes([l + READABLE_OFFSET for l in ct]).decode())

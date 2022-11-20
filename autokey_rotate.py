#!/usr/bin/python3

from common import *
import random

def generate():
    return [random.randrange(CT_ALPHABET_SIZE), random.random()]

MUTATION_COUNT = 5

def mutate(params, choice):
    params = params.copy()
    if choice == -1:
        choice = 1
    if choice == 0: # change direction
        params[1] = 1.0 - params[1]
    elif choice >= 1: # change IV
        params[0] = (params[0] + random.randrange(CT_ALPHABET_SIZE - 1)) % CT_ALPHABET_SIZE
    return params

def encrypt(pts, params):
    iv = params[0]
    direction = params[1]
    def autokeyer_alphabet_generator(l):
        autokey_alphabet = list(CT_ALPHABET)
        if direction > 0.5:
            shift = -l % CT_ALPHABET_SIZE
        else:
            shift = l % CT_ALPHABET_SIZE
        return autokey_alphabet[-shift:] + autokey_alphabet[:-shift]
    return autokeyer(pts, autokeyer_alphabet_generator, iv)

if __name__ == "__main__":
    print_cts(encrypt(get_stdin_texts(), [0, 0.1]))

#!/usr/bin/python3

from common import *
from random_cipher import encrypt_with_cipher_stack

import sys
import pickle

def main():
    with open(sys.argv[1], 'rb') as f:
        cipher_stack = pickle.load(f)
    pts = get_stdin_texts()
    cts = encrypt_with_cipher_stack(cipher_stack, pts)
    print_cts(cts)

if __name__ == "__main__":
    main()

#!/usr/bin/python3

from common import *

import sys
import random

def generate_random_ct():
    return [random.choice(CT_ALPHABET) for _ in range(random.randint(99, 137))]

def generate_no_doubles_ct():
    ct = generate_random_ct()
    i = 0
    while i + 1 < len(ct):
        if ct[i] == ct[i + 1]:
            ct.pop(i)
        i += 1
    return ct

import sys

def generate_random_cts(seed):
    random.seed(seed)
    if "--double-l" in sys.argv:
        return [bytes(generate_random_ct()) for _ in range(9)]
    else:
        return [bytes(generate_no_doubles_ct()) for _ in range(9)]

if __name__ == "__main__":
    if len(sys.argv) > 1:
        seed = int(sys.argv[1])
    else:
        seed = random.randint(0, 2**31)
    for ct in generate_random_cts(seed):
        print("".join([chr(x + 32) for x in ct]))

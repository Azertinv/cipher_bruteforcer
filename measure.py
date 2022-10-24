#!/usr/bin/python3

from common import *

import index_bounds
import isomorphs_size
import letter_frequency
import letter_repeats
import shared_isomorphs

properties = [
    index_bounds,
    isomorphs_size,
    letter_frequency,
    letter_repeats,
    shared_isomorphs,
]

for p in properties:
    assert hasattr(p, "measure")

def measure(cts):
    return [p.measure(cts) for p in properties]

if __name__ == "__main__":
    results = measure(get_stdin_texts())
    for p, r in zip(properties, results):
        print(p.__name__)
        print(r)
        print()

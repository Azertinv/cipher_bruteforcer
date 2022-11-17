#!/usr/bin/python3

from common import *

import index_bounds
import isomorphs_size
import letter_frequency
import letter_frequency_no_shared_letters
import letter_repeats
import shared_isomorphs
import letter_distances
import gapped_pairs_repeats

properties = [
    index_bounds,
    isomorphs_size,
    letter_frequency,
    letter_frequency_no_shared_letters,
    letter_repeats,
    shared_isomorphs,
    letter_distances,
    gapped_pairs_repeats,
]

for p in properties:
    assert hasattr(p, "measure")

def measure(cts):
    return dict([(p, p.measure(cts)) for p in properties])

if __name__ == "__main__":
    results = measure(get_stdin_texts())
    for p, r in results.items():
        print(p.__name__)
        for name, value in r.items():
            print(name, ":", value)
        print()

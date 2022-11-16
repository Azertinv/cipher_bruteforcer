#!/usr/bin/python3

from common import *

from measure import measure
from statistics import stdev
from random_ciphertext import generate_random_cts

import pickle
import os

CACHE_FILE = "measures.cache"

def get_means_and_stdevs(no_cache=False):
    if (not os.path.exists(CACHE_FILE)) or no_cache:
        means = []
        stdevs = []
        measures = []
        for i in range(10000):
            measures.append(measure(generate_random_cts(i)))
        for j in measures[0].keys():
            for k in measures[0][j].keys():
                data = [measures[i][j][k] for i in range(len(measures))]
                means.append(sum(data) / len(data))
                s = stdev(data)
                if s == 0.0:
                    s = 0.0000001
                stdevs.append(s)
        with open(CACHE_FILE, 'wb') as f:
            pickle.dump((means, stdevs), f)
    else:
        with open(CACHE_FILE, 'rb') as f:
            (means, stdevs) = pickle.load(f)
    return (means, stdevs)

def main():
    import sys

    no_cache = False
    if "--no-cache" in sys.argv:
        no_cache = True
    (means, stdevs) = get_means_and_stdevs(no_cache)

    cts = get_stdin_texts()
    cts_measures = measure(cts)

    i = 0
    for j in cts_measures.keys():
        print(j.__name__)
        for k in cts_measures[j].keys():
            diff = (cts_measures[j][k]/stdevs[i]) - (means[i]/stdevs[i])
            print(k+": ", end="")
            if abs(diff) > 3.5:
                print("\x1b[0;37;41m", end="")
            print("{:.1f}\x1b[0;0m".format(diff))
            i += 1
        print()

if __name__ == "__main__":
    main()

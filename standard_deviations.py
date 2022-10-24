#!/usr/bin/python3

from common import *

from measure import measure
from statistics import stdev
from random_ciphertext import generate_random_cts

import pickle
import os

CACHE_FILE = "measures.cache"

def main():
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'rb') as f:
            (means, stdevs) = pickle.load(f)
    else:
        means = []
        stdevs = []
        measures = []
        for i in range(10000):
            measures.append(measure(generate_random_cts(i)))
        for j in range(len(measures[0])):
            for k in range(len(measures[0][j])):
                data = [measures[i][j][k] for i in range(len(measures))]
                means.append(sum(data) / len(data))
                stdevs.append(stdev(data))
        with open(CACHE_FILE, 'wb') as f:
            pickle.dump((means, stdevs), f)

    cts = get_stdin_texts()
    cts_measures = measure(cts)

    i = 0
    for j in range(len(cts_measures)):
        for k in range(len(cts_measures[j])):
            if k == 0:
                print("\n")
            diff = (cts_measures[j][k]/stdevs[i]) - (means[i]/stdevs[i])
            if abs(diff) > 3.5:
                print("\x1b[0;37;41m", end="")
            print("{:.1f}\x1b[0;0m".format(diff), end=" ")
            i += 1

if __name__ == "__main__":
    main()
